BANNER = r"""
 ____            _            _     _  __ _ _
|  _ \ ___ _ __ | |_ ___  ___| |_  | |/ /(_) |_
| |_) / _ \ '_ \| __/ _ \/ __| __| | ' / | | __|
|  __/  __/ | | | ||  __/\__ \ |_  | . \ | | |_
|_|   \___|_| |_|\__\___||___/\__| |_|\_\|_|\__|
                P E N T E S T - K I T
"""

FLAGS = ["-t", "-d", "-h", "-g", "-o"]
COMMAND_NOT_USED = "Usage error: No command provided. Use (pentestkit --help) for usage information."
NOT_VALID = "Invalid option. Use --help for usage information."

USAGE = """Welcome to PentestKit

OPTIONS:

   -t  TinyScanner   Run the simple port scanner.
                     Use this option to specify the target IP address and the ports you wish to scan.
                     Example: -t 192.168.1.1 -p 22,80,443

   -d  DirFinder     Run the directory brute-forcer.
                     Use this option to specify the target URL and the path to a wordlist for discovering hidden directories.
                     Example: -d http://example.com -w /path/to/wordlist.txt

   -h  HostMapper    Run the network host mapper.
                     Use this option to perform a ping sweep on a specified subnet to identify live hosts.
                     Example: -h 192.168.1.0/24

   -g  HeaderGrabber Run the HTTP header analyzer.
                     Use this option to retrieve and analyze HTTP headers from a specified URL, useful for identifying security headers.
                     Example: -g http://example.com

   -o  "FileName"    File name to save output.
                     Use this option to specify the file name where the results of the scan or analysis will be saved.
                     Example: -o result.txt
"""

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
