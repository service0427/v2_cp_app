import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 88
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '5175',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '5175',
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
                'eventTime': '2026-01-10T01:31:27.918+0900',
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
                'featureName': 'search_home_banner',
                'schemaName': 'feature_tracking',
                'additionalComment': 'search_home_banneractive'
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
                'eventTime': '2026-01-10T01:31:28.049+0900',
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
                'schemaId': 2196,
                'schemaVersion': 5
            },
            'data': {
                'domain': 'srp',
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'srp',
                'eventName': 'search_recent_keyword',
                'searchHomeVersion': 'v2',
                'categoryType': None,
                'areaType': 'RC_SCROLL',
                'emptyList': True,
                'numberItemsShown': None,
                'entry': 'searchhome',
                'isOnAc': None,
                'recentKeywords': '',
                'isAACFilter': False,
                'imageType': None
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
                'eventTime': '2026-01-10T01:31:28.289+0900',
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
                'domain': 'home',
                'logCategory': 'view',
                'logType': 'modal',
                'pageName': 'home',
                'eventName': 'page_leave',
                'pvid': '53603966'
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
                'eventTime': '2026-01-10T01:31:28.295+0900',
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
                'schemaId': 17062,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'cmg',
                'logCategory': 'system',
                'logType': 'performance',
                'pageName': None,
                'eventName': 'image_enlargement_logging',
                'eventId': '',
                'definition': '292x292q65ex',
                'compress': 'false',
                'ratio': '1.0'
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
                'eventTime': '2026-01-10T01:31:28.297+0900',
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
                'domain': 'gateway',
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'HomeFragment',
                'eventName': 'image_loads',
                'networkType': 'wifi',
                'fileSizeList': '484416,484416,1088640,484416',
                'imageResolutionList': '348x348,348x348,1080x252,348x348',
                'imageUrlList': 'https://thumbnail8.coupangcdn.com/thumbnails/remote/292x292q65ex/image/vendor_inventory/image_audit/prod/b97749d6-381a-4214-97d8-f49117ffad82_fixing_v2.png,https://thumbnail4.coupangcdn.com/thumbnails/remote/292x292q65ex/image/vendor_inventory/0687/262255e9b0244679bf5d2d3983b420d4b7eae8547130f0259a198974a77e.jpg,https://thumbnail.coupangcdn.com/thumbnails/remote/mhigh/image/displayitem/displayitem_e22090e3-4316-450d-947d-de613bfbd913.jpg,https://thumbnail4.coupangcdn.com/thumbnails/remote/292x292q65ex/image/vendor_inventory/669c/cb45a0d94f7efac2426033308861bed66ab79d2b3deb423f6c2ba34f22f5.jpg',
                'resultList': 'SUCCESS,SUCCESS,SUCCESS,SUCCESS',
                'itemIdList': None,
                'productIdList': None,
                'vendorItemIdList': None,
                'sdpVisitKey': None,
                'searchId': None,
                'q': None,
                'cacheTypeList': 'MEMORY_CACHE,MEMORY_CACHE,MEMORY_CACHE,MEMORY_CACHE',
                'sourceType': 'gateway_dco-ads,gateway_dco-ads,gateway_banner,gateway_dco-ads',
                'imageDurationList': '0,0,0,0',
                'rawByteSizeList': '-1,-1,15459,-1'
            },
            'extra': {}
        }
    ]
    
    return run_request(session, method, url, headers, body)
