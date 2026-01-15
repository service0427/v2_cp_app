import sys
import os
import json
import random
import string
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE, DeviceProfile
from lib.common.utils import generate_common_payload

# Combined Log Script: Post-Product Logs
# Aggregates:
# - 155_P (SDP Impressions)
# - 174_P (SDP Page View & Performance)

def run(session: requests.Session, context: dict):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    # 1. Header & Device Setup
    if context and 'DEVICE' in context:
        device = DeviceProfile(
            model=context['DEVICE'].get('model', DEFAULT_PROFILE.model),
            os_version=context['DEVICE'].get('os_version', DEFAULT_PROFILE.os_version),
            width=context['DEVICE'].get('width', DEFAULT_PROFILE.width),
            height=context['DEVICE'].get('height', DEFAULT_PROFILE.height),
            pcid=context['DEVICE'].get('pcid', DEFAULT_PROFILE.pcid),
            app_session_id=context['DEVICE'].get('app_session_id', DEFAULT_PROFILE.app_session_id),
            ixid=context['DEVICE'].get('ixid', DEFAULT_PROFILE.ixid),
            android_id=context['DEVICE'].get('android_id', DEFAULT_PROFILE.android_id)
        )
    else:
        device = DEFAULT_PROFILE

    coupang_app_header = context.get('DEVICE', {}).get('coupangAppHeader')
    if not coupang_app_header:
        coupang_app_header = device.get_coupang_app_header()
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'accept-encoding': 'gzip',
        'user-agent': device.get_okhttp_user_agent(),
        'x-coupang-origin-region': 'KR',
        'x-coupang-app': coupang_app_header
    }
    
    # 2. Extract Data
    root = context.get('RESULT', {}).get('ROOT', {})
    product_id = root.get('productId')
    item_id = root.get('itemId')
    vendor_item_id = root.get('vendorItemId')
    search_id = root.get('searchId')
    q = context.get('INPUT', {}).get('q')
    
    # [NEW] Extract PV ID
    search = context.get('RESULT', {}).get('SEARCH', {})
    pv_id = search.get('srp_pvId')
    if not pv_id:
        from lib.logger import log_error
        error_msg = "[150] Critical Error: srp_pvId missing in context (from SEARCH)."
        log_error("05_Product_Impression", error_msg, context)
        raise ValueError(error_msg)

    if not product_id or not item_id or not vendor_item_id:
        from lib.logger import log_error
        error_msg = f"[150] Critical Error: Missing Product Context (pId={product_id}, itemId={item_id})."
        log_error("05_Product_Impression", error_msg, context)
        raise ValueError(error_msg)
    
    sdp_visit_key = root.get('sdpVisitKey')
    if not sdp_visit_key:
        from lib.logger import log_error
        error_msg = "[150] Critical Error: sdpVisitKey missing. Must be captured from Action 04."
        log_error("05_Product_Impression", error_msg, context)
        raise ValueError(error_msg)

    payload_common = generate_common_payload(context)

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

    body = []

    # =========================================================================
    # PART 1: 155_P (SDP Impressions)
    # =========================================================================
    body.extend([
        # Schema 14502 (Review/Social Proof)
        make_item(14502, 3, {
            'domain': 'SDP', 'logCategory': 'impression', 'logType': 'impression', 'pageName': 'sdp',
            'eventName': 'sdp_atf_review_social_proof_nudge_impression',
            'sdpVisitKey': sdp_visit_key,
            'productId': product_id, 'itemId': item_id, 'vendorItemId': vendor_item_id,
            'reviewRating': '4.0', 'numberOfReviews': 1
        }),
        # Schema 6739 (Price Policy)
        make_item(6739, 2, {
            'logType': 'impression', 'domain': 'sdp', 'eventName': 'sdp_price_policy_info_button_impression',
            'logCategory': 'impression', 'pageName': 'sdp',
            'productId': product_id, 'itemId': item_id, 'vendorItemId': vendor_item_id
        }),
        # Schema 15268 (Saving Amount)
        make_item(15268, 2, {
            'logType': 'impression', 'domain': 'SDP', 'eventName': 'sdp_saving_amount_impression',
            'logCategory': 'impression', 'pageName': 'sdp',
            'productId': product_id, 'itemId': item_id, 'vendoritemId': vendor_item_id,
            'displayedDiscountAmount': 0
        }),
        # Schema 3432 (PDD Widget)
        make_item(3432, 8, {
            'logCategory': 'impression', 'logType': 'impression', 'pageName': 'sdp',
            'eventName': 'impression_pdd_widget', 'domain': 'sdp',
            'sdpVisitKey': sdp_visit_key,
            'productId': product_id, 'itemId': item_id, 'vendorItemId': vendor_item_id,
            'isWowMember': False, 'isFreeShipping3pBadge': True
        }),
        # Schema 10401 (Wow Cashback)
        make_item(10401, 1, {
            'domain': 'sdp', 'logCategory': 'impression', 'logType': 'impression', 'pageName': 'sdp',
            'eventName': 'sdp_wow_cashback_nudge_impression', 'sdpVisitKey': sdp_visit_key,
            'productId': product_id, 'itemId': item_id, 'vendorItemId': vendor_item_id
        }),
        # Schema 17113 (Social Proof Area)
        make_item(17113, 1, {
            'domain': 'sdp', 'logCategory': 'impression', 'logType': 'impression', 'pageName': 'sdp',
            'eventName': 'social_proof_area_view', 'sdpVisitKey': sdp_visit_key,
            'productId': product_id, 'itemId': item_id, 'vendorItemId': vendor_item_id
        })
    ])

    # =========================================================================
    # PART 2: 174_P (SDP Page View & System)
    # =========================================================================
    body.extend([
        # Schema 4123 (Performance)
        make_item(4123, 5, {
            'logType': 'performance', 'loadTime': random.randint(850, 1100), 'domain': 'WP',
            'moduleName': 'sliderecommendation', 'eventName': 'modx-logger',
            'logCategory': 'system', 'pageName': 'sdp_btf'
        }),
        # Schema 11465 (Background)
        make_item(11465, 1, {
            'domain': 'marketing', 'logCategory': 'system', 'logType': 'platform',
            'eventName': 'background', 'adTrackEnabled': True
        }),
        # Schema 12936 (Login SDK)
        make_item(12936, 1, {
            'domain': 'member', 'logCategory': 'system', 'logType': 'debug',
            'pageName': 'login', 'eventName': 'mobile_coupang_login_sdk_tracking_log',
            'message': 'Authorization canceled'
        }),
        # Schema 4123 (Perf #2)
        make_item(4123, 5, {
            'logType': 'performance', 'loadTime': random.randint(1000, 1300), 'domain': 'WP',
            'moduleName': 'sliderecommendation', 'eventName': 'modx-logger',
            'pageName': 'sdp_btf'
        }),
        # Schema 377 (Marketing)
        make_item(377, 5, {
            'logType': 'processing', 'domain': 'marketing', 'eventName': 'foreground',
            'pageName': 'marketing_foreground', 'adTrackEnabled': True
        }),
        # Schema 4123 (Perf #3)
        make_item(4123, 5, {
            'logType': 'performance', 'loadTime': random.randint(1200, 1500), 'domain': 'WP',
            'moduleName': 'sliderecommendation', 'eventName': 'modx-logger',
            'pageName': 'sdp_btf'
        }),
        # Schema 14042 (Modal)
        make_item(14042, 2, {
            'domain': 'sdp', 'logCategory': 'view', 'logType': 'modal',
            'pageName': 'sdp', 'eventName': 'page_view', 'pvid': pv_id
        }),
        # Schema 7 (SDP Product Page View - CRITICAL)
        make_item(7, 82, {
            'domain': 'sdp', 'logCategory': 'view', 'logType': 'page',
            'pageName': 'sdp', 'eventName': 'sdp_product_page_view',
            'productId': product_id, 'itemId': item_id, 'vendorItemId': vendor_item_id,
            'sdpVisitKey': sdp_visit_key, 'searchId': search_id,
            'sourceType': 'search', 'q': q, 'soldOut': 'false', 'rank': 1
        }),
        # Schema 13840 (Section Impression)
        make_item(13840, 1, {
            'domain': 'sdp', 'logCategory': 'impression', 'logType': 'impression', 'pageName': 'sdp',
            'eventName': 'sdp_section_impression', 'sectionNum': '1', 'actionType': 'in',
            'productId': product_id, 'itemId': item_id, 'vendorItemId': vendor_item_id,
            'sdpVisitKey': sdp_visit_key
        }),
         # Schema 12936 (Login SDK #2)
        make_item(12936, 1, {
            'domain': 'member', 'logCategory': 'system', 'logType': 'debug',
            'pageName': 'login', 'eventName': 'mobile_coupang_login_sdk_tracking_log',
            'message': 'tab is hidden'
        })
    ])
    
    return run_request(session, method, url, headers, body)
