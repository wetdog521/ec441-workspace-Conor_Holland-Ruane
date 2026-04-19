# Week 08: Network Tools and Analysis Quiz

## Multiple Choice Questions

**1. Which tool relies on incrementing the Time To Live (TTL) field to map out the exact path packets take to a destination?**
A) ping
B) traceroute
C) dig
D) ss

**2. The `ping` utility primarily uses which protocol to verify host reachability?**
A) TCP
B) UDP
C) ICMP
D) ARP

**3. A network administrator wants to see the live TCP congestion window (`cwnd`) of active sockets on a Linux server. Which command provides this?**
A) ip route
B) tcpdump
C) ss -ti
D) dig

**4. A domain name fails to resolve to an IP address. Which tool is specifically designed to query DNS records for troubleshooting?**
A) dig
B) ip
C) traceroute
D) tcpdump

**5. What is the correct Berkeley Packet Filter (BPF) syntax to capture only web traffic on port 80 using `tcpdump`?**
A) tcpdump port=80
B) tcpdump grep 80
C) tcpdump tcp port 80
D) tcpdump -p 80

**6. Modern data-center switches (like Arista EOS) and backbone routers typically run operating systems based on:**
A) Windows
B) Custom closed-source firmware
C) Linux or FreeBSD
D) RTOS

**7. In Wireshark, what feature reconstructs the entire application-layer payload of a back-and-forth exchange into a single readable window?**
A) Statistics Protocol Hierarchy
B) Follow TCP Stream
C) Packet Byte View
D) Endpoint List

**8. Which Python library allows a script to load a `.pcap` file and extract specific packet fields programmatically?**
A) networkx
B) matplotlib
C) pyshark
D) sockets

**9. The `ip` command on Linux is a modern replacement for older tools. Which of the following can it display?**
A) Active TCP connections
B) Network interfaces and the routing table
C) DNS cache
D) Packet payloads

**10. Why is capturing traffic on the loopback interface (`127.0.0.1`) particularly useful for studying TCP mechanics?**
A) It bypasses the congestion control algorithm.
B) It carries unencrypted traffic with fully visible headers, making sequence numbers readable.
C) It automatically filters out UDP traffic.
D) It drops packet loss to exactly zero, guaranteeing perfect transmission.

## Open-Ended Questions

**11. Explain the exact mechanism `traceroute` uses to discover the third router on a path to a destination.**

**12. A network engineer suspects a routing loop is causing an outage. How does running `ping` help identify this specific problem?**

**13. Contrast `tcpdump` and `Wireshark`. When is it appropriate to use one over the other?**

**14. An engineer views the output of `ss -ti` during a file transfer. The `cwnd` value drops sharply from 200 to 100. What network event occurred, and what specific transport-layer concept does this demonstrate?**

**15. How does using `pyshark` to analyze network traffic differ from writing a raw socket program that reads bytes directly from the network interface?**

---

## Solutions

### Multiple Choice Solutions
1. **B) traceroute**
2. **C) ICMP**
3. **C) ss -ti**
4. **A) dig**
5. **C) tcpdump tcp port 80**
6. **C) Linux or FreeBSD**
7. **B) Follow TCP Stream**
8. **C) pyshark**
9. **B) Network interfaces and the routing table**
10. **B) It carries unencrypted traffic with fully visible headers, making sequence numbers readable.**

### Open-Ended Solutions

**11.** The `traceroute` tool sends a packet with the TTL set to exactly 3. The packet passes through the first two routers, which decrement the TTL to 2 and 1. The third router decrements the TTL to 0, drops the packet, and sends an ICMP Time Exceeded error back to the source. The source reads the IP address of that returning error message to identify the third router.

**12.** The `ping` command reports the TTL value of returning packets. If a routing loop exists, packets bounce between routers until their TTL hits zero. If `ping` fails but returns an ICMP "Time to live exceeded" message instead of a standard timeout, it confirms the packet died in a routing loop.

**13.** The `tcpdump` tool operates entirely in the command line. It is lightweight and installed on almost every Linux server. Engineers use it to capture raw packets directly from headless, remote systems. `Wireshark` is a desktop GUI application. Engineers typically use `tcpdump` to capture the traffic into a `.pcap` file, then transfer that file to a laptop to visually inspect the protocols in `Wireshark`.

**14.** A packet was lost on the network. The sharp drop by exactly half indicates TCP congestion control reacted to the loss. The congestion algorithm (like Reno or CUBIC) cut the congestion window size to reduce the load on the network.

**15.** A raw socket program just receives a raw stream of binary data. The code must manually slice the bytes into Ethernet, IP, and TCP headers. The `pyshark` library acts as a wrapper around the Wireshark dissection engine. It automatically parses all the raw bytes and converts them into structured Python objects. This allows a script to directly access variables like `packet.ip.src` or `packet.tcp.flags` without doing the binary math.