
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

Tools Used:** Google Gemini
Usage Description:** Gemini generated a 15-question Gradescope-style quiz based on the Lecture 21 notes covering CLI tools, Wireshark, and pyshark. A strict prompt required a mix of multiple-choice and open-ended questions. The prompt also required concise, detailed solutions for every question. The output maps directly to the specific use cases of ping, traceroute, ss, and tcpdump outlined in the class materials.

