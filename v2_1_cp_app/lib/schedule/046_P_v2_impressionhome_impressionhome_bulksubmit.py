import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 45
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '5083',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '5083',
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
                'eventTime': '2026-01-10T01:31:17.924+0900',
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
                'pageNumber': 'CkMINXI_ZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjUzOmd3X3RvcF9hZHNfYmFubmVyCkQIBnI6ZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjY6cHJpdmF0ZV9sYWJlbIUBkoUCQgpACAlyNmZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy45OnByb21vdGlvboUBITTpQQpBcjlmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuMDpwZXJzb25hbGl6ZWSFAQ_Lu0EKXgigAnJTZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjI4ODpwZXJzb25hbGl6ZWRfYmVzdHNlbGxlcl9mb3JfY2F0ZWdvcnmFAadur0EKPAg6cjJmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuNTg6bGl2ZYUBDsSZQQpLCAtyQWZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy4xMTp1bmV4cGxvcmVkX2NhdGVnb3J5hQG_lotBCj8IAXI1ZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjE6dHJlbmRpbmeFAa5jbUEKRQhrcjtmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuMTA3Omd3X3Byb21vdGlvboUBqo1hQQpMCIUBckFmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuMTMzOnVuZmluaXNoZWRfam91cm5leYUBHodeQQo_CCpyNWZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy40Mjpnb2xkYm94hQHFi1dBCkkIqQFyPmZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy4xNjk6amlrZ3VfcHJvbW90aW9uhQFZRVdBCk8IigJyRGZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy4yNjY6Z3dfc2l0ZV93aWRlX2NhbXBhaWduhQGBMDJBCjcIAnIzZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjI6dHJhdmVsCkQIDXJAZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjEzOnRhcmdldGVkX3Byb21vdGlvbgpECOMCcj9mZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuMzU1OmNvdXBhbmdfZ2lmdGNhcmQKQwg2cj9mZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuNTQ6Z3dfbWlkX2Fkc19iYW5uZXIQAholZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNg==_S1',
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
                'eventTime': '2026-01-10T01:31:18.174+0900',
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
                'pageNumber': 'CkAICXI2ZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjk6cHJvbW90aW9uhQEhNOlBCkFyOWZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy4wOnBlcnNvbmFsaXplZIUBD8u7QQpeCKACclNmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuMjg4OnBlcnNvbmFsaXplZF9iZXN0c2VsbGVyX2Zvcl9jYXRlZ29yeYUBp26vQQo8CDpyMmZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy41ODpsaXZlhQEOxJlBCksIC3JBZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjExOnVuZXhwbG9yZWRfY2F0ZWdvcnmFAb-Wi0EKPwgBcjVmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuMTp0cmVuZGluZ4UBrmNtQQpFCGtyO2ZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy4xMDc6Z3dfcHJvbW90aW9uhQGqjWFBCkwIhQFyQWZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy4xMzM6dW5maW5pc2hlZF9qb3VybmV5hQEeh15BCj8IKnI1ZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjQyOmdvbGRib3iFAcWLV0EKSQipAXI-ZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjE2OTpqaWtndV9wcm9tb3Rpb26FAVlFV0EKTwiKAnJEZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjI2Njpnd19zaXRlX3dpZGVfY2FtcGFpZ26FAYEwMkEKNwgCcjNmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuMjp0cmF2ZWwKRAgNckBmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuMTM6dGFyZ2V0ZWRfcHJvbW90aW9uCkQI4wJyP2ZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy4zNTU6Y291cGFuZ19naWZ0Y2FyZApDCDZyP2ZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy41NDpnd19taWRfYWRzX2Jhbm5lchADGiVmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2_S1',
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
