
import os
import re
import glob
import json

LOG_DIR = "/home/tech/v2_cp_app/logs/session/20260114/test1"

def parse_product_log(log_path):
    if not os.path.exists(log_path):
        return None
    
    data = {}
    with open(log_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Extract key fields usually logged in KEY: VALUE format or JSON
    # Based on previous knowledge, PRODUCT.log contains details of the selected product.
    # It might be a text file with "Key: Value" lines or JSON.
    # Let's try to regex common patterns.
    
    prod_id_match = re.search(r'["\']?productId["\']?\s*[:=]\s*["\']?(\d+)["\']?', content)
    rank_match = re.search(r'["\']?rank["\']?\s*[:=]\s*["\']?(\d+)["\']?', content)
    search_rank_match = re.search(r'["\']?searchRank["\']?\s*[:=]\s*["\']?(\d+)["\']?', content)
    vendor_item_match = re.search(r'["\']?vendorItemId["\']?\s*[:=]\s*["\']?(\d+)["\']?', content)
    is_ad_match = re.search(r'["\']?isAd["\']?\s*[:=]\s*["\']?(True|False|true|false)["\']?', content)
    is_rocket_match = re.search(r'["\']?isRocket["\']?\s*[:=]\s*["\']?(True|False|true|false)["\']?', content)
    
    if prod_id_match: data['productId'] = prod_id_match.group(1)
    
    # Priority: searchRank > rank
    if search_rank_match:
        data['rank'] = search_rank_match.group(1)
    elif rank_match: 
        data['rank'] = rank_match.group(1)
        
    if vendor_item_match: data['vendorItemId'] = vendor_item_match.group(1)
    if is_ad_match: data['isAd'] = is_ad_match.group(1)
    if is_rocket_match: data['isRocket'] = is_rocket_match.group(1)
    
    return data

def get_action_log_product_id(session_path):
    log_path = os.path.join(session_path, "Action_Log.log")
    if not os.path.exists(log_path):
        return set()
    
    product_ids = set()
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            # We focus on 03, 04, 05 steps usually for the chosen product
            matches = re.findall(r'["\']productId["\']\s*[:=]\s*["\']?(\d+)["\']?', line)
            product_ids.update(matches)
    return product_ids

print(f"{'Session':<20} | {'Status':<10} | {'PID (PROD)':<12} | {'Rank':<5} | {'PID (ACTION)':<15} | {'Match'}")
print("-" * 90)

files = sorted(glob.glob(os.path.join(LOG_DIR, "*")))
for f in files:
    if os.path.isdir(f):
        name = os.path.basename(f).split('_', 1)[1]
        prod_data = parse_product_log(os.path.join(f, "PRODUCT.log"))
        action_pids = get_action_log_product_id(f)
        
        if not prod_data:
            print(f"{name:<20} | MISSING    | {'-':<12} | {'-':<5} | {str(list(action_pids))[:15]:<15} | FAIL")
            continue
            
        prod_pid = prod_data.get('productId', 'N/A')
        rank = prod_data.get('rank', 'N/A')
        
        # Check if PRODUCT.log PID exists in Action_Log pids
        # Action log might have multiple PIDs (from search results list), so we just check inclusion.
        match = "YES" if prod_pid in action_pids else "NO"
        
        # Flag if it looks like a Fallback (Rank 1 usually indicates fallback if user intended something else, 
        # but here we just report the Rank).
        # We can mark Rank 1 as NOTE.
        
        print(f"{name:<20} | FOUND      | {prod_pid:<12} | {rank:<5} | {str(list(action_pids))[:15]:<15} | {match}")
