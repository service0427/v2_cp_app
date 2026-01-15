import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 133
# Method: GET
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'x-timestamp': '1767976310471',
#     'coupang-app': 'COUPANG|Android|15|9.0.4||null|f0b740d2-3447-3b2b-b118-d66257275f8f|Y|SM-A165N|f0b740d234472b2bb118d66257275f8f|25ede38a-c6e9-41b2-818a-aef7b5c17d0a|XXHDPI|17679762746194168937968||0||wifi|-1|||Asia/Seoul|c658d419f4d046cfb15f281769b15de7fbc66b30||1080|450|-1|1.0|true',
#     'x-coupang-font-scale': '1.0',
#     'run-mode': 'production',
#     'x-coupang-app-request': 'true',
#     'x-cp-app-req-time': '1767976311557',
#     'x-view-name': '/search',
#     'x-coupang-target-market': 'KR',
#     'x-coupang-app-name': 'coupang',
#     'x-cp-app-id': 'com.coupang.mobile',
#     'x-cmg-dco': '',
#     'x-coupang-origin-region': 'KR',
#     'x-signature': '20980371f41d3d4e2894657c99509becdfe3654e9b29b459201c020cd77188f9',
#     'x-coupang-accept-language': 'ko-KR',
#     'x-trace-ix-id': '00014a64-c789-e809-f2ce-1e1abf3ab649',
#     'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 15; SM-A165N Build/AP3A.240905.015.A2)',
#     'accept-encoding': 'gzip'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://cmapi.coupang.com/modular/v1/endpoints/152/v3/search-filter?clientType=SRP&filter=KEYWORD%3A%ED%98%B8%EB%B0%95%EC%8B%9D%ED%98%9C+%EB%8B%AC%EB%B9%9B%7CCCID%3AALL%7CENABLE_ASYNC%3ACATEGORY%7CGET_FILTER%3ANONE%7CEXTRAS%3Achannel%2Fuser@SEARCH&keywordTypes=FOOD&searchId=0797993d22350&totalCount=640&ccidActivated=false&top20HasLuxury=false&keywordLeafInternalCategoryId=58799&exposePremiumBrandShortcutFilter=true&version=V2"
    method = "GET"
    
    headers = {
        'x-timestamp': '1767976310471',
        'coupang-app': 'COUPANG|Android|15|9.0.4||null|f0b740d2-3447-3b2b-b118-d66257275f8f|Y|SM-A165N|f0b740d234472b2bb118d66257275f8f|25ede38a-c6e9-41b2-818a-aef7b5c17d0a|XXHDPI|17679762746194168937968||0||wifi|-1|||Asia/Seoul|c658d419f4d046cfb15f281769b15de7fbc66b30||1080|450|-1|1.0|true',
        'x-coupang-font-scale': '1.0',
        'run-mode': 'production',
        'x-coupang-app-request': 'true',
        'x-cp-app-req-time': '1767976311557',
        'x-view-name': '/search',
        'x-coupang-target-market': 'KR',
        'x-coupang-app-name': 'coupang',
        'x-cp-app-id': 'com.coupang.mobile',
        'x-cmg-dco': '',
        'x-coupang-origin-region': 'KR',
        'x-signature': '20980371f41d3d4e2894657c99509becdfe3654e9b29b459201c020cd77188f9',
        'x-coupang-accept-language': 'ko-KR',
        'x-trace-ix-id': '00014a64-c789-e809-f2ce-1e1abf3ab649',
        'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 15; SM-A165N Build/AP3A.240905.015.A2)',
        'accept-encoding': 'gzip'
    }
    
    body = None
    
    return run_request(session, method, url, headers, body)
