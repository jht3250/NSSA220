#!/usr/bin/env python3

from scapy.all import *

def calculate_metrics(pcap_file, source_ip, target_ips):
    """
    Calculate ICMP metrics from a given pcap file.

    Args:
        pcap_file (str): Path to the pcap file.
        source_ip (str): Source IP address for metrics calculation.
        target_ips (list): List of target IPs for specific metrics.

    Returns:
        dict: A dictionary containing overall and IP-specific metrics.
    """
    # Read the pcap file
    packets = rdpcap(pcap_file)

    # Initialize metrics
    metrics = {
        "Echo Requests Sent": 0,
        "Echo Requests Received": 0,
        "Echo Replies Sent": 0,
        "Echo Replies Received": 0,
        "Echo Request Bytes Sent": 0,
        "Echo Request Bytes Received": 0,
        "Echo Request Data Sent": 0,
        "Echo Request Data Received": 0,
        "IP Address Metrics": {}
    }

    # Process packets
    for packet in packets:
        if ICMP in packet and IP in packet:
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            icmp_type = packet[ICMP].type
            icmp_len = len(packet[ICMP])
            icmp_data_len = icmp_len - 8  # Subtract ICMP header size (8 bytes)

            # Echo Request
            if icmp_type == 8:  # ICMP Echo Request
                if ip_src == source_ip:
                    metrics["Echo Requests Sent"] += 1
                    metrics["Echo Request Bytes Sent"] += icmp_len
                    metrics["Echo Request Data Sent"] += icmp_data_len
                elif ip_dst == source_ip:
                    metrics["Echo Requests Received"] += 1
                    metrics["Echo Request Bytes Received"] += icmp_len
                    metrics["Echo Request Data Received"] += icmp_data_len

            # Echo Reply
            elif icmp_type == 0:  # ICMP Echo Reply
                if ip_src == source_ip:
                    metrics["Echo Replies Sent"] += 1
                elif ip_dst == source_ip:
                    metrics["Echo Replies Received"] += 1

            # IP-specific metrics
            for target_ip in target_ips:
                if ip_src == target_ip or ip_dst == target_ip:
                    if target_ip not in metrics["IP Address Metrics"]:
                        metrics["IP Address Metrics"][target_ip] = 0
                    metrics["IP Address Metrics"][target_ip] += 1
    return metrics

def print_metrics(metrics):
    """
    Print the calculated metrics in a formatted manner.

    Args:
        metrics (dict): Dictionary containing the calculated metrics.
    """
    print("Overall Metrics:")
    for key, value in metrics.items():
        if key != "IP Address Metrics":
            print(f"{key}: {value}")

    print("\nIP Address-Specific Metrics:")
    for ip, count in metrics["IP Address Metrics"].items():
        print(f"{ip}: {count}")

if __name__ == "__main__":
    # Define the source IP and target IPs
    source_ip = "192.168.100.1"
    target_ips = ["192.168.200.1", "192.168.100.2", "192.168.200.2"]

    # Calculate metrics
    metrics = calculate_metrics("Node1.pcap", source_ip, target_ips)

    # Print metrics
    print_metrics(metrics)