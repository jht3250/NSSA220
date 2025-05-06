#!/usr/bin/env python3

from scapy.all import *

# Calculate ICMP metrics from a given pcap file.
# Args: pcap_file (str): The path to the pcap file.
# Returns: a dictionary containing metrics for Echo Requests and Replies from particular IPs.
def calculate_metrics(pcap_file):
    packets = rdpcap(pcap_file)
    metrics = {
        "Echo Requests Received from 192.168.100.2": 0,
        "Echo Request Bytes Sent to 192.168.200.2": 0,
        "Echo Request Data Sent to 192.168.200.2": 0
    }

    for packet in packets:
        if ICMP in packet and IP in packet:
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            icmp_type = packet[ICMP].type
            icmp_len = len(packet)
            icmp_data_len = len(packet[ICMP]) - 8  # Subtract ICMP header from total length

            # Count Echo Requests received from 192.168.100.2
            if icmp_type == 8 and ip_src == "192.168.100.2":
                metrics["Echo Requests Received from 192.168.100.2"] += 1

            # Count Echo Request bytes and data sent to 192.168.200.2
            if icmp_type == 8 and ip_dst == "192.168.200.2":
                metrics["Echo Request Bytes Sent to 192.168.200.2"] += icmp_len
                metrics["Echo Request Data Sent to 192.168.200.2"] += icmp_data_len

    return metrics

def main():
    # Path to the pcap file
    pcap_file = "TeddyBallgame.pcap"

    # Calculate metrics
    metrics = calculate_metrics(pcap_file)

    # Print metrics
    for key, value in metrics.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()