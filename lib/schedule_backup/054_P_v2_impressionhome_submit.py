import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 53
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '1870',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/submit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '1870',
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
            'eventTime': '2026-01-10T01:31:18.929+0900',
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
            'schemaId': 93,
            'schemaVersion': 1
        },
        'data': {
            'logType': 'impression',
            'pageNumber': 'CkUIa3I7ZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjEwNzpnd19wcm9tb3Rpb26FAaqNYUEKTAiFAXJBZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjEzMzp1bmZpbmlzaGVkX2pvdXJuZXmFAR6HXkEKPwgqcjVmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuNDI6Z29sZGJveIUBxYtXQQpJCKkBcj5mZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuMTY5Omppa2d1X3Byb21vdGlvboUBWUVXQQpPCIoCckRmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuMjY2Omd3X3NpdGVfd2lkZV9jYW1wYWlnboUBgTAyQQo3CAJyM2ZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy4yOnRyYXZlbApECA1yQGZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy4xMzp0YXJnZXRlZF9wcm9tb3Rpb24KRAjjAnI_ZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjM1NTpjb3VwYW5nX2dpZnRjYXJkCkMINnI_ZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjU0Omd3X21pZF9hZHNfYmFubmVyEAMaJWZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjY=_S1',
            'itemIds': '',
            'requestCategoryId': '/home_today_recommendation',
            'productTypes': '',
            'sectionId': None,
            'totalCount': None,
            'pageName': 'home',
            'extraContents': '',
            'q': None,
            'searchId': None,
            'productIds': '',
            'domain': 'home',
            'eventName': 'impression_home',
            'rank': None,
            'logCategory': 'impression',
            'filterType': None,
            'contentType': 'ult'
        },
        'extra': {}
    }
    
    return run_request(session, method, url, headers, body)
