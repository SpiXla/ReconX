#!/usr/bin/env python
from config import BANNER, FLAGS, Color
from utils import parser

def main():
    print(BANNER)
    while True:
        user_input = input(f"{Color.GREEN}{"$>"}{Color.RESET} ")
        if user_input == "quit" or user_input == "exit" :
            break
        parser.parse_args(user_input.split(" "))


if __name__ == "__main__":
    main()
