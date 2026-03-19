# Week 06: Network Layer Proposed Problem Set

## Overview
**Topic:** IP Addressing, CIDR, and Subnetting
**Format:** Proposed problem set with solutions

---

## Problems

### Problem 1: The Classful Waste Problem
**Question:**
Before 1993, IP addresses were handed out in fixed classes. A Class C block gave you 254 usable hosts. A Class B block gave you 65,534. 
1. If a company needed 2,000 IP addresses, what happened under this old system?
2. Why did this specific problem cause the global internet routing tables to get too big?

### Problem 2: Basic CIDR Math
**Question:**
You get the address block 10.5.0.0/22. 
1. How many total IP addresses are in this block?
2. How many of those are usable for host devices?
3. What is the dotted-decimal subnet mask for a /22 prefix?

### Problem 3: Subnetting a LAN
**Question:**
Your office uses the network 192.168.50.0/24. You need to split this into 4 equal-sized subnets for different departments.
1. How many bits do you need to borrow from the host portion?
2. What is the new CIDR prefix length?
3. What is the network address and the broadcast address for the second subnet (Subnet 1)?

### Problem 4: Subnet Membership Logic
**Question:**
Two computers are plugged into the same network switch. Computer A has the IP 192.168.10.75/26. Computer B has the IP 192.168.10.130/26.
1. Are these two computers on the same subnet? 
2. Show the binary math the computer uses to figure this out.
3. Do they need a router to talk to each other?

### Problem 5: Route Aggregation (Supernetting)
**Question:**
An internet service provider (ISP) has four customers. They assign these blocks: 192.168.0.0/24, 192.168.1.0/24, 192.168.2.0/24, and 192.168.3.0/24. 
Instead of sending four separate routes to the rest of the internet, the ISP sends just one. What is that single, aggregated CIDR route?

### Problem 6: Variable-Length Subnet Masking (VLSM)
**Question:**
You need to carve up a 192.168.20.0/24 block for three specific use cases:
- A student lab that needs 120 hosts.
- A faculty office that needs 50 hosts.
- A direct link between two routers that only needs 2 hosts.
What prefix length should you assign to each of these three segments to waste the least amount of space?

### Problem 7: Troubleshooting Special IP Addresses
**Question:**
A user complains their laptop can't reach the internet. You check their IP settings and see their address is 169.254.22.5. 
1. What specific type of address is this?
2. What does seeing this address immediately tell you about the network problem?

### Problem 8: Programming with Python
**Question:**
You are writing a Python script to manage IP addresses using the built-in `ipaddress` module. You define a network: `net = ipaddress.IPv4Network("172.16.0.0/20")`.
Write the line of code that would output the total number of usable host addresses in this network.

---

## Solutions

### Solution 1: The Classful Waste Problem
1. **The waste:** The company was too big for a Class C block. [cite_start]So, they were given a Class B block[cite: 5753]. [cite_start]They only needed 2,000 addresses, meaning they wasted over 63,000 IPs that nobody else could use[cite: 5753].
2. [cite_start]**The routing explosion:** Sometimes, ISPs would try to fix this by giving the company eight separate Class C blocks instead[cite: 5746]. [cite_start]But classful routing didn't allow you to group them together[cite: 5749]. [cite_start]So, routers worldwide had to store eight separate entries for one company, which filled up router memory fast[cite: 5748].

### Solution 2: Basic CIDR Math
1. [cite_start]**Total addresses:** A 32-bit address minus a 22-bit network prefix leaves 10 host bits[cite: 5781]. [cite_start]2^10 = 1024 total addresses[cite: 5781].
2. **Usable hosts:** You always subtract 2 (one for the network address, one for the broadcast address). [cite_start]1024 - 2 = 1022 usable hosts[cite: 5782].
3. **Subnet mask:** A /22 mask has 22 ones and 10 zeros. In binary, that is 11111111.11111111.11111100.00000000. [cite_start]In decimal, it is 255.255.252.0[cite: 5770].

### Solution 3: Subnetting a LAN
1. [cite_start]**Borrowed bits:** To get 4 subnets, you need to borrow 2 bits because 2^2 = 4[cite: 5841].
2. **New prefix:** You started with /24. Add 2 borrowed bits. [cite_start]The new prefix is /26[cite: 5841].
3. [cite_start]**Subnet 1 Details:** A /26 gives you a block size of 64[cite: 5842]. Subnet 0 goes from .0 to .63. Subnet 1 goes from .64 to .127. [cite_start]So, the network address is 192.168.50.64, and the broadcast address is 192.168.50.127[cite: 5850].

### Solution 4: Subnet Membership Logic
1. [cite_start]**Same subnet?** No, they are on different subnets[cite: 5871].
2. [cite_start]**The math:** A /26 mask ends in 192 (binary 11000000)[cite: 5856]. The computer performs a bitwise AND operation on the last octet. 
   - [cite_start]75 AND 192 = 64[cite: 5857]. So Computer A is on the .64 network.
   - [cite_start]130 AND 192 = 128[cite: 5866]. So Computer B is on the .128 network.
3. **Router needed?** Yes. Even if they are plugged into the exact same switch, they have different network addresses. [cite_start]Traffic must go through a router to move between subnets[cite: 5872].

### Solution 5: Route Aggregation
[cite_start]The ISP can group all four of those /24 networks into a single 192.168.0.0/22 route[cite: 5794]. [cite_start]Because the IP blocks are adjacent and perfectly aligned, this "supernet" covers all of them with just one routing table entry[cite: 5795].

### Solution 6: Variable-Length Subnet Masking (VLSM)
- **Lab (120 hosts):** You need at least 122 addresses (including network/broadcast). The closest power of 2 is 128. This leaves 7 host bits. [cite_start]32 - 7 = **/25 prefix**[cite: 5882].
- **Office (50 hosts):** You need at least 52 addresses. The closest power of 2 is 64. This leaves 6 host bits. [cite_start]32 - 6 = **/26 prefix**[cite: 5882].
- **Router link (2 hosts):** You need 4 addresses. The closest power of 2 is 4. This leaves 2 host bits. [cite_start]32 - 2 = **/30 prefix**[cite: 5882].

### Solution 7: Troubleshooting Special IP Addresses
1. [cite_start]**Type:** 169.254.x.x is a link-local address, also known as APIPA[cite: 5903]. 
2. [cite_start]**The problem:** This tells you the laptop tried to get an IP address from a DHCP server, but the DHCP server failed or didn't respond[cite: 5903]. [cite_start]The operating system just assigned itself a dummy address so it could talk to other local devices, but it cannot route traffic to the internet[cite: 5903].

### Solution 8: Programming with Python
You can get the total number of usable hosts by finding the total addresses and subtracting 2:
[cite_start]`print(net.num_addresses - 2)` [cite: 5971]
Alternatively, you can count the length of the usable hosts list:
[cite_start]`print(len(list(net.hosts())))` [cite: 5982]