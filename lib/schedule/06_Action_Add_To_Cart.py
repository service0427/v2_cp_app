import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE, DeviceProfile
from lib.common.utils import generate_common_payload

# Reference Data Index: 179 (Derived from v2_1_cp_app)
# Method: POST

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
    target = context.get('RESULT', {}).get('TARGET', {})  # [NEW] Target Product Metadata
    search = context.get('RESULT', {}).get('SEARCH', {})  # [NEW] Search Result Metadata

    product_id = root.get('productId')
    item_id = root.get('itemId')
    vendor_item_id = root.get('vendorItemId')
    search_id = root.get('searchId')
    q = context.get('INPUT', {}).get('q')
    
    # Contextual IDs
    sdp_visit_key = root.get('sdpVisitKey')
    if not sdp_visit_key:
        from lib.logger import log_error
        error_msg = "[06] Critical Error: sdpVisitKey missing in context. Cannot add to cart."
        log_error("06_Add_To_Cart", error_msg, context)
        raise ValueError(error_msg)

    # PV ID extraction
    pv_id = search.get('srp_pvId')
    if not pv_id:
         from lib.logger import log_error
         error_msg = "[06] Critical Error: srp_pvId missing in context."
         log_error("06_Add_To_Cart", error_msg, context)
         raise ValueError(error_msg)

    # [NEW] Dynamic Data Parsing
    # --------------------------
    # Price Parsing: "20,900원" -> 20900
    def parse_price(price_str):
        if not price_str: return 0
        try:
            return int(str(price_str).replace(',', '').replace('원', '').strip())
        except:
            return 0
            
    final_price = parse_price(target.get('finalPrice'))
    original_price = parse_price(target.get('originalPrice'))
    if original_price == 0: original_price = final_price 
    
    # Enforce Price Validation
    if final_price == 0:
        from lib.logger import log_error
        error_msg = "[06] Critical Error: 'finalPrice' missing in TARGET context. Cannot add to cart."
        log_error("06_Add_To_Cart", error_msg, context)
        raise ValueError(error_msg)

    # Rating Count Parsing
    def parse_count(count_str):
        if not count_str: return 0
        try:
            return int(str(count_str).replace('(', '').replace(')', '').replace(',', '').strip())
        except:
            return 0
            
    rating_count = parse_count(target.get('ratingCount'))
    
    # Rating Average
    try:
        val = target.get('ratingAverage')
        rating_average = float(val) if val else 0.0
    except:
        rating_average = 4.0 # Keep sensible default only if parse fails, but input should be real
        
    rank = target.get('rank')
    if rank is None:
         from lib.logger import log_error
         error_msg = "[06] Critical Error: 'rank' missing in TARGET context."
         log_error("06_Add_To_Cart", error_msg, context)
         raise ValueError(error_msg)
    
    # Flags
    # isRocket check
    rocket_type = 'NA'
    if getattr(search, 'get', lambda k: None)('srp_isRocket', False):
         rocket_type = 'ROCKET' # Simple mapping, can be refined

    payload_common = generate_common_payload(context)

    def make_item(schema_id, schema_ver, data_override=None, extra_override=None):
        base_data = {
            'common': payload_common,
            'meta': {'schemaId': schema_id, 'schemaVersion': schema_ver},
            'data': {},
            'extra': {}
        }
        if data_override:
            base_data['data'].update(data_override)
        if extra_override:
            base_data['extra'].update(extra_override)
        return base_data

    body = []

    # =========================================================================
    # PART 1: Schema 15989 (Page Interact)
    # =========================================================================
    body.append(make_item(15989, 1, 
        data_override={
            'domain': 'sdp', 'logCategory': 'event', 'logType': 'processing',
            'pageName': 'sdp', 'eventName': 'page_interact'
        },
        extra_override={
            'pvId': pv_id
        }
    ))

    # [NEW] Capture & Replay Data (High Fidelity)
    atc_schemas = root.get('sdp_atc_click_schemas', {})
    
    # =========================================================================
    # PART 2: Schema 11599 (Handler Click - Add to Cart)
    # =========================================================================
    # Strategy: Capture & Replay if available, else Dynamic Construction
    schema_11599_data = None
    if atc_schemas and '11599' in atc_schemas:
        print("[06] Replaying Captured Schema 11599")
        schema_11599_data = atc_schemas['11599']
        # Patch dynamic fields just in case (e.g. if they are not in the blob)
        # Usually blobs are complete, but we might need to override if context changed.
        # Ideally, we trust the blob. 
        # But we MUST ensure 'sdpHandlerClickType' is set if it's not.
        if 'sdpHandlerClickType' not in schema_11599_data:
             schema_11599_data['sdpHandlerClickType'] = 'add_to_cart'
    else:
        print("[06] Warning: Captured Schema 11599 not found. Using Dynamic Construction.")
        from lib.logger import log_error
        # We allow fallback but log it
        log_error("06_Add_To_Cart", "Missing Captured Schema 11599 - Fidelity Reduced", context)
        
        schema_11599_data = {
            'logType': 'click', 'pageName': 'sdp', 'domain': 'sdp',
            'eventName': 'handler_click', 'logCategory': 'event',
            'productId': product_id, 'itemId': item_id, 'vendorItemId': vendor_item_id,
            'sdpVisitKey': sdp_visit_key,
            'rocketType': rocket_type, 
            'originalPrice': original_price, 
            'finalPrice': final_price,
            'ynCouponDiscount': 'no', 'ynInstantDiscount': 'no',
            'sdpHandlerClickType': 'add_to_cart', 'selectedGiftOption': 'no'
        }

    body.append(make_item(11599, 4, 
        data_override=schema_11599_data,
        extra_override={
            'eventReferrer': 'add_to_cart', 'currentView': '/search_list'
        }
    ))

    # =========================================================================
    # PART 3: Schema 10 (Add to Cart Event) 
    # =========================================================================
    # Strategy: Capture & Replay if available, else Dynamic Construction
    schema_10_data = None
    if atc_schemas and '10' in atc_schemas:
        print("[06] Replaying Captured Schema 10")
        schema_10_data = atc_schemas['10']
        # Patch mandatory dynamic fields that might change per session
        schema_10_data['sdpVisitKey'] = sdp_visit_key
        schema_10_data['searchId'] = search_id
        schema_10_data['q'] = q 
        schema_10_data['rank'] = int(rank)
    else:
        print("[06] Warning: Captured Schema 10 not found. Using Dynamic Construction.")
        from lib.logger import log_error
        log_error("06_Add_To_Cart", "Missing Captured Schema 10 - Fidelity Reduced", context)
        
        schema_10_data = {
            'logType': 'click', 'pageName': 'sdp', 'domain': 'sdp',
            'eventName': 'add_to_cart', 'logCategory': 'event',
            'sdpVisitKey': sdp_visit_key, 'openSource': 'SDP',
            'needIHB': False, 'sourceType': 'search', 'q': q,
            'searchId': search_id, 'filterKey': 'GENDER_TAB:0',
            'rank': int(rank), 'itemProductId': '4',
            'productId': product_id, 'itemId': item_id, 'vendorItemId': vendor_item_id,
            'brandId': -1, 'isRlux': False, 'isFarfetch': False, 'offerCondition': 'NEW',
            'brandName': '', 'isLoser': False, 'isCcidEligible': False,
            'displayCcidBadge': False, 'quantity': 1, 
            'price': final_price,
            'finalPrice': final_price, 
            'couponDiscountApplied': '',
            'isQuickATC': False, 'layoutStyle': 'NORMAL',
            'total_quantity': '1', 'total_vendorItemIds': '',
            'isAddedOrder': 'false', 'isRocketMart': False,
            'hasInstantDiscount': False, 'hasWowInstantDiscount': False,
            'hasOverThreshCoupon': False, 'hasWowOverThreshCoupon': False,
            'isLoyaltyMember': False, 'isBizOnly': False,
            'originalPrice': original_price, 
            'finalUnitPrice': '', # Can be extracted if needed
            'discountRate': target.get('discountRate', ''), 
            'isNoDiscount': 'true' if final_price == original_price else 'false',
            'rocketType': rocket_type, 'hasOptionTable': True,
            'ratingCount': rating_count, 
            'ratingAverage': rating_average,
            'toggleViewType': 'srp_grid', 'currentWidget': 'bottom_button',
            'isPremiumGrocery': False, 'bundleQty': 1,
            'bundleOptionItems': '', 'bundleOptionTypes': '',
            'bundleMappingIds': '', 'searchRank': int(rank)
        }

    body.append(make_item(10, 77, 
        data_override=schema_10_data,
        extra_override={
            'eventReferrer': 'sdp_click_duration', 'currentView': '/search_list'
        }
    ))

    # =========================================================================
    # PART 4: Schema 14044 (Click - Bottom Button)
    # =========================================================================
    body.append(make_item(14044, 1, 
        data_override={
            'domain': 'sdp', 'logCategory': 'event', 'logType': 'click',
            'pageName': 'sdp', 'eventName': '',
            'pvid': pv_id, 'widgetName': 'SECTION_ATF_BOTTOM_BUTTONS',
            'sectionName': None, 'componentName': 'BOTTOM_BUTTON',
            'checked': False
        },
        extra_override={
            'widgetId': '', 'id': '장바구니 담기', 'index': 0,
            'eventReferrer': 'handler_click'
        }
    ))
    
    return run_request(session, method, url, headers, body)
