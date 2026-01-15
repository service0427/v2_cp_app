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
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'x-timestamp': '1767976315609',
#     'coupang-app': 'COUPANG|Android|15|9.0.4||null|f0b740d2-3447-3b2b-b118-d66257275f8f|Y|SM-A165N|f0b740d234472b2bb118d66257275f8f|25ede38a-c6e9-41b2-818a-aef7b5c17d0a|XXHDPI|17679762746194168937968||0||wifi|-1|||Asia/Seoul|c658d419f4d046cfb15f281769b15de7fbc66b30||1080|450|-1|1.0|true',
#     'x-coupang-font-scale': '1.0',
#     'run-mode': 'production',
#     'x-coupang-app-request': 'true',
#     'x-cp-app-req-time': '1767976316695',
#     'x-view-name': '/search',
#     'x-coupang-target-market': 'KR',
#     'x-coupang-app-name': 'coupang',
#     'x-cp-app-id': 'com.coupang.mobile',
#     'x-cmg-dco': '1767946318000',
#     'x-coupang-origin-region': 'KR',
#     'x-signature': 'bfc755caf6b4a08f5c1981df34753c8a7de4906985e3d4dd6863e28bd348fac6',
#     'x-coupang-accept-language': 'ko-KR',
#     'x-trace-ix-id': '00014a65-f8fe-bd29-d300-ffd3750932c3',
#     'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 15; SM-A165N Build/AP3A.240905.015.A2)',
#     'accept-encoding': 'gzip'
# }
# ------------------------------

def run(session: requests.Session, context: dict = None):
    import uuid
    import random

    # 1. Prepare Dynamic Data
    if not context:
        context = {}

    # ========================================
    # 동적 헤더 생성 (v1 로직 적용)
    # ========================================
    device = DeviceProfile(
        model=context['DEVICE']['model'],
        os_version=context['DEVICE']['os_version'],
        width=context['DEVICE']['width'],
        height=context['DEVICE']['height'],
        pcid=context['DEVICE']['pcid'],
        app_session_id=context['DEVICE']['app_session_id'],
        ixid=context['DEVICE']['ixid'],
        android_id=context['DEVICE'].get('android_id', ''),
        dpi=context['DEVICE'].get('dpi', '450'),
        dpi_level=context['DEVICE'].get('dpi_level', 'XXHDPI'),
    )

    # New context structure: INPUT/DEVICE/RESULT
    search_result = context.get('RESULT', {}).get('SEARCH', {})
    root_result = context.get('RESULT', {}).get('ROOT', {})

    # Strict Context Retrieval from RESULT > ROOT
    p_id = root_result.get('productId')
    item_id = root_result.get('itemId')
    vendor_item_id = root_result.get('vendorItemId')
    search_id = root_result.get('searchId')

    # Get q from INPUT
    q = context.get('INPUT', {}).get('q')

    # Strict Context Retrieval - ixid from DEVICE, srp_pvId from RESULT > SEARCH
    ixid = context.get('DEVICE', {}).get('ixid')
    srp_pv_id = search_result.get('srp_pvId')

    # Get Rank (default to 0 if missing)
    srp_rank = search_result.get('srp_rank', '0')
    
    if not p_id or not item_id or not ixid or not srp_pv_id:
        print(f"[145] Error: Missing required context (pId={p_id}, itemId={item_id}, ixid={ixid}, srp_pvId={srp_pv_id})")
        return
    
    # In the Product Detail URL, pvId parameter refers to the Source PV ID (SRP PV ID)
    pv_id = srp_pv_id
    
    # 2. Construct URL
    base_url = f"https://cmapi.coupang.com/modular/v1/endpoints/2333/sdp/v2/platform/products/{p_id}"
    params = f"?searchId={search_id}&rank={srp_rank}&keyword={q}&implicitLogging=B&slideSimilarKeywordType=FOOD&filterKey=GENDER_TAB%3A0&itemId={item_id}&sourceType=search&egiftPromotion=false&vendorItemId={vendor_item_id}&sid={ixid}&chromeVersion=131.0.6778.260&searchRank={srp_rank}&deliveryFeeToggleStatusFromPrevPage=false&unitPriceWithDeliveryFee=true&showWowPriceHandleBar=true&store=false&itemProductId=4&pvId={pv_id}&useNewAPIConvention=true&autoTranslateReview=true"
    url = base_url + params
    method = "GET"


    
    # Explicit Header Construction (based on original capture)
    ts = int(time.time() * 1000)
    
    headers = {
        'x-timestamp': str(ts),
        'coupang-app': device.get_coupang_app_header(),
        'x-coupang-font-scale': '1.0',
        'run-mode': 'production',
        'x-coupang-app-request': 'true',
        'baggage': 'enable-upstream-tti-info=true',
        'x-cp-app-req-time': str(ts + 100),
        'x-view-name': '/search',
        'x-coupang-target-market': 'KR',
        'x-coupang-app-name': 'coupang',
        'x-cp-app-id': 'com.coupang.mobile',
        'x-cmg-dco': device.get_cmg_dco(),
        'x-coupang-origin-region': 'KR',
        'x-signature': device.generate_signature(ts),
        'x-coupang-accept-language': 'ko-KR',
        'x-trace-ix-id': device.generate_trace_id(),
        'user-agent': device.get_user_agent(),
        'accept-encoding': 'gzip'
    }
    
    body = None
    
    response = run_request(session, method, url, headers, body)
    
    # 3. Parse Response for sdpVisitKey
    extracted_data = {
        'pvId': pv_id,
        'productId': p_id,
        'itemId': item_id,
        'vendorItemId': vendor_item_id
    }
    
    if response and response.status_code == 200:
        try:
            data = response.json()

            # Save raw API response to PRODUCT.log
            try:
                if lib.logger.LOG_BASE_DIR:
                    product_log_file = os.path.join(lib.logger.LOG_BASE_DIR, "PRODUCT.log")
                    with open(product_log_file, "w", encoding="utf-8") as f:
                        json.dump(data, f, indent=2, ensure_ascii=False)
                    print(f"[145] Saved raw API response to {product_log_file}")
            except Exception as e:
                print(f"[145] Failed to save PRODUCT.log: {e}")

            r_data = data.get('rData', {})

            # Helper to find sdpVisitKey deeply nested
            def find_key(obj, target):
                if isinstance(obj, dict):
                    if target in obj:
                        return obj[target]
                    for k, v in obj.items():
                        res = find_key(v, target)
                        if res: return res
                elif isinstance(obj, list):
                    for item in obj:
                        res = find_key(item, target)
                        if res: return res
                return None
            
            sdp_key = find_key(r_data, 'sdpVisitKey')
            if sdp_key:
                extracted_data['sdpVisitKey'] = sdp_key
            else:
                print(f"[145] Warning: sdpVisitKey not found in response")
                
            print(f"[145] Extracted Data: {extracted_data}")
            
            # 4. Extract Logging/Bypass Schemas for Downstream (e.g. 179 Add to Cart)
            # Strategy: Look for bottomButtonList with 'clickSchemas'
            # We found 'bottomButtonList' in widgetList entities.
            
            # Log all bypass schemas using shared utility
            from lib.logger import log_bypass_schema

            from lib.logger import log_bypass_schema

            def traverse_and_log_schemas(obj):
                if isinstance(obj, dict):
                    # Check Standard Bypass Keys
                    if 'bypass' in obj:
                            bypass = obj['bypass']
                            if isinstance(bypass, dict):
                                if 'exposureSchema' in bypass:
                                    store_schema_in_context(bypass['exposureSchema'])
                                if 'exposureSchemas' in bypass:
                                    for s in bypass['exposureSchemas']:
                                        store_schema_in_context(s)
                                if 'clickSchemas' in bypass:
                                    for s in bypass['clickSchemas']:
                                        store_schema_in_context(s)

                    # Check generic keys appearing directly
                    if 'exposureSchema' in obj:
                            store_schema_in_context(obj['exposureSchema'])
                    if 'exposureSchemas' in obj and isinstance(obj['exposureSchemas'], list):
                            for s in obj['exposureSchemas']:
                                store_schema_in_context(s)
                    if 'clickSchemas' in obj and isinstance(obj['clickSchemas'], list):
                            for s in obj['clickSchemas']:
                                store_schema_in_context(s)
                                    
                    for k, v in obj.items():
                        if isinstance(v, (dict, list)):
                             traverse_and_log_schemas(v)
                elif isinstance(obj, list):
                    for item in obj:
                        traverse_and_log_schemas(item)

            def store_schema_in_context(schema):
                if not isinstance(schema, dict): return

                s_id = str(schema.get('id', ''))
                if not s_id: s_id = str(schema.get('schemaId', ''))
                version = str(schema.get('version', ''))

                if s_id and version:
                    # Build composite key: schemaId_version
                    meta_key = f"{s_id}_{version}"

                    # Ensure META > PRODUCT exists
                    if 'PRODUCT' not in context['RESULT']['META']:
                        context['RESULT']['META']['PRODUCT'] = {}

                    # Store in RESULT > META with data/extra format
                    context['RESULT']['META']['PRODUCT'][meta_key] = {
                        'data': schema.get('mandatory', {}),
                        'extra': schema.get('extra', {})
                    }

            traverse_and_log_schemas(r_data)

            # Define a collector for schemas belonging to the Add-to-Cart button
            atc_button_schemas = []

            def find_atc_button_schemas(obj, target_widget='handlebar'):
                candidates = []
                
                def deep_search(node):
                    if isinstance(node, dict):
                        if 'bypass' in node:
                            bypass = node['bypass']
                            if isinstance(bypass, dict) and 'clickSchemas' in bypass:
                                click_schemas = bypass.get('clickSchemas', [])
                                is_atc = False
                                widget_type = ''
                                
                                for schema in click_schemas:
                                    s_id = str(schema.get('id', ''))
                                    mandatory = schema.get('mandatory', {})
                                    event_name = mandatory.get('eventName', '')
                                    
                                    if s_id == '10' or event_name == 'add_to_cart':
                                        is_atc = True
                                        widget_type = mandatory.get('currentWidget', '')
                                
                                if is_atc:
                                    candidates.append({
                                        'schemas': click_schemas,
                                        'widget': widget_type
                                    })

                        for k, v in node.items():
                            deep_search(v)
                    elif isinstance(node, list):
                        for item in node:
                            deep_search(item)

                deep_search(obj)
                
                # Priority Selection: Handlebar > Bottom Button > First Found
                for cand in candidates:
                    if cand['widget'] == target_widget:
                        print(f"[145] Found exact match for ATC Widget: {target_widget}")
                        return cand['schemas']
                
                if candidates:
                    print(f"[145] Exact match for {target_widget} not found. Using fallback: {candidates[0]['widget']}")
                    return candidates[0]['schemas']
                    
                return None

            extracted_schemas = find_atc_button_schemas(r_data)
            if extracted_schemas:
                extracted_data['sdp_atc_click_schemas'] = extracted_schemas
                ids = [s.get('id') for s in extracted_schemas]
                print(f"[145] Found ATC Button Click Schemas: {ids}")
            else:
                print("[145] Warning: Could not find Add-to-Cart Button Schemas")

            # Also extract pageSession bypass for generic SDP page logging
            def find_page_session_bypass(obj):
                if isinstance(obj, dict):
                     if 'pageSession' in obj:
                         try:
                             return obj['pageSession']['logging']['bypass']
                         except:
                             pass
                     for k, v in obj.items():
                        res = find_page_session_bypass(v)
                        if res: return res
                elif isinstance(obj, list):
                    for item in obj:
                        res = find_page_session_bypass(item)
                        if res: return res
                return None

            page_bypass = find_page_session_bypass(r_data)
            if page_bypass:
                extracted_data['sdp_page_bypass'] = page_bypass

            # Store in RESULT > PRODUCT (전체 SDP 데이터)
            context['RESULT']['PRODUCT'] = extracted_data

            print(f"[145] Extracted Data: {list(extracted_data.keys())}")

            # RESULT > ROOT 업데이트: SDP에서 추출한 필수 값 추가
            context['RESULT']['ROOT']['sdpVisitKey'] = extracted_data.get('sdpVisitKey')
            print(f"[145] RESULT.ROOT updated: sdpVisitKey={extracted_data.get('sdpVisitKey')}")

        except Exception as e:
            print(f"[145] Failed to parse response: {e}")

    return {}
