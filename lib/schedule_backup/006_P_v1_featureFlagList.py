import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 5
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'x-timestamp': '1767976275508',
#     'coupang-app': 'COUPANG|Android|15|9.0.4||null|f0b740d2-3447-3b2b-b118-d66257275f8f|Y|SM-A165N|f0b740d234472b2bb118d66257275f8f|25ede38a-c6e9-41b2-818a-aef7b5c17d0a|XXHDPI|17679762746194168937968||0||wifi|-1|||Asia/Seoul|||1080|450|-1|1.0|true',
#     'x-coupang-font-scale': '1.0',
#     'run-mode': 'production',
#     'x-coupang-app-request': 'true',
#     'x-cp-app-req-time': '1767976275506',
#     'x-coupang-target-market': 'KR',
#     'x-coupang-app-name': 'coupang',
#     'x-cp-app-id': 'com.coupang.mobile',
#     'x-cmg-dco': '',
#     'x-coupang-origin-region': 'KR',
#     'x-signature': 'ea7c4b2931a2270b21ac7ab5c612a3b03c952814f2c0b9fcf26865df42005226',
#     'x-coupang-accept-language': 'ko-KR',
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '83',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://cmapi.coupang.com/modular/v1/endpoints/12531/ff/v1/featureFlagList"
    method = "POST"
    
    headers = {
        'x-timestamp': '1767976275508',
        'coupang-app': 'COUPANG|Android|15|9.0.4||null|f0b740d2-3447-3b2b-b118-d66257275f8f|Y|SM-A165N|f0b740d234472b2bb118d66257275f8f|25ede38a-c6e9-41b2-818a-aef7b5c17d0a|XXHDPI|17679762746194168937968||0||wifi|-1|||Asia/Seoul|||1080|450|-1|1.0|true',
        'x-coupang-font-scale': '1.0',
        'run-mode': 'production',
        'x-coupang-app-request': 'true',
        'x-cp-app-req-time': '1767976275506',
        'x-coupang-target-market': 'KR',
        'x-coupang-app-name': 'coupang',
        'x-cp-app-id': 'com.coupang.mobile',
        'x-cmg-dco': '',
        'x-coupang-origin-region': 'KR',
        'x-signature': 'ea7c4b2931a2270b21ac7ab5c612a3b03c952814f2c0b9fcf26865df42005226',
        'x-coupang-accept-language': 'ko-KR',
        'content-type': 'application/json; charset=utf-8',
        'content-length': '83',
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/4.9.3'
    }
    
    body = {
        'filter': {
            'osType': 'Android',
            'appType': 'com.coupang.mobile',
            'appVersion': '9.0.4'
        }
    }
    
    return run_request(session, method, url, headers, body)
