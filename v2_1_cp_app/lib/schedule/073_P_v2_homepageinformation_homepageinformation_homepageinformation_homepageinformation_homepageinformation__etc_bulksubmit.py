import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 72
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '9338',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '9338',
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
                'eventTime': '2026-01-10T01:31:22.991+0900',
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
                'sourceType': 'home_related_ads',
                'domain': 'home',
                'isDisplayed': False,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'position': 4,
                'pageName': 'home',
                'pageNum': 1
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
                'eventTime': '2026-01-10T01:31:22.992+0900',
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
                'sourceType': 'home_video_ads_banner',
                'domain': 'home',
                'isDisplayed': False,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'position': 10,
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
                'eventTime': '2026-01-10T01:31:22.993+0900',
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
                'sourceType': 'home_gw_promotion,home_unfinished_journey',
                'domain': 'home',
                'shownWidgetNumber': 3,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'pageName': 'home',
                'pageNum': 9,
                'abTestId': '88611,14554,88610,83334'
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
                'eventTime': '2026-01-10T01:31:22.994+0900',
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
                'sourceType': 'home_gw_top_ads_banner,home_private_label',
                'domain': 'home',
                'shownWidgetNumber': 2,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'pageName': 'home',
                'pageNum': 5,
                'abTestId': '35104,5953,95360,41921,32609,48258,88611,88610,67652,94596,94823,90504,40012,25901,14736,91378,96213,46676,14554,96220,96159,95999'
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
                'eventTime': '2026-01-10T01:31:22.995+0900',
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
                'sourceType': 'home_personalized_bestseller_for_category,home_live',
                'domain': 'home',
                'shownWidgetNumber': 3,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'pageName': 'home',
                'pageNum': 7,
                'abTestId': '88611,14554,88610'
            },
            'extra': {
                'eventTime': 1767976278532
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
                'eventTime': '2026-01-10T01:31:22.996+0900',
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
                'sourceType': 'home_live',
                'domain': 'home',
                'isDisplayed': False,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'position': 16,
                'pageName': 'home',
                'pageNum': 7
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
                'eventTime': '2026-01-10T01:31:22.997+0900',
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
                'sourceType': 'home_gw_promotion',
                'domain': 'home',
                'isDisplayed': True,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'position': 19,
                'pageName': 'home',
                'pageNum': 9
            },
            'extra': {
                'eventTime': 1767976279631
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
                'eventTime': '2026-01-10T01:31:22.998+0900',
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
                'sourceType': 'home_personalized_ads,home_m3',
                'domain': 'home',
                'shownWidgetNumber': 0,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'pageName': 'home',
                'pageNum': 0,
                'abTestId': '41921,95360,5953,48258,67652,94596,94022,90504,40012,63118,95246,14736,94739,8658,96213,46676,96278,14554,96220,96159,95134,35104,32609,88611,88610,94823,25901,95731,91378,95999,85695'
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
                'eventTime': '2026-01-10T01:31:22.999+0900',
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
                'sourceType': 'home_private_label',
                'domain': 'home',
                'isDisplayed': False,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'position': 12,
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
                'eventTime': '2026-01-10T01:31:23.000+0900',
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
                'sourceType': 'home_buy_again_ads,home_video_ads_banner',
                'domain': 'home',
                'shownWidgetNumber': 1,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'pageName': 'home',
                'pageNum': 4,
                'abTestId': '88611,14554,88610,94636'
            },
            'extra': {
                'eventTime': 1767976277730
            }
        }
    ]
    
    return run_request(session, method, url, headers, body)
