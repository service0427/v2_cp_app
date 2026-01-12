import json
import urllib.parse
import re
import os

def parse_capture_file(filepath):
    """
    Parses a JSON capture file to extract search query and product interaction details.
    
    Returns:
        dict: containing 'q', 'productId', 'itemId', 'vendorItemId'
    """
    if not os.path.exists(filepath):
        print(f"[CaptureParser] Error: File nt found: {filepath}")
        return None

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"[CaptureParser] Error loading JSON: {e}")
        return None

    requests_list = data.get('requests', [])
    if not requests_list:
        print("[CaptureParser] No requests found in capture file.")
        return None

    result = {
        'q': None,
        'productId': None,
        'itemId': None,
        'vendorItemId': None
    }

    # 1. Find Search Query
    # Look for /v3/products?filter=KEYWORD:...
    for req in requests_list:
        url = req.get('url', '')
        if '/v3/products' in url and 'filter=' in url:
            # Extract keyword from filter param
            try:
                parsed = urllib.parse.urlparse(url)
                params = urllib.parse.parse_qs(parsed.query)
                filter_val = params.get('filter', [''])[0]
                
                # Format: KEYWORD:value|...
                match = re.search(r'KEYWORD:([^|]+)', filter_val)
                if match:
                    result['q'] = urllib.parse.unquote(match.group(1))
                    print(f"[CaptureParser] Found Search Query: {result['q']}")
                    break
            except Exception as e:
                print(f"[CaptureParser] Error parsing search request: {e}")

    # Fallback: Check auto-complete if v3/products not found (less reliable but possible)
    if not result['q']:
        for req in requests_list:
            url = req.get('url', '')
            if '/auto-completes' in url and 'keyword=' in url:
                 try:
                    parsed = urllib.parse.urlparse(url)
                    params = urllib.parse.parse_qs(parsed.query)
                    result['q'] = params.get('keyword', [''])[0]
                    print(f"[CaptureParser] Found Query from AutoComplete: {result['q']}")
                    break
                 except: pass

    # 2. Find Product Interaction (Click)
    # Look for /sdp/v2/platform/products/{productId}
    for req in requests_list:
        url = req.get('url', '')
        # Pattern: .../products/{productId}?
        # Exclusion: /products/components, /products/brand-shop etc.
        # Strict pattern for PDP: /sdp/v2/platform/products/(\d+)
        
        match = re.search(r'/sdp/v2/platform/products/(\d+)', url)
        if match:
            result['productId'] = match.group(1)
            
            # Extract other IDs from params
            try:
                parsed = urllib.parse.urlparse(url)
                params = urllib.parse.parse_qs(parsed.query)
                
                result['itemId'] = params.get('itemId', [''])[0]
                result['vendorItemId'] = params.get('vendorItemId', [''])[0]
                result['rank'] = params.get('rank', [''])[0]
                
                # Verify logic: Must have productId.
                if result['productId']:
                    print(f"[CaptureParser] Found Product: {result['productId']}, Rank: {result['rank']}")
                    break
            except: pass

    return result
