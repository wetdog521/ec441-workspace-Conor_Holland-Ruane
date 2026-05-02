
WEEK 1:

Type: Problem Set
Tools Used: Google Gemini

Usage Description: For Week 1, I used Gemini to help synthesize my notes from Lecture 3 (Physical Layer) into a proposed problem set. I provided the AI with the course assignment guidelines and the Lecture 3 slide notes. The goal was to generate realistic, exam-style mathematical problems regarding link budgets, Shannon capacity, and M-ary PAM. I then reviewed the generated calculations against the formulas in the lecture notes to verify factual accuracy before rendering the final Markdown.

WEEK 2:

Type: Problem Set
Tools Used: Google Gemini

Usage Description: For this week's artifact, I used Gemini to generate a proposed problem set based on the EC 441 Lecture 5 notes[cite: 64, 1543]. [cite_start]To push beyond surface-level prompting and make the abstract concepts more concrete, I guided the AI to frame the block code and Hamming distance questions around hardware implementations, specifically an Arduino-based smart doorbell and FPGA communication systems. [cite_start]After generating the problems, I reviewed the mathematical solutions against the $d_{min}$ theorem and code rate formulas provided in the lecture notes to ensure factual accuracy.

WEEK 3:

Type: Problem Set
Tools Used: Google Gemini

Usage Description: I used Gemini to synthesize the Lecture 8 Ethernet notes into a proposed problem set. I specifically directed the AI to generate questions that bridge network theory with hardware and physical layer constraints (such as line coding, interrupt handling on NICs, and duplex mismatch diagnostics). After generation, I verified the AI's solutions against the lecture notes, particularly confirming the logic behind the ARP broadcast/unicast asymmetry and the CSMA/CD mechanics causing late collisions.

Week 5:

Type: Problem Set
Tools Used: Google Gemini

Usage Description: I used Gemini to generate an 8-question problem set covering the material from Lecture 14. I asked the AI to focus on practical calculations, like finding usable host ranges, performing subnet membership checks with binary AND logic, and assigning VLSM blocks based on host requirements. After it generated the problems, I double-checked the CIDR math and Python 'ipaddress' module syntax against the class slides to verify it was correct.

Week 6:


Type: Lab
Tools Used:** Google Gemini

Usage Description: I asked Gemini to expand the Python routing lab. I instructed the AI to include more test cases from the assignment, specifically the misleading path topology and a comparison of baseline Distance Vector versus Distance Vector with Poisoned Reverse. I also required the AI to add terminal instructions and dependency requirements to the README so anyone cloning the repo can run it easily. 

How to Run This Lab:

You need Python installed on your computer. This script uses a couple of external libraries to draw the network graphs on your screen.

1. Open your terminal or command prompt.
2. Install the required libraries by running this command:
   'pip install networkx matplotlib'
3. Navigate to the folder containing the script.
4. Run the script with this command:
   'python3 441_LAB_1.py'

A window will pop up showing the network graph. Close the window to let the script continue running the routing math and printing the analysis to your terminal.

Week 7:


Tools Used: Google Gemini
Usage Description: I prompted Gemini to refine the simulation script from earlier. I requested that the `\n` terminal bugs be fixed and that visual network graphs be added to every test case using `networkx` and `matplotlib`. I also enforced specific language constraints to ensure the terminal output reads more naturally and explains the core concepts (like why NAT breaks end-to-end communication and how traceroute abuses TTL logic) in simple, direct terms.

How to Run This Lab

You need Python installed, along with two graphing libraries.

1. Open your terminal.
2. Install the visual libraries:
   `pip install networkx matplotlib`
3. Run the script:
   `python week07-protocol-lab.py`

The script is interactive. It will pop up a window showing a diagram (like a Traceroute path or a DHCP exchange). Close the window to let the script print the step-by-step analysis to your terminal, then press Enter to move to the next topic.

Week 8:

Tools Used: Google Gemini
Usage Description: I expanded my previous iperf3 guide into a formal Performance Analysis Report. I gave the AI a strict prompt requiring a high level of technical detail, specifically asking it to integrate math and bash code blocks directly into the explanations. The AI generated the Mathis Throughput Formula derivation to prove throughput collapse on high-BDP networks. It also generated the specific Linux tc and sysctl commands needed to replicate the theories in a lab environment. I enforced rigid language constraints so the report reads cleanly and directly, avoiding all marketing fluff.


Week 9

Tools Used: Google Gemini
Usage Description: Gemini generated a 15-question Gradescope-style quiz based on the Lecture 21 notes covering CLI tools, Wireshark, and pyshark. A strict prompt required a mix of multiple-choice and open-ended questions. The prompt also required concise, detailed solutions for every question. The output maps directly to the specific use cases of ping, traceroute, ss, and tcpdump outlined in the class materials.


Week 10

Tools Used: Markdown, Mermaid.js, Google Gemini, VS Code

Usage Description: For this technical report, I utilized Gemini to assist in structuring a rigorous analysis of the paradigm shift from kernel-space TCP to user-space QUIC over UDP. The report modeled the QUIC connection lifecycle and TLS 1.3 handshake strictly as a central state machine, utilizing Mermaid.js to diagram the 1-RTT transition sequence. Furthermore, I detailed the cryptographic primitives securing the transport, specifically AES-GCM for payload integrity and HKDF for key derivation. A major focal point was dissecting Ephemeral Elliptic Curve Diffie-Hellman (ECDHE) to explain how the mathematical separation of authentication and confidentiality guarantees forward secrecy. Finally, I contextualized these protocols against physical engineering constraints by exploring hypothetical deployments in low-power embedded hardware and lossy marine telemetry networks.

Week 11

Tools Used:** Python (Scapy), `tcpdump` / `tshark`, Wireshark, Google Gemini

Usage Description:For this laboratory assignment, I utilized Gemini to assist in writing a Python script leveraging the Scapy library to manually forge Transport and Application layer packets, bypassing the standard operating system network stack. The script crafted a raw TCP SYN probe targeting `www.bu.edu` and a UDP DNS query for `www.ietf.org`. I utilized command-line packet capture tools to record the raw wire traffic to a `.pcap` file. During the Wireshark dissection phase, I successfully tracked the DNS resolution chain, specifically observing the "Recursion Desired" bit and the 300-second Time-to-Live (TTL) attribute in the answer records. Furthermore, I identified a critical transport-layer interaction: because Scapy bypasses the kernel to send the initial SYN, the OS network stack interprets the incoming SYN-ACK from the server as an unexpected segment and immediately transmits an RST packet to tear down the connection, perfectly demonstrating standard RFC 793 behavior.



Final Project

Tools Used: Google Gemini, Wireshark, Python (pyshark, matplotlib)

Usage Description: Over the final weeks of the course, I used Gemini as an interactive tutor and pair-programmer to scope, build, and refine my final Demo Day project.

Project Scoping & Methodology: I initially queried the AI to evaluate several project prompts. After selecting the pyshark traffic analysis project, we established a robust methodology focused on the course's grading rubric (Depth, Clarity, and Craft). The AI guided me on how to cleanly capture Wireshark data, isolate application traffic, and simulate active web browsing. We significantly expanded the project's depth by establishing a comparative study: analyzing how applications behave on an enterprise network (Boston University's campus Wi-Fi) versus a residential home network.

Script Development & Iteration: I used Gemini to iteratively develop Python scripts to parse my .pcap files offline. We started with a basic script to plot TCP vs. UDP packet sizes over time. As my understanding deepened, I prompted the AI to help me write more advanced analytical scripts. We developed custom parsers to calculate throughput over time (Mbps), measure UDP packet arrival variance (jitter), and track TCP sequence numbers to map exact network retransmissions (packet drops).

Debugging & Optimization: During the development of the TCP sequence tracking script, I encountered a massive memory leak that caused my system to freeze. I used Gemini to diagnose the issue, learning that pyshark stores all packets in RAM by default. We implemented a fix using keep_packets=False and added a terminal progress counter to handle the massive packet volume of a 4K YouTube download safely.

Data Analysis & Presentation Prep: Once I generated the comparative graphs, I used Gemini to help me interpret the raw data and translate it into a compelling narrative for my Demo Day pitch. We mapped the visual data back to core networking concepts, specifically linking UDP jitter to Layer 2 CSMA/CA interference, and TCP throughput dips to Layer 4 congestion control (Head-of-Line blocking). Finally, I used the AI to simulate a peer-review session, practicing my explanations for edge cases like enterprise firewalls utilizing a "default deny" rule for UDP traffic and forcing applications like Zoom to fall back to TCP.

