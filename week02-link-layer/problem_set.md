# Week 04: Link Layer Proposed Problem Set

## Overview
[cite_start]**Topic:** Link Layer (Error Control Coding) 
**Format:** Proposed problem set with solutions

---

## Problems

### Problem 1: Code Rate and Block Codes
**Question:**
[cite_start]An Arduino-based smart doorbell sends a 4-bit status code (data bits, k=4) to a home hub[cite: 1577]. [cite_start]To ensure reliability against noise, it encodes this into a 7-bit codeword, creating a (7,4) block code[cite: 1577].
1. [cite_start]What is the code rate (Rc) of this transmission? [cite: 1590]
2. [cite_start]How many redundant (check) bits are added to each codeword? [cite: 1581]
3. [cite_start]How many valid codewords exist in this scheme? [cite: 1579]

### Problem 2: Hamming Distance
**Question:**
An FPGA-based communication system uses a specific error control strategy. [cite_start]Consider the code set C = {000, 011, 101, 110}[cite: 1678].
1. [cite_start]Calculate the Hamming distance between the codewords 011 and 101[cite: 1678].
2. [cite_start]Determine the minimum distance (d_min) for this entire code set[cite: 1680].

### Problem 3: The d_min Theorem
**Question:**
[cite_start]For a generic code with a minimum distance of d_min = 4[cite: 1774]:
1. [cite_start]What is the maximum number of errors this code can detect (ed) if we do not attempt any correction (ec = 0)? [cite: 1752, 1753, 1775]
2. [cite_start]What is the maximum number of errors it can correct (ec) if we maximize correction capability? [cite: 1754, 1755, 1775]

### Problem 4: Parity vs. Repetition Codes
**Question:**
[cite_start]Compare a (4,3) even parity code with a (3,1) repetition code[cite: 1625, 1640].
1. [cite_start]Which code is more bandwidth-efficient (has a higher code rate)? [cite: 1630, 1643]
2. [cite_start]Which code provides a higher d_min? [cite: 1634, 1644]

---

## Solutions

### Solution 1: Code Rate and Block Codes
1. [cite_start]**Code Rate:** The code rate is calculated as Rc = k / n[cite: 1591]. [cite_start]For this (7,4) code, Rc = 4 / 7 (approximately 57% of transmitted bits carry data)[cite: 1596].
2. [cite_start]**Redundant Bits:** The number of check bits is n - k = 7 - 4 = 3 redundant bits per codeword[cite: 1581].
3. [cite_start]**Valid Codewords:** There are 2^k valid codewords, so 2^4 = 16 valid codewords out of 128 possible 7-bit words[cite: 1579].

### Solution 2: Hamming Distance
1. [cite_start]**Distance Calculation:** The Hamming distance is the number of bit positions in which the two words differ[cite: 1653]. [cite_start]Comparing 011 and 101, they differ in the first and second positions, so the distance is 2[cite: 1678]. 2. [cite_start]**Minimum Distance:** Comparing all pairs in the set {000, 011, 101, 110} reveals that every single pair differs by exactly 2 bits[cite: 1679]. [cite_start]Therefore, d_min = 2[cite: 1680].

### Solution 3: The d_min Theorem
1. [cite_start]**Maximum Detection:** Using the theorem ed = d_min - 1[cite: 1753]. [cite_start]Thus, it can detect a maximum of 4 - 1 = 3 errors[cite: 1775].
2. [cite_start]**Maximum Correction:** Using the theorem ec = floor((d_min - 1) / 2)[cite: 1755]. [cite_start]Thus, it can correct floor(3 / 2) = 1 error[cite: 1775].

### Solution 4: Parity vs. Repetition Codes
1. [cite_start]**Bandwidth Efficiency:** The (4,3) even parity code has a rate of 3/4[cite: 1630]. [cite_start]The (3,1) repetition code has a rate of 1/3[cite: 1643]. [cite_start]The parity code is more efficient[cite: 1630].
2. [cite_start]**Minimum Distance:** The (4,3) parity code has a d_min of 2[cite: 1634]. [cite_start]The (3,1) repetition code has a d_min of 3[cite: 1644]. [cite_start]The repetition code provides a higher minimum distance[cite: 1644].