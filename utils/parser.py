from config import USAGE ,NOT_VALID, COMMAND_NOT_USED
from tools import tiny_scanner, dir_finder, host_mapper, header_grabber

def parse_args(args):
    if args[0] != "pentestkit":
        print(COMMAND_NOT_USED+"\n")
        return
    if len(args) < 2:
        print(NOT_VALID)
        return None
    if args[1] == '--help':
        print(USAGE)
        return None
    if args[1] not in ["-t", "-d", "-h", "-g"]:
        print(NOT_VALID)
        return None
    match args[1]:
        case "-t":
            if len(args) < 5 or args[1] != "-t" or args[3] != "-p":
                print(NOT_VALID)
                return None
            tiny_scanner.run(args[2], args[4].split(","))
        case "-h":
            return
        case "-d":
            return
        case "-g":
            return


    return args
