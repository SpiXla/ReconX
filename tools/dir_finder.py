import concurrent.futures
import requests

def run(url, wordlist):
    url = url.rstrip('/')
    res = f"Directory Finder Results for {url} \n"
    dirs = []
    headers = {'User-Agent': 'Mozilla/5.0'}
    found = 0
    try:
        with open(wordlist, 'r') as file:
            content = file.read() 
            dirs = content.splitlines()
            
            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = {executor.submit(requests.get, f"{url}/{dir}", headers=headers, timeout=5): dir for dir in dirs}
                for future in concurrent.futures.as_completed(futures):
                    dir = futures[future]
                    try:
                        response = future.result()
                        if response.status_code != 404:
                            res += f"/{dir}      [Status: {response.status_code}]\n"
                            found += 1
                    except Exception:
                        pass

    except FileNotFoundError:
        print(f"Error: The file '{wordlist}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    if found == 0:
        res += "No directories found.\n"
    return res