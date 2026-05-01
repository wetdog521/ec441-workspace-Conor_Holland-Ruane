import pyshark
import matplotlib.pyplot as plt

def get_tcp_behavior(pcap_file):
    # Only look at TCP
    cap = pyshark.FileCapture(pcap_file, display_filter='tcp')
    
    times = []
    seq_nums = []
    
    drop_times = []
    drop_seqs = []
    
    first_time = None

    for pkt in cap:
        try:
            timestamp = float(pkt.sniff_timestamp)
            if first_time is None:
                first_time = timestamp
            
            time_norm = timestamp - first_time
            seq = int(pkt.tcp.seq)
            
            times.append(time_norm)
            seq_nums.append(seq)
            
            # Check if Wireshark flagged this as a retransmission
            if hasattr(pkt.tcp, 'analysis_retransmission'):
                drop_times.append(time_norm)
                drop_seqs.append(seq)
                
        except AttributeError:
            continue
            
    cap.close()
    return times, seq_nums, drop_times, drop_seqs

print("Hunting for TCP drops in YouTube traffic...")
# Using the steady YouTube video file for this test
t, seq, dt, dseq = get_tcp_behavior("youtube_full_video_traffic_home.pcap")

plt.figure(figsize=(10, 5))
plt.scatter(t, seq, s=2, color='black', label='Valid Packets')
plt.scatter(dt, dseq, s=50, color='red', marker='X', label='Retransmissions (Drops)')

plt.title("TCP Sequence Numbers and Packet Drops")
plt.xlabel("Time (seconds)")
plt.ylabel("TCP Sequence Number")
plt.legend()
plt.show()