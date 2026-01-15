import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 121
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '1422',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/submit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '1422',
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
            'eventTime': '2026-01-10T01:31:46.218+0900',
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
            'imageLoadingTime': 0,
            'viewBindingTime': 2,
            'apiResponseTime': 196,
            'viewCreateTime': 0,
            'screenType': 'autoComplete',
            'bounced': False,
            'tti': 253,
            'cancelledRequestCount': 1,
            'jsonParsingTime': 2,
            'query': '호박식혜 달비',
            'responseSize': 6947,
            'serverFetchingTime': None
        },
        'extra': {
            'api': '[{"key":"autoComplete","time":196,"parse":2,"dispatch":1,"binding":2}]',
            'total': 209,
            'categoryDepth': None,
            'campaignId': None,
            'signal': -1,
            'viewUpdateTime': 0,
            'prepareApiTime': 6,
            'prepareImageTime': 0,
            'type': 'autoComplete',
            'query': '호박식혜 달비',
            'isAutocomplete': True,
            'dataSize': 6947,
            'cancelledRequestCount': 1
        }
    }
    
    return run_request(session, method, url, headers, body)
