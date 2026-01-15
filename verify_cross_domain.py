import requests as standard_requests
from curl_cffi import requests
import time
import sys
import os

# Import JA3 from utils to ensure exact match
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from lib.utils import JA3_STRING

def run_verification():
    print(f"[Verify] Initializing Session with JA3: OkHttp Standard")
    session = requests.Session(ja3=JA3_STRING)
    
    # 1. Simulate App Request (to prime session/IP reputation)
    print(f"[Verify] Step 1: App Search (cmapi.coupang.com)...")
    app_headers = {
        'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 15; SM-A165N Build/AP3A.240905.015.A2)',
        'x-coupang-origin-region': 'KR'
    }
    try:
        resp_app = session.get("https://cmapi.coupang.com/v3/products?filter=KEYWORD:%EB%8B%AC%EB%B9%9B%EC%88%98%EC%A0%9C%EC%8B%9D%ED%98%9C", headers=app_headers, timeout=10)
        print(f"      Status: {resp_app.status_code}")
        print(f"      Cookies: {session.cookies.get_dict()}")
    except Exception as e:
        print(f"      App Error: {e}")

    # 2. Cross-Domain Web Request (www.coupang.com)
    # User Hypothesis: "If I use this session to hit Web, I will get 429 (99.9%)"
    print(f"\n[Verify] Step 2: Web Search (www.coupang.com)...")
    
    # Use a standard Mobile Chrome UA (to be valid for Web) 
    # BUT keep the OkHttp TLS Fingerprint (cur_cffi session reused)
    web_headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'referer': 'https://www.coupang.com/'
    }
    
    try:
        # We reuse the SAME session (cookies preserved if any)
        url = "https://www.coupang.com/np/search?q=%EB%8B%AC%EB%B9%9B%EC%88%98%EC%A0%9C%EC%8B%9D%ED%98%9C"
        resp_web = session.get(url, headers=web_headers, timeout=10)
        
        print(f"      Status: {resp_web.status_code}")
        if resp_web.status_code == 429:
            print("      Result: BLOCKED (429) - User Hypothesis CONFIRMED")
        elif resp_web.status_code == 200:
            print("      Result: SUCCESS (200) - Akamai Passed!")
            if "akamai" in resp_web.text.lower() or "_abck" in str(session.cookies.get_dict()):
                 print("      Note: Akamai challenge/cookie detected.")
        else:
             print(f"      Result: {resp_web.status_code}")

    except Exception as e:
        print(f"      Web Error: {e}")

if __name__ == "__main__":
    run_verification()
