from scapy.all import rdpcap, IP, ICMP

def analyze_icmp_packets(pcap_file):
    packets = rdpcap(pcap_file)
    for i, packet in enumerate(packets, start=1):
        if IP in packet and ICMP in packet:
            ip_total_length = packet[IP].len  # Total Length field from IP header
            ip_header_length = packet[IP].ihl * 4  # IHL field (in 32-bit words, so multiply by 4)
            icmp_header_length = 8  # ICMP header is always 8 bytes
            
            # Calculate ICMP payload size
            icmp_payload_size = ip_total_length - ip_header_length - icmp_header_length
            
            print(f"Packet {i}:")
            print(f"  Total Frame Length: {ip_total_length} bytes")
            print(f"  ICMP Payload Size: {icmp_payload_size} bytes")
            print()

if __name__ == "__main__":
    pcap_file = "example.pcap"  # Replace with the path to your pcap file
    analyze_icmp_packets(pcap_file)