import sys
import os
import json
import time
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE, DeviceProfile
import lib.logger

# Reference Data Index: 144
# Method: GET

def run(session: requests.Session, context: dict = None):
    # 1. Prepare Dynamic Data
    if not context:
        context = {}

    # ========================================
    # 동적 헤더 생성 (v1 로직 적용)
    # ========================================
    if context and 'DEVICE' in context:
        device = DeviceProfile(
            model=context['DEVICE'].get('model', DEFAULT_PROFILE.model),
            os_version=context['DEVICE'].get('os_version', DEFAULT_PROFILE.os_version),
            width=context['DEVICE'].get('width', DEFAULT_PROFILE.width),
            height=context['DEVICE'].get('height', DEFAULT_PROFILE.height),
            pcid=context['DEVICE'].get('pcid', DEFAULT_PROFILE.pcid),
            app_session_id=context['DEVICE'].get('app_session_id', DEFAULT_PROFILE.app_session_id),
            ixid=context['DEVICE'].get('ixid', DEFAULT_PROFILE.ixid),
            android_id=context['DEVICE'].get('android_id', DEFAULT_PROFILE.android_id),
            dpi=context['DEVICE'].get('dpi', '450'),
            dpi_level=context['DEVICE'].get('dpi_level', 'XXHDPI'),
        )
    else:
        device = DEFAULT_PROFILE

    # New context structure: INPUT/DEVICE/RESULT
    search_result = context.get('RESULT', {}).get('SEARCH', {})
    root_result = context.get('RESULT', {}).get('ROOT', {})

    # Strict Context Retrieval from RESULT > ROOT (populated by 128_G)
    p_id = root_result.get('productId')
    item_id = root_result.get('itemId')
    vendor_item_id = root_result.get('vendorItemId')
    search_id = root_result.get('searchId')

    # Get q from INPUT
    q = context.get('INPUT', {}).get('q')

    # Strict Context Retrieval - ixid from DEVICE, srp_pvId from RESULT > SEARCH
    ixid = device.ixid
    srp_pv_id = search_result.get('srp_pvId') # 128_G extracts this

    
    if not p_id or not item_id or not srp_pv_id:
        print(f"[145] Warning: Missing context (pId={p_id}, itemId={item_id}, srp_pvId={srp_pv_id}). Using fallbacks/defaults for robustness.")
        # Fallback mechanism if 128_G failed or partial run
        if not p_id: p_id = "9183773210" # Default fallback
        if not item_id: item_id = "27087300155"
        if not vendor_item_id: vendor_item_id = "94055536142"
        if not srp_pv_id: srp_pv_id = "38578584" # Dummy
    
    # In the Product Detail URL, pvId parameter refers to the Source PV ID (SRP PV ID)
    pv_id = srp_pv_id
    
    # 2. Construct URL Helpers
    item_product_id = root_result.get('itemProductId', '4')
    # keywordType from SEARCH > ROOT
    # 2026-01-14: User requested to avoid 'OTHER' or arbitrary defaults like 'FOOD'
    keyword_type = root_result.get('keywordType', '')
    # Default filterKey if not found
    filter_key = root_result.get('filterKey', 'GENDER_TAB:0') 

    # 3. Construct URL
    base_url = f"https://cmapi.coupang.com/modular/v1/endpoints/2333/sdp/v2/platform/products/{p_id}"
    
    # Query Parameters (mimicking exact app structure)
    params = [
        f"itemId={item_id}",
        f"vendorItemId={vendor_item_id}",
        f"sourceType=search",
        f"searchId={search_id}",
        f"q={q}",
        f"filterKey={filter_key}",
        f"rank=0", # Rank is 0 in SDP call usually, or actual rank? App traces usually show 0 or actual.
        # Let's use actual rank if available, else 0
        f"isRocket=true", # This should ideally be dynamic but true is common default for top products
        f"itemProductId={item_product_id}",
        f"ts={int(time.time()*1000)}",
        f"aurora=true",
        f"org=Android",
        f"pvId={pv_id}",
        f"keywordType={keyword_type}",
        f"page-from=search",
        f"platform=app"
    ]
    
    full_url = f"{base_url}?{'&'.join(params)}"
    
    # 4. Construct Headers (API Headers use DALVIK UA)
    ts = int(time.time() * 1000)
    headers = {
        'x-timestamp': str(ts),
        'coupang-app': device.get_coupang_app_header(),
        'x-coupang-font-scale': '1.0',
        'run-mode': 'production',
        'x-coupang-app-request': 'true',
        'x-cp-app-req-time': str(ts + 120),
        'x-view-name': '/search', # The logical view is search transitioning to SDP
        'x-coupang-target-market': 'KR',
        'x-coupang-app-name': 'coupang',
        'x-cp-app-id': 'com.coupang.mobile',
        'x-cmg-dco': device.get_cmg_dco(),
        'x-coupang-origin-region': 'KR',
        'x-signature': device.generate_signature(ts),
        'x-coupang-accept-language': 'ko-KR',
        'x-trace-ix-id': device.generate_trace_id(),
        'user-agent': device.get_user_agent(), # Dalvik User-Agent for API
        'accept-encoding': 'gzip'
    }

    # 5. Execute
    response = run_request(session, 'GET', full_url, headers)
    
    if response and response.status_code == 200:
        try:
            # Store SDP result (optional, for debugging or future steps)
            data = response.json()
            context['RESULT']['SDP'] = {'status': 'loaded'}
            
            # [NEW] Extract sdpVisitKey from Response (Critical for 05_Log_Product_Impression)
            # It is deeply nested, so we use a recursive search.
            def find_key(obj, key):
                if isinstance(obj, dict):
                    if key in obj and obj[key]:
                        return obj[key]
                    for k, v in obj.items():
                        res = find_key(v, key)
                        if res: return res
                elif isinstance(obj, list):
                    for item in obj:
                        res = find_key(item, key)
                        if res: return res
                return None

            sdp_visit_key = find_key(data, 'sdpVisitKey')
            if sdp_visit_key:
                print(f"[04] Extracted sdpVisitKey from Response: {sdp_visit_key}")
                if 'RESULT' in context and 'ROOT' in context['RESULT']:
                    context['RESULT']['ROOT']['sdpVisitKey'] = sdp_visit_key
            else:
                print("[04] Warning: sdpVisitKey not found in SDP Response.")

        except Exception as e:
            print(f"[04] Error parsing SDP response: {e}")
            
    return response
