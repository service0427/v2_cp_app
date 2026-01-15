import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE, DeviceProfile
from lib.common.utils import generate_common_payload

# Reference Data Index: 130
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '4651',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session, context: dict):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    # Instantiate DeviceProfile from context (or default)
    if context and 'DEVICE' in context:
        device = DeviceProfile(
            model=context['DEVICE'].get('model', DEFAULT_PROFILE.model),
            os_version=context['DEVICE'].get('os_version', DEFAULT_PROFILE.os_version),
            pcid=context['DEVICE'].get('pcid', DEFAULT_PROFILE.pcid),
            app_session_id=context['DEVICE'].get('app_session_id', DEFAULT_PROFILE.app_session_id)
        )
    else:
        device = DEFAULT_PROFILE

    # Retrieve cached coupang-app header or generate new one using device profile
    coupang_app_header = context.get('DEVICE', {}).get('coupangAppHeader')
    if not coupang_app_header:
        coupang_app_header = device.get_coupang_app_header()
    
    okhttp_ua = device.get_okhttp_user_agent()

    headers = {
        'content-type': 'application/json; charset=utf-8',
        'accept-encoding': 'gzip',
        'user-agent': okhttp_ua, # Dynamic OkHttp UA
        'x-coupang-origin-region': 'KR',
        'x-coupang-app': coupang_app_header
    }
    
    # Dynamic Data
    q = context['INPUT'].get('q', '')
    # Schema 120 usually uses the query as 'q'
    
    # We construct the payload manually or use ScenarioManager?
    # For speed, we patch the existing manual dictionary structure here, 
    # but strictly injecting IDs.
    
    # Note: 131 is "Search List Actions". 
    # It might need a specific 'requestId' for the autocomplete session? 
    # or just reuse a random one.
    import uuid
    request_id = str(uuid.uuid4())
    
    payload_common = generate_common_payload(context)

    # ---------------------------------------------------
    # Schema 3894: search_autocomplete_keyword
    # ---------------------------------------------------
    # This implies we clicked an autocomplete keyword? 
    # Or just searched? 
    # If the user just "Searched" via hitting enter, this schema might be optional or specific.
    # But we will preserve it, injecting 'q'.
    
    body = [
        # Schema 3894 (Autocomplete Click?)
        {
            'common': payload_common,
            'meta': {
                'schemaId': 3894,
                'schemaVersion': 9
            },
            'data': {
                'domain': 'srp',
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'srp',
                'eventName': 'search_autocomplete_keyword',
                'requestId': request_id, 
                'qPos': '1-9',
                'prefix': q,
                'filters': None,
                'filterKeys': '',
                'hasCavenue': None,
                'types': None,
                'subTypes': None,
                'hasRecent': False,
                # 'autoKeywords': ... (Hardcoded example kept or cleared?)
                # Keeping hardcoded dummy for now or clearing. 
                # Ideally should be real but we don't have it.
                'autoKeywords': '', 
                'officialBrand': '',
                'isRlux': False,
                'hasBrandShop': None,
                'hasOfficialBrand': None,
                'hasFashionBrand': None,
                'selectedTheme': None,
                'hasPremiumBrand': None,
                'isPremiumBrandShopEligible': None,
                'recentKeywords': None,
                'isFarfetch': False,
                'officialBrandShopExposureCase': None,
                'brandId': 0
            },
            'extra': {
                'hasImageKeyword': False
            }
        },
        # Schema 120 (Click Search List - CRITICAL)
        {
            'common': payload_common,
            'meta': {
                'schemaId': 120,
                'schemaVersion': 4
            },
            'data': {
                'domain': 'srp',
                'logCategory': 'event',
                'logType': 'click',
                'pageName': 'srp',
                'eventName': 'click_search_list',
                'q': q,
                'channel': None,
                'isFromRecoHintKeyword': None,
                'searchClickedArea': None
            },
            'extra': {
                'currentView': '/home_today_recommendation',
                'eventReferrer': 'click_top_gnb_search'
            }
        },
        # Schema 7761/7762 (Recommendations - Optional but good for noise)
        {
            'common': payload_common,
            'meta': {
                'schemaId': 7761,
                'schemaVersion': 1
            },
            'data': {
                'logType': 'impression',
                'numVisibleKeywords': 5,
                'numScrolledToKeywords': 0,
                'requestId': request_id,
                'domain': 'srp',
                'eventName': 'search_home_fresh_recommended_keyword',
                'searchHomeVersion': 'V2',
                'logCategory': 'impression',
                'recoKeywords': '핫도그,연두부,슬라이스치즈,샌드위치햄,순두부,냉동식품,고기,닭,밀키트,밀크티',
                'pageName': 'srp'
            },
            'extra': {}
        }
    ]
    
    return run_request(session, method, url, headers, body)
