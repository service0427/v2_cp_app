import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 144
# Method: GET
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'x-timestamp': '1767976315609',
#     'coupang-app': 'COUPANG|Android|15|9.0.4||null|f0b740d2-3447-3b2b-b118-d66257275f8f|Y|SM-A165N|f0b740d234472b2bb118d66257275f8f|25ede38a-c6e9-41b2-818a-aef7b5c17d0a|XXHDPI|17679762746194168937968||0||wifi|-1|||Asia/Seoul|c658d419f4d046cfb15f281769b15de7fbc66b30||1080|450|-1|1.0|true',
#     'x-coupang-font-scale': '1.0',
#     'run-mode': 'production',
#     'x-coupang-app-request': 'true',
#     'x-cp-app-req-time': '1767976316695',
#     'x-view-name': '/search',
#     'x-coupang-target-market': 'KR',
#     'x-coupang-app-name': 'coupang',
#     'x-cp-app-id': 'com.coupang.mobile',
#     'x-cmg-dco': '1767946318000',
#     'x-coupang-origin-region': 'KR',
#     'x-signature': 'bfc755caf6b4a08f5c1981df34753c8a7de4906985e3d4dd6863e28bd348fac6',
#     'x-coupang-accept-language': 'ko-KR',
#     'x-trace-ix-id': '00014a65-f8fe-bd29-d300-ffd3750932c3',
#     'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 15; SM-A165N Build/AP3A.240905.015.A2)',
#     'accept-encoding': 'gzip'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://cmapi.coupang.com/modular/v1/endpoints/2333/sdp/v2/platform/products/9024146312?searchId=0797993d22350&rank=1&keyword=%ED%98%B8%EB%B0%95%EC%8B%9D%ED%98%9C%20%EB%8B%AC%EB%B9%9B&implicitLogging=B&slideSimilarKeywordType=FOOD&filterKey=GENDER_TAB%3A0&itemId=26462223018&sourceType=search&egiftPromotion=false&vendorItemId=93437504336&sid=c658d419f4d046cfb15f281769b15de7fbc66b30&chromeVersion=131.0.6778.260&searchRank=1&deliveryFeeToggleStatusFromPrevPage=false&unitPriceWithDeliveryFee=true&showWowPriceHandleBar=true&store=false&itemProductId=4&pvId=92910302&useNewAPIConvention=true&autoTranslateReview=true"
    method = "GET"
    
    headers = {
        'x-timestamp': '1767976315609',
        'coupang-app': 'COUPANG|Android|15|9.0.4||null|f0b740d2-3447-3b2b-b118-d66257275f8f|Y|SM-A165N|f0b740d234472b2bb118d66257275f8f|25ede38a-c6e9-41b2-818a-aef7b5c17d0a|XXHDPI|17679762746194168937968||0||wifi|-1|||Asia/Seoul|c658d419f4d046cfb15f281769b15de7fbc66b30||1080|450|-1|1.0|true',
        'x-coupang-font-scale': '1.0',
        'run-mode': 'production',
        'x-coupang-app-request': 'true',
        'x-cp-app-req-time': '1767976316695',
        'x-view-name': '/search',
        'x-coupang-target-market': 'KR',
        'x-coupang-app-name': 'coupang',
        'x-cp-app-id': 'com.coupang.mobile',
        'x-cmg-dco': '1767946318000',
        'x-coupang-origin-region': 'KR',
        'x-signature': 'bfc755caf6b4a08f5c1981df34753c8a7de4906985e3d4dd6863e28bd348fac6',
        'x-coupang-accept-language': 'ko-KR',
        'x-trace-ix-id': '00014a65-f8fe-bd29-d300-ffd3750932c3',
        'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 15; SM-A165N Build/AP3A.240905.015.A2)',
        'accept-encoding': 'gzip'
    }
    
    body = None
    
    return run_request(session, method, url, headers, body)
