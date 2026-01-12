import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 43
# Method: GET
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'x-timestamp': '1767976276850',
#     'coupang-app': 'COUPANG|Android|15|9.0.4||null|f0b740d2-3447-3b2b-b118-d66257275f8f|Y|SM-A165N|f0b740d234472b2bb118d66257275f8f|25ede38a-c6e9-41b2-818a-aef7b5c17d0a|XXHDPI|17679762746194168937968||0||wifi|-1|||Asia/Seoul|c658d419f4d046cfb15f281769b15de7fbc66b30||1080|450|-1|1.0|true',
#     'x-coupang-font-scale': '1.0',
#     'run-mode': 'production',
#     'x-coupang-app-request': 'true',
#     'x-cp-app-req-time': '1767976277934',
#     'x-coupang-target-market': 'KR',
#     'x-coupang-app-name': 'coupang',
#     'x-cp-app-id': 'com.coupang.mobile',
#     'x-cmg-dco': '1767946318000',
#     'x-coupang-origin-region': 'KR',
#     'x-signature': '28d7616827950c2575853047ab154e7db1b308836fe1eaf2bd89aacb0b291c24',
#     'x-coupang-accept-language': 'ko-KR',
#     'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 15; SM-A165N Build/AP3A.240905.015.A2)',
#     'accept-encoding': 'gzip'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://cmapi.coupang.com/modular/v1/pages/32/home/main?curPage=5&cartSessionId=c658d419f4d046cfb15f281769b15de7fbc66b30&apiCall=true&abOptions=90573:A|95563:A&lastViewTypes=NONE_CLICK_IMAGE_PAGER,NONE,QUICK_GRID_CATEGORY,LIST_BANNER&nextPageKey=CkMINXI_ZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjUzOmd3X3RvcF9hZHNfYmFubmVyCkQIBnI6ZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjY6cHJpdmF0ZV9sYWJlbIUBkoUCQgpACAlyNmZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy45OnByb21vdGlvboUBITTpQQpBcjlmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuMDpwZXJzb25hbGl6ZWSFAQ_Lu0EKXgigAnJTZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjI4ODpwZXJzb25hbGl6ZWRfYmVzdHNlbGxlcl9mb3JfY2F0ZWdvcnmFAadur0EKPAg6cjJmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuNTg6bGl2ZYUBDsSZQQpLCAtyQWZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy4xMTp1bmV4cGxvcmVkX2NhdGVnb3J5hQG_lotBCj8IAXI1ZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjE6dHJlbmRpbmeFAa5jbUEKRQhrcjtmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuMTA3Omd3X3Byb21vdGlvboUBqo1hQQpMCIUBckFmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuMTMzOnVuZmluaXNoZWRfam91cm5leYUBHodeQQo_CCpyNWZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy40Mjpnb2xkYm94hQHFi1dBCkkIqQFyPmZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy4xNjk6amlrZ3VfcHJvbW90aW9uhQFZRVdBCk8IigJyRGZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy4yNjY6Z3dfc2l0ZV93aWRlX2NhbXBhaWduhQGBMDJBCjcIAnIzZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjI6dHJhdmVsCkQIDXJAZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjEzOnRhcmdldGVkX3Byb21vdGlvbgpECOMCcj9mZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuMzU1OmNvdXBhbmdfZ2lmdGNhcmQKQwg2cj9mZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuNTQ6Z3dfbWlkX2Fkc19iYW5uZXIQAholZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNg==|S1&cartSessionId=c658d419f4d046cfb15f281769b15de7fbc66b30&apiCall=true&lastViewTypes=NONE_CLICK_IMAGE_PAGER,QUICK_GRID_CATEGORY,LIST_BANNER,FEED_POSITION,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG&abOptions=90573:A|95563:A"
    method = "GET"
    
    headers = {
        'x-timestamp': '1767976276850',
        'coupang-app': 'COUPANG|Android|15|9.0.4||null|f0b740d2-3447-3b2b-b118-d66257275f8f|Y|SM-A165N|f0b740d234472b2bb118d66257275f8f|25ede38a-c6e9-41b2-818a-aef7b5c17d0a|XXHDPI|17679762746194168937968||0||wifi|-1|||Asia/Seoul|c658d419f4d046cfb15f281769b15de7fbc66b30||1080|450|-1|1.0|true',
        'x-coupang-font-scale': '1.0',
        'run-mode': 'production',
        'x-coupang-app-request': 'true',
        'x-cp-app-req-time': '1767976277934',
        'x-coupang-target-market': 'KR',
        'x-coupang-app-name': 'coupang',
        'x-cp-app-id': 'com.coupang.mobile',
        'x-cmg-dco': '1767946318000',
        'x-coupang-origin-region': 'KR',
        'x-signature': '28d7616827950c2575853047ab154e7db1b308836fe1eaf2bd89aacb0b291c24',
        'x-coupang-accept-language': 'ko-KR',
        'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 15; SM-A165N Build/AP3A.240905.015.A2)',
        'accept-encoding': 'gzip'
    }
    
    body = None
    
    return run_request(session, method, url, headers, body)
