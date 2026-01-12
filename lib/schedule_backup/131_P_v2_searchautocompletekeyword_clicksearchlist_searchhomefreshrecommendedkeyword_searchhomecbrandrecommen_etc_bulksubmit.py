import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 130
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '4651',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '4651',
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
                'eventTime': '2026-01-10T01:31:50.451+0900',
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
                'schemaId': 3894,
                'schemaVersion': 9
            },
            'data': {
                'domain': 'srp',
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'srp',
                'eventName': 'search_autocomplete_keyword',
                'requestId': '7ab97d51-5504-4c9b-a071-ef439797fafd',
                'qPos': '1-9',
                'prefix': '호박식혜 달빛',
                'filters': None,
                'filterKeys': '',
                'hasCavenue': None,
                'types': None,
                'subTypes': None,
                'hasRecent': False,
                'autoKeywords': '{1: 장수식혜 맛있는 호박식혜, 500ml, 9병, 2: 장수식혜 맛있는 호박식혜, 1.5l, 4병, 3: 장수식혜 맛있는 호박식혜, 500ml, 3병, 4: 장수식혜 맛있는 호박식혜, 500ml, 6병, 5: 달보드레 냉동 호박식혜, 500ml, 9병, 6: 유진네 수제 호박 식혜, 1000ml, 2개, 7: 유진네 수제 호박 식혜, 1000ml, 5개, 8: 유진네 수제 호박 식혜, 1000ml, 10개, 9: 호박식혜 만드는 법, 10: 호박식혜 1리터, 11: 느린부엌 호박식혜, 12: 호박식혜}',
                'officialBrand': '',
                'isRlux': False,
                'hasBrandShop': None,
                'hasOfficialBrand': None,
                'hasFashionBrand': None,
                'selectedTheme': None,
                'hasPremiumBrand': None,
                'isPremiumBrandShopEligible': None,
                'recentKeywords': None,
                'isFarfetch': False,
                'officialBrandShopExposureCase': None,
                'brandId': 0
            },
            'extra': {
                'hasImageKeyword': False
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
                'eventTime': '2026-01-10T01:31:50.455+0900',
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
                'schemaId': 120,
                'schemaVersion': 4
            },
            'data': {
                'domain': 'srp',
                'logCategory': 'event',
                'logType': 'click',
                'pageName': 'srp',
                'eventName': 'click_search_list',
                'q': '호박식혜 달빛',
                'channel': None,
                'isFromRecoHintKeyword': None,
                'searchClickedArea': None
            },
            'extra': {
                'currentView': '/home_today_recommendation',
                'eventReferrer': 'click_top_gnb_search'
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
                'eventTime': '2026-01-10T01:31:50.463+0900',
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
                'schemaId': 7761,
                'schemaVersion': 1
            },
            'data': {
                'logType': 'impression',
                'numVisibleKeywords': 5,
                'numScrolledToKeywords': 0,
                'requestId': 'b8e37892efb64e63a036202af47b2b29',
                'domain': 'srp',
                'eventName': 'search_home_fresh_recommended_keyword',
                'searchHomeVersion': 'V2',
                'logCategory': 'impression',
                'recoKeywords': '핫도그,연두부,슬라이스치즈,샌드위치햄,순두부,냉동식품,고기,닭,밀키트,밀크티',
                'pageName': 'srp'
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
                'eventTime': '2026-01-10T01:31:50.463+0900',
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
                'schemaId': 7762,
                'schemaVersion': 1
            },
            'data': {
                'logType': 'impression',
                'numVisibleKeywords': 6,
                'numScrolledToKeywords': 0,
                'requestId': 'b8e37892efb64e63a036202af47b2b29',
                'domain': 'srp',
                'eventName': 'search_home_cbrand_recommended_keyword',
                'searchHomeVersion': 'V2',
                'logCategory': 'impression',
                'recoKeywords': '베네통키즈,오리진스,비디비치,아이아이,아모레퍼시픽,일꼬르소,로라로라,키르시,록시땅,마르헨제이',
                'pageName': 'srp'
            },
            'extra': {}
        }
    ]
    
    return run_request(session, method, url, headers, body)
