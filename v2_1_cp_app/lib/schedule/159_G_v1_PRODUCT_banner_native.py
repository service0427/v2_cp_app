import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 158
# Method: GET
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'x-timestamp': '1767976317031',
#     'coupang-app': 'COUPANG|Android|15|9.0.4||null|f0b740d2-3447-3b2b-b118-d66257275f8f|Y|SM-A165N|f0b740d234472b2bb118d66257275f8f|25ede38a-c6e9-41b2-818a-aef7b5c17d0a|XXHDPI|17679762746194168937968||0||wifi|-1|||Asia/Seoul|c658d419f4d046cfb15f281769b15de7fbc66b30||1080|450|-1|1.0|true',
#     'x-coupang-font-scale': '1.0',
#     'run-mode': 'production',
#     'x-coupang-app-request': 'true',
#     'x-cp-app-req-time': '1767976318117',
#     'x-view-name': '/pdp',
#     'x-coupang-target-market': 'KR',
#     'x-coupang-app-name': 'coupang',
#     'x-cp-app-id': 'com.coupang.mobile',
#     'x-cmg-dco': '1767946318000',
#     'x-coupang-origin-region': 'KR',
#     'x-signature': '839d99e99cd36a8e018e2a78ff7e7f29310fc1bd9e7b68cc7c1abd099ca61dbc',
#     'x-coupang-accept-language': 'ko-KR',
#     'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 15; SM-A165N Build/AP3A.240905.015.A2)',
#     'accept-encoding': 'gzip'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://cmapi.coupang.com/modular/v1/endpoints/2373/products/9024146312/items/26462223018/offers/banner-native?vendorItemId=93437504336&sdpVisitKey=fyuk5pnr11rkb1z4qh&isForUsedProduct=false&sdp-st=H4sIAAAAAAAA_12OzQ6CMBCE36VnDp65gSZ6JAHiudC1bFK6pD82Snh3gQZQb5OZb2dnZDeuhYKGm4Ib3luWjiwQSx9cWUiYhV3KYHfdbnJKWK3RFQZbqEhKBUeN10Gw1Bm_UFWgFTpTPyjkuo3gwtmOwp3CGsc1OTfxMGEdKTGHJUpdD1_p9v0CCp9gXv_PxY9_8LlfKg7OgoLWgYi-LfE9w6cZzIRAh6S5ypwz2HgHV0N-2GZP0wfNCvcKPAEAAA"
    method = "GET"
    
    headers = {
        'x-timestamp': '1767976317031',
        'coupang-app': 'COUPANG|Android|15|9.0.4||null|f0b740d2-3447-3b2b-b118-d66257275f8f|Y|SM-A165N|f0b740d234472b2bb118d66257275f8f|25ede38a-c6e9-41b2-818a-aef7b5c17d0a|XXHDPI|17679762746194168937968||0||wifi|-1|||Asia/Seoul|c658d419f4d046cfb15f281769b15de7fbc66b30||1080|450|-1|1.0|true',
        'x-coupang-font-scale': '1.0',
        'run-mode': 'production',
        'x-coupang-app-request': 'true',
        'x-cp-app-req-time': '1767976318117',
        'x-view-name': '/pdp',
        'x-coupang-target-market': 'KR',
        'x-coupang-app-name': 'coupang',
        'x-cp-app-id': 'com.coupang.mobile',
        'x-cmg-dco': '1767946318000',
        'x-coupang-origin-region': 'KR',
        'x-signature': '839d99e99cd36a8e018e2a78ff7e7f29310fc1bd9e7b68cc7c1abd099ca61dbc',
        'x-coupang-accept-language': 'ko-KR',
        'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 15; SM-A165N Build/AP3A.240905.015.A2)',
        'accept-encoding': 'gzip'
    }
    
    body = None
    
    return run_request(session, method, url, headers, body)
