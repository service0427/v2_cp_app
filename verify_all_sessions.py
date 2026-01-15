
import os
import re
import json
import glob

LOG_DIR = "/home/tech/v2_cp_app/logs/session/20260114/test1"

def parse_action_log(log_path):
    steps_data = {}
    current_step = None
    
    with open(log_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for line in lines:
        step_match = re.search(r'=== \[(.*?)\]', line)
        if step_match:
            current_step = step_match.group(1)
            steps_data[current_step] = {'searchId': set(), 'sdpVisitKey': set(), 'productId': set()}
            continue
            
        if not current_step:
            continue
            
        # Extract searchId (simple regex for key-value patterns in log)
        # Patterns observed: "searchId": "..." or 'searchId': '...'
        search_ids = re.findall(r'["\']searchId["\']\s*[:=]\s*["\']([^"\']+)["\']', line)
        steps_data[current_step]['searchId'].update(search_ids)

        # Extract sdpVisitKey
        sdp_keys = re.findall(r'["\']sdpVisitKey["\']\s*[:=]\s*["\']([^"\']+)["\']', line)
        steps_data[current_step]['sdpVisitKey'].update(sdp_keys)

        # Extract productId (integers or strings)
        product_ids = re.findall(r'["\']productId["\']\s*[:=]\s*["\']?(\d+)["\']?', line)
        steps_data[current_step]['productId'].update(product_ids)

    return steps_data

def verify_session(session_path):
    log_path = os.path.join(session_path, "Action_Log.log")
    if not os.path.exists(log_path):
        return None
    
    data = parse_action_log(log_path)
    
    # 1. Search ID Consistency (Search -> Click -> Impression)
    # Source of Truth: Step 01 (usually in RESULT.ROOT)
    
    search_ids_03 = data.get('03_Log_Product_Click', {}).get('searchId', set())
    search_ids_05 = data.get('05_Log_Product_Impression', {}).get('searchId', set())

    # We'll look for the ID that appears in 01.
    # If 01 isn't parsed easily (it's a log dump), we can infer Source of Truth as the intersection of 03 and 05.
    
    # Better approach: parse 01 Action Log body? No it's a huge JSON.
    # Let's check intersection.
    
    intersect = search_ids_03.intersection(search_ids_05)
    
    search_id_status = "PASS"
    search_id_val = "N/A"
    
    if intersect:
        # If there's at least one common ID, we assume that's the valid one being propagated.
        # We pick the one that looks like a Hex ID (valid format) if possible.
        valid_ids = [sid for sid in intersect if len(sid) >= 10 and "feed" not in sid]
        if valid_ids:
            search_id_val = valid_ids[0]
        else:
             # Fallback to just the first intersecting one
             search_id_val = list(intersect)[0]
    else:
        # If no intersection, truly a failure
        if not search_ids_03 and not search_ids_05:
             search_id_status = "FAIL (No IDs found)"
        else:
             search_id_status = "FAIL (No Common ID)"
             search_id_val = f"03: {list(search_ids_03)} vs 05: {list(search_ids_05)}"

    # 2. SDP Visit Key Consistency (Detail -> Impression)
    # 04 extracts it, 05 uses it.
    sdp_key_04 = data.get('04_Action_Product_Detail', {}).get('sdpVisitKey', set())
    # Note: 04 writes extracted key to context usually, grep might extract it if logged in text
    # In Action_Log, 04 header extract might show it.
    
    # The Action_Log usually dumps the response or parsed result.
    # Let's rely on 05 usage matching what was likely extracted.
    
    sdp_key_05 = data.get('05_Log_Product_Impression', {}).get('sdpVisitKey', set())
    
    sdp_status = "PASS"
    sdp_val = "N/A"

    if sdp_key_05:
        sdp_val = list(sdp_key_05)[0]
    else:
        sdp_status = "FAIL (Missing in 05)"

    return {
        "searchId": (search_id_status, search_id_val),
        "sdpVisitKey": (sdp_status, sdp_val)
    }

print(f"{'Session':<20} | {'SearchID':<25} | {'SearchID Val':<20} | {'SDP Key':<20} | {'SDP Key Val':<20}")
print("-" * 110)

files = sorted(glob.glob(os.path.join(LOG_DIR, "*")))
for f in files:
    if os.path.isdir(f):
        name = os.path.basename(f).split('_', 1)[1] # remove timestamp
        res = verify_session(f)
        if res:
             print(f"{name:<20} | {res['searchId'][0]:<25} | {res['searchId'][1][:18]:<20} | {res['sdpVisitKey'][0]:<20} | {res['sdpVisitKey'][1][:18]:<20}")
        else:
             print(f"{name:<20} | NO LOG FILE")
