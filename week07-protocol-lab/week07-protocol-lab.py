# Week 06: Network Layer Protocols Lab

## Overview
##**Topic:** IPv4, ICMP, Fragmentation, NAT, IPv6, and DHCP
##**Format:** Python simulation and dynamic analysis
##**Generated with:** Google Gemini (See README for details)


## Lab Script (`protocol_lab.py`)

import math

# --- SECTION 1 & 2: IPv4 and ICMP (Traceroute) ---
class IPv4Packet:
    def __init__(self, src, dst, size, ttl, df=False):
        self.src = src
        self.dst = dst
        self.size = size
        self.ttl = ttl
        self.df = df # Don't Fragment flag
        self.mf = False # More Fragments flag
        self.offset = 0
        self.protocol = "ICMP"
        self.checksum = self.calculate_checksum()

    def calculate_checksum(self):
        # Fake checksum for simulation
        return hash((self.src, self.dst, self.size, self.ttl, self.df, self.mf, self.offset))

    def decrement_ttl(self):
        self.ttl -= 1
        self.checksum = self.calculate_checksum()
        return self.ttl

def run_traceroute_simulation():
    print("==================================================")
    print("--- SECTION 1 & 2: Traceroute & ICMP ---")
    print("==================================================")
    
    path = ["RouterA", "RouterB", "Destination"]
    
    for attempt_ttl in range(1, 4):
        print(f"\\n[Host] Sending packet with TTL={attempt_ttl}")
        pkt = IPv4Packet("10.0.0.5", "8.8.8.8", 64, attempt_ttl)
        
        hop_count = 0
        for node in path:
            print(f"  [{node}] Received packet. TTL is {pkt.ttl}.")
            new_ttl = pkt.decrement_ttl()
            print(f"  [{node}] Decremented TTL to {new_ttl}. New checksum: {pkt.checksum}")
            
            if new_ttl == 0 and node != "Destination":
                print(f"  [{node}] TTL hit 0! Dropping packet.")
                print(f"  [{node}] Sending ICMP Type 11 (Time Exceeded) back to 10.0.0.5")
                break
            elif node == "Destination":
                print(f"  [{node}] Reached target! Sending ICMP Type 0 (Echo Reply).")
                break
            hop_count += 1

    print("\\n[ANALYSIS: TTL and ICMP]")
    print("TTL stops infinite loops. If there is a routing loop, the packet dies when TTL hits zero.")
    print("Traceroute uses this on purpose. It sends TTL=1, then TTL=2, to force routers to reply with ICMP errors.")
    print("Also, routers never send an ICMP error in response to another ICMP error. That prevents infinite error storms.")

# --- SECTION 3 & 4: FRAGMENTATION vs PMTUD ---
def run_fragmentation_simulation():
    print("\\n==================================================")
    print("--- SECTION 3: IPv4 Fragmentation ---")
    print("==================================================")
    
    packet_size = 4000
    mtu = 1500
    header_size = 20
    payload = packet_size - header_size
    
    print(f"Packet: {packet_size} bytes. MTU: {mtu} bytes.")
    
    # Calculate fragments
    max_payload = mtu - header_size
    # Must be multiple of 8 for offset
    max_payload = (max_payload // 8) * 8 
    
    fragments = []
    remaining = payload
    offset = 0
    
    while remaining > 0:
        if remaining > max_payload:
            frag_payload = max_payload
            mf = 1
        else:
            frag_payload = remaining
            mf = 0
            
        fragments.append({
            "size": frag_payload + header_size,
            "offset": offset // 8,
            "mf": mf
        })
        offset += frag_payload
        remaining -= frag_payload

    for i, f in enumerate(fragments):
        print(f"Fragment {i+1}: Size={f['size']}, Offset={f['offset']}, MF={f['mf']}")

    print("\\n[ANALYSIS: Fragmentation Issues]")
    print("Fragmentation is bad for performance. The router has to stop and chop up the packet.")
    print("If even one fragment drops, the receiver has to throw the whole datagram away.")

def run_pmtud_simulation():
    print("\\n==================================================")
    print("--- SECTION 4: Path MTU Discovery (PMTUD) ---")
    print("==================================================")
    
    print("Sending packet with DF=1 (Don't Fragment) set to True.")
    print("Router MTU is 1500. Packet is 4000.")
    print("Router drops packet! Sends ICMP Type 3, Code 4 (Fragmentation Needed and DF set).")
    print("Sender receives ICMP, lowers packet size to 1500, and tries again.")
    print("Success.")
    
    print("\\n[ANALYSIS: PMTUD Black Holes]")
    print("Sometimes PMTUD fails. If a firewall blocks all ICMP traffic, the sender never gets the 'Fragmentation Needed' message.")
    print("The packet just vanishes. The sender keeps trying 4000-byte packets, and the connection hangs.")

# --- SECTION 5: NAT ---
class NATRouter:
    def __init__(self):
        self.public_ip = "203.0.113.5"
        self.table = {}
        self.next_port = 50000

    def outbound(self, private_ip, private_port):
        pub_port = self.next_port
        self.table[(self.public_ip, pub_port)] = (private_ip, private_port)
        self.next_port += 1
        print(f"[NAT] Outbound: Mapped {private_ip}:{private_port} -> {self.public_ip}:{pub_port}")
        return pub_port

    def inbound(self, public_port):
        if (self.public_ip, public_port) in self.table:
            priv_ip, priv_port = self.table[(self.public_ip, public_port)]
            print(f"[NAT] Inbound: Forwarding to {priv_ip}:{priv_port}")
        else:
            print(f"[NAT] Inbound: Port {public_port} not in table. DROP PACKET.")

def run_nat_simulation():
    print("\\n==================================================")
    print("--- SECTION 5: NAT (Port Address Translation) ---")
    print("==================================================")
    
    nat = NATRouter()
    port = nat.outbound("192.168.1.50", 443)
    nat.inbound(port)
    
    print("\\nExternal server tries to initiate connection to random port 8080...")
    nat.inbound(8080)
    
    print("\\n[ANALYSIS: NAT Violates End-to-End]")
    print("NAT breaks the rule that every device should have a unique address. It hides private IPs behind one public IP.")
    print("Because of this, an outside host cannot initiate a connection. The NAT drops it.")

# --- SECTION 6 & 7: IPv6 and DHCP ---
def run_ipv6_and_dhcp():
    print("\\n==================================================")
    print("--- SECTION 6: IPv6 Differences ---")
    print("==================================================")
    print("IPv6 addresses are 128 bits. The header has a fixed 40-byte length.")
    print("IPv6 removes the header checksum completely. Link-layer and transport-layer checksums are good enough.")
    print("IPv6 routers do not fragment packets. If a packet is too big, it drops it and relies entirely on PMTUD.")
    
    print("\\n==================================================")
    print("--- SECTION 7: DHCP (DORA Process) ---")
    print("==================================================")
    print("1. [Discover] Client broadcasts: 'I need an IP!' (Src: 0.0.0.0, Dst: 255.255.255.255)")
    print("2. [Offer] DHCP Server replies: 'Here is 192.168.1.100. It is good for 24 hours.'")
    print("3. [Request] Client broadcasts: 'I accept 192.168.1.100 from this server.'")
    print("4. [Ack] DHCP Server replies: 'Confirmed. The IP is yours.'")
    
    print("\\n[ANALYSIS: DHCP vs SLAAC]")
    print("DHCP is stateful. The server keeps a big table of who owns which IP.")
    print("IPv6 uses SLAAC (Stateless Address Autoconfiguration). The router just hands out the prefix, and the client creates its own unique host ID. No central tracking table is needed.")

if __name__ == "__main__":
    run_traceroute_simulation()
    run_fragmentation_simulation()
    run_pmtud_simulation()
    run_nat_simulation()
    run_ipv6_and_dhcp()