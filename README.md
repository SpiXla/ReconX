# Pentest-Kit 🛡️

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)

A multi-functional penetration testing toolkit for educational use.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Development Environment](#development-environment)
- [Usage](#usage)
- [Output Format](#output-format)
- [Testing Environment](#testing-environment)
- [Privilege Requirements](#privilege-requirements)
- [Troubleshooting](#troubleshooting)
- [Known Limitations](#known-limitations)
- [Legal & Ethical Guidelines](#legal--ethical-guidelines)
- [Project Architecture](#project-architecture)
- [License](#license)
- [Contributing](#contributing)

## Prerequisites
- Python 3.8+
- `requests` and `ping3` (installed via requirements.txt)
- Wordlists for DirFinder (directory optional, create `./wordlists/common.txt`)

## Installation & Setup
```bash
git clone <repo-url>  # e.g., https://github.com/username/pentest-kit.git
cd pentest-kit
pip install -r requirements.txt
mkdir -p wordlists results  # Optional dirs
python main.py --help
```


Configuration: Edit `config.py` for custom banners/colors/USAGE if needed.

## Development Environment
Recommended: Kali Linux VM or Ubuntu with Python. No special VM setup required. Test on isolated network/VMs (e.g., VirtualBox with NAT/Host-only).

## Usage
Run `python main.py` to start the interactive pentest shell.

Once in the shell (`$>` prompt):
- Enter command flags directly (space-separated), e.g., `-t scanme.nmap.org -p 22,80,443`
- Type `--help` to show full usage.
- Type `quit` or `exit` to leave the shell.

**Tools & Flags** (from `--help`):

**TinyScanner** (`-t TARGET -p PORTS`): TCP port scan with banner/service detection.
- Example (in shell): `-t scanme.nmap.org -p 22,80,443 -o scan_results.txt`
- Params: `-t` IP/hostname, `-p` comma-separated ports (default common).

**DirFinder** (`-d URL -w WORDLIST`): Brute-force directories.
- Example (in shell): `-d http://test.com -w wordlists/common.txt -o dirs.txt`
- Params: `-d` base URL, `-w` wordlist path. Uses threads, checks !=404.

**HostMapper** (`-n SUBNET`): Ping sweep for live hosts.
- Example (in shell): `-n 192.168.1.0/24 -o hosts.txt`
- Params: `-n` CIDR (e.g., 10.0.0.0/24).

**HeaderGrabber** (`-g URL`): Fetch/analyze HTTP headers, check security.
- Example (in shell): `-g https://example.com -o headers.txt`
- Params: `-g` URL (auto http:// if needed).

**Common Flag**: `-o FILENAME` saves to `./results/FILENAME`.

## Output Format
- Console: Real-time results (e.g., "Port 80 open (HTTP)").
- File: `./results/FILENAME` – plain text summary.

## Testing Environment
**Golang Test Targets** (pure stdlib; no deps):
- Port scanning: `cd tests/port_scanning && go run port_scanning_target.go` (TCP servers on 21/FTP, 22/SSH, 25/SMTP, 80/HTTP, 3306/MySQL, 9000/slow, 1111/HTTPS sim).
- Fuzzing/DirFinder: `cd tests/fuzzing && go run fuzz_target.go` (HTTP on localhost:8080; paths: /admin=200, /created=201, /old-page=301→/admin, /temp-redirect=302→/login, /bad=400, /private=401, /uploads=403, /method POST=200 else 405, /crash=500, /maintenance=503, else 404).

**Public Targets**:
- scanme.nmap.org (ports)
- http://testphp.vulnweb.com (dirs/headers)

**Setup**: Use isolated VMs/network for HostMapper/DirFinder tests.

## Privilege Requirements
- **TinyScanner/DirFinder/HeaderGrabber**: User-level (TCP/HTTP).
- **HostMapper**: May require root/sudo for ICMP ping (ping3 limitation); fails silently otherwise.
- Run `sudo python main.py ...` if ping issues.

## Troubleshooting
- **No wordlist**: Create `./wordlists/common.txt` with dirs (e.g., admin, login).
- **Ping fails**: Use sudo, check firewall/ICMP.
- **Requests errors**: Proxy/firewall; increase timeout in code.
- **Permission denied**: chmod +x *.py, mkdir results.
- **Module not found**: `pip install -r requirements.txt`.

## Known Limitations
- HostMapper: ICMP-dependent, silent fail on firewalls/no privs; max 50 threads.
- DirFinder/HeaderGrabber: HTTP only (requests lib), no HTTPS bypass, timeout=5/10s.
- No raw sockets (needs root for SYN scan).
- Environment: Unix-like (macOS/Linux); Windows ping3 may vary.
- Wordlists empty by default.

## Legal & Ethical Guidelines
⚠️ **Educational/authorized use ONLY.** 
- Obtain written permission before scanning.
- Comply with CFAA/laws.
- Do not target production systems without approval.
- Report vulnerabilities responsibly.

## Project Architecture
```
pentest-kit/
├── main.py              # CLI parser
├── config.py            # Configs
├── requirements.txt     # requests, ping3
├── tools/
│   ├── tiny_scanner.py  # socket/thread port scan
│   ├── dir_finder.py    # requests brute-force
│   ├── host_mapper.py   # ping3 sweep
│   └── header_grabber.py # requests headers
├── utils/
│   ├── output.py        # Save to results/
│   └── parser.py        # Arg parsing
├── wordlists/           # Create common.txt
├── results/             # Outputs
└── tests/               # Go test targets
```

