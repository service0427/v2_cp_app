import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 173
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '9972',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '9972',
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
                'eventTime': '2026-01-10T01:32:02.645+0900',
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
                'schemaId': 4123,
                'schemaVersion': 5
            },
            'data': {
                'logType': 'performance',
                'loadTime': 975,
                'domain': 'WP',
                'moduleName': 'sliderecommendation',
                'eventName': 'modx-logger',
                'logCategory': 'system',
                'pageName': 'sdp_btf',
                'pendingTime': 3620,
                'renderTime': 2
            },
            'extra': {
                'sentTime': '2026-01-09T16:32:02.625Z'
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
                'eventTime': '2026-01-10T01:32:02.646+0900',
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
                'schemaId': 11465,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'marketing',
                'logCategory': 'system',
                'logType': 'platform',
                'pageName': None,
                'eventName': 'background',
                'adTrackEnabled': True,
                'adTrackId': '25ede38a-c6e9-41b2-818a-aef7b5c17d0a',
                'pushToken': '',
                'isAllowDevicePush': None,
                'isAppFinished': False,
                'eventTime': '2026-01-10T01:32:00.611+0900'
            },
            'extra': {}
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
                'eventTime': '2026-01-10T01:32:02.708+0900',
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
                'schemaId': 12936,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'member',
                'logCategory': 'system',
                'logType': 'debug',
                'pageName': 'login',
                'eventName': 'mobile_coupang_login_sdk_tracking_log',
                'message': 'Authorization canceled'
            },
            'extra': {
                'reason': 'Canceled by user',
                'isWebView': 'false',
                'apiResponseTime': '3988'
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
                'eventTime': '2026-01-10T01:32:02.708+0900',
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
                'schemaId': 4123,
                'schemaVersion': 5
            },
            'data': {
                'logType': 'performance',
                'loadTime': 1043,
                'domain': 'WP',
                'moduleName': 'sliderecommendation',
                'eventName': 'modx-logger',
                'logCategory': 'system',
                'pageName': 'sdp_btf',
                'pendingTime': 3619,
                'renderTime': 1
            },
            'extra': {
                'sentTime': '2026-01-09T16:32:02.691Z'
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
                'eventTime': '2026-01-10T01:32:02.739+0900',
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
                'schemaId': 377,
                'schemaVersion': 5
            },
            'data': {
                'logType': 'processing',
                'adTrackEnabled': True,
                'domain': 'marketing',
                'eventName': 'foreground',
                'isAllowDevicePush': 'Y',
                'logCategory': 'event',
                'pageName': 'marketing_foreground',
                'pushToken': '',
                'adTrackId': '25ede38a-c6e9-41b2-818a-aef7b5c17d0a'
            },
            'extra': {}
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
                'eventTime': '2026-01-10T01:32:02.772+0900',
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
                'schemaId': 4123,
                'schemaVersion': 5
            },
            'data': {
                'logType': 'performance',
                'loadTime': 1113,
                'domain': 'WP',
                'moduleName': 'sliderecommendation',
                'eventName': 'modx-logger',
                'logCategory': 'system',
                'pageName': 'sdp_btf',
                'pendingTime': 3619,
                'renderTime': 2
            },
            'extra': {
                'sentTime': '2026-01-09T16:32:02.763Z'
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
                'eventTime': '2026-01-10T01:32:02.849+0900',
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
                'schemaId': 14042,
                'schemaVersion': 2
            },
            'data': {
                'domain': 'sdp',
                'logCategory': 'view',
                'logType': 'modal',
                'pageName': 'sdp',
                'eventName': 'page_view',
                'pvid': '92910302'
            },
            'extra': {}
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
                'eventTime': '2026-01-10T01:32:02.851+0900',
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
                'schemaId': 7,
                'schemaVersion': 82
            },
            'data': {
                'domain': 'sdp',
                'logCategory': 'view',
                'logType': 'page',
                'pageName': 'sdp',
                'eventName': 'sdp_product_page_view',
                'productId': 9024146312,
                'itemId': 26462223018,
                'vendorItemId': 93437504336,
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'style': 'NORMAL',
                'isLoyaltyMember': False,
                'searchId': '0797993d22350',
                'filterKey': 'GENDER_TAB:0',
                'q': '호박식혜 달빛',
                'sourceType': 'search',
                'soldOut': 'false',
                'rank': 1,
                'brandId': -1,
                'isRlux': False,
                'isFarfetch': False,
                'vendorId': 'A01492649',
                'offerCondition': 'NEW',
                'brandName': '',
                'invalid': False,
                'isCoupick': False,
                'isPremium': False,
                'withBundleOption': 'NONE',
                'canEGift': False,
                'isCcidEligible': False,
                'displayCcidBadge': False,
                'normalInstantDiscountRate': 0,
                'wowOnlyInstantDiscountRate': 0,
                'layoutStyle': 'NORMAL',
                'is3p': True,
                'isRocketMart': False,
                'isQuickView': False,
                'unitPrice': '(100ml당 675원)',
                'hasInstantDiscount': False,
                'hasWowInstantDiscount': False,
                'hasOverThreshCoupon': False,
                'hasWowOverThreshCoupon': False,
                'isGiftWrappingAvailable': False,
                'isRetailReturnedItem': False,
                'isOrangeBadge': False,
                'isPreOrder': False,
                'isRocketInstall': False,
                'hasBrandShop': False,
                'rocketType': 'NA',
                'hasPrevPurchasedProduct': False,
                'reviewRating': '4.0',
                'hasRuleBasedTitle': 'false',
                'isRuleBasedTitleEligible': 'false',
                'hasTimedealDiscount': False,
                'hasGoldboxDiscount': False,
                'isAlmostOOS': False,
                'isBadDiscount': 'false',
                'finalPrice': 26990,
                'appliedInstantDiscount': False,
                'appliedWowInstantDiscount': False,
                'appliedOverThreshCoupon': False,
                'appliedWowOverThreshCoupon': False,
                'appliedCcidApplied': False,
                'appliedWCcidApplied': False,
                'appliedTargetedCoupon': False,
                'toggleViewType': 'srp_grid',
                'hasDisplayMyCcidPrice': False,
                'isSocialProofEligibleList': '',
                'isUnderThreshold': False,
                'isPremiumGrocery': False,
                'extraAttributes': 'freshReorderNudgeFlag:false',
                'hasUspGeneratedByAi': False,
                'numAtfImages': '9',
                'isLanding': False,
                'appliedFontScale': '1.0',
                'systemFontScale': '1.0'
            },
            'extra': {
                'pvId': '92910302',
                'layoutType': 'NORMAL',
                'abCriteria': False
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
                'eventTime': '2026-01-10T01:32:02.858+0900',
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
                'schemaId': 13840,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'sdp',
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'sdp',
                'eventName': 'sdp_section_impression',
                'sectionNum': '1',
                'actionType': 'in',
                'productId': 9024146312,
                'itemId': 26462223018,
                'vendorItemId': 93437504336,
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh'
            },
            'extra': {}
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
                'eventTime': '2026-01-10T01:32:03.011+0900',
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
                'schemaId': 12936,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'member',
                'logCategory': 'system',
                'logType': 'debug',
                'pageName': 'login',
                'eventName': 'mobile_coupang_login_sdk_tracking_log',
                'message': 'tab is hidden'
            },
            'extra': {}
        }
    ]
    
    return run_request(session, method, url, headers, body)
