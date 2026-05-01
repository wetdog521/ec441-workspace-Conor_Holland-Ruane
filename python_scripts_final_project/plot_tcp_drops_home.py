import pyshark
import matplotlib.pyplot as plt

def get_tcp_behavior(pcap_file):
    times, seq_nums = [], []
    drop_times, drop_seqs = [], []
    first_time = None

    print(f"Opening {pcap_file}...")
    
    # keep_packets=False is CRITICAL for large files to prevent RAM exhaustion
    with pyshark.FileCapture(pcap_file, display_filter='tcp', keep_packets=False) as cap:
        packet_count = 0
        
        for pkt in cap:
            packet_count += 1
            
            # Print a progress update every 1000 packets so you know it's not stuck
            if packet_count % 1000 == 0:
                print(f"Processed {packet_count} packets...", end='\r')
                
            try:
                timestamp = float(pkt.sniff_timestamp)
                if first_time is None:
                    first_time = timestamp
                
                time_norm = timestamp - first_time
                seq = int(pkt.tcp.seq)
                
                times.append(time_norm)
                seq_nums.append(seq)
                
                # Check for retransmissions
                if hasattr(pkt.tcp, 'analysis_retransmission'):
                    drop_times.append(time_norm)
                    drop_seqs.append(seq)
                    
            except AttributeError:
                continue
                
    print(f"\nFinished processing {packet_count} packets.")
    return times, seq_nums, drop_times, drop_seqs

print("Hunting for TCP drops in Home YouTube traffic...")
t, seq, dt, dseq = get_tcp_behavior("youtube_full_video_traffic_home.pcap")

plt.figure(figsize=(10, 5))
plt.scatter(t, seq, s=2, color='black', label='Valid Packets')
plt.scatter(dt, dseq, s=50, color='red', marker='X', label='Retransmissions (Drops)')

plt.title("TCP Sequence Numbers and Packet Drops (Home Wi-Fi)")
plt.xlabel("Time (seconds)")
plt.ylabel("TCP Sequence Number")
plt.legend()
plt.show()