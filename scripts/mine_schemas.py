import os
import json
import glob
from urllib.parse import urlparse
import re # Added for re.search

CAPTURE_DIR = "/home/tech/v2_cp_app/captures"
OUTPUT_FILE = "/home/tech/v2_cp_app/schema_mining_report.json"

# Key URL patterns to identify "Anchor Events"
SEARCH_URL_PART = "/v3/products"
# Updated based on 145_G source code
PRODUCT_DETAIL_URL_PART = "/sdp/v2/platform/products" 
CART_URL_PART = "/sdp/v2/widget/products/.*/add-to-cart"
BULKSUBMIT_URL_PART = "/v2/bulksubmit"

# Anchor definitions (for potential future use or clarity)
SEARCH_ANCHOR = "Search Anchor"
PRODUCT_DETAIL_ANCHOR = "Product Detail Anchor"
CART_ANCHOR = "Add to Cart Anchor"

def mine_captures():
    files = glob.glob(os.path.join(CAPTURE_DIR, "*.json"))
    
    # Store schemas found:
    # {
    #   "SEARCH": { "124_53": { "count": 10, "example_file": "..." } },
    #   "PRODUCT": { ... }
    # }
    mining_results = {
        "SEARCH_BEFORE": {},
        "SEARCH_AFTER": {}, 
        "PRODUCT_Detail_BEFORE": {},
        "PRODUCT_Detail_AFTER": {},
        "CART_BEFORE": {}, # Added for CART context
        "CART_AFTER": {}   # Added for CART context
    }

    print(f"Mining schemas from {len(files)} capture files...")

    for file_path in files:
        filename = os.path.basename(file_path)
        # print(f"Processing {filename}...") # Reduce noise
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, dict):
                    packets = data.get('requests', [])
                elif isinstance(data, list):
                    packets = data
                else:
                    packets = []
        except Exception as e:
            print(f"Error reading {filename}: {e}")
            continue

        # Find indexes of Anchor Events
        search_indexes = []
        product_detail_indexes = []
        cart_indexes = [] # Added for CART indexes
        
        for i, pkt in enumerate(packets):
            if not isinstance(pkt, dict): continue
            
            # Check Request URL
            url = ""
            if 'request' in pkt:
                 url = pkt['request'].get('url', '')
            elif 'url' in pkt: # Some internal format
                 url = pkt['url']
            
            if re.search(SEARCH_URL_PART, url): # Changed to re.search
                search_indexes.append(i)
            elif PRODUCT_DETAIL_URL_PART in url:
                product_detail_indexes.append(i)
            elif re.search(CART_URL_PART, url): # Added for CART
                cart_indexes.append(i)
        
        if search_indexes or product_detail_indexes or cart_indexes: # Updated print statement
            print(f"[{filename}] Found Search anchors: {len(search_indexes)}, Product anchors: {len(product_detail_indexes)}, Cart anchors: {len(cart_indexes)}")

        # Helper to extract bulksubmit schemas
        def extract_schemas_from_packet(pkt):
            schemas = []
            
            # Check URL
            url = ""
            if 'request' in pkt:
                 url = pkt['request'].get('url', '')
            elif 'url' in pkt: 
                 url = pkt['url']
                 
            if BULKSUBMIT_URL_PART not in url:
                return []
            
            body = None
            
            # Case A: Body is already in 'body' field (common in some captures)
            if 'body' in pkt and isinstance(pkt['body'], list):
               body = pkt['body']
               
            # Case B: Body is in 'request.postData.text' (HAR style)
            elif 'request' in pkt and 'postData' in pkt['request']:
                try:
                    text = pkt['request']['postData'].get('text', '')
                    if text:
                        body = json.loads(text)
                except:
                    pass
            
            # Case C: Body is in 'request.body' (Some internal format)
            elif 'request' in pkt and 'body' in pkt['request']:
                 body_content = pkt['request']['body']
                 if isinstance(body_content, list):
                     body = body_content
                 elif isinstance(body_content, str):
                     try:
                         body = json.loads(body_content)
                     except: pass

            if isinstance(body, list):
                for item in body:
                    meta = item.get('meta', {})
                    s_id = meta.get('schemaId')
                    s_ver = meta.get('schemaVersion')
                    if s_id:
                        schemas.append(f"{s_id}_{s_ver}")
            
            return schemas

        # 1. Analyze SEARCH Context
        for search_idx in search_indexes:
            # Look BEFORE (last 5 packets)
            start = max(0, search_idx - 10)
            for i in range(start, search_idx):
                schemas = extract_schemas_from_packet(packets[i])
                for s in schemas:
                    entry = mining_results["SEARCH_BEFORE"].setdefault(s, {"count": 0, "files": set()})
                    entry["count"] += 1
                    entry["files"].add(filename)

            # Look AFTER (next 20 packets - until next major event usually)
            end = min(len(packets), search_idx + 30)
            for i in range(search_idx + 1, end):
                # Stop if we hit another search or product detail to avoid overlap
                url = packets[i].get('request', {}).get('url', '')
                if re.search(SEARCH_URL_PART, url) or PRODUCT_DETAIL_URL_PART in url or re.search(CART_URL_PART, url): # Updated condition
                    break
                    
                schemas = extract_schemas_from_packet(packets[i])
                for s in schemas:
                    entry = mining_results["SEARCH_AFTER"].setdefault(s, {"count": 0, "files": set()})
                    entry["count"] += 1
                    entry["files"].add(filename)

        # 2. Analyze PRODUCT DETAIL Context
        for pd_idx in product_detail_indexes:
             # Look BEFORE
            start = max(0, pd_idx - 10)
            for i in range(start, pd_idx):
                # Stop if we hit search
                url = packets[i].get('request', {}).get('url', '')
                if SEARCH_URL_PART in url: break

                schemas = extract_schemas_from_packet(packets[i])
                for s in schemas:
                    entry = mining_results["PRODUCT_Detail_BEFORE"].setdefault(s, {"count": 0, "files": set()})
                    entry["count"] += 1
                    entry["files"].add(filename)

            # Look AFTER
            end = min(len(packets), pd_idx + 30)
            for i in range(pd_idx + 1, end):
                schemas = extract_schemas_from_packet(packets[i])
                for s in schemas:
                    entry = mining_results["PRODUCT_Detail_AFTER"].setdefault(s, {"count": 0, "files": set()})
                    entry["count"] += 1
                    entry["files"].add(filename)

        # 3. Analyze CART Context
        for cart_idx in cart_indexes:
             # Look BEFORE
            start = max(0, cart_idx - 10)
            for i in range(start, cart_idx):
                # Stop if we hit product detail logic
                url = packets[i].get('request', {}).get('url', '')
                if PRODUCT_DETAIL_URL_PART in url: break

                schemas = extract_schemas_from_packet(packets[i])
                for s in schemas:
                    entry = mining_results["CART_BEFORE"].setdefault(s, {"count": 0, "files": set()})
                    entry["count"] += 1
                    entry["files"].add(filename)

            # Look AFTER
            end = min(len(packets), cart_idx + 30)
            for i in range(cart_idx + 1, end):
                schemas = extract_schemas_from_packet(packets[i])
                for s in schemas:
                    entry = mining_results["CART_AFTER"].setdefault(s, {"count": 0, "files": set()})
                    entry["count"] += 1
                    entry["files"].add(filename)

    # Convert sets to lists for JSON serialization
    for category in mining_results.values():
        for s_key in category:
            category[s_key]["files"] = list(category[s_key]["files"])

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(mining_results, f, indent=2, ensure_ascii=False)
    
    print(f"Mining complete. Results saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    mine_captures()
