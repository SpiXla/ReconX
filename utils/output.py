import os

def save_results(filename, data):
    """Save results to file"""
    directory_path_str = "results"
    try :
        os.makedirs(directory_path_str,exist_ok=True)
    except:
        print(f"Error: Permission denied to create '{directory_path_str}'")
        return

    if data is None:
        data = ""
    with open(directory_path_str+"/"+filename, 'w') as f:
        f.write(str(data))
