from scapy.all import *
import random
import socket

# --- Task A: TCP SYN Probe ---
print("Forging TCP SYN Probe to www.bu.edu on port 443...")

# Resolve the target IP
target_ip_tcp = socket.gethostbyname("www.bu.edu")
# Generate a random source port
src_port = random.randint(1024, 65535)

# Build the layers
ip_layer_tcp = IP(dst=target_ip_tcp)
# dport is 443 (HTTPS), flags="S" means SYN
tcp_layer = TCP(sport=src_port, dport=443, flags="S", seq=1000)

# Stack the layers
tcp_pkt = ip_layer_tcp / tcp_layer

# Send packet and wait for 1 response (sr1)
print(f"Sending to {target_ip_tcp}:{src_port}...")
tcp_resp = sr1(tcp_pkt, timeout=5)

if tcp_resp:
    print("Received TCP Response!")
else:
    print("No TCP response received.")


# --- Task B: DNS Query ---
print("\nForging DNS Query for www.ietf.org to 8.8.8.8...")

target_ip_dns = "8.8.8.8"

# Build the layers
ip_layer_dns = IP(dst=target_ip_dns)
udp_layer = UDP(dport=53)
# rd=1 means "Recursion Desired". qd specifies the Question Data.
dns_layer = DNS(rd=1, qd=DNSQR(qname="www.ietf.org", qtype="A"))

# Stack the layers
dns_pkt = ip_layer_dns / udp_layer / dns_layer

# Send packet and wait for 1 response
print(f"Sending DNS query...")
dns_resp = sr1(dns_pkt, timeout=5)

if dns_resp:
    print("Received DNS Response!")
else:
    print("No DNS response received.")