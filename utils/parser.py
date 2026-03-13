from config import USAGE, NOT_VALID, COMMAND_NOT_USED, BANNER
from tools import tiny_scanner, dir_finder, host_mapper, header_grabber
from utils.output import save_results

def parse_args(args):
    if not args:
        print(COMMAND_NOT_USED)
        return
    
    if args[0] == '--help':
        print(USAGE)
        return
    
    valid_flags = {'-t', '-d', '-n', '-g', '-o'}
    if args[0] not in valid_flags:
        print(NOT_VALID)
        return
    
    target = None
    url = None
    subnet = None
    graburl = None
    ports = None
    wordlist = None
    output = None
    
    i = 0
    while i < len(args):
        arg = args[i]
        
        if arg == '-t':
            if i + 1 >= len(args):
                print(NOT_VALID)
                return
            target = args[i + 1]
            i += 2
        elif arg == '-d':
            if i + 1 >= len(args):
                print(NOT_VALID)
                return
            url = args[i + 1]
            i += 2
        elif arg == '-n':
            if i + 1 >= len(args):
                print(NOT_VALID)
                return
            subnet = args[i + 1]
            i += 2
        elif arg == '-g':
            if i + 1 >= len(args):
                print(NOT_VALID)
                return
            graburl = args[i + 1]
            i += 2
        elif arg == '-p':
            if i + 1 >= len(args):
                print(NOT_VALID)
                return
            ports = args[i + 1]
            i += 2
        elif arg == '-w':
            if i + 1 >= len(args):
                print(NOT_VALID)
                return
            wordlist = args[i + 1]
            i += 2
        elif arg == '-o':
            if i + 1 >= len(args):
                print(NOT_VALID)
                return
            output = args[i + 1]
            i += 2
        else:
            print(NOT_VALID)
            return
    
    if target:
        if not ports:
            print(NOT_VALID)
            return
        port_list = ports.split(',')
        if not all(p.strip().isdigit() for p in port_list):
            print("Error: Invalid port format")
            return
        result = tiny_scanner.run(target, port_list)
        print(result)
        if output:
            save_results(output, result)
            print(f"Data saved in {output}")
    
    elif url:
        if not wordlist:
            print(NOT_VALID)
            return
        result = dir_finder.run(url, wordlist)
        print(result)
        if output:
            save_results(output, result)
            print(f"Data saved in {output}")
    
    elif subnet:
        result = host_mapper.run(subnet)
        if output:
            save_results(output, result)
            print(f"Data saved in {output}")
    
    elif graburl:
        result = header_grabber.run(graburl)
        print(result)
        if output:
            save_results(output, result)
            print(f"Data saved in {output}")
    
    else:
        print(NOT_VALID)


if __name__ == "__main__":
    import sys
    print(BANNER)
    if len(sys.argv) > 1 and sys.argv[1] == '--help':
        print(USAGE)
    else:
        parse_args(sys.argv[1:])
