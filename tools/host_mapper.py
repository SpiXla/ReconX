import ipaddress
from ping3 import ping
import concurrent.futures
import threading

# pentestkit -n 127.0.0.1/32
# pentestkit -n 192.168.1.0/24
# pentestkit -n 192.168.100.0/24

output_lock = threading.Lock()

def check_host(ip_str):
    try:
        response_time = ping(ip_str, timeout=4)
        if response_time is not None:
            return f"{ip_str} is reachable (delay: {response_time:.4f}s)"
    except Exception as e:
        # return f"Error pinging {ip_str}: {e}"
        pass

def run(subnet):
    network = ipaddress.ip_network(subnet, strict=False)
    # Generate a list of all host IPs in the subnet
    hosts = [str(ip) for ip in network.hosts()]
    results = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        # Map the check_host function to the list of hosts
        results = list(executor.map(check_host, hosts))

    up_hosts = [result for result in results if result]
    output = []
    if not up_hosts:
        output.append("No hosts are up")
    else:
        output.append("Live hosts found:")
        for result in up_hosts:
            output.append(result.split()[0])
    
    with output_lock:
        for line in output:
            print(line)
    
    return "\n".join(output)

