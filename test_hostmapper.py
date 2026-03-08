#!/usr/bin/env python3
from tools.host_mapper import run

if __name__ == "__main__":
    # Test with your local network subnet
    # Examples:
    # run("192.168.1.0/24")  # Scan 254 hosts
    # run("192.168.1.0/28")  # Scan 14 hosts (smaller, faster)
    # run("10.0.0.0/24")     # Different subnet
    
    subnet = input("Enter subnet (e.g., 192.168.1.0/24): ")
    print(f"\nScanning {subnet}...\n")
    run(subnet)
