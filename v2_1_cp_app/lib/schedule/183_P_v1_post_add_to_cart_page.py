import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 182
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'x-timestamp': '1767976324923',
#     'coupang-app': 'COUPANG|Android|15|9.0.4||null|f0b740d2-3447-3b2b-b118-d66257275f8f|Y|SM-A165N|f0b740d234472b2bb118d66257275f8f|25ede38a-c6e9-41b2-818a-aef7b5c17d0a|XXHDPI|17679762746194168937968||0||wifi|-1|||Asia/Seoul|c658d419f4d046cfb15f281769b15de7fbc66b30||1080|450|-1|1.0|true',
#     'x-coupang-font-scale': '1.0',
#     'run-mode': 'production',
#     'x-coupang-app-request': 'true',
#     'x-cp-app-req-time': '1767976326009',
#     'x-view-name': '/pdp',
#     'x-coupang-target-market': 'KR',
#     'x-coupang-app-name': 'coupang',
#     'x-cp-app-id': 'com.coupang.mobile',
#     'x-cmg-dco': '1767946318000',
#     'x-coupang-origin-region': 'KR',
#     'x-signature': '18f2c588447169983b153b7abb5737907f213e13add61c0bbcb001b132f62959',
#     'x-coupang-accept-language': 'ko-KR',
#     'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 15; SM-A165N Build/AP3A.240905.015.A2)',
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '773',
#     'accept-encoding': 'gzip'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://cmapi.coupang.com/modular/v1/endpoints/3333/post-add-to-cart-page?vendorItemId=93437504336"
    method = "POST"
    
    headers = {
        'x-timestamp': '1767976324923',
        'coupang-app': 'COUPANG|Android|15|9.0.4||null|f0b740d2-3447-3b2b-b118-d66257275f8f|Y|SM-A165N|f0b740d234472b2bb118d66257275f8f|25ede38a-c6e9-41b2-818a-aef7b5c17d0a|XXHDPI|17679762746194168937968||0||wifi|-1|||Asia/Seoul|c658d419f4d046cfb15f281769b15de7fbc66b30||1080|450|-1|1.0|true',
        'x-coupang-font-scale': '1.0',
        'run-mode': 'production',
        'x-coupang-app-request': 'true',
        'x-cp-app-req-time': '1767976326009',
        'x-view-name': '/pdp',
        'x-coupang-target-market': 'KR',
        'x-coupang-app-name': 'coupang',
        'x-cp-app-id': 'com.coupang.mobile',
        'x-cmg-dco': '1767946318000',
        'x-coupang-origin-region': 'KR',
        'x-signature': '18f2c588447169983b153b7abb5737907f213e13add61c0bbcb001b132f62959',
        'x-coupang-accept-language': 'ko-KR',
        'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 15; SM-A165N Build/AP3A.240905.015.A2)',
        'content-type': 'application/json; charset=utf-8',
        'content-length': '773',
        'accept-encoding': 'gzip'
    }
    
    body = {
        'addressEligible': True,
        'aging': False,
        'bannerImageUrl': 'http://thumbnail.coupangcdn.com/thumbnails/remote/292x292q65ex/image/vendor_inventory/3b3a/29bcfec71c7f96c93b580e2df31da837e3779be4f7c74f953bd1d0535197.jpg',
        'beauty': False,
        'categoryIds': '1474,1480,1449,1171,1170,1',
        'discountAmount': '0',
        'fashion': False,
        'freshEligible': False,
        'hitDacPromotion': False,
        'hrpCategory': True,
        'inScopeOfCelebrateSavingOnPac': True,
        'inScopeOfChangeStyle': True,
        'inScopeOfExpandPacFully': True,
        'itemId': 26462223018.0,
        'jikgu': False,
        'living': False,
        'loyaltyMember': False,
        'minSize': 3.0,
        'preOrder': False,
        'productId': 9024146312.0,
        'savingAmount': '0',
        'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
        'selectedPrice': 26990.0,
        'sourceType': 'sdp',
        'stockQuantity': 50.0,
        'underThreshold': True,
        'vendorItemId': 93437504336.0
    }
    
    return run_request(session, method, url, headers, body)
