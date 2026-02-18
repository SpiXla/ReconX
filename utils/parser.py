from config import USAGE, NOT_VALID, COMMAND_NOT_USED
from tools import tiny_scanner, dir_finder, host_mapper, header_grabber

def parse_args(args):
    if len(args) < 2:
        print(COMMAND_NOT_USED)
        return None
    
    if args[0] != 'pentestkit':
        print(COMMAND_NOT_USED)
        return None
    
    if args[1] == '--help':
        print(USAGE)
        return None
    
    if args[1] not in ['-t', '-d', '-n', '-g', '-o']:
        print(NOT_VALID)
        return None
    
    try:
        match args[1]:
            case '-t':
                if len(args) < 5 or args[3] != '-p':
                    print(NOT_VALID)
                    return None
                ports = args[4].split(',')
                if not ports or not all(p.strip().isdigit() for p in ports):
                    print("Error: Invalid port format")
                    return None
                result = tiny_scanner.run(args[2], ports)
                print(result)
            
            case '-d':
                if len(args) < 5 or args[3] != '-w':
                    print(NOT_VALID)
                    return None
                result = dir_finder.run(args[2], args[4])
                print(result)
            
            case '-n':
                if len(args) < 3:
                    print(NOT_VALID)
                    return None
                result = host_mapper.run(args[2])
                print(result)
            
            case '-g':
                if len(args) < 3:
                    print(NOT_VALID)
                    return None
                result = header_grabber.run(args[2])
                print(result)
    
    except Exception as e:
        print(f"Error: {e}")
        return None
    
    return None
