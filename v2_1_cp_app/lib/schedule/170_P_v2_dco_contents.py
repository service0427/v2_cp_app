import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 169
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-length': '1122',
#     'sec-ch-ua-platform': '"Android"',
#     'user-agent': 'Mozilla/5.0 (Linux; Android 15; SM-A165N Build/AP3A.240905.015.A2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/131.0.6778.260 Mobile Safari/537.36',
#     'accept': 'application/json, text/plain, */*',
#     'sec-ch-ua': '"Android WebView";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
#     'content-type': 'application/json',
#     'sec-ch-ua-mobile': '?1',
#     'origin': 'https://m.coupang.com',
#     'x-requested-with': 'com.coupang.mobile',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-dest': 'empty',
#     'referer': 'https://m.coupang.com/vm/products/9024146312/brand-sdp-node/items/26462223018/?sourceType=search&unitCategoryFirstDepth=Beverages&unitCategorySecondDepth=Drinks&unitPrice=%28100ml%EB%8B%B9+675%EC%9B%90%29&sdpVisitKey=fyuk5pnr11rkb1z4qh&bundleId=52&categoryId=1474&keyword=%25ED%2598%25B8%25EB%25B0%2595%25EC%258B%259D%25ED%2598%259C%2520%25EB%258B%25AC%25EB%25B9%259B&searchId=0797993d22350&vendorItemId=93437504336&sid=c658d419f4d046cfb15f281769b15de7fbc66b30&freshProduct=false&deliveryType=VENDOR_DELIVERY&style=BRAND_SDP&innerWebView=true&productCategory=&productCategories=&internalCategoryCodes=58799&brandShopWidgetStyle=A&itemId=26462223018&soldOut=false&brandShopAvailable=false&expandBottom=false&memberEligible=true&methodLoadedKey=vid93437504336&memberSrl=0&loyaltyMember=false&segments=&warningBanner3p=true&ce=false&finalPrice=26990&price=26990&categoryCodes=1474%252C1480%252C1449%252C1171%252C1170%252C1&sortBy=ORDER_SCORE_ASC&isAddToCart=true&btfStyle=NOT_APPLICABLE&showFilterDropdownList=false&sourceItemPdd=1768316399999&hasOptionTable=true&isFashion=false&usedItem=false&isGiftCard=false&luxuryItem=false&lockedPhone=false&goldItem=false&preOrder=false&adultProduct=false&optionAmount=2&reviewExtraParams=%257B%2522isMatchedShowDataAtRdpEnableDirectV2%2522%253Afalse%252C%2522isGiftCard%2522%253Afalse%252C%2522isValidItem%2522%253Atrue%252C%2522reviewWritableStyle%2522%253A%2522FLOATING_BANNER%2522%252C%2522noticeTemplateId%2522%253A%252220%2522%252C%2522isMatchedHideDataAtRdpEnableDirectV2%2522%253Afalse%252C%2522isUsedItem%2522%253Afalse%252C%2522isHideHandleBar%2522%253Atrue%252C%2522isLuxury%2522%253Afalse%252C%2522sdpVisitKey%2522%253A%2522fyuk5pnr11rkb1z4qh%2522%252C%2522isAdjustRankingTarget%2522%253Afalse%252C%2522hideGNB%2522%253Atrue%252C%2522isTravelItem%2522%253Afalse%252C%2522isAdult%2522%253Afalse%257D&adParams=%7B%22systemTextSizeScale%22%3A1%7D',
#     'accept-encoding': 'gzip, deflate, br, zstd',
#     'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
#     'priority': 'u=1, i',
#     'cookie': 'PCID=17857832397245944678246; MARKETID=17857832397245944678246; x-coupang-accept-language=ko-KR; x-coupang-target-market=KR; coupang-app=COUPANG%7CAndroid%7C15%7C9.0.4%7C%7Cnull%7Cf0b740d2-3447-3b2b-b118-d66257275f8f%7CY%7CSM-A165N%7Cf0b740d234472b2bb118d66257275f8f%7C25ede38a-c6e9-41b2-818a-aef7b5c17d0a%7CXXHDPI%7C17679762746194168937968%7C%7C0%7C%7Cwifi%7C-1%7C%7C%7CAsia%2FSeoul%7Cc658d419f4d046cfb15f281769b15de7fbc66b30%7C%7C1080%7C450%7C-1%7C1.0%7Ctrue; run-mode=production; helloCoupang=Y; ISAPP=Y; sid=c658d419f4d046cfb15f281769b15de7fbc66b30; timeZoneCode=Asia%2FSeoul; UUID=f0b740d2-3447-3b2b-b118-d66257275f8f'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://m.coupang.com/dco/api/v2/dco-contents"
    method = "POST"
    
    headers = {
        'content-length': '1122',
        'sec-ch-ua-platform': '"Android"',
        'user-agent': 'Mozilla/5.0 (Linux; Android 15; SM-A165N Build/AP3A.240905.015.A2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/131.0.6778.260 Mobile Safari/537.36',
        'accept': 'application/json, text/plain, */*',
        'sec-ch-ua': '"Android WebView";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'content-type': 'application/json',
        'sec-ch-ua-mobile': '?1',
        'origin': 'https://m.coupang.com',
        'x-requested-with': 'com.coupang.mobile',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://m.coupang.com/vm/products/9024146312/brand-sdp-node/items/26462223018/?sourceType=search&unitCategoryFirstDepth=Beverages&unitCategorySecondDepth=Drinks&unitPrice=%28100ml%EB%8B%B9+675%EC%9B%90%29&sdpVisitKey=fyuk5pnr11rkb1z4qh&bundleId=52&categoryId=1474&keyword=%25ED%2598%25B8%25EB%25B0%2595%25EC%258B%259D%25ED%2598%259C%2520%25EB%258B%25AC%25EB%25B9%259B&searchId=0797993d22350&vendorItemId=93437504336&sid=c658d419f4d046cfb15f281769b15de7fbc66b30&freshProduct=false&deliveryType=VENDOR_DELIVERY&style=BRAND_SDP&innerWebView=true&productCategory=&productCategories=&internalCategoryCodes=58799&brandShopWidgetStyle=A&itemId=26462223018&soldOut=false&brandShopAvailable=false&expandBottom=false&memberEligible=true&methodLoadedKey=vid93437504336&memberSrl=0&loyaltyMember=false&segments=&warningBanner3p=true&ce=false&finalPrice=26990&price=26990&categoryCodes=1474%252C1480%252C1449%252C1171%252C1170%252C1&sortBy=ORDER_SCORE_ASC&isAddToCart=true&btfStyle=NOT_APPLICABLE&showFilterDropdownList=false&sourceItemPdd=1768316399999&hasOptionTable=true&isFashion=false&usedItem=false&isGiftCard=false&luxuryItem=false&lockedPhone=false&goldItem=false&preOrder=false&adultProduct=false&optionAmount=2&reviewExtraParams=%257B%2522isMatchedShowDataAtRdpEnableDirectV2%2522%253Afalse%252C%2522isGiftCard%2522%253Afalse%252C%2522isValidItem%2522%253Atrue%252C%2522reviewWritableStyle%2522%253A%2522FLOATING_BANNER%2522%252C%2522noticeTemplateId%2522%253A%252220%2522%252C%2522isMatchedHideDataAtRdpEnableDirectV2%2522%253Afalse%252C%2522isUsedItem%2522%253Afalse%252C%2522isHideHandleBar%2522%253Atrue%252C%2522isLuxury%2522%253Afalse%252C%2522sdpVisitKey%2522%253A%2522fyuk5pnr11rkb1z4qh%2522%252C%2522isAdjustRankingTarget%2522%253Afalse%252C%2522hideGNB%2522%253Atrue%252C%2522isTravelItem%2522%253Afalse%252C%2522isAdult%2522%253Afalse%257D&adParams=%7B%22systemTextSizeScale%22%3A1%7D',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'priority': 'u=1, i',
        'cookie': 'PCID=17857832397245944678246; MARKETID=17857832397245944678246; x-coupang-accept-language=ko-KR; x-coupang-target-market=KR; coupang-app=COUPANG%7CAndroid%7C15%7C9.0.4%7C%7Cnull%7Cf0b740d2-3447-3b2b-b118-d66257275f8f%7CY%7CSM-A165N%7Cf0b740d234472b2bb118d66257275f8f%7C25ede38a-c6e9-41b2-818a-aef7b5c17d0a%7CXXHDPI%7C17679762746194168937968%7C%7C0%7C%7Cwifi%7C-1%7C%7C%7CAsia%2FSeoul%7Cc658d419f4d046cfb15f281769b15de7fbc66b30%7C%7C1080%7C450%7C-1%7C1.0%7Ctrue; run-mode=production; helloCoupang=Y; ISAPP=Y; sid=c658d419f4d046cfb15f281769b15de7fbc66b30; timeZoneCode=Asia%2FSeoul; UUID=f0b740d2-3447-3b2b-b118-d66257275f8f'
    }
    
    body = {
        'productId': 9024146312,
        'itemId': 26462223018,
        'vendorItemId': 93437504336,
        'adRequests': [
            {
                'adType': 'SDP_CAROUSEL3',
                'additionalParameters': {
                    'searchQuery': '%ED%98%B8%EB%B0%95%EC%8B%9D%ED%98%9C%20%EB%8B%AC%EB%B9%9B',
                    'unitname1': 'Beverages',
                    'unitname2': 'Drinks',
                    'widgetRank': 0,
                    'widgetIndexOnPage': 1
                },
                'continuationToken': 'placeholderfeed=CJABEhhQOTAyNDE0NjMxMl9JMjY0NjIyMjMwMThSFAoLc3dhcElmSmlrZ3USBWZhbHNlUiQKHGVuYWJsZVN0b3JlQmVzdFNlbGxpbmdXaWRnZXQSBHRydWVSFwoOaXNSb2NrZXRMdXh1cnkSBWZhbHNlUhQKC2hhc1ZhbGlkQ1RMEgVmYWxzZVIZChBzaG93QXBsdXNDb250ZW50EgVmYWxzZVIWCgl1bml0bmFtZTESCUJldmVyYWdlc1IWCg1zd2FwSWZTZWFmb29kEgVmYWxzZVITCgl1bml0bmFtZTISBkRyaW5rc1IYChBzdXBwb3J0QWRkVG9DYXJ0EgR0cnVlUhwKE3Nob3dOZXdBbmRIb3RXaWRnZXQSBWZhbHNlUhkKEHByZW1pdW1GcmVzaFVzZXISBWZhbHNlUh0KFW5lZWRUb1N3YXBNaWRDYXJvdXNlbBIEdHJ1ZVIRCghzd2FwSWZDRRIFZmFsc2VSIgoZc2hvd1F1YWxpdHlBc3N1cmFuY2VWaWRlbxIFZmFsc2VSFwoPa2FuQ2F0ZWdvcnlDb2RlEgQxNDc0UiYKCnByb2R1Y3RJZHMSGFA5MDI0MTQ2MzEyX0kyNjQ2MjIyMzAxOFISCglpc0Zhc2hpb24SBWZhbHNlUhsKEmlzQ3VzdG9tRHV0eUFCVGVzdBIFZmFsc2VSGwoSYnJhbmRTaG9wQXZhaWxhYmxlEgVmYWxzZVIQCgdpc0FnaW5nEgVmYWxzZVIXCg5pc0ZyZXNoUHJlbWl1bRIFZmFsc2WIAQE='
            }
        ]
    }
    
    return run_request(session, method, url, headers, body)
