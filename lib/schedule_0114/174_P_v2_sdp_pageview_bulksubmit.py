import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE, DeviceProfile
from lib.common.utils import generate_common_payload

# Reference Data Index: 173
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
    search_id = root.get('searchId', '0797993d22350')
    q = context.get('INPUT', {}).get('q', '호박식혜 달빛')
    
    sdp_visit_key = root.get('sdpVisitKey', '')
    if not sdp_visit_key:
        print("[174] Warning: sdpVisitKey not found. Generating fallback.")
        import random, string
        sdp_visit_key = ''.join(random.choices(string.ascii_lowercase + string.digits, k=18))

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
        # Schema 4123 (Performance)
        make_item(4123, 5, {
            'logType': 'performance', 'loadTime': 975, 'domain': 'WP',
            'moduleName': 'sliderecommendation', 'eventName': 'modx-logger',
            'logCategory': 'system', 'pageName': 'sdp_btf', 'pendingTime': 3620, 'renderTime': 2
        }),
        # Schema 11465 (Background/Platform)
        make_item(11465, 1, {
            'domain': 'marketing', 'logCategory': 'system', 'logType': 'platform',
            'pageName': None, 'eventName': 'background', 'adTrackEnabled': True,
            'adTrackId': '25ede38a-c6e9-41b2-818a-aef7b5c17d0a', 'pushToken': '',
            'isAllowDevicePush': None, 'isAppFinished': False
        }),
        # Schema 12936 (Login SDK - maybe keep for noise)
        make_item(12936, 1, {
            'domain': 'member', 'logCategory': 'system', 'logType': 'debug',
            'pageName': 'login', 'eventName': 'mobile_coupang_login_sdk_tracking_log',
            'message': 'Authorization canceled'
        }),
        # Schema 4123 (Performance #2)
        make_item(4123, 5, {
            'logType': 'performance', 'loadTime': 1043, 'domain': 'WP',
            'moduleName': 'sliderecommendation', 'eventName': 'modx-logger',
            'logCategory': 'system', 'pageName': 'sdp_btf', 'pendingTime': 3619, 'renderTime': 1
        }),
        # Schema 377 (Marketing Foreground)
        make_item(377, 5, {
            'logType': 'processing', 'adTrackEnabled': True, 'domain': 'marketing',
            'eventName': 'foreground', 'isAllowDevicePush': 'Y', 'logCategory': 'event',
            'pageName': 'marketing_foreground', 'pushToken': '', 
            'adTrackId': '25ede38a-c6e9-41b2-818a-aef7b5c17d0a'
        }),
        # Schema 4123 (Performance #3)
        make_item(4123, 5, {
            'logType': 'performance', 'loadTime': 1113, 'domain': 'WP',
            'moduleName': 'sliderecommendation', 'eventName': 'modx-logger',
            'logCategory': 'system', 'pageName': 'sdp_btf', 'pendingTime': 3619, 'renderTime': 2
        }),
        # Schema 14042 (Modal View)
        make_item(14042, 2, {
            'domain': 'sdp', 'logCategory': 'view', 'logType': 'modal',
            'pageName': 'sdp', 'eventName': 'page_view', 'pvid': '92910302' # Keep static pvid for now or randomize?
        }),
        # Schema 7 (SDP Product Page View - CRITICAL)
        make_item(7, 82, {
            'domain': 'sdp', 'logCategory': 'view', 'logType': 'page',
            'pageName': 'sdp', 'eventName': 'sdp_product_page_view',
            'productId': product_id, 'itemId': item_id, 'vendorItemId': vendor_item_id,
            'sdpVisitKey': sdp_visit_key,
            'style': 'NORMAL', 'isLoyaltyMember': False,
            'searchId': search_id,
            'filterKey': 'GENDER_TAB:0', 'q': q, 'sourceType': 'search',
            'soldOut': 'false', 'rank': 1, 'brandId': -1, 'isRlux': False, 'isFarfetch': False,
            'vendorId': 'A01492649', 'offerCondition': 'NEW', 'brandName': '', 'invalid': False,
            'isCoupick': False, 'isPremium': False, 'withBundleOption': 'NONE', 'canEGift': False,
            'isCcidEligible': False, 'displayCcidBadge': False, 'normalInstantDiscountRate': 0,
            'wowOnlyInstantDiscountRate': 0, 'layoutStyle': 'NORMAL', 'is3p': True,
            'isRocketMart': False, 'isQuickView': False, 'unitPrice': '(100ml당 675원)',
            'hasInstantDiscount': False, 'hasWowInstantDiscount': False, 'hasOverThreshCoupon': False,
            'hasWowOverThreshCoupon': False, 'isGiftWrappingAvailable': False,
            'isRetailReturnedItem': False, 'isOrangeBadge': False, 'isPreOrder': False,
            'isRocketInstall': False, 'hasBrandShop': False, 'rocketType': 'NA',
            'hasPrevPurchasedProduct': False, 'reviewRating': '4.0', 'hasRuleBasedTitle': 'false',
            'isRuleBasedTitleEligible': 'false', 'hasTimedealDiscount': False,
            'hasGoldboxDiscount': False, 'isAlmostOOS': False, 'isBadDiscount': 'false',
            'finalPrice': 26990, 'appliedInstantDiscount': False, 'appliedWowInstantDiscount': False,
            'appliedOverThreshCoupon': False, 'appliedWowOverThreshCoupon': False,
            'appliedCcidApplied': False, 'appliedWCcidApplied': False, 'appliedTargetedCoupon': False,
            'toggleViewType': 'srp_grid', 'hasDisplayMyCcidPrice': False,
            'isSocialProofEligibleList': '', 'isUnderThreshold': False, 'isPremiumGrocery': False,
            'extraAttributes': 'freshReorderNudgeFlag:false', 'hasUspGeneratedByAi': False,
            'numAtfImages': '9', 'isLanding': True, 'appliedFontScale': '1.0', 'systemFontScale': '1.0'
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
    ]
    
    return run_request(session, method, url, headers, body)
