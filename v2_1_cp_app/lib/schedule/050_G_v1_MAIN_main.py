import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 49
# Method: GET
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'x-timestamp': '1767976277620',
#     'coupang-app': 'COUPANG|Android|15|9.0.4||null|f0b740d2-3447-3b2b-b118-d66257275f8f|Y|SM-A165N|f0b740d234472b2bb118d66257275f8f|25ede38a-c6e9-41b2-818a-aef7b5c17d0a|XXHDPI|17679762746194168937968||0||wifi|-1|||Asia/Seoul|c658d419f4d046cfb15f281769b15de7fbc66b30||1080|450|-1|1.0|true',
#     'x-coupang-font-scale': '1.0',
#     'run-mode': 'production',
#     'x-coupang-app-request': 'true',
#     'x-cp-app-req-time': '1767976278705',
#     'x-coupang-target-market': 'KR',
#     'x-coupang-app-name': 'coupang',
#     'x-cp-app-id': 'com.coupang.mobile',
#     'x-cmg-dco': '1767946318000',
#     'x-coupang-origin-region': 'KR',
#     'x-signature': 'bb0430dd1533b0d7871ad13b4313551db0d428488f8de20e08b9aa2fdfe36f28',
#     'x-coupang-accept-language': 'ko-KR',
#     'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 15; SM-A165N Build/AP3A.240905.015.A2)',
#     'accept-encoding': 'gzip'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://cmapi.coupang.com/modular/v1/pages/32/home/main?curPage=8&cartSessionId=c658d419f4d046cfb15f281769b15de7fbc66b30&apiCall=true&abOptions=90573:A|95563:A&lastViewTypes=NONE_CLICK_IMAGE_PAGER,NONE,QUICK_GRID_CATEGORY,LIST_BANNER&nextPageKey=CksIC3JBZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjExOnVuZXhwbG9yZWRfY2F0ZWdvcnmFAb-Wi0EKPwgBcjVmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuMTp0cmVuZGluZ4UBrmNtQQpFCGtyO2ZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy4xMDc6Z3dfcHJvbW90aW9uhQGqjWFBCkwIhQFyQWZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy4xMzM6dW5maW5pc2hlZF9qb3VybmV5hQEeh15BCj8IKnI1ZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjQyOmdvbGRib3iFAcWLV0EKSQipAXI-ZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjE2OTpqaWtndV9wcm9tb3Rpb26FAVlFV0EKTwiKAnJEZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjI2Njpnd19zaXRlX3dpZGVfY2FtcGFpZ26FAYEwMkEKNwgCcjNmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuMjp0cmF2ZWwKRAgNckBmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuMTM6dGFyZ2V0ZWRfcHJvbW90aW9uCkQI4wJyP2ZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy4zNTU6Y291cGFuZ19naWZ0Y2FyZApDCDZyP2ZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy41NDpnd19taWRfYWRzX2Jhbm5lchADGiVmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2|S1&cartSessionId=c658d419f4d046cfb15f281769b15de7fbc66b30&apiCall=true&lastViewTypes=NONE_CLICK_IMAGE_PAGER,QUICK_GRID_CATEGORY,LIST_BANNER,FEED_POSITION,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG&abOptions=90573:A|95563:A"
    method = "GET"
    
    headers = {
        'x-timestamp': '1767976277620',
        'coupang-app': 'COUPANG|Android|15|9.0.4||null|f0b740d2-3447-3b2b-b118-d66257275f8f|Y|SM-A165N|f0b740d234472b2bb118d66257275f8f|25ede38a-c6e9-41b2-818a-aef7b5c17d0a|XXHDPI|17679762746194168937968||0||wifi|-1|||Asia/Seoul|c658d419f4d046cfb15f281769b15de7fbc66b30||1080|450|-1|1.0|true',
        'x-coupang-font-scale': '1.0',
        'run-mode': 'production',
        'x-coupang-app-request': 'true',
        'x-cp-app-req-time': '1767976278705',
        'x-coupang-target-market': 'KR',
        'x-coupang-app-name': 'coupang',
        'x-cp-app-id': 'com.coupang.mobile',
        'x-cmg-dco': '1767946318000',
        'x-coupang-origin-region': 'KR',
        'x-signature': 'bb0430dd1533b0d7871ad13b4313551db0d428488f8de20e08b9aa2fdfe36f28',
        'x-coupang-accept-language': 'ko-KR',
        'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 15; SM-A165N Build/AP3A.240905.015.A2)',
        'accept-encoding': 'gzip'
    }
    
    body = None
    
    return run_request(session, method, url, headers, body)
