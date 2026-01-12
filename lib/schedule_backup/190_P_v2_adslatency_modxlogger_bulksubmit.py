import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 189
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '1926',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '1926',
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
                'eventTime': '2026-01-10T01:32:07.589+0900',
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
                'schemaVersion': 8
            },
            'data': {
                'domain': 'ads',
                'logCategory': 'event',
                'logType': 'processing',
                'pageName': 'recommendation',
                'eventName': 'ads_latency',
                'widgetRanking': -1,
                'placementId': 95,
                'adType': 'APP_PAC_ADS',
                'networkType': 'wifi',
                'apiLatency': -1,
                'waitingTime': -1,
                'renderingLatency': 718,
                'totalLatency': 718,
                'launchId': 'AOS:1767976274728',
                'totalImageLoadingLatency': 48,
                'avgImageLoadingLatency': 35.333333333333336,
                'minImageLoadingLatency': 28,
                'maxImageLoadingLatency': 48,
                'imageCount': 3,
                'viewCreationLatency': 119
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
                'eventTime': '2026-01-10T01:32:07.933+0900',
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
                'loadTime': 6279,
                'domain': 'WP',
                'moduleName': 'ssva-dynamic-ad-widget',
                'eventName': 'modx-logger',
                'logCategory': 'system',
                'pageName': 'sdp_btf',
                'pendingTime': 3618,
                'renderTime': 1
            },
            'extra': {
                'sentTime': '2026-01-09T16:32:07.926Z'
            }
        }
    ]
    
    return run_request(session, method, url, headers, body)
