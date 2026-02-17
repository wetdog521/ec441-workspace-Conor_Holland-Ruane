# Week 03: Physical Layer Proposed Problem Set

## Overview
**Topic:** Physical Layer (Guided Media & Digital Signaling)
**Format:** Proposed problem set with solutions
**Generated with:** Google Gemini (See README for details)

---

## Problems

### Problem 1: Fiber Optic Link Budget
**Question:**
A network engineer is designing a 60 km optical fiber link using single-mode fiber (SMF) operating at a 1550 nm wavelength. The transmitter has an output power of 5 dBm. The link includes 6 splices and 2 connectors. The receiver requires a minimum power of -25 dBm to decode the signal. Given the following specifications, calculate the received power and the link margin:
* Fiber attenuation at 1550 nm: $0.2~dB/km$
* Splice loss: 0.1 dB per splice
* Connector loss: 0.5 dB per connector

### Problem 2: Shannon Capacity and Noise Power
**Question:**
Consider a communication channel with a bandwidth $B = 20~MHz$. The received signal power is $P_{rx} = -70~dBm$, and the noise power spectral density is $N_{0} = -174~dBm/Hz$. Calculate the noise power in dBm, the signal-to-noise ratio (SNR) in dB, and the theoretical maximum data rate (Shannon capacity).

### Problem 3: Multi-Level Signaling (M-ary PAM)
**Question:**
A network upgrade is shifting from binary signaling (2-PAM) to 16-PAM to increase bandwidth efficiency.
1.  How many bits per symbol does the 16-PAM system transmit?
2.  What is the spectral efficiency ($\eta$) of the 16-PAM system, assuming a raised cosine pulse with a roll-off factor of $\alpha = 0.5$?
3.  What is the primary tradeoff or disadvantage of increasing $M$ from 2 to 16?

### Problem 4: Propagation Latency
**Question:**
Compare the propagation latency of a signal traveling between New York and Los Angeles (approx. 4000 km) through two different media:
1.  A vacuum (free space), where $v = c$.
2.  Optical fiber, where the refractive index $n \approx 1.5$.
Use $c = 3 \times 10^8~m/s$ for the speed of light. How much additional latency does the fiber medium introduce compared to the vacuum baseline?

### Problem 5: Thermal Noise Calculation
**Question:**
A receiver operating at room temperature ($T = 290~K$) has a bandwidth of $10~MHz$. Calculate the thermal noise power ($N$) in Watts and dBm. Use the Boltzmann constant $k_B = 1.38 \times 10^{-23}~J/K$.

### Problem 6: Pulse Shaping Bandwidth
**Question:**
A digital transmission system uses Raised Cosine pulse shaping to mitigate Intersymbol Interference (ISI).
1.  If the system transmits at a symbol rate of $R_s = 1~Msps$ (Mega-symbols per second) and uses a roll-off factor of $\alpha = 1.0$, what is the required bandwidth?
2.  How much bandwidth could be saved if the roll-off factor was reduced to $\alpha = 0.5$, keeping the same symbol rate?

---

## Solutions

### Solution 1: Fiber Optic Link Budget
1.  **Calculate Total Loss:**
    * Fiber loss: $0.2~dB/km \times 60~km = 12~dB$
    * Splice loss: $0.1~dB/splice \times 6~splices = 0.6~dB$
    * Connector loss: $0.5~dB/connector \times 2~connectors = 1.0~dB$
    * Total loss $= 12~dB + 0.6~dB + 1.0~dB = 13.6~dB$
2.  **Calculate Received Power ($P_{rx}$):**
    * $P_{rx} = P_{tx} - Total~Loss$
    * $P_{rx} = 5~dBm - 13.6~dB = -8.6~dBm$
3.  **Calculate Link Margin:**
    * $Margin = P_{rx} - Receiver~Sensitivity$
    * $Margin = -8.6~dBm - (-25~dBm) = 16.4~dB$

### Solution 2: Shannon Capacity
1.  **Calculate Noise Power ($N$):**
    * $N (dBm) = N_{0} + 10 \log_{10}(B)$
    * $N = -174 + 10 \log_{10}(20 \times 10^6) \approx -174 + 73.01 = -100.99~dBm$
2.  **Calculate SNR (dB):**
    * $SNR (dB) = P_{rx} (dBm) - N (dBm)$
    * $SNR = -70 - (-100.99) = 30.99~dB$
3.  **Calculate Shannon Capacity ($C$):**
    * Convert SNR to linear: $SNR_{linear} = 10^{30.99/10} \approx 1256$
    * $C = B \log_{2}(1 + SNR) = (20 \times 10^6) \times \log_{2}(1257)$
    * $C \approx 20 \times 10^6 \times 10.29 \approx 205.8~Mbps$

### Solution 3: M-ary PAM
1.  **Bits per symbol:** $\log_{2}(16) = 4$ bits/symbol.
2.  **Spectral efficiency:** $\eta = \frac{\log_{2}(M)}{1 + \alpha} \times 2$? *Correction based on notes:* The notes define bandwidth $B = \frac{1+\alpha}{2T}$. Therefore $R_s/B = \frac{2}{1+\alpha}$. Spectral efficiency $\eta = R_b/B = \frac{R_s \log_2 M}{0.75 R_s}$ (for $\alpha=0.5$).
    * $\eta = \frac{4}{0.75} = 5.33~bits/sec/Hz$.
3.  **Tradeoff:** Higher $M$ reduces the Euclidean distance between symbols, requiring higher transmit power (SNR) to maintain the same error rate.

### Solution 4: Propagation Latency
1.  **Vacuum Time:** $t_{vac} = \frac{d}{c} = \frac{4000 \times 10^3}{3 \times 10^8} \approx 13.33~ms$.
2.  **Fiber Time:** Speed in fiber $v = c/n = c/1.5 \approx 0.67c$.
    * $t_{fib} = \frac{4000 \times 10^3}{0.667 \times 3 \times 10^8} \approx \frac{4 \times 10^6}{2 \times 10^8} = 20~ms$.
3.  **Difference:** $20~ms - 13.33~ms = 6.67~ms$ additional latency.

### Solution 5: Thermal Noise
1.  **Formula:** $N = k_B T B$
2.  **Calculation:** $N = (1.38 \times 10^{-23}) \times 290 \times (10 \times 10^6)$
    * $N = 4.002 \times 10^{-14}~Watts$.
3.  **Convert to dBm:**
    * $dBm = 10 \log_{10}(\frac{4.002 \times 10^{-14}}{1 \times 10^{-3}})$
    * $dBm = 10 \log_{10}(4.002 \times 10^{-11}) \approx -104~dBm$.

### Solution 6: Pulse Shaping Bandwidth
1.  **For $\alpha = 1.0$:**
    * $B = \frac{1+\alpha}{2T} = \frac{2}{2} R_s = R_s$.
    * $B = 1~MHz$.
2.  **For $\alpha = 0.5$:**
    * $B = \frac{1.5}{2} R_s = 0.75 R_s$.
    * $B = 0.75~MHz$.
3.  **Saved Bandwidth:** $1~MHz - 0.75~MHz = 250~kHz$ saved.