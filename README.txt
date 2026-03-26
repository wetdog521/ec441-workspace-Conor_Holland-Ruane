
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


