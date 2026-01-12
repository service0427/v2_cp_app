
import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.getcwd())

from lib.schedule import 128_G_v3_SEARCH_products as search_module
from lib.device_profile import DEFAULT_PROFILE

def test():
    session = requests.Session()
    # Mock/Setup session if needed (e.g. headers)
    # But the module sets its own headers.
    
    response = search_module.run(session)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        try:
            data = response.json()
            # Print keys to avoid huge output
            print("Top Level Keys:", data.keys())
            if 'rData' in data:
                print("rData Keys:", data['rData'].keys())
                if 'searchId' in data['rData']:
                    print(f"FOUND searchId: {data['rData']['searchId']}")
                if 'totalCount' in data['rData']:
                     print(f"FOUND totalCount: {data['rData']['totalCount']}")
            else:
                # Fallback check
                print(json.dumps(data, indent=2)[:500]) 
                
        except Exception as e:
            print(f"Failed to parse JSON: {e}")
            print(response.text[:500])
    else:
        print(response.text[:500])

if __name__ == "__main__":
    test()
