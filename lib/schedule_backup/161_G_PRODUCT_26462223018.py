import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 160
# Method: GET
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'sec-ch-ua': '"Android WebView";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
#     'sec-ch-ua-mobile': '?1',
#     'sec-ch-ua-platform': '"Android"',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Linux; Android 15; SM-A165N Build/AP3A.240905.015.A2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/131.0.6778.260 Mobile Safari/537.36',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'x-timestamp': '1767976316935',
#     'coupang-app': 'COUPANG|Android|15|9.0.4||null|f0b740d2-3447-3b2b-b118-d66257275f8f|Y|SM-A165N|f0b740d234472b2bb118d66257275f8f|25ede38a-c6e9-41b2-818a-aef7b5c17d0a|XXHDPI|17679762746194168937968||0||wifi|-1|||Asia/Seoul|c658d419f4d046cfb15f281769b15de7fbc66b30||1080|450|-1|1.0|true',
#     'x-coupang-font-scale': '1.0',
#     'run-mode': 'production',
#     'x-coupang-app-request': 'true',
#     'install-market-info': 'unknown',
#     'x-coupang-target-market': 'KR',
#     'x-coupang-app-name': 'coupang',
#     'x-cp-app-id': 'com.coupang.mobile',
#     'x-coupang-app-id': 'coupang-global',
#     'x-coupang-origin-region': 'KR',
#     'x-signature': '121110db7f367099c3a114384ea1b83021ee4bd8e2d07cb9cd747a020a5e5810',
#     'x-coupang-accept-language': 'ko-KR',
#     'x-requested-with': 'com.coupang.mobile',
#     'sec-fetch-site': 'none',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-user': '?1',
#     'sec-fetch-dest': 'document',
#     'accept-encoding': 'gzip, deflate, br, zstd',
#     'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
#     'priority': 'u=0, i'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://m.coupang.com/vm/products/9024146312/brand-sdp-node/items/26462223018/?sourceType=search&unitCategoryFirstDepth=Beverages&unitCategorySecondDepth=Drinks&unitPrice=%28100ml%EB%8B%B9+675%EC%9B%90%29&sdpVisitKey=fyuk5pnr11rkb1z4qh&bundleId=52&categoryId=1474&keyword=%25ED%2598%25B8%25EB%25B0%2595%25EC%258B%259D%25ED%2598%259C%2520%25EB%258B%25AC%25EB%25B9%259B&searchId=0797993d22350&vendorItemId=93437504336&sid=c658d419f4d046cfb15f281769b15de7fbc66b30&freshProduct=false&deliveryType=VENDOR_DELIVERY&style=BRAND_SDP&innerWebView=true&productCategory=&productCategories=&internalCategoryCodes=58799&brandShopWidgetStyle=A&itemId=26462223018&soldOut=false&brandShopAvailable=false&expandBottom=false&memberEligible=true&methodLoadedKey=vid93437504336&memberSrl=0&loyaltyMember=false&segments=&warningBanner3p=true&ce=false&finalPrice=26990&price=26990&categoryCodes=1474%252C1480%252C1449%252C1171%252C1170%252C1&sortBy=ORDER_SCORE_ASC&isAddToCart=true&btfStyle=NOT_APPLICABLE&showFilterDropdownList=false&sourceItemPdd=1768316399999&hasOptionTable=true&isFashion=false&usedItem=false&isGiftCard=false&luxuryItem=false&lockedPhone=false&goldItem=false&preOrder=false&adultProduct=false&optionAmount=2&reviewExtraParams=%257B%2522isMatchedShowDataAtRdpEnableDirectV2%2522%253Afalse%252C%2522isGiftCard%2522%253Afalse%252C%2522isValidItem%2522%253Atrue%252C%2522reviewWritableStyle%2522%253A%2522FLOATING_BANNER%2522%252C%2522noticeTemplateId%2522%253A%252220%2522%252C%2522isMatchedHideDataAtRdpEnableDirectV2%2522%253Afalse%252C%2522isUsedItem%2522%253Afalse%252C%2522isHideHandleBar%2522%253Atrue%252C%2522isLuxury%2522%253Afalse%252C%2522sdpVisitKey%2522%253A%2522fyuk5pnr11rkb1z4qh%2522%252C%2522isAdjustRankingTarget%2522%253Afalse%252C%2522hideGNB%2522%253Atrue%252C%2522isTravelItem%2522%253Afalse%252C%2522isAdult%2522%253Afalse%257D&adParams=%7B%22systemTextSizeScale%22%3A1%7D"
    method = "GET"
    
    headers = {
        'sec-ch-ua': '"Android WebView";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 15; SM-A165N Build/AP3A.240905.015.A2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/131.0.6778.260 Mobile Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'x-timestamp': '1767976316935',
        'coupang-app': 'COUPANG|Android|15|9.0.4||null|f0b740d2-3447-3b2b-b118-d66257275f8f|Y|SM-A165N|f0b740d234472b2bb118d66257275f8f|25ede38a-c6e9-41b2-818a-aef7b5c17d0a|XXHDPI|17679762746194168937968||0||wifi|-1|||Asia/Seoul|c658d419f4d046cfb15f281769b15de7fbc66b30||1080|450|-1|1.0|true',
        'x-coupang-font-scale': '1.0',
        'run-mode': 'production',
        'x-coupang-app-request': 'true',
        'install-market-info': 'unknown',
        'x-coupang-target-market': 'KR',
        'x-coupang-app-name': 'coupang',
        'x-cp-app-id': 'com.coupang.mobile',
        'x-coupang-app-id': 'coupang-global',
        'x-coupang-origin-region': 'KR',
        'x-signature': '121110db7f367099c3a114384ea1b83021ee4bd8e2d07cb9cd747a020a5e5810',
        'x-coupang-accept-language': 'ko-KR',
        'x-requested-with': 'com.coupang.mobile',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'priority': 'u=0, i'
    }
    
    body = None
    
    return run_request(session, method, url, headers, body)
