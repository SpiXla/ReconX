# Pentest-Kit

A multi-functional penetration testing toolkit.

## Features

- **TinyScanner**: Port scanner
- **DirFinder**: Directory brute-forcer
- **HostMapper**: Network host mapper
- **HeaderGrabber**: HTTP header analyzer

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py -t 192.168.1.1 -p 22,80,443 -o results.txt
```

## Legal Notice

⚠️ For educational purposes only. Always obtain permission before testing.

## Project Architecture
````

pentest-kit/
├── main.py
├── config.py
├── tools/
│   ├── __init__.py
│   ├── tiny_scanner.py
│   ├── dir_finder.py
│   ├── host_mapper.py
│   └── header_grabber.py
├── utils/
│   ├── __init__.py
│   ├── output.py
│   ├── network.py
│   └── parser.py
├── wordlists/
│   └── common.txt
├── results/
└── README.md
````
