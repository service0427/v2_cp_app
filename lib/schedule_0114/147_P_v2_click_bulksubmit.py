import sys
import os
import json
import datetime
import random
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.common.utils import generate_common_payload


# Reference Data Index: 155
# Method: POST

def run(session: requests.Session, context: dict = None):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"

    # Retrieve cached coupang-app header
    coupang_app_header = context.get('DEVICE', {}).get('coupangAppHeader')
    if not coupang_app_header:
        coupang_app_header = "COUPANG|ANDROID|9.0.4|2409040|15|SM-A165N|56b36f12-6759-43bb-9077-f7cddcecc13c|3.0.0"

    import lib.device_profile # Ensure import if not present check top
    from lib.device_profile import DeviceProfile, DEFAULT_PROFILE 
    
    # Get OkHttp UA
    if context and 'DEVICE' in context:
        device = DeviceProfile(
            model=context['DEVICE'].get('model', DEFAULT_PROFILE.model),
            os_version=context['DEVICE'].get('os_version', DEFAULT_PROFILE.os_version),
            pcid=context['DEVICE'].get('pcid', DEFAULT_PROFILE.pcid)
        )
        okhttp_ua = device.get_okhttp_user_agent()
    else:
        okhttp_ua = DEFAULT_PROFILE.get_okhttp_user_agent()

    headers = {
        'content-type': 'application/json; charset=utf-8',
        'accept-encoding': 'gzip',
        'user-agent': okhttp_ua,
        'x-coupang-origin-region': 'KR',
        'x-coupang-app': coupang_app_header
    }

    if not context: context = {}
    
    # -------------------------------------------------------------------------
    # [NEW] APK Logic Reconstruction (APK Reconstruction)
    # -------------------------------------------------------------------------
    # Logic: Client (APK) calculates composite fields BEFORE generating logs
    # -------------------------------------------------------------------------
    from lib.common.log_manager.scenario import ScenarioManager
    
    input_data = context.get('INPUT', {})
    
    # 1. Logic: Composite Search ID (searchId + rank)
    # Used by: Schema 152
    search_id = context.get('RESULT', {}).get('ROOT', {}).get('searchId')
    rank = context.get('RESULT', {}).get('SEARCH', {}).get('srp_rank', 0)
    input_data['searchIdCombined'] = f"{search_id}:{rank}"
    
    # 2. Logic: AB Test Attribute (Conditional Logic)
    # Used by: Schema 11942
    # Rules: "srp,lowestpricein7days" if ID is 85005/6/7, else "srp"
    ab_id = context.get('RESULT', {}).get('SEARCH', {}).get('srp_abTestId', '')
    if str(ab_id) in ['85005', '85006', '85007']:
        input_data['abTestAttribute'] = 'srp,lowestpricein7days'
    else:
        input_data['abTestAttribute'] = 'srp'
        
    # 3. Logic: Ensure Basic Context
    input_data['q'] = context.get('INPUT', {}).get('q') or input_data.get('q')
    input_data['searchId'] = search_id
    input_data['productId'] = context.get('RESULT', {}).get('ROOT', {}).get('productId')
    input_data['itemId'] = context.get('RESULT', {}).get('ROOT', {}).get('itemId')
    input_data['vendorItemId'] = context.get('RESULT', {}).get('ROOT', {}).get('vendorItemId')
    input_data['itemProductId'] = context.get('RESULT', {}).get('ROOT', {}).get('itemProductId', 4)
    input_data['rank'] = rank
    
    # 4. [NEW] Generate sdpVisitKey (Critical Linkage)
    import string
    # Pattern: 18 chars, lowercase alphanumeric (e.g. 'fyuk5pnr11rkb1z4qh')
    sdp_visit_key = ''.join(random.choices(string.ascii_lowercase + string.digits, k=18))
    input_data['sdpVisitKey'] = sdp_visit_key
    
    # Store globally for next steps (155_P, 174_P)
    if 'RESULT' in context and 'ROOT' in context['RESULT']:
        context['RESULT']['ROOT']['sdpVisitKey'] = sdp_visit_key
    
    print(f"[147] Generated sdpVisitKey: {sdp_visit_key}")
    
    # Update Context
    context['INPUT'] = input_data
    
    # Instantiate Manager
    manager = ScenarioManager(context)
    
    # Execute 'search_product_click' Scenario
    # Bundle: [7960, 124, 7598, 9453, 152, 11942]
    body = manager.execute_scenario("search_product_click")
    
    if not body:
         print("[147] Warning: ScenarioManager returned empty body.")
         return None
         
    return run_request(session, method, url, headers, body)
