import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 150
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '9225',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '9225',
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
                'eventTime': '2026-01-10T01:31:57.583+0900',
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
                'schemaId': 16869,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'sdp',
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'sdp',
                'eventName': 'top_gnb_impression',
                'productId': 9024146312,
                'itemId': 26462223018,
                'vendorItemId': 93437504336,
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'exposedArea': 'Back,Search,Cart',
                'categoryId': '1474'
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
                'eventTime': '2026-01-10T01:31:57.590+0900',
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
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'sdp',
                'eventName': 'ab_test_exposure',
                'domain': 'sdp',
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'productId': 9024146312,
                'itemId': 26462223018,
                'vendorItemId': 93437504336,
                'abGroup': 'D',
                'abTestId': '91364'
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
                'eventTime': '2026-01-10T01:31:57.594+0900',
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
                'schemaId': 14043,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'sdp',
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'sdp',
                'eventName': '',
                'pvid': '92910302',
                'traceId': '3bc42af30268f9137afa534259b804e3',
                'widgetName': 'SECTION_ATF_BOTTOM_BUTTONS',
                'sectionName': None,
                'componentName': None,
                'serverTime': 1767976316919
            },
            'extra': {
                'widgetId': ''
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
                'eventTime': '2026-01-10T01:31:57.603+0900',
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
                'schemaVersion': 10
            },
            'data': {
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'sdp',
                'eventName': 'ab_test_exposure',
                'domain': 'sdp',
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'productId': 9024146312,
                'itemId': 26462223018,
                'vendorItemId': 93437504336,
                'abGroup': 'B',
                'abTestId': '94679',
                'exposureCase': 'sdp_bottom_cta_bar'
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
                'eventTime': '2026-01-10T01:31:57.664+0900',
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
                'schemaId': 2319,
                'schemaVersion': 2
            },
            'data': {
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'sdp',
                'eventName': 'atf_multi_images',
                'domain': 'sdp',
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'productId': 9024146312,
                'itemId': 26462223018,
                'vendorItemId': 93437504336,
                'hasVideo': 'false',
                'hasNewVideo': False,
                'isSellingPointEligible': False,
                'hasSellingPoint': False
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
                'eventTime': '2026-01-10T01:31:57.673+0900',
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
                'schemaId': 9382,
                'schemaVersion': 10
            },
            'data': {
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'sdp',
                'eventName': 'sdp_atf_image_video',
                'domain': 'sdp',
                'productId': 9024146312,
                'itemId': 26462223018,
                'vendorItemId': 93437504336,
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'pageNum': 1,
                'type': 'image',
                'isSizeImage': False,
                'isNutritionChartAiCropped': 'false'
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
                'eventTime': '2026-01-10T01:31:57.674+0900',
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
                'schemaId': 17015,
                'schemaVersion': 3
            },
            'data': {
                'logCategory': 'event',
                'logType': 'click',
                'pageName': 'sdp',
                'eventName': 'sdp_atf_image_video_click',
                'domain': 'sdp',
                'productId': 9024146312,
                'itemId': 26462223018,
                'vendorItemId': 93437504336,
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'pageNum': 1,
                'type': 'image',
                'sdpAtfTotalImageCount': 9,
                'isNutritionChartAiCropped': 'false',
                'isNewVideo': 'false'
            },
            'extra': {
                'eventReferrer': 'click_search_product',
                'currentView': '/search_list'
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
                'eventTime': '2026-01-10T01:31:57.699+0900',
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
                'schemaId': 15431,
                'schemaVersion': 1
            },
            'data': {
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'sdp',
                'eventName': 'sdp_product_detail_page_ingression_impression',
                'domain': 'sdp',
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'productId': 9024146312,
                'itemId': 26462223018,
                'vendorItemId': 93437504336
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
                'eventTime': '2026-01-10T01:31:57.718+0900',
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
                'schemaId': 8,
                'schemaVersion': 4
            },
            'data': {
                'domain': 'sdp',
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'sdp',
                'eventName': 'product_review',
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'invalid': False,
                'productId': 9024146312,
                'itemId': 26462223018,
                'vendorItemId': 93437504336
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
                'eventTime': '2026-01-10T01:31:57.719+0900',
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
                'schemaId': 17158,
                'schemaVersion': 3
            },
            'data': {
                'domain': 'SDP',
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'sdp',
                'eventName': 'social_proof_badge_area_view',
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'productId': 9024146312,
                'vendorItemId': 93437504336,
                'itemId': 26462223018,
                'isSpecialPriceBadge': False,
                'isBestReviewBadge': 'false',
                'isBestReviewBadgeEligible': 'false',
                'isPurchaseNudgeEligible': 'False',
                'isPurchaseNudge': 'False',
                'isPreviousPurchaseBadge': 'False',
                'isPreviousPurchaseBadgeEligible': 'False',
                'isPurchaseNudgeTestTarget': 'False',
                'purchaseNudgeTestInfo': '0,0,0'
            },
            'extra': {}
        }
    ]
    
    return run_request(session, method, url, headers, body)
