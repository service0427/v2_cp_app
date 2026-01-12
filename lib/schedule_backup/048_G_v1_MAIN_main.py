import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 47
# Method: GET
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'x-timestamp': '1767976277355',
#     'coupang-app': 'COUPANG|Android|15|9.0.4||null|f0b740d2-3447-3b2b-b118-d66257275f8f|Y|SM-A165N|f0b740d234472b2bb118d66257275f8f|25ede38a-c6e9-41b2-818a-aef7b5c17d0a|XXHDPI|17679762746194168937968||0||wifi|-1|||Asia/Seoul|c658d419f4d046cfb15f281769b15de7fbc66b30||1080|450|-1|1.0|true',
#     'x-coupang-font-scale': '1.0',
#     'run-mode': 'production',
#     'x-coupang-app-request': 'true',
#     'x-cp-app-req-time': '1767976278440',
#     'x-coupang-target-market': 'KR',
#     'x-coupang-app-name': 'coupang',
#     'x-cp-app-id': 'com.coupang.mobile',
#     'x-cmg-dco': '1767946318000',
#     'x-coupang-origin-region': 'KR',
#     'x-signature': '39c1c896e0767380d92a1ce4c6d27578a8d948d3eda4c132b36ac526bdc2a4b3',
#     'x-coupang-accept-language': 'ko-KR',
#     'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 15; SM-A165N Build/AP3A.240905.015.A2)',
#     'accept-encoding': 'gzip'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://cmapi.coupang.com/modular/v1/pages/32/home/main?curPage=7&cartSessionId=c658d419f4d046cfb15f281769b15de7fbc66b30&apiCall=true&abOptions=90573:A|95563:A&lastViewTypes=NONE_CLICK_IMAGE_PAGER,NONE,QUICK_GRID_CATEGORY,LIST_BANNER&nextPageKey=Cl4IoAJyU2ZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy4yODg6cGVyc29uYWxpemVkX2Jlc3RzZWxsZXJfZm9yX2NhdGVnb3J5hQGnbq9BCjwIOnIyZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjU4OmxpdmWFAQ7EmUEKSwgLckFmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuMTE6dW5leHBsb3JlZF9jYXRlZ29yeYUBv5aLQQo_CAFyNWZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy4xOnRyZW5kaW5nhQGuY21BCkUIa3I7ZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjEwNzpnd19wcm9tb3Rpb26FAaqNYUEKTAiFAXJBZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjEzMzp1bmZpbmlzaGVkX2pvdXJuZXmFAR6HXkEKPwgqcjVmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuNDI6Z29sZGJveIUBxYtXQQpJCKkBcj5mZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuMTY5Omppa2d1X3Byb21vdGlvboUBWUVXQQpPCIoCckRmZWVkLTUzNzI0OGU3ZDZkODQ0ZDA5MWIxNGE2MTU2NGVlYzI2LTEuMzMuMjY2Omd3X3NpdGVfd2lkZV9jYW1wYWlnboUBgTAyQQo3CAJyM2ZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy4yOnRyYXZlbApECA1yQGZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjYtMS4zMy4xMzp0YXJnZXRlZF9wcm9tb3Rpb24KRAjjAnI_ZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjM1NTpjb3VwYW5nX2dpZnRjYXJkCkMINnI_ZmVlZC01MzcyNDhlN2Q2ZDg0NGQwOTFiMTRhNjE1NjRlZWMyNi0xLjMzLjU0Omd3X21pZF9hZHNfYmFubmVyEAMaJWZlZWQtNTM3MjQ4ZTdkNmQ4NDRkMDkxYjE0YTYxNTY0ZWVjMjY=|S1&cartSessionId=c658d419f4d046cfb15f281769b15de7fbc66b30&apiCall=true&lastViewTypes=NONE_CLICK_IMAGE_PAGER,QUICK_GRID_CATEGORY,LIST_BANNER,FEED_POSITION,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG,ON_SCREEN_GHOST_LOG&abOptions=90573:A|95563:A"
    method = "GET"
    
    headers = {
        'x-timestamp': '1767976277355',
        'coupang-app': 'COUPANG|Android|15|9.0.4||null|f0b740d2-3447-3b2b-b118-d66257275f8f|Y|SM-A165N|f0b740d234472b2bb118d66257275f8f|25ede38a-c6e9-41b2-818a-aef7b5c17d0a|XXHDPI|17679762746194168937968||0||wifi|-1|||Asia/Seoul|c658d419f4d046cfb15f281769b15de7fbc66b30||1080|450|-1|1.0|true',
        'x-coupang-font-scale': '1.0',
        'run-mode': 'production',
        'x-coupang-app-request': 'true',
        'x-cp-app-req-time': '1767976278440',
        'x-coupang-target-market': 'KR',
        'x-coupang-app-name': 'coupang',
        'x-cp-app-id': 'com.coupang.mobile',
        'x-cmg-dco': '1767946318000',
        'x-coupang-origin-region': 'KR',
        'x-signature': '39c1c896e0767380d92a1ce4c6d27578a8d948d3eda4c132b36ac526bdc2a4b3',
        'x-coupang-accept-language': 'ko-KR',
        'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 15; SM-A165N Build/AP3A.240905.015.A2)',
        'accept-encoding': 'gzip'
    }
    
    body = None
    
    return run_request(session, method, url, headers, body)
