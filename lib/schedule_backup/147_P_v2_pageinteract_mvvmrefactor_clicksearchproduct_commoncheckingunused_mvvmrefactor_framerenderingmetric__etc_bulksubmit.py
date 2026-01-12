import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 146
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '11812',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '11812',
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
                'eventTime': '2026-01-10T01:31:56.549+0900',
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
                'schemaId': 15989,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'srp',
                'logCategory': 'event',
                'logType': 'processing',
                'pageName': 'srp',
                'eventName': 'page_interact'
            },
            'extra': {
                'pvid': '70757900'
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
                'eventTime': '2026-01-10T01:31:56.648+0900',
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
                'schemaId': 7960,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'android',
                'logCategory': 'system',
                'logType': 'debug',
                'pageName': 'mvvm refactor',
                'eventName': 'mvvm refactor',
                'featureName': 'MoveToSdpMigration',
                'schemaName': 'move_to_sdp',
                'additionalComment': 'start'
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
                'eventTime': '2026-01-10T01:31:56.654+0900',
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
                'schemaId': 124,
                'schemaVersion': 53
            },
            'data': {
                'isNewBadge': False,
                'searchCount': 640,
                'isCartItem': False,
                'isRecentViewBadgeEligible': 'False',
                'pageName': 'srp',
                'reviewRating': '4.0',
                'isPremiumBrand': False,
                'isRecentViewBadge': 'False',
                'isRlux': False,
                'bestAwardsBadgeType': 'N',
                'searchId': '0797993d22350',
                'searchViewType': 'GRID_2',
                'isAiUspTargetProduct': False,
                'hasColorChip': 'false',
                'eventName': 'click_search_product',
                'rank': 1,
                'isNewArrival': False,
                'snsDiscountRate': -1,
                'isCashOnDelivery': 'false',
                'kan3CategoryId': 1449,
                'productId': '9024146312',
                'hasFirstPurchaseBadge': False,
                'unitname1': 'Beverages',
                'productPickType': '',
                'unitname2': 'Drinks',
                'isCoupick': False,
                'emphasizeText': '',
                'isStockQtyImpressed': False,
                'isNonWowPremiumBrandKitchenBadge': 'false',
                'isLoyaltyMember': False,
                'filterKey': None,
                'itemId': '26462223018',
                'domain': 'srp',
                'isRetail': False,
                'islatestModelStamp': False,
                'sortIsChecked': 'N',
                'isPastPurchase': False,
                'logType': 'click',
                'isCcidEligible': False,
                'vendorItemId': '93437504336',
                'isPreviousPurchaseBadge': 'False',
                'purposeTag': '',
                'queryCategory': 'Beverages',
                'isFarfetch': False,
                'isWowHomeFitting': False,
                'isBestReviewBadgeEligible': 'False',
                'hasUspGeneratedByAi': False,
                'hasAsHandymanBadge': False,
                'searchRank': 1,
                'wowOnlyInstantDiscountRate': -1,
                'isPremiumBrandBadge': 'false',
                'keywordType': 'FOOD',
                'logCategory': 'event',
                'displayCcidBadge': False,
                'salePrice': 0,
                'isBestReviewBadge': 'False',
                'isRuleBasedTitleEligible': 'false',
                'isPreviousPurchaseBadgeEligible': 'False',
                'displayFreeShippingBadge': False,
                'isBypass': True,
                'hasRuleBasedTitle': 'false',
                'isBestAwardsBadge': 'False',
                'q': '호박식혜 달빛',
                'internalCategoryId': '58799',
                'id': '9024146312',
                'itemProductId': '4'
            },
            'extra': {
                'abGroups': 'B,C',
                'catalogBrandName': '달빛기정떡',
                'hasMultipleImages': 'false',
                'hasTopBrand': False,
                'isTargetBadgeOverImage': False,
                'isRlux': False,
                'isFashionQuery': False,
                'hasLlmBrand': 'true',
                'sdpThumbnailImageCount': '9',
                'boldedBrandType': 'LLM',
                'isCashOnDelivery': 'false',
                'deliveryBadge': '',
                'isSamedayDeliveryItem': 'false',
                'isFreeReturnAvailable': 'false',
                'hasAttributeTag': False,
                'availableColorChipType': '',
                'unitname1': 'Beverages',
                'unitname2': 'Drinks',
                'highlightedKeywordsAvailable': '달빛,호박식혜',
                'ratingCount': '(1)',
                'isFreeDelivery': True,
                'isSellingFastItem': 'false',
                'badges': '',
                'abTestIds': '88757,96074',
                'llmRootBrandName': '달빛기정떡',
                'hasCatalogBrand': 'true',
                'srpThumbnailImageCount': '1',
                'referViewType': 'KEYWORD_SEARCH_PRODUCT',
                'isDawnDeliveryItem': 'false',
                'currentView': '/search_list',
                'eventReferrer': 'click_search_list'
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
                'eventTime': '2026-01-10T01:31:56.658+0900',
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
                'schemaId': 7598,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'common',
                'logCategory': 'system',
                'logType': 'platform',
                'pageName': '',
                'eventName': 'common_checking_unused',
                'key': 'MPA_3281',
                'value': 'getSelectedParamsString - has filter data'
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
                'eventTime': '2026-01-10T01:31:56.677+0900',
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
                'schemaId': 7960,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'android',
                'logCategory': 'system',
                'logType': 'debug',
                'pageName': 'mvvm refactor',
                'eventName': 'mvvm refactor',
                'featureName': 'fbi_pup_migration',
                'schemaName': None,
                'additionalComment': None
            },
            'extra': {
                'KEY_RATING_HIGHLIGHT': 'true',
                'sdp.requestParams': '{}',
                'sdp.sub.discount': '0.0',
                'sdp.sub.price': '0',
                'sdp.previousViewType': 'GRID_2',
                'KEY_PRODUCT_ID': '9024146312',
                'KEY_THUMBNAIL_IMAGE': 'com.coupang.mobile.common.dto.widget.ImageVO@b0d644cf',
                'KEY_SALE_PRICE': '26,990원',
                'KEY_RATING_COUNT': '(1)',
                'KEY_SIMILAR_SEARCH_KEYWORD_TYPE': 'FOOD',
                'sdp.productImageScaleType': 'FIT_CENTER',
                'KEY_ITEM_PRODUCT_ID': '4',
                'KEY_RATING_AVERAGE': '4.0',
                'sdp.o.price': '32,000원',
                'KEY_PRODUCT_NAME': '[달빛식혜] 맛있는 국내산 쌀 얼음호박식혜/ 전통 수제 식혜, 8개, 500ml',
                'KEY_FILTER_KEY': 'GENDER_TAB:0',
                'sdp.egiftPromotion': 'false',
                'KEY_SEARCH_COUNT': '640',
                'sdp.discount': '15%',
                'KEY_ITEM_ID': '26462223018',
                'sdp.previousActivity': 'SearchRedesignActivity',
                'KEY_VENDOR_ITEM_ID': '93437504336',
                'sdp.toggleViewType': 'srp_grid',
                'KEY_RANK': '1',
                'KEY_SEARCH_RANK': '1',
                'KEY_SEARCH_KEYWORD': '호박식혜 달빛',
                'KEY_SEARCH_ID': '0797993d22350',
                'sdp.mvp': '11',
                'KEY_SOURCE_TYPE': 'search'
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
                'eventTime': '2026-01-10T01:31:56.728+0900',
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
                'schemaId': 9453,
                'schemaVersion': 2
            },
            'data': {
                'domain': 'AMP',
                'logCategory': 'system',
                'logType': 'performance',
                'pageName': 'domain.search.presentation.view.search.SearchRedesignActivity(SearchFragment)',
                'eventName': 'frame_rendering_metric',
                'totalFrameCount': 262,
                'totalSlowFrameCount': 150,
                'totalFrozenFrameCount': 0,
                'isTotalSlow': True,
                'totalAverageRenderingTime': 28,
                'idleFrameCount': 262,
                'idleSlowFrameCount': 150,
                'idleFrozenFrameCount': 0,
                'isIdleSlow': True,
                'isIdleFrozen': False,
                'idleAverageRenderingTime': 28,
                'scrollFrameCount': 0,
                'scrollSlowFrameCount': 0,
                'scrollFrozenFrameCount': 0,
                'isScrollSlow': None,
                'isScrollFrozen': None,
                'scrollAverageRenderingTime': None,
                'startTimeStamp': 1767976287501,
                'endTimeStamp': 1767976316727,
                'maximumFPS': None,
                'applicationId': 'com.coupang.mobile',
                'deviceName': 'SM-A165N',
                'buildType': 'prod',
                'osType': 'ANDROID',
                'sourceUserAgent': 'COUPANG|Android|15|9.0.4||null|f0b740d2-3447-3b2b-b118-d66257275f8f|Y|SM-A165N|f0b740d234472b2bb118d66257275f8f|25ede38a-c6e9-41b2-818a-aef7b5c17d0a|XXHDPI|17679762746194168937968||0||wifi|-1|||Asia/Seoul|c658d419f4d046cfb15f281769b15de7fbc66b30||1080|450|-1|1.0|true',
                'networkType': 'wifi',
                'isTotalFrozen': False,
                'screenType': None,
                'screenName': 'SearchFragment'
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
                'eventTime': '2026-01-10T01:31:56.731+0900',
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
                'schemaId': 152,
                'schemaVersion': 4
            },
            'data': {
                'domain': 'srp',
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'srp',
                'eventName': 'impression_ranking',
                'domainType': 'SRP',
                'searchId': '0797993d22350:3',
                'q': '호박식혜 달빛',
                'rank': 3,
                'totalCount': 640,
                'recommendationCount': None,
                'channel': 'user',
                'subChannel': None,
                'sourceType': None
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
                'eventTime': '2026-01-10T01:31:56.731+0900',
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
                'schemaId': 11942,
                'schemaVersion': 6
            },
            'data': {
                'logType': 'impression',
                'extraAttribute': 'srp,lowestpricein7days',
                'productId': '9183773210',
                'vendorItemId': '94055536143',
                'abGroup': 'A',
                'pageName': 'srp',
                'itemId': '27087300150',
                'q': '호박식혜 달빛',
                'searchId': 'searchId:0797993d22350',
                'domain': 'srp',
                'eventName': 'ab_test_exposure',
                'logCategory': 'impression',
                'abTestId': '85005'
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
                'eventTime': '2026-01-10T01:31:56.732+0900',
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
                'schemaId': 2851,
                'schemaVersion': 1
            },
            'data': {
                'logType': 'impression',
                'originalPrice': 23370,
                'salePrice': 18000,
                'query': '호박식혜 달빛',
                'eventName': 'attr_srp_product_ads',
                'rank': 0,
                'logCategory': 'impression',
                'adsId': 'none',
                'itemId': '27087300150',
                'q': '호박식혜 달빛',
                'searchRank': 0,
                'productId': '9183773210',
                'searchId': '0797993d22350',
                'vendorItemId': '94055536143',
                'domain': 'srp',
                'internalCategoryId': '58799',
                'id': '9183773210',
                'itemProductId': '0',
                'pageName': 'srp'
            },
            'extra': {}
        }
    ]
    
    return run_request(session, method, url, headers, body)
