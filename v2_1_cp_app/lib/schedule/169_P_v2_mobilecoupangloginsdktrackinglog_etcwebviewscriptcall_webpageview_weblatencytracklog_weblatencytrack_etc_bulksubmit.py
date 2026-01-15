import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 168
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '25270',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '25270',
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/4.9.3'
    }
    
    body = [
        {
            'common': {
                'platform': 'android',
                'libraryVersion': '0.6.7',
                'pcid': '17679762746194168937968',
                'lang': 'ko-KR',
                'appCode': 'coupang',
                'market': 'KR',
                'resolution': '1080x2340',
                'eventTime': '2026-01-10T01:32:00.364+0900',
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
                'schemaId': 12936,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'member',
                'logCategory': 'system',
                'logType': 'debug',
                'pageName': 'login',
                'eventName': 'mobile_coupang_login_sdk_tracking_log',
                'message': 'tab has finished loading'
            },
            'extra': {}
        },
        {
            'common': {
                'platform': 'android',
                'libraryVersion': '0.6.7',
                'pcid': '17679762746194168937968',
                'lang': 'ko-KR',
                'appCode': 'coupang',
                'market': 'KR',
                'resolution': '1080x2340',
                'eventTime': '2026-01-10T01:32:00.533+0900',
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
                'schemaId': 1154,
                'schemaVersion': 1
            },
            'data': {
                'logType': 'system',
                'domain': 'webView',
                'eventName': 'etc_webview_script_call',
                'scriptName': 'logEvent',
                'logCategory': 'etc'
            },
            'extra': {}
        },
        {
            'common': {
                'platform': 'android',
                'libraryVersion': '0.6.7',
                'pcid': '17679762746194168937968',
                'lang': 'ko-KR',
                'appCode': 'coupang',
                'market': 'KR',
                'resolution': '1080x2340',
                'eventTime': '2026-01-10T01:32:00.538+0900',
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
                'schemaId': 10943,
                'schemaVersion': 4
            },
            'data': {
                'logType': 'performance',
                'origin': 'https://m.coupang.com',
                'platformType': 'browser',
                'userAgent': 'Mozilla/5.0 (Linux; Android 15; SM-A165N Build/AP3A.240905.015.A2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/131.0.6778.260 Mobile Safari/537.36',
                'title': 'BTF',
                'pageName': 'sdp',
                'url': 'https://m.coupang.com/vm/products/9024146312/brand-sdp-node/items/26462223018/?sourceType=search&unitCategoryFirstDepth=Beverages&unitCategorySecondDepth=Drinks&unitPrice=%28100ml%EB%8B%B9+675%EC%9B%90%29&sdpVisitKey=fyuk5pnr11rkb1z4qh&bundleId=52&categoryId=1474&keyword=%25ED%2598%25B8%25EB%25B0%2595%25EC%258B%259D%25ED%2598%259C%2520%25EB%258B%25AC%25EB%25B9%259B&searchId=0797993d22350&vendorItemId=93437504336&sid=c658d419f4d046cfb15f281769b15de7fbc66b30&freshProduct=false&deliveryType=VENDOR_DELIVERY&style=BRAND_SDP&innerWebView=true&productCategory=&productCategories=&internalCategoryCodes=58799&brandShopWidgetStyle=A&itemId=26462223018&soldOut=false&brandShopAvailable=false&expandBottom=false&memberEligible=true&methodLoadedKey=vid93437504336&memberSrl=0&loyaltyMember=false&segments=&warningBanner3p=true&ce=false&finalPrice=26990&price=26990&categoryCodes=1474%252C1480%252C1449%252C1171%252C1170%252C1&sortBy=ORDER_SCORE_ASC&isAddToCart=true&btfStyle=NOT_APPLICABLE&showFilterDropdownList=false&sourceItemPdd=1768316399999&hasOptionTable=true&isFashion=false&usedItem=false&isGiftCard=false&luxuryItem=false&lockedPhone=false&goldItem=false&preOrder=false&adultProduct=false&optionAmount=2&reviewExtraParams=%257B%2522isMatchedShowDataAtRdpEnableDirectV2%2522%253Afalse%252C%2522isGiftCard%2522%253Afalse%252C%2522isValidItem%2522%253Atrue%252C%2522reviewWritableStyle%2522%253A%2522FLOATING_BANNER%2522%252C%2522noticeTemplateId%2522%253A%252220%2522%252C%2522isMatchedHideDataAtRdpEnableDirectV2%2522%253Afalse%252C%2522isUsedItem%2522%253Afalse%252C%2522isHideHandleBar%2522%253Atrue%252C%2522isLuxury%2522%253Afalse%252C%2522sdpVisitKey%2522%253A%2522fyuk5pnr11rkb1z4qh%2522%252C%2522isAdjustRankingTarget%2522%253Afalse%252C%2522hideGNB%2522%253Atrue%252C%2522isTravelItem%2522%253Afalse%252C%2522isAdult%2522%253Afalse%257D&adParams=%7B%22systemTextSizeScale%22%3A1%7D',
                'searchParams': 'sourceType=search&unitCategoryFirstDepth=Beverages&unitCategorySecondDepth=Drinks&unitPrice=%28100ml%EB%8B%B9+675%EC%9B%90%29&sdpVisitKey=fyuk5pnr11rkb1z4qh&bundleId=52&categoryId=1474&keyword=%25ED%2598%25B8%25EB%25B0%2595%25EC%258B%259D%25ED%2598%259C%2520%25EB%258B%25AC%25EB%25B9%259B&searchId=0797993d22350&vendorItemId=93437504336&sid=c658d419f4d046cfb15f281769b15de7fbc66b30&freshProduct=false&deliveryType=VENDOR_DELIVERY&style=BRAND_SDP&innerWebView=true&productCategory=&productCategories=&internalCategoryCodes=58799&brandShopWidgetStyle=A&itemId=26462223018&soldOut=false&brandShopAvailable=false&expandBottom=false&memberEligible=true&methodLoadedKey=vid93437504336&memberSrl=0&loyaltyMember=false&segments=&warningBanner3p=true&ce=false&finalPrice=26990&price=26990&categoryCodes=1474%252C1480%252C1449%252C1171%252C1170%252C1&sortBy=ORDER_SCORE_ASC&isAddToCart=true&btfStyle=NOT_APPLICABLE&showFilterDropdownList=false&sourceItemPdd=1768316399999&hasOptionTable=true&isFashion=false&usedItem=false&isGiftCard=false&luxuryItem=false&lockedPhone=false&goldItem=false&preOrder=false&adultProduct=false&optionAmount=2&reviewExtraParams=%257B%2522isMatchedShowDataAtRdpEnableDirectV2%2522%253Afalse%252C%2522isGiftCard%2522%253Afalse%252C%2522isValidItem%2522%253Atrue%252C%2522reviewWritableStyle%2522%253A%2522FLOATING_BANNER%2522%252C%2522noticeTemplateId%2522%253A%252220%2522%252C%2522isMatchedHideDataAtRdpEnableDirectV2%2522%253Afalse%252C%2522isUsedItem%2522%253Afalse%252C%2522isHideHandleBar%2522%253Atrue%252C%2522isLuxury%2522%253Afalse%252C%2522sdpVisitKey%2522%253A%2522fyuk5pnr11rkb1z4qh%2522%252C%2522isAdjustRankingTarget%2522%253Afalse%252C%2522hideGNB%2522%253Atrue%252C%2522isTravelItem%2522%253Afalse%252C%2522isAdult%2522%253Afalse%257D&adParams=%7B%22systemTextSizeScale%22%3A1%7D',
                'path': '/vm/products/9024146312/brand-sdp-node/items/26462223018/',
                'referrer': '',
                'domain': 'page view',
                'eventName': 'web_page_view',
                'logCategory': 'system',
                'ixid': '909d3cac-5744-4f2e-8ab7-30fed8a5a996',
                'viewCount': 1,
                'applicationId': 'no_applicationId_assigned',
                'hash': ''
            },
            'extra': {
                'redirect': 3,
                'request': 611,
                'dns': 0,
                'responseStart': 1767976318830,
                'domainLookupStart': 1767976318031,
                'ssl': 131,
                'url': 'https://m.coupang.com/vm/products/9024146312/brand-sdp-node/items/26462223018/?sourceType=search&unitCategoryFirstDepth=Beverages&unitCategorySecondDepth=Drinks&unitPrice=%28100ml%EB%8B%B9+675%EC%9B%90%29&sdpVisitKey=fyuk5pnr11rkb1z4qh&bundleId=52&categoryId=1474&keyword=%25ED%2598%25B8%25EB%25B0%2595%25EC%258B%259D%25ED%2598%259C%2520%25EB%258B%25AC%25EB%25B9%259B&searchId=0797993d22350&vendorItemId=93437504336&sid=c658d419f4d046cfb15f281769b15de7fbc66b30&freshProduct=false&deliveryType=VENDOR_DELIVERY&style=BRAND_SDP&innerWebView=true&productCategory=&productCategories=&internalCategoryCodes=58799&brandShopWidgetStyle=A&itemId=26462223018&soldOut=false&brandShopAvailable=false&expandBottom=false&memberEligible=true&methodLoadedKey=vid93437504336&memberSrl=0&loyaltyMember=false&segments=&warningBanner3p=true&ce=false&finalPrice=26990&price=26990&categoryCodes=1474%252C1480%252C1449%252C1171%252C1170%252C1&sortBy=ORDER_SCORE_ASC&isAddToCart=true&btfStyle=NOT_APPLICABLE&showFilterDropdownList=false&sourceItemPdd=1768316399999&hasOptionTable=true&isFashion=false&usedItem=false&isGiftCard=false&luxuryItem=false&lockedPhone=false&goldItem=false&preOrder=false&adultProduct=false&optionAmount=2&reviewExtraParams=%257B%2522isMatchedShowDataAtRdpEnableDirectV2%2522%253Afalse%252C%2522isGiftCard%2522%253Afalse%252C%2522isValidItem%2522%253Atrue%252C%2522reviewWritableStyle%2522%253A%2522FLOATING_BANNER%2522%252C%2522noticeTemplateId%2522%253A%252220%2522%252C%2522isMatchedHideDataAtRdpEnableDirectV2%2522%253Afalse%252C%2522isUsedItem%2522%253Afalse%252C%2522isHideHandleBar%2522%253Atrue%252C%2522isLuxury%2522%253Afalse%252C%2522sdpVisitKey%2522%253A%2522fyuk5pnr11rkb1z4qh%2522%252C%2522isAdjustRankingTarget%2522%253Afalse%252C%2522hideGNB%2522%253Atrue%252C%2522isTravelItem%2522%253Afalse%252C%2522isAdult%2522%253Afalse%257D&adParams=%7B%22systemTextSizeScale%22%3A1%7D',
                'platform': 'mweb',
                'redirectStart': 0,
                'connectStart': 1767976318058,
                'navigationStart': 1767976318028,
                'requestStart': 1767976318219,
                'response': 32,
                'secureConnectionStart': 1767976318083,
                'sentTime': '2026-01-09T16:32:00.510Z',
                'pcid': '17857832397245944678246',
                'fetchStart': 1767976318031,
                'connect': 156
            }
        },
        {
            'common': {
                'platform': 'android',
                'libraryVersion': '0.6.7',
                'pcid': '17679762746194168937968',
                'lang': 'ko-KR',
                'appCode': 'coupang',
                'market': 'KR',
                'resolution': '1080x2340',
                'eventTime': '2026-01-10T01:32:00.573+0900',
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
                'schemaId': 10797,
                'schemaVersion': 2
            },
            'data': {
                'logType': 'performance',
                'fcp': 1960,
                'domain': 'fcp',
                'platformType': 'browser',
                'eventName': 'web_latency_track_log',
                'logCategory': 'system',
                'ixid': '7bea35dc-d3d5-4a8a-8d3d-9d97ea9d7aad',
                'applicationId': 'no_applicationId_assigned',
                'pageName': 'sdp'
            },
            'extra': {
                'redirect': 3,
                'request': 611,
                'dns': 0,
                'responseStart': 1767976318830,
                'domainLookupStart': 1767976318031,
                'ssl': 131,
                'url': 'https://m.coupang.com/vm/products/9024146312/brand-sdp-node/items/26462223018/?sourceType=search&unitCategoryFirstDepth=Beverages&unitCategorySecondDepth=Drinks&unitPrice=%28100ml%EB%8B%B9+675%EC%9B%90%29&sdpVisitKey=fyuk5pnr11rkb1z4qh&bundleId=52&categoryId=1474&keyword=%25ED%2598%25B8%25EB%25B0%2595%25EC%258B%259D%25ED%2598%259C%2520%25EB%258B%25AC%25EB%25B9%259B&searchId=0797993d22350&vendorItemId=93437504336&sid=c658d419f4d046cfb15f281769b15de7fbc66b30&freshProduct=false&deliveryType=VENDOR_DELIVERY&style=BRAND_SDP&innerWebView=true&productCategory=&productCategories=&internalCategoryCodes=58799&brandShopWidgetStyle=A&itemId=26462223018&soldOut=false&brandShopAvailable=false&expandBottom=false&memberEligible=true&methodLoadedKey=vid93437504336&memberSrl=0&loyaltyMember=false&segments=&warningBanner3p=true&ce=false&finalPrice=26990&price=26990&categoryCodes=1474%252C1480%252C1449%252C1171%252C1170%252C1&sortBy=ORDER_SCORE_ASC&isAddToCart=true&btfStyle=NOT_APPLICABLE&showFilterDropdownList=false&sourceItemPdd=1768316399999&hasOptionTable=true&isFashion=false&usedItem=false&isGiftCard=false&luxuryItem=false&lockedPhone=false&goldItem=false&preOrder=false&adultProduct=false&optionAmount=2&reviewExtraParams=%257B%2522isMatchedShowDataAtRdpEnableDirectV2%2522%253Afalse%252C%2522isGiftCard%2522%253Afalse%252C%2522isValidItem%2522%253Atrue%252C%2522reviewWritableStyle%2522%253A%2522FLOATING_BANNER%2522%252C%2522noticeTemplateId%2522%253A%252220%2522%252C%2522isMatchedHideDataAtRdpEnableDirectV2%2522%253Afalse%252C%2522isUsedItem%2522%253Afalse%252C%2522isHideHandleBar%2522%253Atrue%252C%2522isLuxury%2522%253Afalse%252C%2522sdpVisitKey%2522%253A%2522fyuk5pnr11rkb1z4qh%2522%252C%2522isAdjustRankingTarget%2522%253Afalse%252C%2522hideGNB%2522%253Atrue%252C%2522isTravelItem%2522%253Afalse%252C%2522isAdult%2522%253Afalse%257D&adParams=%7B%22systemTextSizeScale%22%3A1%7D',
                'platform': 'mweb',
                'redirectStart': 0,
                'connectStart': 1767976318058,
                'navigationStart': 1767976318028,
                'requestStart': 1767976318219,
                'response': 32,
                'secureConnectionStart': 1767976318083,
                'sentTime': '2026-01-09T16:32:00.572Z',
                'pcid': '17857832397245944678246',
                'fetchStart': 1767976318031,
                'connect': 156
            }
        },
        {
            'common': {
                'platform': 'android',
                'libraryVersion': '0.6.7',
                'pcid': '17679762746194168937968',
                'lang': 'ko-KR',
                'appCode': 'coupang',
                'market': 'KR',
                'resolution': '1080x2340',
                'eventTime': '2026-01-10T01:32:00.576+0900',
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
                'schemaId': 11778,
                'schemaVersion': 1
            },
            'data': {
                'logType': 'performance',
                'domain': 'lcp',
                'lcp': 1960,
                'platformType': 'browser',
                'eventName': 'web_latency_track_log',
                'logCategory': 'system',
                'ixid': '4901542f-4d39-4cf5-9e89-567075d92574',
                'applicationId': 'no_applicationId_assigned',
                'pageName': 'sdp'
            },
            'extra': {
                'redirect': 3,
                'request': 611,
                'dns': 0,
                'responseStart': 1767976318830,
                'domainLookupStart': 1767976318031,
                'ssl': 131,
                'url': 'https://m.coupang.com/vm/products/9024146312/brand-sdp-node/items/26462223018/?sourceType=search&unitCategoryFirstDepth=Beverages&unitCategorySecondDepth=Drinks&unitPrice=%28100ml%EB%8B%B9+675%EC%9B%90%29&sdpVisitKey=fyuk5pnr11rkb1z4qh&bundleId=52&categoryId=1474&keyword=%25ED%2598%25B8%25EB%25B0%2595%25EC%258B%259D%25ED%2598%259C%2520%25EB%258B%25AC%25EB%25B9%259B&searchId=0797993d22350&vendorItemId=93437504336&sid=c658d419f4d046cfb15f281769b15de7fbc66b30&freshProduct=false&deliveryType=VENDOR_DELIVERY&style=BRAND_SDP&innerWebView=true&productCategory=&productCategories=&internalCategoryCodes=58799&brandShopWidgetStyle=A&itemId=26462223018&soldOut=false&brandShopAvailable=false&expandBottom=false&memberEligible=true&methodLoadedKey=vid93437504336&memberSrl=0&loyaltyMember=false&segments=&warningBanner3p=true&ce=false&finalPrice=26990&price=26990&categoryCodes=1474%252C1480%252C1449%252C1171%252C1170%252C1&sortBy=ORDER_SCORE_ASC&isAddToCart=true&btfStyle=NOT_APPLICABLE&showFilterDropdownList=false&sourceItemPdd=1768316399999&hasOptionTable=true&isFashion=false&usedItem=false&isGiftCard=false&luxuryItem=false&lockedPhone=false&goldItem=false&preOrder=false&adultProduct=false&optionAmount=2&reviewExtraParams=%257B%2522isMatchedShowDataAtRdpEnableDirectV2%2522%253Afalse%252C%2522isGiftCard%2522%253Afalse%252C%2522isValidItem%2522%253Atrue%252C%2522reviewWritableStyle%2522%253A%2522FLOATING_BANNER%2522%252C%2522noticeTemplateId%2522%253A%252220%2522%252C%2522isMatchedHideDataAtRdpEnableDirectV2%2522%253Afalse%252C%2522isUsedItem%2522%253Afalse%252C%2522isHideHandleBar%2522%253Atrue%252C%2522isLuxury%2522%253Afalse%252C%2522sdpVisitKey%2522%253A%2522fyuk5pnr11rkb1z4qh%2522%252C%2522isAdjustRankingTarget%2522%253Afalse%252C%2522hideGNB%2522%253Atrue%252C%2522isTravelItem%2522%253Afalse%252C%2522isAdult%2522%253Afalse%257D&adParams=%7B%22systemTextSizeScale%22%3A1%7D',
                'platform': 'mweb',
                'redirectStart': 0,
                'connectStart': 1767976318058,
                'navigationStart': 1767976318028,
                'requestStart': 1767976318219,
                'response': 32,
                'secureConnectionStart': 1767976318083,
                'sentTime': '2026-01-09T16:32:00.575Z',
                'pcid': '17857832397245944678246',
                'fetchStart': 1767976318031,
                'connect': 156
            }
        },
        {
            'common': {
                'platform': 'android',
                'libraryVersion': '0.6.7',
                'pcid': '17679762746194168937968',
                'lang': 'ko-KR',
                'appCode': 'coupang',
                'market': 'KR',
                'resolution': '1080x2340',
                'eventTime': '2026-01-10T01:32:00.603+0900',
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
                'schemaVersion': 12
            },
            'data': {
                'domain': 'tti',
                'logCategory': 'system',
                'logType': 'performance',
                'pageName': 'pdp',
                'eventName': 'tti-logger',
                'platformType': 'native',
                'tti': 0,
                'bounced': True,
                'screenType': 'NORMAL',
                'viewCreateTime': 0,
                'apiResponseTime': 0,
                'viewBindingTime': 0,
                'imageLoadingTime': 0,
                'networkState': 'wifi',
                'carrier': 'unknown',
                'webViewVersion': '131.0.6778.260',
                'ixid': '00014a65-f8fe-bd29-d300-ffd3750932c3',
                'async': None,
                'serverTime': None,
                'domReady': None,
                'applicationId': None,
                'serverProcessingTime': 0,
                'serverFetchingTime': 0,
                'responseSize': 0,
                'akamaiToGatewayServiceTime': None,
                'internalProcessingTime': None,
                'transferTime': None,
                'imageCount': 0,
                'prepareApiTime': 0,
                'prepareImageTime': 0,
                'maxImageSize': None,
                'averageImageSize': None,
                'parsingTime': None,
                'pageVersion': None,
                'cdn': None,
                'viewUpdateTime': 0,
                'gatewayProcessingTime': 0,
                'responseTransferTime': 0,
                'apiBeforeFetchingTime': 0,
                'apiAfterFetchingTime': 0
            },
            'extra': {
                'api': '[{"key":"productDetail","time":308,"parse":276,"dispatch":248,"binding":77,"client_request_to_cdn":75,"client_request_to_gw":82,"gw_response_to_client":78,"response_transfer_time":2,"content_length":20377,"unzipped_size":132877},{"key":"","time":-1,"parse":-1,"dispatch":-1,"binding":-1,"client_request_to_cdn":-1,"client_request_to_gw":-1,"gw_response_to_client":-1,"response_transfer_time":-1,"content_length":0,"unzipped_size":0}]',
                'image': '[{"key":"PRELOAD","time":2,"url":"https:\\/\\/thumbnail.coupangcdn.com\\/thumbnails\\/remote\\/657x657q90trim\\/image\\/vendor_inventory\\/3b3a\\/29bcfec71c7f96c93b580e2df31da837e3779be4f7c74f953bd1d0535197.jpg.webp","preload":"PRELOAD_SUCCESS","image_loading_end":"363277297","image_decoding":"-1","image_loading_start":"363277296","after_decoding":"-1","image_fetching":"-1","before_fetching":"-1","cacheType":"MEMORY_CACHE"}]',
                'total': '',
                'categoryDepth': '',
                'campaignId': '',
                'signal': -1,
                'viewUpdateTime': 0,
                'prepareApiTime': 0,
                'prepareImageTime': 0,
                'maxImageUrl': 'https://thumbnail.coupangcdn.com/thumbnails/remote/657x657q90trim/image/vendor_inventory/3b3a/29bcfec71c7f96c93b580e2df31da837e3779be4f7c74f953bd1d0535197.jpg.webp',
                'reason': 'java.lang.Exception: Process LandingAfterAction will redirect to other page',
                'pagesnapshottime': '1',
                'sdpvisitkey': 'fyuk5pnr11rkb1z4qh',
                'isorganic': 'true',
                'pagesnapshot': '{"domainPageArea":[{"viewName":"ProductDetailThumbnailView","isHidden":false,"isZeroSize":false,"viewType":"PRODUCT_DETAIL_ITEM_THUMBNAILS"},{"viewName":"BadgesView","isHidden":false,"isZeroSize":false,"viewType":"PRODUCT_DETAIL_PRODUCT_BADGES"},{"viewName":"ProductInfoView","isHidden":false,"isZeroSize":false,"viewType":"PRODUCT_DETAIL_PRODUCT_INFO"},{"viewName":"ProductDetailUWidgetView","isHidden":false,"isZeroSize":false,"viewType":"PRODUCT_DETAIL_UWIDGET"},{"viewName":"ProductDetailFlexboxView","isHidden":false,"isZeroSize":false,"viewType":"PRODUCT_DETAIL_FLEXBOX"},{"viewName":"PriceView","isHidden":false,"isZeroSize":false,"viewType":"PRODUCT_DETAIL_PRICE_INFO"},{"viewName":"ToggleHeaderView","isHidden":false,"isZeroSize":false,"viewType":"PRODUCT_DETAIL_TOGGLE_HEADER"},{"viewName":"LinearLayout","isHidden":false,"isZeroSize":true,"viewType":"PRODUCT_DETAIL_OPTION_TAB_SELECTOR"},{"viewName":"TableOptionListView","isHidden":false,"isZeroSize":false,"viewType":"PRODUCT_OPTION_TABLE_LIST_VIEW"},{"viewName":"SimilarItemsWidgetView","isHidden":false,"isZeroSize":true,"viewType":"PRODUCT_DETAIL_SIMILAR_ITEM_RECOMMENDATIONS_INFO"},{"viewName":"BenefitView","isHidden":false,"isZeroSize":false,"viewType":"PRODUCT_DETAIL_BENEFIT_INFO"},{"viewName":"DeliveryInfoView","isHidden":false,"isZeroSize":false,"viewType":"PRODUCT_DETAIL_DELIVERY_INFO"},{"viewName":"SellerInfoView","isHidden":false,"isZeroSize":false,"viewType":"PRODUCT_DETAIL_SELLER_INFO"},{"viewName":"ProductDetailCommonWebView","isHidden":false,"isZeroSize":false},{"viewName":"ProductDetailTitleBar","isHidden":false,"isZeroSize":false},{"viewName":"ProductDetailFrameLayoutV2","isHidden":false,"isZeroSize":false},{"viewName":"TabMenu","isHidden":false,"isZeroSize":false},{"viewName":"BottomButtonView","isHidden":false,"isZeroSize":false},{"viewName":"TranslateReportPersistentBottomSheet","isHidden":false,"isZeroSize":false},{"viewName":"ProductDetailFrameLayoutV2","isHidden":false,"isZeroSize":false}],"domainPageName":"sdp"}',
                'preloadviewstime': '280',
                'webschema': 'false',
                'sourcetype': 'search',
                'imagelag': '-2147483648',
                'optioncount': '2',
                'key': 'productId',
                'previousviewtype': 'GRID_2',
                'sdpatfimagestartcost': '11',
                'value': '9024146312',
                'viewcreatebreakdown': '{"applyThemeDuration":0,"attachFragmentDuration":3,"operationInitDuration":3,"operationInitDurationInBaseFragment":18,"viewInflateDuration":76,"viewInitDurationInBaseFragment":132}',
                'fragmentlayoutcreatetime': '230',
                'previousactivity': 'SearchRedesignActivity',
                'bodysize': '132877',
                'mediatype': 'IMAGE'
            }
        },
        {
            'common': {
                'platform': 'android',
                'libraryVersion': '0.6.7',
                'pcid': '17679762746194168937968',
                'lang': 'ko-KR',
                'appCode': 'coupang',
                'market': 'KR',
                'resolution': '1080x2340',
                'eventTime': '2026-01-10T01:32:00.605+0900',
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
                'schemaId': 11501,
                'schemaVersion': 4
            },
            'data': {
                'domain': 'sdp',
                'logCategory': 'event',
                'logType': 'click',
                'pageName': 'sdp',
                'eventName': 'sdp_click_duration',
                'sourceType': 'search',
                'searchId': '0797993d22350',
                'query': '호박식혜 달빛',
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'productId': 9024146312,
                'itemId': 26462223018,
                'vendorItemId': 93437504336,
                'isStart': True,
                'timeStamp': '1767976318111',
                'eventType': None,
                'pageViewKey': 'sdp_1',
                'emptySdpVisitKeyCause': None,
                'missingCount': None,
                'ixid': '00014a65-f8fe-bd29-d300-ffd3750932c3'
            },
            'extra': {
                'eventReferrer': 'sdp_time_spent_image_logging_event'
            }
        },
        {
            'common': {
                'platform': 'android',
                'libraryVersion': '0.6.7',
                'pcid': '17679762746194168937968',
                'lang': 'ko-KR',
                'appCode': 'coupang',
                'market': 'KR',
                'resolution': '1080x2340',
                'eventTime': '2026-01-10T01:32:00.606+0900',
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
                'schemaId': 11501,
                'schemaVersion': 4
            },
            'data': {
                'domain': 'sdp',
                'logCategory': 'event',
                'logType': 'click',
                'pageName': 'sdp',
                'eventName': 'sdp_click_duration',
                'sourceType': 'search',
                'searchId': '0797993d22350',
                'query': '호박식혜 달빛',
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'productId': 9024146312,
                'itemId': 26462223018,
                'vendorItemId': 93437504336,
                'isStart': False,
                'timeStamp': '1767976318339',
                'eventType': 'UNLABELED_EXIT',
                'pageViewKey': 'sdp_1',
                'emptySdpVisitKeyCause': None,
                'missingCount': None,
                'ixid': '00014a65-f8fe-bd29-d300-ffd3750932c3'
            },
            'extra': {
                'eventReferrer': 'sdp_click_duration'
            }
        },
        {
            'common': {
                'platform': 'android',
                'libraryVersion': '0.6.7',
                'pcid': '17679762746194168937968',
                'lang': 'ko-KR',
                'appCode': 'coupang',
                'market': 'KR',
                'resolution': '1080x2340',
                'eventTime': '2026-01-10T01:32:00.612+0900',
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
                'schemaId': 15987,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'sdp',
                'logCategory': 'view',
                'logType': 'modal',
                'pageName': 'sdp',
                'eventName': 'page_leave',
                'pvid': '92910302'
            },
            'extra': {}
        },
        {
            'common': {
                'platform': 'android',
                'libraryVersion': '0.6.7',
                'pcid': '17679762746194168937968',
                'lang': 'ko-KR',
                'appCode': 'coupang',
                'market': 'KR',
                'resolution': '1080x2340',
                'eventTime': '2026-01-10T01:32:00.616+0900',
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
                'schemaId': 14057,
                'schemaVersion': 2
            },
            'data': {
                'domain': 'sdp',
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'ProductDetailFragment',
                'eventName': 'image_loads',
                'networkType': 'wifi',
                'fileSizeList': '4419360,814784',
                'imageResolutionList': '1023x1080,439x464',
                'imageUrlList': 'https://thumbnail.coupangcdn.com/thumbnails/remote/1000x1000trim/image/vendor_inventory/3b3a/29bcfec71c7f96c93b580e2df31da837e3779be4f7c74f953bd1d0535197.jpg.webp,https://thumbnail.coupangcdn.com/thumbnails/remote/657x657q90trim/image/vendor_inventory/3b3a/29bcfec71c7f96c93b580e2df31da837e3779be4f7c74f953bd1d0535197.jpg.webp',
                'resultList': 'SUCCESS,SUCCESS',
                'itemIdList': None,
                'productIdList': None,
                'vendorItemIdList': '93437504336,93437504336',
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'searchId': '0797993d22350',
                'q': None,
                'cacheTypeList': 'MEMORY_CACHE,MEMORY_CACHE',
                'sourceType': 'sdp_atf,sdp_thumbnail',
                'imageDurationList': '119,1',
                'rawByteSizeList': '-1,-1'
            },
            'extra': {}
        }
    ]
    
    return run_request(session, method, url, headers, body)
