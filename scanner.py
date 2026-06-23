# simple-network-scanner
# This script performs a basic ping to check for active devices on a local network.

import os

def scan_network(network_prefix):
    print(f"Scanning network: {network_prefix}.0/24")
    for i in range(1, 255):
        ip = f"{network_prefix}.{i}"
        # Ping the IP address
        response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")
        if response == 0:
            print(f"Device found: {ip}")

# Example usage: Change '192.168.1' to your local network prefix
scan_network("192.168.1")

