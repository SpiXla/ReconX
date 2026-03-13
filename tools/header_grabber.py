import requests
from config import Color

SECURITY_HEADERS = [
    'X-Content-Type-Options',
    'X-Frame-Options',
    'Content-Security-Policy',
    'Strict-Transport-Security',
    'X-XSS-Protection'
]

def run(url):
    if not url.startswith('http'):
        url = 'http://' + url
    
    try:
        response = requests.get(url, timeout=10)
        
        print(f"\nHTTP/1.1 {response.status_code} {response.reason}\n")
        
        for key, value in response.headers.items():
            print(f"{Color.BLUE}{key}:{Color.RESET} {value}")
        
        missing = [h for h in SECURITY_HEADERS if h not in response.headers]
        
        if missing:
            print(f"\n{Color.RED}Warning: Missing Security Headers - {', '.join(missing)}{Color.RESET}")
        
        return ""
        
    except requests.exceptions.RequestException as e:
        error_msg = f"Error: {e}"
        print(f"{Color.RED}{error_msg}{Color.RESET}")
        return error_msg
