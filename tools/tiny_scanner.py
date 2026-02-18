import socket
import threading
from concurrent.futures import ThreadPoolExecutor

# pentestkit -t 127.0.0.1 -p 8080,8000,22 
# pentestkit -t scanme.nmap.org -p 80,22,443,3306,8080
# pentestkit -t bandit.labs.overthewire.org -p 2220
# pentestkit -t ftp.debian.org -p 21
# pentestkit -t smtp.gmail.com -p 25
# pentestkit -t example.com -p 443,80
# pentestkit -t localhost -p 22,21,80,25,9000,3306,1111


def grab_banner(s):
    try:
        s.settimeout(5)
        s.send(b'\r\n')
        banner = s.recv(1024).decode().strip()
        return banner
    except:
        return None

def get_service_from_banner(banner):
    banner_lower = banner.lower()
    if 'ssh' in banner_lower:
        return 'SSH'
    if 'https' in banner_lower:
        return 'HTTPS'
    elif 'ftp' in banner_lower:
        return 'FTP'
    elif 'smtp' in banner_lower or 'mail' in banner_lower:
        return 'SMTP'
    elif 'http' in banner_lower or 'apache' in banner_lower or 'nginx' in banner_lower:
        return 'HTTP'
    elif 'mysql' in banner_lower:
        return 'MySQL'
    elif 'postgres' in banner_lower:
        return 'PostgreSQL'
    elif 'redis' in banner_lower:
        return 'Redis'
    
    return None

def get_service(port):
    services = {
        22: "SSH", 80: "HTTP", 443: "HTTPS", 21: "FTP",
        25: "SMTP", 53: "DNS", 110: "POP3", 143: "IMAP",
        3306: "MySQL", 5432: "PostgreSQL", 27017: "MongoDB",
        6379: "Redis", 8080: "HTTP-Proxy", 3389: "RDP"
    }
    return services.get(int(port), "Unknown")

def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect((target, int(port)))
        banner = grab_banner(s)
        if banner:
            # print(f"Banner for port {port}: {banner}")
            service = get_service_from_banner(banner) or get_service(port)
            return f"Port {port} is open ({service})"
        return f"Port {port} is open ({get_service(port)})"
    except:
        return f"Port {port} is closed"
    finally:
        s.close()

def run(target, ports):
    results = []
    threads = []
    
    def worker(port):
        result = scan_port(target, port)
        results.append(result)
    
    for port in ports:
        thread = threading.Thread(target=worker, args=(port,))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    return "\n".join(results)