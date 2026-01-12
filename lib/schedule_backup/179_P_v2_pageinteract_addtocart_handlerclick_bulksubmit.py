import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 178
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '4673',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '4673',
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/4.9.3'
    }
    
    body = [
        {
            'common': {
                'platform': 'android',
                'libraryVersion': '0.6.7',
                'pcid': '17679762746194168937968',
                'lang': 'ko-KR',
                'appCode': 'coupang',
                'market': 'KR',
                'resolution': '1080x2340',
                'eventTime': '2026-01-10T01:32:04.579+0900',
                'memberSrl': '',
                'app': {
                    'osVersion': '15',
                    'model': 'SM-A165N',
                    'appVersionName': '9.0.4',
                    'appVersionCode': 2409040,
                    'uuid': 'f0b740d2-3447-3b2b-b118-d66257275f8f'
                },
                'location': {
                    'region': 'KR',
                    'locale': 'ko-KR',
                    'mcc': '',
                    'timezone': 'Asia/Seoul'
                },
                'appId': 'com.coupang.mobile',
                'appSessionId': '56b36f12-6759-43bb-9077-f7cddcecc13c',
                'systemLanguage': 'ko'
            },
            'meta': {
                'schemaId': 15989,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'sdp',
                'logCategory': 'event',
                'logType': 'processing',
                'pageName': 'sdp',
                'eventName': 'page_interact'
            },
            'extra': {
                'pvId': '92910302'
            }
        },
        {
            'common': {
                'platform': 'android',
                'libraryVersion': '0.6.7',
                'pcid': '17679762746194168937968',
                'lang': 'ko-KR',
                'appCode': 'coupang',
                'market': 'KR',
                'resolution': '1080x2340',
                'eventTime': '2026-01-10T01:32:04.743+0900',
                'memberSrl': '',
                'app': {
                    'osVersion': '15',
                    'model': 'SM-A165N',
                    'appVersionName': '9.0.4',
                    'appVersionCode': 2409040,
                    'uuid': 'f0b740d2-3447-3b2b-b118-d66257275f8f'
                },
                'location': {
                    'region': 'KR',
                    'locale': 'ko-KR',
                    'mcc': '',
                    'timezone': 'Asia/Seoul'
                },
                'appId': 'com.coupang.mobile',
                'appSessionId': '56b36f12-6759-43bb-9077-f7cddcecc13c',
                'systemLanguage': 'ko'
            },
            'meta': {
                'schemaId': 10,
                'schemaVersion': 77
            },
            'data': {
                'logType': 'click',
                'pageName': 'sdp',
                'domain': 'sdp',
                'eventName': 'add_to_cart',
                'logCategory': 'event',
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'openSource': 'SDP',
                'needIHB': False,
                'sourceType': 'search',
                'q': '호박식혜 달빛',
                'searchId': '0797993d22350',
                'filterKey': 'GENDER_TAB:0',
                'rank': 1,
                'itemProductId': '4',
                'productId': 9024146312,
                'itemId': 26462223018,
                'vendorItemId': 93437504336,
                'brandId': -1,
                'isRlux': False,
                'isFarfetch': False,
                'offerCondition': 'NEW',
                'brandName': '',
                'isLoser': False,
                'isCcidEligible': False,
                'displayCcidBadge': False,
                'quantity': 1,
                'price': 26990,
                'finalPrice': 26990,
                'couponDiscountApplied': '',
                'isQuickATC': False,
                'layoutStyle': 'NORMAL',
                'total_quantity': '1',
                'total_vendorItemIds': '',
                'isAddedOrder': 'false',
                'isRocketMart': False,
                'hasInstantDiscount': False,
                'hasWowInstantDiscount': False,
                'hasOverThreshCoupon': False,
                'hasWowOverThreshCoupon': False,
                'isLoyaltyMember': False,
                'isBizOnly': False,
                'originalPrice': 32000,
                'finalUnitPrice': '(100ml당 675원)',
                'discountRate': '15',
                'isNoDiscount': 'true',
                'rocketType': 'NA',
                'hasOptionTable': True,
                'ratingCount': 1,
                'ratingAverage': 4,
                'toggleViewType': 'srp_grid',
                'currentWidget': 'bottom_button',
                'isPremiumGrocery': False,
                'bundleQty': 1,
                'bundleOptionItems': '',
                'bundleOptionTypes': '',
                'bundleMappingIds': '',
                'searchRank': 1
            },
            'extra': {
                'eventReferrer': 'sdp_click_duration',
                'currentView': '/search_list'
            }
        },
        {
            'common': {
                'platform': 'android',
                'libraryVersion': '0.6.7',
                'pcid': '17679762746194168937968',
                'lang': 'ko-KR',
                'appCode': 'coupang',
                'market': 'KR',
                'resolution': '1080x2340',
                'eventTime': '2026-01-10T01:32:04.744+0900',
                'memberSrl': '',
                'app': {
                    'osVersion': '15',
                    'model': 'SM-A165N',
                    'appVersionName': '9.0.4',
                    'appVersionCode': 2409040,
                    'uuid': 'f0b740d2-3447-3b2b-b118-d66257275f8f'
                },
                'location': {
                    'region': 'KR',
                    'locale': 'ko-KR',
                    'mcc': '',
                    'timezone': 'Asia/Seoul'
                },
                'appId': 'com.coupang.mobile',
                'appSessionId': '56b36f12-6759-43bb-9077-f7cddcecc13c',
                'systemLanguage': 'ko'
            },
            'meta': {
                'schemaId': 11599,
                'schemaVersion': 4
            },
            'data': {
                'domain': 'sdp',
                'logCategory': 'event',
                'logType': 'click',
                'pageName': 'sdp',
                'eventName': 'handler_click',
                'productId': 9024146312,
                'itemId': 26462223018,
                'vendorItemId': 93437504336,
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'rocketType': 'NA',
                'originalPrice': 32000,
                'finalPrice': 26990,
                'ynCouponDiscount': 'no',
                'ynInstantDiscount': 'no',
                'sdpHandlerClickType': 'add_to_cart',
                'selectedGiftOption': 'no'
            },
            'extra': {
                'eventReferrer': 'add_to_cart',
                'currentView': '/search_list'
            }
        },
        {
            'common': {
                'platform': 'android',
                'libraryVersion': '0.6.7',
                'pcid': '17679762746194168937968',
                'lang': 'ko-KR',
                'appCode': 'coupang',
                'market': 'KR',
                'resolution': '1080x2340',
                'eventTime': '2026-01-10T01:32:04.747+0900',
                'memberSrl': '',
                'app': {
                    'osVersion': '15',
                    'model': 'SM-A165N',
                    'appVersionName': '9.0.4',
                    'appVersionCode': 2409040,
                    'uuid': 'f0b740d2-3447-3b2b-b118-d66257275f8f'
                },
                'location': {
                    'region': 'KR',
                    'locale': 'ko-KR',
                    'mcc': '',
                    'timezone': 'Asia/Seoul'
                },
                'appId': 'com.coupang.mobile',
                'appSessionId': '56b36f12-6759-43bb-9077-f7cddcecc13c',
                'systemLanguage': 'ko'
            },
            'meta': {
                'schemaId': 14044,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'sdp',
                'logCategory': 'event',
                'logType': 'click',
                'pageName': 'sdp',
                'eventName': '',
                'pvid': '92910302',
                'traceId': '3bc42af30268f9137afa534259b804e3',
                'widgetName': 'SECTION_ATF_BOTTOM_BUTTONS',
                'sectionName': None,
                'componentName': 'BOTTOM_BUTTON',
                'serverTime': 1767976316919,
                'checked': False
            },
            'extra': {
                'widgetId': '',
                'id': '장바구니 담기',
                'index': 0,
                'eventReferrer': 'handler_click'
            }
        }
    ]
    
    return run_request(session, method, url, headers, body)
