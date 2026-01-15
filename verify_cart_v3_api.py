import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE, DeviceProfile
from lib.common.utils import generate_common_payload

def test_cart_v3(session: requests.Session):
    # Hardcoded test data from 06_Action_Add_To_Cart.py
    product_id = 9024146312
    item_id = 26462223018
    vendor_item_id = 93437504336
    quantity = 1
    
    # URL - Found in APK: /v3/cart/products/%s/add
    # Trying api-gateway first, usually where v3 apis live.
    url = f"https://api-gateway.coupang.com/v3/cart/products/{product_id}/add"
    
    # Headers
    device = DEFAULT_PROFILE
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'accept-encoding': 'gzip',
        'user-agent': device.get_okhttp_user_agent(),
        'x-coupang-origin-region': 'KR',
        'x-coupang-app': device.get_coupang_app_header()
    }
    
    # Payload - List of AddToCartItemInfo
    # Fields: vendorItemId, quantity, productId, itemId
    payload = [
        {
            "vendorItemId": str(vendor_item_id),
            "quantity": quantity,
            "productId": str(product_id),
            "itemId": str(item_id)
        }
    ]
    
    print(f"Testing Cart V3 API...")
    print(f"URL: {url}")
    print(f"Payload: {json.dumps(payload, indent=2)}")
    
    try:
        response = session.post(url, headers=headers, json=payload)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code != 200:
             # Try alternate host if first fails (just in case)
             alt_url = f"https://ljc.coupang.com/v3/cart/products/{product_id}/add"
             print(f"Retrying with alternate host: {alt_url}")
             response = session.post(alt_url, headers=headers, json=payload)
             print(f"Status Code: {response.status_code}")
             print(f"Response: {response.text}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    session = requests.Session()
    # In a real scenario, session would have cookies/tokens. 
    # This test might fail 401/403 if not logged in, but we want to see if the endpoint exists (not 404).
    test_cart_v3(session)
