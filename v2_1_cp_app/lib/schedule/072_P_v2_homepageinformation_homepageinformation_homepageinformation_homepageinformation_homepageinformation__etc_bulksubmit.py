import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 71
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '8976',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '8976',
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
                'eventTime': '2026-01-10T01:31:22.981+0900',
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
                'schemaId': 18912,
                'schemaVersion': 1
            },
            'data': {
                'logType': 'impression',
                'feedId': 'feed-537248e7d6d844d091b14a61564eec26',
                'sourceType': 'home_trending',
                'domain': 'home',
                'isDisplayed': False,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'position': 18,
                'pageName': 'home',
                'pageNum': 8
            },
            'extra': {
                'eventTime': 1767976279031
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
                'eventTime': '2026-01-10T01:31:22.982+0900',
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
                'schemaId': 17110,
                'schemaVersion': 1
            },
            'data': {
                'logType': 'impression',
                'feedId': 'feed-537248e7d6d844d091b14a61564eec26',
                'sourceType': 'home_unexplored_category,home_trending',
                'domain': 'home',
                'shownWidgetNumber': 3,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'pageName': 'home',
                'pageNum': 8,
                'abTestId': '88611,14554,88610'
            },
            'extra': {
                'eventTime': 1767976278782
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
                'eventTime': '2026-01-10T01:31:22.983+0900',
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
                'schemaId': 18912,
                'schemaVersion': 1
            },
            'data': {
                'logType': 'impression',
                'feedId': 'feed-537248e7d6d844d091b14a61564eec26',
                'sourceType': 'home_coumall_reco',
                'domain': 'home',
                'isDisplayed': False,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'position': 7,
                'pageName': 'home',
                'pageNum': 3
            },
            'extra': {
                'eventTime': 1767976277730
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
                'eventTime': '2026-01-10T01:31:22.984+0900',
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
                'schemaId': 18912,
                'schemaVersion': 1
            },
            'data': {
                'logType': 'impression',
                'feedId': 'feed-537248e7d6d844d091b14a61564eec26',
                'sourceType': 'home_repeated_purchase_ads',
                'domain': 'home',
                'isDisplayed': False,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'position': 6,
                'pageName': 'home',
                'pageNum': 2
            },
            'extra': {
                'eventTime': 1767976277480
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
                'eventTime': '2026-01-10T01:31:22.985+0900',
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
                'schemaId': 18912,
                'schemaVersion': 1
            },
            'data': {
                'logType': 'impression',
                'feedId': 'feed-537248e7d6d844d091b14a61564eec26',
                'sourceType': 'home_buy_again_ads',
                'domain': 'home',
                'isDisplayed': False,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'position': 9,
                'pageName': 'home',
                'pageNum': 4
            },
            'extra': {
                'eventTime': 1767976278030
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
                'eventTime': '2026-01-10T01:31:22.986+0900',
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
                'schemaId': 17110,
                'schemaVersion': 1
            },
            'data': {
                'logType': 'impression',
                'feedId': 'feed-537248e7d6d844d091b14a61564eec26',
                'sourceType': 'home_keep_shopping_ads,home_repeated_purchase_ads',
                'domain': 'home',
                'shownWidgetNumber': 1,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'pageName': 'home',
                'pageNum': 2,
                'abTestId': '88611,14554,88610'
            },
            'extra': {
                'eventTime': 1767976277330
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
                'eventTime': '2026-01-10T01:31:22.987+0900',
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
                'schemaId': 18912,
                'schemaVersion': 1
            },
            'data': {
                'logType': 'impression',
                'feedId': 'feed-537248e7d6d844d091b14a61564eec26',
                'sourceType': 'home_unexplored_category',
                'domain': 'home',
                'isDisplayed': False,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'position': 17,
                'pageName': 'home',
                'pageNum': 8
            },
            'extra': {
                'eventTime': 1767976279031
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
                'eventTime': '2026-01-10T01:31:22.988+0900',
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
                'schemaId': 18912,
                'schemaVersion': 1
            },
            'data': {
                'logType': 'impression',
                'feedId': 'feed-537248e7d6d844d091b14a61564eec26',
                'sourceType': 'home_gw_top_ads_banner',
                'domain': 'home',
                'isDisplayed': False,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'position': 11,
                'pageName': 'home',
                'pageNum': 5
            },
            'extra': {
                'eventTime': 1767976278281
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
                'eventTime': '2026-01-10T01:31:22.989+0900',
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
                'schemaId': 18912,
                'schemaVersion': 1
            },
            'data': {
                'logType': 'impression',
                'feedId': 'feed-537248e7d6d844d091b14a61564eec26',
                'sourceType': 'home_m3',
                'domain': 'home',
                'isDisplayed': False,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'position': 2,
                'pageName': 'home',
                'pageNum': 0
            },
            'extra': {
                'eventTime': 1767976277083
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
                'eventTime': '2026-01-10T01:31:22.990+0900',
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
                'schemaId': 17110,
                'schemaVersion': 1
            },
            'data': {
                'logType': 'impression',
                'feedId': 'feed-537248e7d6d844d091b14a61564eec26',
                'sourceType': 'home_coumall_reco,home_related_product',
                'domain': 'home',
                'shownWidgetNumber': 1,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'pageName': 'home',
                'pageNum': 3,
                'abTestId': '88611,14554,88610'
            },
            'extra': {
                'eventTime': 1767976277480
            }
        }
    ]
    
    return run_request(session, method, url, headers, body)
