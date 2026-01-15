import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 194
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '10835',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '10835',
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
                'eventTime': '2026-01-10T01:32:08.903+0900',
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
                'schemaId': 4345,
                'schemaVersion': 12
            },
            'data': {
                'logType': 'error',
                'browserMajor': '131',
                'message': 'Error occurred during product review: /vm/products/9024146312/brand-sdp/reviews/list?uuid=cf7e5884-b8bf-4051-b191-e1c72cb7886c&vendorId=A01492649&vendorItemId=93437504336&roleCode=&sdpVisitKey=fyuk5pnr11rkb1z4qh&deliveryType=VENDOR_DELIVERY&fresh=false&fruit=false&reviewExtraParams=%7B%22isMatchedShowDataAtRdpEnableDirectV2%22%3Afalse%2C%22isGiftCard%22%3Afalse%2C%22isValidItem%22%3Atrue%2C%22reviewWritableStyle%22%3A%22FLOATING_BANNER%22%2C%22noticeTemplateId%22%3A%2220%22%2C%22isMatchedHideDataAtRdpEnableDirectV2%22%3Afalse%2C%22isUsedItem%22%3Afalse%2C%22isHideHandleBar%22%3Atrue%2C%22isLuxury%22%3Afalse%2C%22sdpVisitKey%22%3A%22fyuk5pnr11rkb1z4qh%22%2C%22isAdjustRankingTarget%22%3Afalse%2C%22hideGNB%22%3Atrue%2C%22isTravelItem%22%3Afalse%2C%22isAdult%22%3Afalse%7D&optionAmount=2&isGiftCard=false&adultProduct=false&sortBy=ORDER_SCORE_ASC&recencyFilterType=ATTACHMENT_REVIEWS&isFirst=true&keyword=&page=0&slotSize=10&autoTranslateReview=false: 403',
                'pageName': 'sdp',
                'deviceName': 'SM-A165N',
                'browserEngineName': 'Blink',
                'sourceUrl': 'https://m.coupang.com/vm/products/9024146312/brand-sdp-node/items/26462223018/?sourceType=search&unitCategoryFirstDepth=Beverages&unitCategorySecondDepth=Drinks&unitPrice=%28100ml%EB%8B%B9+675%EC%9B%90%29&sdpVisitKey=fyuk5pnr11rkb1z4qh&bundleId=52&categoryId=1474&keyword=%25ED%2598%25B8%25EB%25B0%2595%25EC%258B%259D%25ED%2598%259C%2520%25EB%258B%25AC%25EB%25B9%259B&searchId=0797993d22350&vendorItemId=93437504336&sid=c658d419f4d046cfb15f281769b15de7fbc66b30&freshProduct=false&deliveryType=VENDOR_DELIVERY&style=BRAND_SDP&innerWebView=true&productCategory=&productCategories=&internalCategoryCodes=58799&brandShopWidgetStyle=A&itemId=26462223018&soldOut=false&brandShopAvailable=false&expandBottom=false&memberEligible=true&methodLoadedKey=vid93437504336&memberSrl=0&loyaltyMember=false&segments=&warningBanner3p=true&ce=false&finalPrice=26990&price=26990&categoryCodes=1474%252C1480%252C1449%252C1171%252C1170%252C1&sortBy=ORDER_SCORE_ASC&isAddToCart=true&btfStyle=NOT_APPLICABLE&showFilterDropdownList=false&sourceItemPdd=1768316399999&hasOptionTable=true&isFashion=false&usedItem=false&isGiftCard=false&luxuryItem=false&lockedPhone=false&goldItem=false&preOrder=false&adultProduct=false&optionAmount=2&reviewExtraParams=%257B%2522isMatchedShowDataAtRdpEnableDirectV2%2522%253Afalse%252C%2522isGiftCard%2522%253Afalse%252C%2522isValidItem%2522%253Atrue%252C%2522reviewWritableStyle%2522%253A%2522FLOATING_BANNER%2522%252C%2522noticeTemplateId%2522%253A%252220%2522%252C%2522isMatchedHideDataAtRdpEnableDirectV2%2522%253Afalse%252C%2522isUsedItem%2522%253Afalse%252C%2522isHideHandleBar%2522%253Atrue%252C%2522isLuxury%2522%253Afalse%252C%2522sdpVisitKey%2522%253A%2522fyuk5pnr11rkb1z4qh%2522%252C%2522isAdjustRankingTarget%2522%253Afalse%252C%2522hideGNB%2522%253Atrue%252C%2522isTravelItem%2522%253Afalse%252C%2522isAdult%2522%253Afalse%257D&adParams=%7B%22systemTextSizeScale%22%3A1%7D',
                'instanceId': 'primary-green-5c6cd8c4fc-qr8gq',
                'browserEngineVersion': '131.0.6778.260',
                'domain': 'sdp_mobile_web',
                'browserVersion': '131.0.6778.260',
                'osType': 'Android 15',
                'eventName': 'report',
                'browserName': 'Chrome WebView',
                'webPlatformType': 'pc',
                'pageSource': '',
                'sourceUserAgent': 'Mozilla/5.0 (Linux; Android 15; SM-A165N Build/AP3A.240905.015.A2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/131.0.6778.260 Mobile Safari/537.36',
                'logCategory': 'system',
                'applicationId': 'sdp_webview',
                'networkType': 'wifi',
                'sourceDomain': 'm.coupang.com',
                'sourcePath': '/vm/products/9024146312/brand-sdp-node/items/26462223018/',
                'errorCount': 1
            },
            'extra': {
                'jslog_tag': 'manual_report',
                'sentTime': '2026-01-09T16:32:08.896Z',
                'jslog_version': '4.0.7-beta-12',
                'stackTrace': 'Error\n    at e.report (https://assets.coupangcdn.com/customjs/jserror/4.0.7-beta-12/jslog-iife.pe.min.js:1:29892)\n    at https://assets.coupangcdn.com/front/sdp-mobile-web/20260109090035/modules/product-review/dist/product-review.module.csr.js:2:1054346\n    at https://assets.coupangcdn.com/front/sdp-mobile-web/20260109090035/modules/product-review/dist/product-review.module.csr.js:2:1052232\n    at Object.next (https://assets.coupangcdn.com/front/sdp-mobile-web/20260109090035/modules/product-review/dist/product-review.module.csr.js:2:1052337)\n    at o (https://assets.coupangcdn.com/front/sdp-mobile-web/20260109090035/modules/product-review/dist/product-review.module.csr.js:2:1051054)'
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
                'eventTime': '2026-01-10T01:32:09.121+0900',
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
                'schemaId': 238,
                'schemaVersion': 57
            },
            'data': {
                'logType': 'impression',
                'numScrolledToItems': 0,
                'feedsId': 'feed-062ecc4edae248c5bd910909a379b899-1.17.60:pac_ads-P9024146312_I26462223018',
                'targetItems': 'p9183773210_i27087300150_v94055536143,p7090545477_i25504526058_v92496599920,p9294395160_i13349235003_v92291667645,p1713938713_i24974246715_v70905531768,p8670726272_i20920725654_v81382472687,p4664196008_i12854806708_v73088343227,p9294242580_i27528818705_v92557549302,p8439185584_i236326205_v3579198651,p9257665278_i24997994042_v92022026919,p8243592423_i26832005654_v86092864793,p8585218788_i24888122629_v91894789258,p9061173786_i24922359587_v86092886994,p8444687533_i24428814718_v91436309864,p8783302384_i25556975234_v92457891981,p8444686525_i24428810886_v91436320667,p4368687880_i5146609740_v72455947215,p9296273926_i27535829904_v94500367443,p7919053402_i21752240820_v88801264113,p9006013570_i26395144744_v93371439656,p7719137153_i20711407434_v70597731561,p7694516482_i18034968455_v85189445419,p8238308736_i24051652993_v85791572241,p9296538177_i27536706322_v94501223545,p8288420616_i23303147421_v86092944789,p2057983357_i3497916607_v71484115677,p8705044838_i25280248679_v92275835995,p9294382995_i23926473323_v90948656429,p8114968257_i23518104201_v92262582139,p9080831656_i26676668432_v93553705516,p7251500_i18729358101_v85861964231',
                'pageName': 'recommendation',
                'rocketWowType': 'p9183773210_i27087300150_v94055536143_null,p7090545477_i25504526058_v92496599920_null,p9294395160_i13349235003_v92291667645_null,p1713938713_i24974246715_v70905531768_null,p8670726272_i20920725654_v81382472687_null,p4664196008_i12854806708_v73088343227_null,p9294242580_i27528818705_v92557549302_null,p8439185584_i236326205_v3579198651_null,p9257665278_i24997994042_v92022026919_null,p8243592423_i26832005654_v86092864793_null,p8585218788_i24888122629_v91894789258_null,p9061173786_i24922359587_v86092886994_null,p8444687533_i24428814718_v91436309864_null,p8783302384_i25556975234_v92457891981_null,p8444686525_i24428810886_v91436320667_null,p4368687880_i5146609740_v72455947215_null,p9296273926_i27535829904_v94500367443_null,p7919053402_i21752240820_v88801264113_null,p9006013570_i26395144744_v93371439656_null,p7719137153_i20711407434_v70597731561_null,p7694516482_i18034968455_v85189445419_null,p8238308736_i24051652993_v85791572241_null,p9296538177_i27536706322_v94501223545_null,p8288420616_i23303147421_v86092944789_null,p2057983357_i3497916607_v71484115677_null,p8705044838_i25280248679_v92275835995_null,p9294382995_i23926473323_v90948656429_null,p8114968257_i23518104201_v92262582139_null,p9080831656_i26676668432_v93553705516_null,p7251500_i18729358101_v85861964231_null',
                'rmdValue': '',
                'numVisibleItems': 3,
                'sourceType': 'pac_ad_carousel',
                'domain': 'sdp',
                'dataFeedId': 'feed-062ecc4edae248c5bd910909a379b899',
                'eventName': 'attr_pac_ad_carousel',
                'rank': 1,
                'logCategory': 'impression',
                'rocketType': 'p9183773210_i27087300150_v94055536143_null,p7090545477_i25504526058_v92496599920_null,p9294395160_i13349235003_v92291667645_null,p1713938713_i24974246715_v70905531768_null,p8670726272_i20920725654_v81382472687_ROCKET,p4664196008_i12854806708_v73088343227_null,p9294242580_i27528818705_v92557549302_rocket_merchant_v3,p8439185584_i236326205_v3579198651_null,p9257665278_i24997994042_v92022026919_null,p8243592423_i26832005654_v86092864793_null,p8585218788_i24888122629_v91894789258_rocket_merchant_v3,p9061173786_i24922359587_v86092886994_null,p8444687533_i24428814718_v91436309864_null,p8783302384_i25556975234_v92457891981_ROCKET,p8444686525_i24428810886_v91436320667_null,p4368687880_i5146609740_v72455947215_ROCKET,p9296273926_i27535829904_v94500367443_null,p7919053402_i21752240820_v88801264113_null,p9006013570_i26395144744_v93371439656_null,p7719137153_i20711407434_v70597731561_ROCKET,p7694516482_i18034968455_v85189445419_ROCKET,p8238308736_i24051652993_v85791572241_rocket_merchant_v3,p9296538177_i27536706322_v94501223545_null,p8288420616_i23303147421_v86092944789_null,p2057983357_i3497916607_v71484115677_ROCKET,p8705044838_i25280248679_v92275835995_null,p9294382995_i23926473323_v90948656429_null,p8114968257_i23518104201_v92262582139_null,p9080831656_i26676668432_v93553705516_ROCKET,p7251500_i18729358101_v85861964231_ROCKET'
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
                'eventTime': '2026-01-10T01:32:09.132+0900',
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
                'schemaId': 14455,
                'schemaVersion': 2
            },
            'data': {
                'logType': 'click',
                'itemId': 26462223018,
                'clickArea': 'Close',
                'productId': 9024146312,
                'vendorItemId': 93437504336,
                'domain': 'sdp',
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'eventName': 'sdp_pac_widget_click',
                'addToCartSource': 'sdp',
                'logCategory': 'event',
                'pageName': 'sdp_pac',
                'isFresh': False
            },
            'extra': {
                'eventReferrer': '',
                'currentView': '/search_list'
            }
        }
    ]
    
    return run_request(session, method, url, headers, body)
