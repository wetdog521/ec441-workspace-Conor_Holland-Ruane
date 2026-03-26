import math
import networkx as nx
import matplotlib.pyplot as plt

# --- VISUALIZATION TOOL ---
def draw_network(edges, title="Network Topology"):
    print(f"\n[Opening Window: {title}] - Close the popup window to continue the script...")
    G = nx.Graph()
    for u, v, cost in edges:
        G.add_edge(u, v, weight=cost)
    
    pos = nx.spring_layout(G, seed=42) 
    labels = nx.get_edge_attributes(G, 'weight')
    
    plt.figure(figsize=(6, 4))
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=2000, font_size=15, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=12)
    plt.title(title)
    plt.show()

# --- LINK STATE (DIJKSTRA) ---
class RouterLS:
    def __init__(self, name):
        self.name = name
        self.graph = {}
        self.lsa_messages = 0
        
    def add_link(self, u, v, cost):
        if u not in self.graph: self.graph[u] = {}
        if v not in self.graph: self.graph[v] = {}
        self.graph[u][v] = cost
        self.graph[v][u] = cost

    def run_dijkstra(self):
        # Flooding approximation: each node sends its links to everyone
        self.lsa_messages = len(self.graph) * len(self.graph) 
        
        N_prime = [self.name]
        D = {node: math.inf for node in self.graph}
        p = {node: None for node in self.graph}
        
        D[self.name] = 0
        for neighbor, cost in self.graph[self.name].items():
            D[neighbor] = cost
            p[neighbor] = self.name
            
        while len(N_prime) < len(self.graph):
            min_node = None
            min_dist = math.inf
            for node in self.graph:
                if node not in N_prime and D[node] < min_dist:
                    min_node = node
                    min_dist = D[node]
            
            if min_node is None: break 
            N_prime.append(min_node)
            
            for v, cost in self.graph[min_node].items():
                if v not in N_prime:
                    if D[min_node] + cost < D[v]:
                        D[v] = D[min_node] + cost
                        p[v] = min_node
                        
        print(f"Final Forwarding Table for {self.name}:")
        for dest in self.graph:
            if dest != self.name:
                curr = dest
                while p[curr] != self.name and p[curr] is not None:
                    curr = p[curr]
                print(f"  -> To {dest}, send to {curr} (Cost: {D[dest]})")

# --- DISTANCE VECTOR (BELLMAN-FORD) ---
class RouterDV:
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors
        self.dv = {name: 0}
        self.next_hop = {name: name}
        for n, cost in neighbors.items():
            self.dv[n] = cost
            self.next_hop[n] = n

    def generate_dv_for_neighbor(self, neighbor, use_poison=False):
        export_dv = {}
        for dest, cost in self.dv.items():
            # Poisoned reverse logic: lie and say distance is infinity if we route through them
            if use_poison and self.next_hop.get(dest) == neighbor and dest != neighbor:
                export_dv[dest] = math.inf
            else:
                export_dv[dest] = cost
        return export_dv
            
    def receive_dv(self, neighbor_name, neighbor_dv):
        changed = False
        cost_to_neighbor = self.neighbors.get(neighbor_name, math.inf)
        
        for dest, dest_cost in neighbor_dv.items():
            new_cost = cost_to_neighbor + dest_cost
            if dest not in self.dv or new_cost < self.dv[dest]:
                self.dv[dest] = new_cost
                self.next_hop[dest] = neighbor_name
                changed = True
        return changed

# --- SCENARIOS & ANALYSIS ---

def run_dv_network(routers, use_poison=False, max_rounds=20):
    round_num = 1
    while round_num <= max_rounds:
        any_changes = False
        dvs_in_transit = []
        for r_name, r_obj in routers.items():
            for neighbor in r_obj.neighbors:
                dv_copy = r_obj.generate_dv_for_neighbor(neighbor, use_poison)
                dvs_in_transit.append((neighbor, r_name, dv_copy))
                
        for target, sender, dv in dvs_in_transit:
            if routers[target].receive_dv(sender, dv):
                any_changes = True
                
        if not any_changes:
            print(f"Converged in {round_num} rounds.")
            return
        round_num += 1
    print(f"Did not converge after {max_rounds} rounds (Count to Infinity detected).")

def scenario_1_misleading_path():
    print("\n==================================================")
    print("--- SCENARIO 1: Misleading Path ---")
    print("==================================================")
    edges = [('A', 'B', 10), ('A', 'C', 1), ('C', 'D', 1), ('D', 'B', 1)]
    draw_network(edges, "Misleading Path Topology")
    
    print("\n[Link State Analysis]")
    rA = RouterLS('A')
    for u, v, cost in edges:
        rA.add_link(u, v, cost)
    rA.run_dijkstra()
    print("\nANALYSIS: LS sees the whole map immediately. It knows the direct link A->B costs 10.")
    print("But because it has the whole map, it instantly calculates that going A->C->D->B is cheaper (cost 3).")
    
    print("\n[Distance Vector Analysis]")
    routers = {
        'A': RouterDV('A', {'B': 10, 'C': 1}),
        'B': RouterDV('B', {'A': 10, 'D': 1}),
        'C': RouterDV('C', {'A': 1, 'D': 1}),
        'D': RouterDV('D', {'C': 1, 'B': 1})
    }
    run_dv_network(routers)
    print("\nANALYSIS: DV takes multiple rounds. At first, A only knows its direct neighbors.")
    print("It thinks the only way to B is the direct cost 10 link. It has to wait for D to tell C about B,")
    print("and then C has to tell A. This is why DV can be slow to find the best route in complex networks.")

def scenario_2_count_to_infinity():
    print("\n==================================================")
    print("--- SCENARIO 2: Failure & Count to Infinity ---")
    print("==================================================")
    edges = [('A', 'B', 1), ('B', 'C', 1)]
    draw_network(edges, "Topology: A-B link goes down")
    
    print("\n[Baseline DV (No Poisoned Reverse)]")
    # Setting up the failure state. The link to A is dead.
    routers = {
        'B': RouterDV('B', {'C': 1}), 
        'C': RouterDV('C', {'B': 1})
    }
    # Simulate C having the old, outdated route to A
    routers['C'].dv['A'] = 2
    routers['C'].next_hop['A'] = 'B'
    
    run_dv_network(routers, use_poison=False)
    
    print("\nANALYSIS: Why did it fail to converge (Count to Infinity)?")
    print("1. B realizes the direct link to A is dead.")
    print("2. But C tells B: 'Hey, I have a path to A with a cost of 2!'")
    print("3. B doesn't realize C's path actually goes backwards through B.")
    print("4. So B thinks: 'Great, I'll route through C. My cost is now 2 + 1 = 3.'")
    print("5. Then C sees B's cost went up to 3. C updates its own cost to 3 + 1 = 4.")
    print("6. They bounce this back and forth forever, adding 1 each time. Bad news travels slow.")

def scenario_3_poisoned_reverse():
    print("\n==================================================")
    print("--- SCENARIO 3: Fixing it with Poisoned Reverse ---")
    print("==================================================")
    edges = [('A', 'B', 1), ('B', 'C', 1)]
    draw_network(edges, "Fixing Count to Infinity")
    
    # Same failure state as before
    routers = {
        'B': RouterDV('B', {'C': 1}), 
        'C': RouterDV('C', {'B': 1})
    }
    routers['C'].dv['A'] = 2
    routers['C'].next_hop['A'] = 'B'
    
    run_dv_network(routers, use_poison=True)
    
    print("\nANALYSIS: How did Poisoned Reverse fix the loop?")
    print("1. C's best route to A goes through B.")
    print("2. Because we turned on Poisoned Reverse, C lies to B. C tells B: 'My distance to A is infinity.'")
    print("3. When the A-B link breaks, B looks at C for a backup route.")
    print("4. But since C is claiming its distance to A is infinity, B immediately knows there is no backup.")
    print("5. The loop is broken instantly and the network converges.")

if __name__ == "__main__":
    scenario_1_misleading_path()
    input("\nPress Enter to start Scenario 2 (Count to Infinity)...")
    scenario_2_count_to_infinity()
    input("\nPress Enter to start Scenario 3 (Poisoned Reverse)...")
    scenario_3_poisoned_reverse()