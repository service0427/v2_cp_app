import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 187
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '7338',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '7338',
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
                'eventTime': '2026-01-10T01:32:06.592+0900',
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
                'schemaId': 1154,
                'schemaVersion': 1
            },
            'data': {
                'logType': 'system',
                'domain': 'webView',
                'eventName': 'etc_webview_script_call',
                'scriptName': 'getSystemLanguage',
                'logCategory': 'etc'
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
                'eventTime': '2026-01-10T01:32:06.615+0900',
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
                'loadTime': 4754,
                'domain': 'WP',
                'moduleName': 'product-review',
                'eventName': 'modx-logger',
                'logCategory': 'system',
                'pageName': 'sdp_btf',
                'pendingTime': 3612,
                'renderTime': 217
            },
            'extra': {
                'sentTime': '2026-01-09T16:32:06.611Z'
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
                'eventTime': '2026-01-10T01:32:06.820+0900',
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
                'schemaId': 5440,
                'schemaVersion': 2
            },
            'data': {
                'logType': 'impression',
                'itemId': 26462223018,
                'productId': 9024146312,
                'vendorItemId': 93437504336,
                'sourceType': 'SDP_ESSENTIAL_PRODUCTS_PAC',
                'domain': 'sdp',
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'hasSaveInCart': False,
                'eventName': 'imp_recommendation_widget_list',
                'logCategory': 'impression',
                'pageName': 'recommendation'
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
                'eventTime': '2026-01-10T01:32:06.820+0900',
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
                'schemaId': 14453,
                'schemaVersion': 3
            },
            'data': {
                'logType': 'impression',
                'productId': 9024146312,
                'vendorItemId': 93437504336,
                'addToCartSource': 'sdp',
                'pageName': 'sdp_pac',
                'isDeadlineWithin1hr': False,
                'isRlux': False,
                'hasDoNotShowAgainToday': False,
                'isDeadlineWithin3hr': False,
                'itemId': 26462223018,
                'domain': 'sdp',
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'eventName': 'sdp_pac_widget_impression',
                'logCategory': 'impression',
                'isFresh': False
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
                'eventTime': '2026-01-10T01:32:06.821+0900',
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
                'schemaId': 14586,
                'schemaVersion': 1
            },
            'data': {
                'logType': 'impression',
                'itemId': 26462223018,
                'productId': 9024146312,
                'vendorItemId': 93437504336,
                'domain': 'sdp',
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'eventName': 'sdp_pac_bottom_sheet_impression',
                'logCategory': 'impression',
                'pageName': 'sdp',
                'isFresh': False
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
                'eventTime': '2026-01-10T01:32:06.975+0900',
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
                'schemaId': 5571,
                'schemaVersion': 2
            },
            'data': {
                'logType': 'impression',
                'avgHeight': 799,
                'productId': 9024146312,
                'vendorItemId': 93437504336,
                'num': 5,
                'pageName': 'sdp',
                'minHeight': 374,
                'itemId': 26462223018,
                'seeMoreTimeInSecs': 9,
                'maxHeight': 1328,
                'domain': 'sdp',
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'eventName': 'product_review_img_loading',
                'logCategory': 'impression'
            },
            'extra': {
                'sentTime': '2026-01-09T16:32:06.966Z'
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
                'eventTime': '2026-01-10T01:32:07.066+0900',
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
                'schemaId': 14369,
                'schemaVersion': 1
            },
            'data': {
                'logType': 'impression',
                'itemId': 26462223018,
                'descriptionStatus': 'expanded',
                'productId': 9024146312,
                'descriptionHeight': 7649,
                'vendorItemId': 93437504336,
                'domain': 'sdp',
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'eventName': 'sdp_product_description_height',
                'logCategory': 'impression',
                'pageName': 'sdp'
            },
            'extra': {
                'sentTime': '2026-01-09T16:32:07.062Z'
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
                'eventTime': '2026-01-10T01:32:07.076+0900',
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
                'schemaId': 14043,
                'schemaVersion': 1
            },
            'data': {
                'logType': 'impression',
                'traceId': '',
                'widgetName': 'product-details',
                'pvid': 'ca3e9e96-45d1-4a50-ab81-19787e452a45',
                'domain': 'sdp',
                'eventName': 'impression_product-details',
                'serverTime': 1767976318704,
                'logCategory': 'impression',
                'componentName': 'product-detail-image',
                'pageName': 'sdp_btf'
            },
            'extra': {
                'itemId': 26462223018,
                'descriptionStatus': 'expanded',
                'hasSeeMore': False,
                'productId': 9024146312,
                'vendorItemId': 93437504336,
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'sentTime': '2026-01-09T16:32:07.071Z',
                'baseHeight': 7649
            }
        }
    ]
    
    return run_request(session, method, url, headers, body)
