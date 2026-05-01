import pyshark
import matplotlib.pyplot as plt
from collections import defaultdict

def get_throughput(pcap_file):
    cap = pyshark.FileCapture(pcap_file, display_filter='ip')
    
    # Dictionary to hold bytes per second
    bytes_per_sec = defaultdict(int)
    first_time = None

    for pkt in cap:
        try:
            timestamp = float(pkt.sniff_timestamp)
            if first_time is None:
                first_time = timestamp
            
            # Round down to the nearest second
            sec = int(timestamp - first_time)
            bytes_per_sec[sec] += int(pkt.length)
        except AttributeError:
            continue
            
    cap.close()
    
    # Convert dictionaries to sorted lists for plotting
    times = sorted(bytes_per_sec.keys())
    # Convert bytes to Megabits (bytes * 8 / 1,000,000)
    mbps = [(bytes_per_sec[t] * 8) / 1000000 for t in times]
    
    return times, mbps

print("Calculating bandwidth... this will take a moment.")

files = [
    ("zoom_traffic_home.pcap", "Zoom"),
    ("youtube_full_video_traffic_home.pcap", "YouTube (Steady)"),
    ("youtube_multp_video_traffic_home.pcap", "YouTube (Clicking)"),
    ("bbc_traffic_home.pcap", "BBC News")
]

fig, axs = plt.subplots(2, 2, figsize=(14, 8))
axs = axs.flatten()

for i, (filename, title) in enumerate(files):
    print(f"Processing {filename}...")
    times, mbps = get_throughput(filename)
    
    axs[i].plot(times, mbps, color='green', linewidth=2)
    axs[i].set_title(title + " Bandwidth")
    axs[i].set_xlabel("Time (seconds)")
    axs[i].set_ylabel("Throughput (Mbps)")
    axs[i].grid(True)

plt.tight_layout()
plt.show()