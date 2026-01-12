import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 9
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'x-timestamp': '1767976275004',
#     'coupang-app': 'COUPANG|Android|15|9.0.4||null|f0b740d2-3447-3b2b-b118-d66257275f8f|Y|SM-A165N|f0b740d234472b2bb118d66257275f8f|25ede38a-c6e9-41b2-818a-aef7b5c17d0a|XXHDPI|17679762746194168937968||0||wifi|-1|||Asia/Seoul|c658d419f4d046cfb15f281769b15de7fbc66b30||1080|450|-1|1.0|true',
#     'x-coupang-font-scale': '1.0',
#     'run-mode': 'production',
#     'x-coupang-app-request': 'true',
#     'x-cp-app-req-time': '1767976276089',
#     'x-coupang-target-market': 'KR',
#     'x-coupang-app-name': 'coupang',
#     'x-cp-app-id': 'com.coupang.mobile',
#     'x-cmg-dco': '1767946318000',
#     'x-coupang-origin-region': 'KR',
#     'x-signature': '9713f27a3dcd7887ece71b3172e27dad41e1e2baf6ff2446ade7d5d3eb945695',
#     'x-coupang-accept-language': 'ko-KR',
#     'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 15; SM-A165N Build/AP3A.240905.015.A2)',
#     'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'content-length': '402',
#     'accept-encoding': 'gzip'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://cmapi.coupang.com/v3/abtest/tracking"
    method = "POST"
    
    headers = {
        'x-timestamp': '1767976275004',
        'coupang-app': 'COUPANG|Android|15|9.0.4||null|f0b740d2-3447-3b2b-b118-d66257275f8f|Y|SM-A165N|f0b740d234472b2bb118d66257275f8f|25ede38a-c6e9-41b2-818a-aef7b5c17d0a|XXHDPI|17679762746194168937968||0||wifi|-1|||Asia/Seoul|c658d419f4d046cfb15f281769b15de7fbc66b30||1080|450|-1|1.0|true',
        'x-coupang-font-scale': '1.0',
        'run-mode': 'production',
        'x-coupang-app-request': 'true',
        'x-cp-app-req-time': '1767976276089',
        'x-coupang-target-market': 'KR',
        'x-coupang-app-name': 'coupang',
        'x-cp-app-id': 'com.coupang.mobile',
        'x-cmg-dco': '1767946318000',
        'x-coupang-origin-region': 'KR',
        'x-signature': '9713f27a3dcd7887ece71b3172e27dad41e1e2baf6ff2446ade7d5d3eb945695',
        'x-coupang-accept-language': 'ko-KR',
        'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 15; SM-A165N Build/AP3A.240905.015.A2)',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'content-length': '402',
        'accept-encoding': 'gzip'
    }
    
    body = 'key=90541%2C92918%2C92919%2C92916%2C21908%2C92579%2C85158%2C92960%2C95520%2C93428%2C94196%2C96180%2C88939%2C95491%2C94647%2C88936%2C95521%2C95957%2C92803%2C93763%2C95519%2C92804%2C92592%2C91048%2C92583%2C85200%2C92591%2C87850%2C88932%2C92802%2C84239%2C95958%2C94261%2C93048%2C84233%2C92959%2C92958%2C96179%2C85413%2C94646%2C92957%2C93765%2C85412%2C95512%2C88930%2C94648%2C93728%2C87849%2C93766%2C95151&'
    
    return run_request(session, method, url, headers, body)
