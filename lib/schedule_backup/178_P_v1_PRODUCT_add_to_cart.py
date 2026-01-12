import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 177
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'x-timestamp': '1767976323612',
#     'coupang-app': 'COUPANG|Android|15|9.0.4||null|f0b740d2-3447-3b2b-b118-d66257275f8f|Y|SM-A165N|f0b740d234472b2bb118d66257275f8f|25ede38a-c6e9-41b2-818a-aef7b5c17d0a|XXHDPI|17679762746194168937968||0||wifi|-1|||Asia/Seoul|c658d419f4d046cfb15f281769b15de7fbc66b30||1080|450|-1|1.0|true',
#     'x-coupang-font-scale': '1.0',
#     'run-mode': 'production',
#     'x-coupang-app-request': 'true',
#     'x-cp-app-req-time': '1767976324699',
#     'x-view-name': '/pdp',
#     'x-coupang-target-market': 'KR',
#     'x-coupang-app-name': 'coupang',
#     'x-cp-app-id': 'com.coupang.mobile',
#     'x-cmg-dco': '1767946318000',
#     'x-coupang-origin-region': 'KR',
#     'x-signature': '75235d55fdb194aa9ac468ae2113dd914d4fa94317be0f8dc609bcfb1c578161',
#     'x-coupang-accept-language': 'ko-KR',
#     'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 15; SM-A165N Build/AP3A.240905.015.A2)',
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '1884',
#     'accept-encoding': 'gzip'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://cmapi.coupang.com/modular/v1/endpoints/2356/sdp/v2/widget/products/9024146312/add-to-cart?sdp-st=H4sIAAAAAAAA_12OzQ6CMBCE36VnDp65gSZ6JAHiudC1bFK6pD82Snh3gQZQb5OZb2dnZDeuhYKGm4Ib3luWjiwQSx9cWUiYhV3KYHfdbnJKWK3RFQZbqEhKBUeN10Gw1Bm_UFWgFTpTPyjkuo3gwtmOwp3CGsc1OTfxMGEdKTGHJUpdD1_p9v0CCp9gXv_PxY9_8LlfKg7OgoLWgYi-LfE9w6cZzIRAh6S5ypwz2HgHV0N-2GZP0wfNCvcKPAEAAA&metaData=eyJzIjoiTk9STUFMXzAiLCJrIjoiZnl1azVwbnIxMXJrYjF6NHFoIiwiZCI6W3sidCI6Wzc4MjMsNzY2M119XSwibyI6MiwibCI6eyJwIjo5MDI0MTQ2MzEyLCJpIjoyNjQ2MjIyMzAxOCwidiI6OTM0Mzc1MDQzMzZ9LCJlIjp7InMiOiJjNjU4ZDQxOWY0ZDA0NmNmYjE1ZjI4MTc2OWIxNWRlN2ZiYzY2YjMwIiwic3QiOiJzZWFyY2giLCJrIjoi7Zi467CV7Iud7ZicIOuLrOu5myIsInNpIjoiMDc5Nzk5M2QyMjM1MCIsImF0ciI6dHJ1ZSwiZSI6ZmFsc2UsInIiOjEsImYiOiJHRU5ERVJfVEFCOjAiLCJpIjoiNCIsInB2IjoiOTI5MTAzMDIiLCJjdiI6IjEzMS4wLjY3NzguMjYwIiwibmMiOnRydWUsImZzIjpmYWxzZSwic2ZiIjpmYWxzZSwic3FiIjpmYWxzZSwic2JzbmIiOmZhbHNlLCJzcHBpIjpmYWxzZSwiaWwiOiJCIiwibmxjIjpmYWxzZSwic3Nrd3QiOiJGT09EIn0sImYiOnRydWV9"
    method = "POST"
    
    headers = {
        'x-timestamp': '1767976323612',
        'coupang-app': 'COUPANG|Android|15|9.0.4||null|f0b740d2-3447-3b2b-b118-d66257275f8f|Y|SM-A165N|f0b740d234472b2bb118d66257275f8f|25ede38a-c6e9-41b2-818a-aef7b5c17d0a|XXHDPI|17679762746194168937968||0||wifi|-1|||Asia/Seoul|c658d419f4d046cfb15f281769b15de7fbc66b30||1080|450|-1|1.0|true',
        'x-coupang-font-scale': '1.0',
        'run-mode': 'production',
        'x-coupang-app-request': 'true',
        'x-cp-app-req-time': '1767976324699',
        'x-view-name': '/pdp',
        'x-coupang-target-market': 'KR',
        'x-coupang-app-name': 'coupang',
        'x-cp-app-id': 'com.coupang.mobile',
        'x-cmg-dco': '1767946318000',
        'x-coupang-origin-region': 'KR',
        'x-signature': '75235d55fdb194aa9ac468ae2113dd914d4fa94317be0f8dc609bcfb1c578161',
        'x-coupang-accept-language': 'ko-KR',
        'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 15; SM-A165N Build/AP3A.240905.015.A2)',
        'content-type': 'application/json; charset=utf-8',
        'content-length': '1884',
        'accept-encoding': 'gzip'
    }
    
    body = {
        'aging': False,
        'almostSoldOut': False,
        'bannerImageUrl': 'http://thumbnail.coupangcdn.com/thumbnails/remote/292x292q65ex/image/vendor_inventory/3b3a/29bcfec71c7f96c93b580e2df31da837e3779be4f7c74f953bd1d0535197.jpg',
        'beauty': False,
        'bundleOverwrite': False,
        'cartItemId': '26462223018',
        'categoryIds': '1474,1480,1449,1171,1170,1',
        'celebrateSavingsAfterATC': {
            'inScopeOfCelebrateSavingOnPac': True,
            'inScopeOfChangeStyle': True,
            'savingAmount': '0',
            'underThreshold': True
        },
        'clickItemId': '26462223018',
        'clickProductId': '9024146312',
        'defaultAddressEligible': True,
        'discountAmount': '0',
        'fashion': False,
        'freshEligible': False,
        'hasId': False,
        'hasOt': False,
        'hasWid': False,
        'hasWot': False,
        'hitDacPromotion': False,
        'hrpCategory': True,
        'inScopeOfExpandPacFully': True,
        'jikgu': False,
        'landingProductId': '9024146312',
        'living': False,
        'loyaltyMember': False,
        'openPacCelebrationFromReview': False,
        'preOrder': False,
        'q': '%ED%98%B8%EB%B0%95%EC%8B%9D%ED%98%9C%20%EB%8B%AC%EB%B9%9B',
        'realStockQuantity': 50,
        'referrer': 'product_detail_page',
        'rocketInstall': False,
        'sdpSourceType': 'search',
        'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
        'searchId': '0797993d22350',
        'showPac': True,
        'sid': 'c658d419f4d046cfb15f281769b15de7fbc66b30',
        'twoPricePacSignupScope': False,
        'type': 'PRODUCT',
        'vendorItemId': '93437504336',
        'vendorItems': [
            {
                'accessoryType': 'MAIN',
                'applyGiftWrapping': False,
                'bundleInfoList': [],
                'enableGiftWrapping': False,
                'hasGiftChangeOptions': False,
                'pricesWhenAtc': {
                    'SALES_PRICE': 26990
                },
                'primaryVendorItemId': 93437504336,
                'quantity': 1
            }
        ],
        'wowCardCcidPacScope': False,
        'wowCardPacScope': False,
        'wowCardPacUsagePromotionScope': False,
        'totalPrice': 26990.0,
        'invalidPAC': 'WOW_CARD_PAC',
        'price': 26990,
        'productId': 9024146312,
        'itemId': 26462223018,
        'brandName': '',
        'categoryId': '',
        'itemName': '[달빛식혜] 맛있는 국내산 쌀 얼음호박식혜/ 전통 수제 식혜, 8개, 500ml',
        'cpBusiness': '',
        'cpCategoryIds': '',
        'unitName1': 'Beverages',
        'unitName2': 'Drinks'
    }
    
    return run_request(session, method, url, headers, body)
