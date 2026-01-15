import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE, DeviceProfile
from lib.common.utils import generate_common_payload

# Reference Data Index: 154
# Method: POST

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
        'user-agent': okhttp_ua,
        'x-coupang-origin-region': 'KR',
        'x-coupang-app': coupang_app_header
    }

    # Extract Dynamic Data
    root = context.get('RESULT', {}).get('ROOT', {})
    
    product_id = root.get('productId', 9024146312)
    item_id = root.get('itemId', 26462223018)
    vendor_item_id = root.get('vendorItemId', 93437504336)
    sdp_visit_key = root.get('sdpVisitKey', '') # Must exist from 147_P
    
    if not sdp_visit_key:
        print("[155] Warning: sdpVisitKey not found in context. Generating fallback.")
        import random, string
        sdp_visit_key = ''.join(random.choices(string.ascii_lowercase + string.digits, k=18))

    # Helper function to create payload with common fields
    payload_common = generate_common_payload(context)

    # Helper to generate item
    def make_item(schema_id, schema_ver, data_override=None):
        base_data = {
            'common': payload_common,
            'meta': {'schemaId': schema_id, 'schemaVersion': schema_ver},
            'data': {},
            'extra': {}
        }
        if data_override:
            base_data['data'].update(data_override)
        return base_data

    body = [
        # Schema 14502
        make_item(14502, 3, {
            'domain': 'SDP', 'logCategory': 'impression', 'logType': 'impression', 'pageName': 'sdp',
            'eventName': 'sdp_atf_review_social_proof_nudge_impression',
            'sdpVisitKey': sdp_visit_key,
            'productId': product_id, 'itemId': item_id, 'vendorItemId': vendor_item_id,
            'reviewRating': '4.0', 'numberOfReviews': 1, 'socialProofNumUsers': 1, 'socialProofNumUsersList': ''
        }),
        # Schema 6739
        make_item(6739, 2, {
            'logType': 'impression', 'domain': 'sdp', 'eventName': 'sdp_price_policy_info_button_impression',
            'logCategory': 'impression', 'pageName': 'sdp',
            'productId': product_id, 'itemId': item_id, 'vendorItemId': vendor_item_id
        }),
        # Schema 15268
        make_item(15268, 2, {
            'logType': 'impression', 'domain': 'SDP', 'eventName': 'sdp_saving_amount_impression',
            'logCategory': 'impression', 'pageName': 'sdp',
            'productId': product_id, 'itemId': item_id, 'vendoritemId': vendor_item_id,
            'displayedDiscountAmount': 0
        }),
        # Schema 3432
        make_item(3432, 8, {
            'logCategory': 'impression', 'logType': 'impression', 'pageName': 'sdp',
            'eventName': 'impression_pdd_widget', 'domain': 'sdp',
            'sdpVisitKey': sdp_visit_key,
            'productId': product_id, 'itemId': item_id, 'vendorItemId': vendor_item_id,
            'isWowMember': False, 'pdd': '', 'pddMessage': '', 'cutoffTime': '',
            'isFreeShipping3pBadge': True, 'isFreeReturn3pBadge': False, 'isSameDayShipOut3pBadge': True,
            'isUrgent': False, 'rocketType': 'NA'
        }),
        # Schema 10401
        make_item(10401, 1, {
            'domain': 'sdp', 'logCategory': 'impression', 'logType': 'impression', 'pageName': 'sdp',
            'eventName': 'sdp_wow_cashback_nudge_impression',
            'sdpVisitKey': sdp_visit_key,
            'productId': product_id, 'itemId': item_id, 'vendorItemId': vendor_item_id
        }),
        # Schema 17113
        make_item(17113, 1, {
            'domain': 'sdp', 'logCategory': 'impression', 'logType': 'impression', 'pageName': 'sdp',
            'eventName': 'social_proof_area_view',
            'productId': product_id, 'itemId': item_id, 'vendorItemId': vendor_item_id,
            'sdpVisitKey': sdp_visit_key,
            'isSocialProofEligibleList': '', 'isSocialProofNudgeExist': False, 'socialProofEligibleLocation': 'SDP_ATF'
        })
    ]
    
    return run_request(session, method, url, headers, body)
