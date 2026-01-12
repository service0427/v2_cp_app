import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 37
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '6742',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '6742',
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
                'eventTime': '2026-01-10T01:31:16.635+0900',
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
                'schemaId': 1693,
                'schemaVersion': 8
            },
            'data': {
                'logType': 'impression',
                'trAid': 'home_middle_banner',
                'pageName': 'home',
                'domain': 'home',
                'trCid': '72462',
                'viewType': 'LIST_BANNER',
                'eventName': 'impression_home_middle_line_banner',
                'logCategory': 'impression',
                'eventGroup': 'HOME_BANNER',
                'targetUrl': 'coupang://webview?tab=Y&pushEvent=Y&allowsInlineMediaPlayback=Y&title=반품마켓&url=https://pages.coupang.com/m/54908',
                'contentType': 'HOME_BANNER_UNIT'
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
                'eventTime': '2026-01-10T01:31:16.677+0900',
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
                'schemaId': 12535,
                'schemaVersion': 4
            },
            'data': {
                'domain': 'home',
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': '',
                'eventName': 'impress_titlebar_dropdown_header',
                'headerTooltipText': None,
                'headerTooltipAnimation': 0
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
                'eventTime': '2026-01-10T01:31:16.680+0900',
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
                'schemaId': 15834,
                'schemaVersion': 3
            },
            'data': {
                'logType': 'impression',
                'iconTitle': 'coupang',
                'pageName': 'home',
                'domain': 'home',
                'iconPosition': 'left',
                'eventName': 'coupang_logo_impression',
                'logCategory': 'impression'
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
                'eventTime': '2026-01-10T01:31:16.683+0900',
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
                'schemaId': 18430,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'home',
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': '',
                'eventName': '',
                'elapsedTime': 3,
                'functionName': 'handleAppIcon'
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
                'eventTime': '2026-01-10T01:31:16.997+0900',
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
                'pageNumber': 'CjsIGHIxZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjI0OmZiaYUBp9yvRApDCDdyOWZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy41NTpyZWxhdGVkX2Fkc4UBifihRApLCIQBckBmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuMTMyOmtlZXBfc2hvcHBpbmdfYWRzhQEHMSZDCk0ISXJDZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjczOnJlcGVhdGVkX3B1cmNoYXNlX2Fkc4UBKULjQgpGCI4BcjtmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuMTQyOmNvdW1hbGxfcmVjb4UBs0W2QgpGCAdyPGZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy43OnJlbGF0ZWRfcHJvZHVjdIUB1FR-QgpHCKECcjxmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuMjg5OmJ1eV9hZ2Fpbl9hZHOFAVAaZkIKSgiSAXI_ZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjE0Njp2aWRlb19hZHNfYmFubmVyhQFuKEJCCkMINXI_ZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjUzOmd3X3RvcF9hZHNfYmFubmVyCkQIBnI6ZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjY6cHJpdmF0ZV9sYWJlbIUBkoUCQgpACAlyNmZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy45OnByb21vdGlvboUBITTpQQpBcjlmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuMDpwZXJzb25hbGl6ZWSFAQ_Lu0EKXgigAnJTZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjI4ODpwZXJzb25hbGl6ZWRfYmVzdHNlbGxlcl9mb3JfY2F0ZWdvcnmFAadur0EKPAg6cjJmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuNTg6bGl2ZYUBDsSZQQpLCAtyQWZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy4xMTp1bmV4cGxvcmVkX2NhdGVnb3J5hQG_lotBCj8IAXI1ZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjE6dHJlbmRpbmeFAa5jbUEKRQhrcjtmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuMTA3Omd3X3Byb21vdGlvboUBqo1hQQpMCIUBckFmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuMTMzOnVuZmluaXNoZWRfam91cm5leYUBHodeQQo_CCpyNWZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy40Mjpnb2xkYm94hQHFi1dBCkkIqQFyPmZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy4xNjk6amlrZ3VfcHJvbW90aW9uhQFZRVdBCk8IigJyRGZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy4yNjY6Z3dfc2l0ZV93aWRlX2NhbXBhaWduhQGBMDJBCjcIAnIzZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjI6dHJhdmVsCkQIDXJAZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjEzOnRhcmdldGVkX3Byb21vdGlvbgpECOMCcj9mZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuMzU1OmNvdXBhbmdfZ2lmdGNhcmQKQwg2cj9mZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuNTQ6Z3dfbWlkX2Fkc19iYW5uZXIQARolZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNg==_S1',
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
    ]
    
    return run_request(session, method, url, headers, body)
