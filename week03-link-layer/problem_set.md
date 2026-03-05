# Week 03: Ethernet (Physical and Link Layers) Proposed Problem Set

## Overview
**Topic:** Ethernet (MAC Addressing, ARP, Switching, and Line Codes)
**Format:** Proposed problem set with solutions
**Generated with:** Google Gemini (See README for details)

---

## Problems

### Problem 1: Frame Sizes and Hardware Interrupts
**Question:**
A network interface controller (NIC) is processing incoming traffic. [cite_start]Empirical data shows internet traffic follows a "mice and elephants" bimodal distribution[cite: 2090, 2092]. 
1. [cite_start]What is the minimum and maximum size of an Ethernet frame (including the header and FCS, but excluding the preamble)? [cite: 2062, 2064]
2. [cite_start]Why is a high volume of minimum-sized frames computationally expensive for a software-based router, even if the total bandwidth (in bytes per second) is low? [cite: 2141, 2144]

### Problem 2: Address Resolution Protocol (ARP) Asymmetry
**Question:**
[cite_start]Host A (IP: 192.168.1.10) needs to send an IP datagram to Host B (IP: 192.168.1.20) on the same subnet[cite: 2180]. 
1. [cite_start]Describe the destination MAC address used in the ARP Request sent by Host A. [cite: 2194]
2. [cite_start]Describe the destination MAC address used in the ARP Reply sent by Host B. [cite: 2197]
3. [cite_start]Why is the ARP Request sent differently than the ARP Reply? [cite: 2204, 2205]

### Problem 3: Switch Self-Learning
**Question:**
[cite_start]Three embedded devices (A, B, and C) are connected to ports 1, 2, and 3 of an Ethernet switch, respectively[cite: 2270]. [cite_start]The switch's forwarding table is currently empty[cite: 2271]. 
1. [cite_start]Device A sends a frame to Device B. What does the switch record in its forwarding table, and out of which ports does it forward the frame? [cite: 2260, 2273, 2274]
2. [cite_start]Device B responds with a frame back to Device A. What does the switch record, and out of which ports is this frame forwarded? [cite: 2260, 2275, 2276, 2277]

### Problem 4: Duplex Mismatch Diagnostics
**Question:**
While troubleshooting a legacy piece of lab equipment, a network engineer notices severely degraded throughput. [cite_start]The switch port connected to the equipment shows a rapidly incrementing "Late Collision" counter, while the equipment's interface reports FCS/CRC errors[cite: 2363, 2374].
1. [cite_start]What configuration error is the canonical cause of this specific combination of symptoms? [cite: 2358, 2378]
2. [cite_start]Briefly explain the mechanics of a "late collision" in this scenario. [cite: 2365, 2368, 2369, 2370, 2371]

### Problem 5: Line Coding Efficiency (Manchester vs. PAM-5)
**Question:**
Ethernet's physical layer has evolved significantly. [cite_start]10BASE-T utilizes Manchester encoding, while 1000BASE-T uses 4D-PAM5[cite: 1953, 1993].
1. [cite_start]What is the primary advantage of Manchester encoding regarding clock recovery? [cite: 1957]
2. [cite_start]Why is Manchester encoding unsuitable for 1 Gigabit Ethernet? [cite: 1960, 1961]
3. [cite_start]How does PAM-5 utilize redundancy to improve reliability over Cat 5e cable? [cite: 2008, 2011, 2012]

---

## Solutions

### Solution 1: Frame Sizes
1. [cite_start]**Sizes:** The minimum frame size is 64 bytes (14 bytes header + 46 bytes minimum payload + 4 bytes FCS)[cite: 2043, 2054, 2064]. [cite_start]The maximum frame size is 1518 bytes (14 bytes header + 1500 bytes payload + 4 bytes FCS)[cite: 2043, 2054, 2062]. 
2. [cite_start]**Computational Expense:** Interrupt and CPU overhead in a router scales with the *frame count*, not the byte count[cite: 2144]. [cite_start]Processing millions of tiny 64-byte frames requires millions of forwarding table lookups, exhausting CPU resources faster than processing the same amount of data packed into 1500-byte frames[cite: 2142, 2144].

### Solution 2: ARP Asymmetry
1. [cite_start]**ARP Request:** The request uses the broadcast MAC address (FF:FF:FF:FF:FF:FF) because Host A does not yet know Host B's MAC address, so it must ask every device on the subnet[cite: 2157, 2194].
2. [cite_start]**ARP Reply:** The reply uses Host A's specific unicast MAC address[cite: 2197].
3. **Reason for Asymmetry:** Broadcasting the reply is unnecessary since Host B now knows exactly who asked. [cite_start]Sending a unicast reply prevents unnecessary traffic from interrupting the CPUs of all other hosts on the LAN[cite: 2204, 2205]. 
### Solution 3: Switch Self-Learning
1. [cite_start]**Frame 1 (A to B):** The switch learns that MAC A is on Port 1[cite: 2273]. [cite_start]Because MAC B is not yet in the table, the switch floods the frame out of all other active ports (Ports 2 and 3)[cite: 2254, 2274].
2. [cite_start]**Frame 2 (B to A):** The switch learns that MAC B is on Port 2[cite: 2275]. [cite_start]Because MAC A is already in the forwarding table (mapped to Port 1), the switch forwards the frame *only* out of Port 1[cite: 2276, 2277].

### Solution 4: Duplex Mismatch
1. [cite_start]**Cause:** A duplex mismatch (one side is half-duplex, the other is full-duplex)[cite: 2358, 2378].
2. [cite_start]**Late Collision Mechanics:** The full-duplex side ignores CSMA/CD and transmits whenever it wants[cite: 2369]. [cite_start]If the half-duplex side is transmitting a frame and has already sent more than 64 bytes, and the full-duplex side suddenly transmits, the signals collide[cite: 2370, 2371]. [cite_start]The half-duplex side detects this collision "late" (after the 512-bit slot time)[cite: 2365, 2371].

### Solution 5: Line Coding
1. [cite_start]**Manchester Clock Recovery:** It guarantees a mid-bit voltage transition during every single bit period, providing a reliable clock signal for the receiver's phase-locked loop regardless of the data pattern[cite: 1957]. 2. [cite_start]**1Gbps Limitation:** Manchester requires a signal bandwidth twice the bit rate[cite: 1960]. [cite_start]1 Gb/s would require a 2 GHz bandwidth, which massively exceeds the ~100 MHz limit of twisted-pair Cat 5e cable[cite: 1995, 1996].
3. **PAM-5 Redundancy:** PAM-5 uses 5 voltage levels. [cite_start]Since $log_2(4) = 2$, only 4 levels are strictly needed to encode 2 bits per symbol[cite: 1998, 2008]. [cite_start]The 5th level acts as an extra symbol providing Forward Error Correction (FEC) redundancy (specifically trellis coded modulation), which compensates for the increased noise sensitivity of having more amplitude levels[cite: 2011, 2012, 2014].