import requests
import random
import json

PROXY_API_URL = "http://mkt.techb.kr:3001/api/proxy/status?remain=30"

def get_random_proxy():
    """
    Fetches the proxy list from the API and returns a random SOCKS5 proxy URL.
    Returns:
        str: "socks5://IP:PORT" or None if failed.
    """
    try:
        print(f"[ProxyManager] Fetching proxies from {PROXY_API_URL}...")
        resp = requests.get(PROXY_API_URL, timeout=5)
        resp.raise_for_status()
        
        data = resp.json()
        if not data.get("success") or not data.get("proxies"):
            print("[ProxyManager] No proxies available in API response.")
            return None
            
        proxies = data["proxies"]
        print(f"[ProxyManager] Found {len(proxies)} candidates.")
        
        selected = random.choice(proxies)
        proxy_address = selected.get("proxy") # "IP:PORT"
        
        if not proxy_address:
            print("[ProxyManager] selected proxy has no address.")
            return None
            
        # Format as socks5://IP:PORT
        proxy_url = f"socks5://{proxy_address}"
        print(f"[ProxyManager] Selected: {proxy_url} (External IP: {selected.get('external_ip')})")
        return proxy_url
        
    except Exception as e:
        print(f"[ProxyManager] Failed to fetch proxy: {e}")
        return None
