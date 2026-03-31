# ReconX 🛡️

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)

A multi-functional penetration testing toolkit for educational use.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Development Environment](#development-environment)
- [Usage](#usage)
- [Make Commands](#make-commands)
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
- Go 1.21+ (for tests)
- `requests` and `ping3` (via `make install`)

## Installation & Setup
Use Makefile:
```bash
make install      # Creates venv, installs deps
make setup        # Creates wordlists/results dirs
make run          # Starts app in venv
```
Or manual:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
make setup
make run
```

Config: Edit `config.py` for banners/colors.

## Development Environment
Kali/Ubuntu/macOS with Python/Go. Test on isolated VMs.

## Usage
```bash
make run
```
Interactive shell (`$>`):
- `-t scanme.nmap.org -p 22,80`
- `--help`
- `quit`

**Tools**:
- **TinyScanner** (`-t TARGET -p PORTS`)
- **DirFinder** (`-d URL -w WORDLIST`)
- **HostMapper** (`-n SUBNET`, requires root/sudo for raw ICMP scans)
- **HeaderGrabber** (`-g URL`)
- `-o FILE` → `./results/FILE`

## Make Commands
```bash
make help         # List all
make install      # Venv + deps
make run          # App
make test         # Python stub + Go servers (sudo for low ports)
make lint         # black/ruff/mypy (needs dev deps)
make clean        # Remove venv/caches
make setup        # Dirs/wordlist
```

## Output Format
Console real-time, `-o` → `./results/`.

## Testing Environment
**Make test** starts:
- Go port_scanning: TCP (21/22/25/80/3306/9000/1111)
- Go fuzzing: HTTP localhost:8080 (statuses/redirects)

Public: scanme.nmap.org, testphp.vulnweb.com.

## Privilege Requirements
- HostMapper: root/sudo required for ICMP scanning.
- make test: sudo for ports <1024.
- `sudo make test/run` if needed.

## Troubleshooting
- No venv: `make install`
- HostMapper permission error: run with `sudo` because raw ICMP requires root privileges
- Port bind: `sudo make test`, `pkill -f target.go`
- Mod not found: `make install`

## Known Limitations
- HostMapper depends on root/sudo access for ICMP host discovery.
- HTTP only.
- Unix-like.

## Legal & Ethical Guidelines
Educational/authorized only.

## Project Architecture
```
ReconX/
├── Makefile          # Dev workflow
├── main.py
├── config.py
├── requirements.txt
├── tools/            # Tools
├── utils/
├── wordlists/
├── results/          # Outputs
└── tests/            # Go targets
```
