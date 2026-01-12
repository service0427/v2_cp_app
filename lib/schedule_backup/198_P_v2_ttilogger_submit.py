import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 197
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '3260',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/submit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '3260',
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/4.9.3'
    }
    
    body = {
        'common': {
            'platform': 'android',
            'libraryVersion': '0.6.7',
            'pcid': '17679762746194168937968',
            'lang': 'ko-KR',
            'appCode': 'coupang',
            'market': 'KR',
            'resolution': '1080x2340',
            'eventTime': '2026-01-10T01:32:10.491+0900',
            'memberSrl': '',
            'app': {
                'osVersion': '15',
                'model': 'SM-A165N',
                'appVersionName': '9.0.4',
                'appVersionCode': 2409040,
                'uuid': 'f0b740d2-3447-3b2b-b118-d66257275f8f'
            },
            'location': {
                'region': 'KR',
                'locale': 'ko-KR',
                'mcc': '',
                'timezone': 'Asia/Seoul'
            },
            'appId': 'com.coupang.mobile',
            'appSessionId': '56b36f12-6759-43bb-9077-f7cddcecc13c',
            'systemLanguage': 'ko'
        },
        'meta': {
            'schemaId': 137,
            'schemaVersion': 6
        },
        'data': {
            'logType': 'performance',
            'imageLoadingTime': 0,
            'tti': 3776,
            'platformType': 'browser',
            'pageName': 'sdp',
            'networkState': 'wifi',
            'async': False,
            'domain': 'tti',
            'eventName': 'tti-logger',
            'serverTime': 643,
            'logCategory': 'system',
            'ixid': '8542cf4f-aa79-4921-b00a-5485de92fd51',
            'applicationId': 'no_applicationId_assigned',
            'domReady': 3776
        },
        'extra': {
            'redirect': 3,
            'newLanding': 379,
            'request': 611,
            'dns': 0,
            'responseStart': 1767976318830,
            'moduleRender': 4,
            'newLandingApi': 356,
            'domainLookupStart': 1767976318031,
            'ssl': 131,
            'url': 'https://m.coupang.com/vm/products/9024146312/brand-sdp-node/items/26462223018/?sourceType=search&unitCategoryFirstDepth=Beverages&unitCategorySecondDepth=Drinks&unitPrice=%28100ml%EB%8B%B9+675%EC%9B%90%29&sdpVisitKey=fyuk5pnr11rkb1z4qh&bundleId=52&categoryId=1474&keyword=%25ED%2598%25B8%25EB%25B0%2595%25EC%258B%259D%25ED%2598%259C%2520%25EB%258B%25AC%25EB%25B9%259B&searchId=0797993d22350&vendorItemId=93437504336&sid=c658d419f4d046cfb15f281769b15de7fbc66b30&freshProduct=false&deliveryType=VENDOR_DELIVERY&style=BRAND_SDP&innerWebView=true&productCategory=&productCategories=&internalCategoryCodes=58799&brandShopWidgetStyle=A&itemId=26462223018&soldOut=false&brandShopAvailable=false&expandBottom=false&memberEligible=true&methodLoadedKey=vid93437504336&memberSrl=0&loyaltyMember=false&segments=&warningBanner3p=true&ce=false&finalPrice=26990&price=26990&categoryCodes=1474%252C1480%252C1449%252C1171%252C1170%252C1&sortBy=ORDER_SCORE_ASC&isAddToCart=true&btfStyle=NOT_APPLICABLE&showFilterDropdownList=false&sourceItemPdd=1768316399999&hasOptionTable=true&isFashion=false&usedItem=false&isGiftCard=false&luxuryItem=false&lockedPhone=false&goldItem=false&preOrder=false&adultProduct=false&optionAmount=2&reviewExtraParams=%257B%2522isMatchedShowDataAtRdpEnableDirectV2%2522%253Afalse%252C%2522isGiftCard%2522%253Afalse%252C%2522isValidItem%2522%253Atrue%252C%2522reviewWritableStyle%2522%253A%2522FLOATING_BANNER%2522%252C%2522noticeTemplateId%2522%253A%252220%2522%252C%2522isMatchedHideDataAtRdpEnableDirectV2%2522%253Afalse%252C%2522isUsedItem%2522%253Afalse%252C%2522isHideHandleBar%2522%253Atrue%252C%2522isLuxury%2522%253Afalse%252C%2522sdpVisitKey%2522%253A%2522fyuk5pnr11rkb1z4qh%2522%252C%2522isAdjustRankingTarget%2522%253Afalse%252C%2522hideGNB%2522%253Atrue%252C%2522isTravelItem%2522%253Afalse%252C%2522isAdult%2522%253Afalse%257D&adParams=%7B%22systemTextSizeScale%22%3A1%7D',
            'redirectStart': 0,
            'connectStart': 1767976318058,
            'navigationStart': 1767976318028,
            'requestStart': 1767976318219,
            'response': 32,
            'secureConnectionStart': 1767976318083,
            'calcType': 'default',
            'sentTime': '2026-01-09T16:32:10.489Z',
            'fetchStart': 1767976318031,
            'connect': 156
        }
    }
    
    return run_request(session, method, url, headers, body)
