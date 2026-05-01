import pyshark
import matplotlib.pyplot as plt

def get_udp_jitter(pcap_file):
    # Only look at UDP traffic
    cap = pyshark.FileCapture(pcap_file, display_filter='udp')
    
    packet_numbers = []
    time_deltas = []
    
    last_time = None
    count = 0

    for pkt in cap:
        try:
            current_time = float(pkt.sniff_timestamp)
            if last_time is not None:
                # Calculate the gap in milliseconds
                delta_ms = (current_time - last_time) * 1000
                
                # Ignore massive gaps (likely just silence/pauses)
                if delta_ms < 100: 
                    time_deltas.append(delta_ms)
                    packet_numbers.append(count)
                    count += 1
                    
            last_time = current_time
        except AttributeError:
            continue
            
    cap.close()
    return packet_numbers, time_deltas

print("Analyzing Zoom UDP jitter...")
pkts, deltas = get_udp_jitter("zoom_traffic_home.pcap")

plt.figure(figsize=(10, 5))
plt.plot(pkts, deltas, color='blue', alpha=0.6)
plt.title("Zoom UDP Jitter on Campus Wi-Fi")
plt.xlabel("Packet Sequence Number")
plt.ylabel("Time Since Previous Packet (ms)")
plt.axhline(y=(sum(deltas)/len(deltas)), color='red', linestyle='--', label='Average Gap')
plt.legend()
plt.show()