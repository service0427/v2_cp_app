import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 97
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '1920',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/submit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '1920',
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
            'eventTime': '2026-01-10T01:31:34.707+0900',
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
            'imageLoadingTime': 7,
            'viewBindingTime': 2,
            'apiResponseTime': 197,
            'viewCreateTime': 0,
            'screenType': 'autoComplete',
            'bounced': False,
            'tti': 259,
            'cancelledRequestCount': 1,
            'jsonParsingTime': 0,
            'query': '호바',
            'responseSize': 6566,
            'serverFetchingTime': None
        },
        'extra': {
            'api': '[{"key":"autoComplete","time":197,"parse":0,"dispatch":2,"binding":2}]',
            'image': '[{"key":"","time":1,"url":"https:\\/\\/thumbnail.coupangcdn.com\\/thumbnails\\/remote\\/100x100ex\\/image\\/retail\\/images\\/716222707318952-32594ffc-e63b-4c9b-98ae-4d9f0682b2ae.jpg","preload":"NONE","cacheType":"MEMORY_CACHE"},{"key":"","time":1,"url":"https:\\/\\/thumbnail.coupangcdn.com\\/thumbnails\\/remote\\/100x100ex\\/image\\/retail\\/images\\/15794414225432-ded856fa-3681-4dde-a972-824b8b71df3c.jpg","preload":"NONE","cacheType":"MEMORY_CACHE"}]',
            'total': 208,
            'categoryDepth': None,
            'campaignId': None,
            'signal': -1,
            'viewUpdateTime': 12,
            'prepareApiTime': 6,
            'prepareImageTime': 220,
            'type': 'autoComplete',
            'query': '호바',
            'isAutocomplete': True,
            'dataSize': 6566,
            'cancelledRequestCount': 1
        }
    }
    
    return run_request(session, method, url, headers, body)
