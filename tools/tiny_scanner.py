import socket

# pentestkit -t 127.0.0.1 -p 8080,8000,22 
# pentestkit -t scanme.nmap.org -p 80,22,443,3306,8080
# pentestkit -t bandit.labs.overthewire.org -p 2220
# pentestkit -t ftp.debian.org -p 21
# pentestkit -t smtp.gmail.com -p 25
# pentestkit -t example.com -p 443,80
# pentestkit -t example.com -p 443,80

def grab_banner(s):
    try:
        s.send(b'\r\n')
        banner = s.recv(1024).decode().strip()
        if banner:
            return banner.split()[0].split('/')[0]
        return None
    except:
        return None

def get_service(port):
    services = {
        22: "SSH", 80: "HTTP", 443: "HTTPS", 21: "FTP",
        25: "SMTP", 53: "DNS", 110: "POP3", 143: "IMAP",
        3306: "MySQL", 5432: "PostgreSQL", 27017: "MongoDB",
        6379: "Redis", 8080: "HTTP-Proxy", 3389: "RDP"
    }
    return services.get(int(port), "Unknown")

def run(target, ports):
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((target, int(port)))
            banner = grab_banner(s)
            # print("banner: ", banner)
            service = banner if banner else get_service(port)
            print(f"Port {port} is open ({service})")
        except:
            print(f"Port {port} is closed")
        finally:
            s.close()
