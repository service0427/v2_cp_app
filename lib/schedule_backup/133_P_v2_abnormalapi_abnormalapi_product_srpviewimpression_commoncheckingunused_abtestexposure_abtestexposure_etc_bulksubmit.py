import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 132
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '10621',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '10621',
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
                'eventTime': '2026-01-10T01:31:51.536+0900',
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
                'schemaId': 17211,
                'schemaVersion': 2
            },
            'data': {
                'domain': 'srp',
                'logCategory': 'system',
                'logType': 'debug',
                'pageName': None,
                'eventName': None,
                'widgetTotalCount': 30,
                'widgetTypeCount': 3,
                'widgetDistribution': '{"DYNAMIC_TEMPLATE":3,"U_WIDGET":26,"AB_TRACKING":1}',
                'analyzeDuration': 2
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
                'eventTime': '2026-01-10T01:31:51.539+0900',
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
                'schemaId': 9854,
                'schemaVersion': 2
            },
            'data': {
                'domain': 'search',
                'logCategory': 'system',
                'logType': 'error',
                'pageName': 'search',
                'eventName': 'abnormal_api',
                'abnormalLevel': 'component',
                'abnormalSubLevel': 'title',
                'requestParam': None,
                'requestURL': 'https://cmapi.coupang.com/v3/products',
                'fullRequestURL': 'https://cmapi.coupang.com/v3/products?filter=KEYWORD:%ED%98%B8%EB%B0%95%EC%8B%9D%ED%98%9C+%EB%8B%AC%EB%B9%9B|CCID:ALL|EXTRAS:channel/user|GET_FILTER:NONE|SINGLE_ENTITY:TRUE@SEARCH&preventingRedirection=false&resultType=default&ccidActivated=false&referrerPage=HOME'
            },
            'extra': {
                'errorType': 'DYNAMIC_TEMPLATE',
                'viewType': 'SRP_TOP_DYNAMIC_TEMPLATE',
                'errorMessage': 'APP_SRP_TOP_BANNER: variableMap',
                'vendorItemIds': [
                    ''
                ]
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
                'eventTime': '2026-01-10T01:31:51.540+0900',
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
                'schemaId': 9854,
                'schemaVersion': 2
            },
            'data': {
                'domain': 'search',
                'logCategory': 'system',
                'logType': 'error',
                'pageName': 'search',
                'eventName': 'abnormal_api',
                'abnormalLevel': 'component',
                'abnormalSubLevel': 'title',
                'requestParam': None,
                'requestURL': 'https://cmapi.coupang.com/v3/products',
                'fullRequestURL': 'https://cmapi.coupang.com/v3/products?filter=KEYWORD:%ED%98%B8%EB%B0%95%EC%8B%9D%ED%98%9C+%EB%8B%AC%EB%B9%9B|CCID:ALL|EXTRAS:channel/user|GET_FILTER:NONE|SINGLE_ENTITY:TRUE@SEARCH&preventingRedirection=false&resultType=default&ccidActivated=false&referrerPage=HOME'
            },
            'extra': {
                'errorType': 'DYNAMIC_TEMPLATE',
                'viewType': 'SRP_MID_DYNAMIC_TEMPLATE',
                'errorMessage': 'APP_SRP_MID_BANNER: variableMap',
                'vendorItemIds': [
                    ''
                ]
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
                'eventTime': '2026-01-10T01:31:51.541+0900',
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
                'schemaId': 11965,
                'schemaVersion': 15
            },
            'data': {
                'domain': '-',
                'logCategory': 'system',
                'logType': 'error',
                'pageName': 'SearchFragment',
                'eventName': 'product',
                'domainName': 'search',
                'errorDescription': 'PRODUCT_VITAMIN Type is not exist',
                'errorName': 'requiredViewTypeNotExist',
                'eventType': 'render',
                'source': 'server',
                'errorType': 'apiError'
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
                'eventTime': '2026-01-10T01:31:51.551+0900',
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
                'schemaId': 15704,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'srp',
                'logCategory': 'view',
                'logType': 'page',
                'pageName': 'srp',
                'eventName': 'srp_view_impression',
                'q': '호박식혜 달빛',
                'searchId': '0797993d22350',
                'rootSearchId': '0797993d22350',
                'previousRootSearchId': ''
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
                'eventTime': '2026-01-10T01:31:51.573+0900',
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
                'schemaId': 116,
                'schemaVersion': 23
            },
            'data': {
                'domain': 'srp',
                'logCategory': 'view',
                'logType': 'page',
                'pageName': 'srp',
                'eventName': None,
                'q': '호박식혜 달빛',
                'channel': 'user',
                'filterKeys': '',
                'searchViewType': 'GRID_2',
                'searchId': '0797993d22350',
                'searchCount': 640,
                'isCoupick': False,
                'rankOfCoupick': -1,
                'keywordType': 'FOOD',
                'isGenderTabTest': False,
                'hasSeeOtherRocketItem': None,
                'previousPage': None,
                'referralPage': None,
                'isFromRecoHintKeyword': False,
                'isCcidPriceSelect': None,
                'multiImageItemIds': None,
                'isLoyaltyMember': False,
                'rank': None,
                'ixid': '00014a5f-2f79-23fb-e384-abdc292008d4',
                'dpi': '450',
                'deviceFontScale': '1.0',
                'hasProdWColorChips': False,
                'hasProdWColorTexts': False,
                'turnoffAutosave': False,
                'hasProdOTLink': False,
                'subChannel': None,
                'sourceType': None,
                'selectedTheme': None,
                'subSourceType': None,
                'channelPremium': None,
                'filterType': '',
                'appliedFontScale': '1.0',
                'systemFontScale': '1.0',
                'midFilterKeys': None,
                'ga': None,
                'fbc': None,
                'fbp': None,
                'brandId': None
            },
            'extra': {
                'parentView': '/home',
                'pvId': '110251425',
                'dpi': 'XHDPI'
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
                'eventTime': '2026-01-10T01:31:51.575+0900',
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
                'key': '59701',
                'value': 'AddImageToRecentKeywordUseCase'
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
                'eventTime': '2026-01-10T01:31:51.576+0900',
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
                'schemaVersion': 8
            },
            'data': {
                'domain': 'srp',
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'srp',
                'eventName': 'ab_test_exposure',
                'productId': None,
                'itemId': None,
                'vendorItemId': None,
                'sdpVisitKey': None,
                'abTestId': '88343',
                'abGroup': 'B',
                'extraAttribute': None,
                'searchId': '0797993d22350',
                'cartSessionId': None,
                'cartId': None,
                'checkoutId': None,
                'categoryId': None,
                'categoryType': None,
                'campaignId': None,
                'toggleViewType': None,
                'widgetPosition': None,
                'subSourceType': None,
                'requestId': None,
                'q': None,
                'exposureCase': None,
                'premiumCategory': None,
                'isBadDiscount': None,
                'isNoDiscount': None
            },
            'extra': {
                'domainName': 'SRP'
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
                'eventTime': '2026-01-10T01:31:51.576+0900',
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
                'schemaVersion': 8
            },
            'data': {
                'domain': 'srp',
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'srp',
                'eventName': 'ab_test_exposure',
                'productId': None,
                'itemId': None,
                'vendorItemId': None,
                'sdpVisitKey': None,
                'abTestId': '88344',
                'abGroup': 'A',
                'extraAttribute': None,
                'searchId': '0797993d22350',
                'cartSessionId': None,
                'cartId': None,
                'checkoutId': None,
                'categoryId': None,
                'categoryType': None,
                'campaignId': None,
                'toggleViewType': None,
                'widgetPosition': None,
                'subSourceType': None,
                'requestId': None,
                'q': None,
                'exposureCase': None,
                'premiumCategory': None,
                'isBadDiscount': None,
                'isNoDiscount': None
            },
            'extra': {
                'domainName': 'SRP'
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
                'eventTime': '2026-01-10T01:31:51.587+0900',
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
                'schemaId': 12636,
                'schemaVersion': 1
            },
            'data': {
                'logType': 'impression',
                'q': '호박식혜 달빛',
                'searchId': '0797993d22350',
                'domain': 'srp',
                'eventName': 'srp_floating_banner_impression',
                'logCategory': 'impression',
                'msgTopic': 'login',
                'pageName': 'srp'
            },
            'extra': {}
        }
    ]
    
    return run_request(session, method, url, headers, body)
