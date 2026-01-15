import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 181
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '5674',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '5674',
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
                'eventTime': '2026-01-10T01:32:05.357+0900',
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
                'loadTime': 2985,
                'domain': 'WP',
                'moduleName': 'compare-price-banner',
                'eventName': 'modx-logger',
                'logCategory': 'system',
                'pageName': 'sdp_btf',
                'pendingTime': 3615,
                'renderTime': 722
            },
            'extra': {
                'sentTime': '2026-01-09T16:32:05.350Z'
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
                'eventTime': '2026-01-10T01:32:05.605+0900',
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
                'schemaId': 14387,
                'schemaVersion': 7
            },
            'data': {
                'logType': 'processing',
                'placementId': 236,
                'widgetRanking': 1,
                'waitingTime': 1,
                'pageName': 'sdp_btf',
                'adType': 'HYBRID_VT',
                'renderingLatency': 1937.1000000238419,
                'totalLatency': 3748.100000023842,
                'apiLatency': 1810,
                'domain': 'sdp',
                'eventName': 'BTF_WIDGET_RENDER',
                'logCategory': 'event',
                'networkType': 'wifi'
            },
            'extra': {
                'sentTime': '2026-01-09T16:32:05.467Z'
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
                'eventTime': '2026-01-10T01:32:05.625+0900',
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
                'schemaId': 14387,
                'schemaVersion': 7
            },
            'data': {
                'logType': 'processing',
                'placementId': 31,
                'widgetRanking': 5,
                'waitingTime': 373.39999997615814,
                'pageName': 'sdp_btf',
                'adType': 'SDP_BOTTOM_CAROUSEL',
                'renderingLatency': 1718.1000000238419,
                'totalLatency': 3901.600000023842,
                'apiLatency': 1810.1000000238419,
                'domain': 'sdp',
                'eventName': 'BTF_WIDGET_RENDER',
                'logCategory': 'event',
                'networkType': 'wifi'
            },
            'extra': {
                'sentTime': '2026-01-09T16:32:05.620Z'
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
                'eventTime': '2026-01-10T01:32:05.634+0900',
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
                'schemaId': 14387,
                'schemaVersion': 7
            },
            'data': {
                'logType': 'processing',
                'placementId': 14,
                'widgetRanking': 3,
                'waitingTime': 463.5,
                'pageName': 'sdp_btf',
                'adType': 'SDP_CAROUSEL1',
                'renderingLatency': 1638.3999999761581,
                'totalLatency': 3912.2999999523163,
                'apiLatency': 1810.3999999761581,
                'domain': 'sdp',
                'eventName': 'BTF_WIDGET_RENDER',
                'logCategory': 'event',
                'networkType': 'wifi'
            },
            'extra': {
                'sentTime': '2026-01-09T16:32:05.630Z'
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
                'eventTime': '2026-01-10T01:32:05.659+0900',
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
                'schemaId': 14387,
                'schemaVersion': 7
            },
            'data': {
                'logType': 'processing',
                'placementId': 204,
                'widgetRanking': 4,
                'waitingTime': 788.6999999880791,
                'pageName': 'sdp_btf',
                'adType': 'SDP_VISUALLY_SIMILAR',
                'renderingLatency': 1337.5,
                'totalLatency': 3936.199999988079,
                'apiLatency': 1810,
                'domain': 'sdp',
                'eventName': 'BTF_WIDGET_RENDER',
                'logCategory': 'event',
                'networkType': 'wifi'
            },
            'extra': {
                'sentTime': '2026-01-09T16:32:05.654Z'
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
                'eventTime': '2026-01-10T01:32:05.669+0900',
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
                'schemaId': 14387,
                'schemaVersion': 7
            },
            'data': {
                'logType': 'processing',
                'placementId': 150,
                'widgetRanking': 0,
                'waitingTime': 81.39999997615814,
                'pageName': 'sdp_btf',
                'adType': 'SDP_CAROUSEL3',
                'renderingLatency': 2256.300000011921,
                'totalLatency': 3942.800000011921,
                'apiLatency': 1605.1000000238419,
                'domain': 'sdp',
                'eventName': 'BTF_WIDGET_RENDER',
                'logCategory': 'event',
                'networkType': 'wifi'
            },
            'extra': {
                'sentTime': '2026-01-09T16:32:05.665Z'
            }
        }
    ]
    
    return run_request(session, method, url, headers, body)
