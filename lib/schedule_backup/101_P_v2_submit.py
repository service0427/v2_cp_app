import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 100
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '1917',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/submit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '1917',
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/4.9.3'
    }
    
    body = {
        'common': {
            'platform': 'android',
            'libraryVersion': '0.6.7',
            'pcid': '17679762746194168937968',
            'lang': 'ko-KR',
            'appCode': 'coupang',
            'market': 'KR',
            'resolution': '1080x2340',
            'eventTime': '2026-01-10T01:31:35.492+0900',
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
            'schemaId': 9353,
            'schemaVersion': 6
        },
        'data': {
            'domain': 'srp',
            'logCategory': 'system',
            'logType': 'performance',
            'pageName': 'srp',
            'eventName': '',
            'domReady': None,
            'serverTime': 0,
            'async': False,
            'ixid': '00014a5f-2fcd-311c-e844-6a5011635731',
            'carrier': 'unknown',
            'networkState': 'wifi',
            'imageLoadingTime': 144,
            'viewBindingTime': 2,
            'apiResponseTime': 213,
            'viewCreateTime': 0,
            'screenType': 'autoComplete',
            'bounced': False,
            'tti': 377,
            'cancelledRequestCount': 1,
            'jsonParsingTime': 3,
            'query': '호박',
            'responseSize': 7725,
            'serverFetchingTime': None
        },
        'extra': {
            'api': '[{"key":"autoComplete","time":213,"parse":3,"dispatch":2,"binding":2}]',
            'image': '[{"key":"","time":1,"url":"https:\\/\\/thumbnail.coupangcdn.com\\/thumbnails\\/remote\\/100x100ex\\/image\\/retail\\/images\\/15794414225432-ded856fa-3681-4dde-a972-824b8b71df3c.jpg","preload":"NONE","cacheType":"MEMORY_CACHE"},{"key":"","time":139,"url":"https:\\/\\/thumbnail.coupangcdn.com\\/thumbnails\\/remote\\/100x100ex\\/image\\/retail\\/images\\/291150405912400-02e3d806-b297-4cf2-a0b9-2f627e21c932.jpg","preload":"NONE","cacheType":"REMOTE"}]',
            'total': 228,
            'categoryDepth': None,
            'campaignId': None,
            'signal': -1,
            'viewUpdateTime': 5,
            'prepareApiTime': 6,
            'prepareImageTime': 233,
            'type': 'autoComplete',
            'query': '호박',
            'isAutocomplete': True,
            'dataSize': 7725,
            'cancelledRequestCount': 1
        }
    }
    
    return run_request(session, method, url, headers, body)
