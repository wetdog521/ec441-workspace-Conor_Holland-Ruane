# Performance Analysis Report: TCP Congestion Control and Measurement

## 1. Theoretical Grounding: The Throughput Limit

We use the Mathis Throughput Formula to predict the maximum steady-state speed of a TCP connection. 

The formula is:
$$BW \approx \frac{1.22 \cdot MSS}{RTT \cdot \sqrt{p}}$$

We can test this on a hypothetical 10 Gb/s link. Assume a 100 ms RTT and a very small 0.01% packet loss rate ($p = 0.0001$). The standard Maximum Segment Size (MSS) is 1460 bytes. 

First, convert MSS to bits:
$$1460 \text{ bytes} \cdot 8 = 11,680 \text{ bits}$$

Next, plug the values into the formula:
$$BW \approx \frac{1.22 \cdot 11,680}{0.1 \cdot \sqrt{0.0001}}$$
$$BW \approx \frac{14,249.6}{0.1 \cdot 0.01}$$
$$BW \approx 14,249,600 \text{ bps} \approx 14.25 \text{ Mbps}$$

The physical link can handle 10 Gb/s. But TCP restricts the speed to 14.25 Mb/s. This is a throughput collapse. 

Standard TCP Reno adds only one MSS per RTT. When a network has a high Bandwidth-Delay Product (BDP), Reno simply cannot recover fast enough from a dropped packet.

You can prove this in a lab using the Linux Traffic Control (`tc`) utility. Run this before your `iperf3` test to simulate the exact conditions:

    # Add 100ms delay and 0.01% loss to the network interface
    sudo tc qdisc add dev eth0 root netem delay 100ms loss 0.01%

    # Run iperf3 to verify the throughput limit matches the math
    iperf3 -c 192.168.1.50

## 2. CUBIC vs. Reno: The Growth Clock

Reno and CUBIC use different methods to increase the Congestion Window (**cwnd**).

**Reno** uses the RTT as its clock. Every time an RTT passes, it adds 1 to the window:
$$W_{next} = W_{curr} + 1$$

This creates RTT unfairness. A connection with a short RTT updates its window more frequently. It ends up stealing bandwidth from connections with longer RTTs.

**CUBIC** solves this by using a real-time clock. The growth function is:
$$W(t) = C(t - K)^3 + W_{max}$$

Here, $t$ is the exact time since the last packet dropped. $W_{max}$ is the window size right before that drop. Because CUBIC relies on real time $t$, two different flows on the same link will grow their windows at the same speed. Their individual RTTs do not matter. 

You can change the congestion algorithm in Linux to test how they differ:

    # Check the current algorithm
    sysctl net.ipv4.tcp_congestion_control

    # Switch to Reno
    sudo sysctl -w net.ipv4.tcp_congestion_control=reno

    # Switch to CUBIC
    sudo sysctl -w net.ipv4.tcp_congestion_control=cubic

## 3. Observational Evidence: Kernel State Analysis

The `iperf3` tool only shows you the final bandwidth. The `ss -ti` command lets you see the TCP stack's internal state in real time.

You can watch the kernel adjust variables during a test by using the `watch` command:

    # Start iperf3 in the background for 30 seconds
    iperf3 -c 192.168.1.50 -t 30 &

    # Watch the TCP socket statistics update every 1 second
    watch -n 1 'ss -ti dst 192.168.1.50'

You will see an output string that looks like this:

    State  Recv-Q Send-Q Local Address:Port  Peer Address:Port
    ESTAB  0      24576  192.168.1.10:53123  192.168.1.50:5201
         cubic wscale:7,7 rto:204 rtt:100.5/0.1 ato:40 cwnd:150 ssthresh:120 bytes_acked:145620

Here is exactly what the kernel is tracking:
* **cwnd:150**: The sender currently has exactly 150 segments in flight.
* **ssthresh:120**: The Slow Start Threshold. The kernel switched from exponential window growth to linear growth when it hit 120 segments.
* **rtt:100.5**: The smoothed RTT estimate is 100.5 milliseconds.
* **rto:204**: The Retransmission Timeout. If an ACK does not arrive within 204 milliseconds, the kernel assumes the packet is lost and retransmits.

## 4. Modern Alternatives: The QUIC Advantage

TCP puts all data into one continuous stream. If one packet drops, the entire stream halts until that specific packet is retransmitted. This flaw is called Head-of-Line (HOL) blocking.

QUIC is the protocol that powers HTTP/3. It solves this problem by using independent streams. 

If you download three images over QUIC, they travel in different streams. If a packet for Image 1 drops, Image 2 and Image 3 keep arriving without delay. QUIC does not let one dropped packet stall the entire connection. This makes QUIC much faster than TCP on lossy networks.

