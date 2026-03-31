# Test Commands

Reference commands for manually testing the tools.

## HostMapper

```bash
-n 127.0.0.1/32
-n 192.168.1.0/24
-n 192.168.100.0/24
```

## TinyScanner

```bash
-t 127.0.0.1 -p 8080,8000,22
-t scanme.nmap.org -p 80,22,443,3306,8080
-t bandit.labs.overthewire.org -p 2220
-t ftp.debian.org -p 21
-t smtp.gmail.com -p 25
-t example.com -p 443,80
-t localhost -p 22,21,80,25,9000,3306,1111
```

## DirFinder

```bash
-d http://example.com -w ./wordlists/common.txt
-d http://localhost:8080 -w ./wordlists/common.txt
```
