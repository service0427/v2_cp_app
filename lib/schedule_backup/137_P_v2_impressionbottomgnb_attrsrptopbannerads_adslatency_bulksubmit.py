import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 136
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '2917',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '2917',
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
                'eventTime': '2026-01-10T01:31:51.591+0900',
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
                'schemaId': 17020,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'srp',
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'srp',
                'eventName': 'impression_bottom_gnb',
                'searchId': '0797993d22350',
                'parentView': '/search',
                'eventGroup': 'bottom_gnb'
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
                'eventTime': '2026-01-10T01:31:51.634+0900',
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
                'schemaVersion': 5
            },
            'data': {
                'logType': 'impression',
                'productId': '1653813380',
                'originalPrice': 0,
                'vendorItemId': '85401959202',
                'salePrice': 67400,
                'query': '호박식혜 달빛',
                'trAid': 'adzerk_keyword_banner',
                'templateId': 6765,
                'pageName': 'srp',
                'adsId': '502057518',
                'itemId': '2817652108',
                'searchId': '0797993d22350',
                'domain': 'srp',
                'trCid': '502057518',
                'eventName': 'attr_srp_top_banner_ads',
                'rank': 0,
                'logCategory': 'impression',
                'contentType': 'ADZERK_KEYWORD',
                'adCid': '502057518'
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
                'eventTime': '2026-01-10T01:31:51.995+0900',
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
                'schemaId': 14387,
                'schemaVersion': 8
            },
            'data': {
                'domain': 'ads',
                'logCategory': 'event',
                'logType': 'processing',
                'pageName': 'srp',
                'eventName': 'ads_latency',
                'widgetRanking': -1,
                'placementId': 19,
                'adType': 'APP_SRP_TOP_BANNER',
                'networkType': 'wifi',
                'apiLatency': -1,
                'waitingTime': -1,
                'renderingLatency': 398,
                'totalLatency': 398,
                'launchId': 'AOS:1767976274728',
                'totalImageLoadingLatency': 24,
                'avgImageLoadingLatency': 24,
                'minImageLoadingLatency': 24,
                'maxImageLoadingLatency': 24,
                'imageCount': 1,
                'viewCreationLatency': 38
            },
            'extra': {}
        }
    ]
    
    return run_request(session, method, url, headers, body)
