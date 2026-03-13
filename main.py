#!/usr/bin/env python
import sys
import signal
from config import BANNER, Color
from utils import parser

def signal_handler(sig, frame):
    print(f"\n{Color.RED}Interrupted. Exiting...{Color.RESET}")
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    print(BANNER)
    while True:
        try:
            user_input = input(f"{Color.GREEN}$>{Color.RESET} ")
        except EOFError:
            break
        if user_input.strip() == "quit" or user_input.strip() == "exit":
            break
        if user_input.strip() == "--help":
            from config import USAGE
            print(USAGE)
            continue
        parser.parse_args(user_input.split())


if __name__ == "__main__":
    main()
