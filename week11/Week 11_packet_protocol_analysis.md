# EC 441 Week 12 Laboratory Report: Manual Packet Forging and Protocol Dissection
**Student:** Conor Ruane

## Section 1: Application-Layer DNS Dissection

*(Insert `Screenshot 2026-05-02 at 2.29.59 PM.jpg` here)*

Based on the Wireshark capture, the manual UDP DNS probe successfully completed the resolution chain.
* **The Query:** The manually forged packet successfully reached Google's public resolver (`8.8.8.8`) with the `Recursion Desired` bit set to 1, instructing the server to traverse the DNS hierarchy on our behalf. 
* **The Resolution:** The expanded Answer record in the response packet shows that `www.ietf.org` resolves to the IPv4 addresses `104.16.45.99` and `104.16.44.99`. 
* **Time to Live (TTL):** The Answer record provides a specific TTL value of `300` seconds (5 minutes). This dictates exactly how long the client's local DNS cache is permitted to store this IP mapping. Once this timer expires, the OS must flush the record and initiate a new DNS query to ensure it doesn't connect to a stale or reassigned IP address.

---

## Section 2: Transport-Layer TCP State Analysis

*(Insert `Screenshot 2026-05-02 at 2.23.18 PM.jpg` here)*

Based on the Wireshark capture, the manual SYN probe triggered a specific three-packet sequence that demonstrates how the operating system's network stack handles unexpected segments.

1. **The Forged Probe (Frame 15509):** The capture shows the manually crafted TCP `SYN` packet departing my machine (`10.239.183.18`) destined for port 443 on the server (`10.236.0.52`). Because this packet was forged using Scapy, it bypassed the host OS's network stack; the Linux kernel did not open a socket or register a connection attempt for this source port (3510).
2. **The Server Response (Frame 15527):** The server successfully received the probe and replied with a `SYN-ACK` packet, acknowledging the sequence number and allocating a window size (5360) to establish the connection.
3. **The Kernel Reset (Frame 15528):** Immediately after the `SYN-ACK` arrived, my host machine automatically transmitted an `RST` (Reset) packet back to the server. Because the host kernel had no record of initiating a connection on port 3510, it evaluated the incoming `SYN-ACK` as an unexpected segment. Following the strict guidelines of RFC 793, the kernel fired the `RST` to immediately abort the unrecognized connection and prevent a half-open state on the server.