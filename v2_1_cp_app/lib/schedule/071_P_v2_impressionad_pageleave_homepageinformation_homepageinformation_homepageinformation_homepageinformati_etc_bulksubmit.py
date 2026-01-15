import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 70
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '9383',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '9383',
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
                'eventTime': '2026-01-10T01:31:22.807+0900',
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
                'schemaId': 60,
                'schemaVersion': 5
            },
            'data': {
                'logType': 'impression',
                'crmCid': '812431028581',
                'trAid': 'home_C1',
                'totalCount': 10,
                'pageName': 'list',
                'crmPlacementId': 'TARGETED_PROMOTION_BANNER_ON_HOME_C1',
                'sourceType': 'gm_crm_oms',
                'domain': 'list',
                'trCid': '812431028581',
                'segmentId': 'OM_260109_Mass_Login_2',
                'viewType': 'NONE_CLICK_IMAGE_PAGER',
                'eventName': 'impression_ad',
                'rank': 1,
                'logCategory': 'impression',
                'eventGroup': 'HOME_C1',
                'contentType': 'WHATS_NEW',
                'targetUrl': 'coupang://webview?tab=Y&pushEvent=Y&allowsInlineMediaPlayback=Y&title=로켓설치_내일도착&url=https://pages.coupang.com/m/54479?subSourceType=gm_crm_gwc1bnr_p000000_b173897_c477962&sourceType=gm_crm_oms',
                'crmCampaignSubgroupId': '573223',
                'subSourceType': 'gm_crm_gwc1bnr_p000000_b173897_c477962'
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
                'eventTime': '2026-01-10T01:31:22.970+0900',
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
                'eventTime': '2026-01-10T01:31:22.972+0900',
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
                'sourceType': 'home_promotion,home_personalized',
                'domain': 'home',
                'shownWidgetNumber': 3,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'pageName': 'home',
                'pageNum': 6,
                'abTestId': '88611,14554,88610'
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
                'eventTime': '2026-01-10T01:31:22.973+0900',
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
                'sourceType': 'home_personalized_ads',
                'domain': 'home',
                'isDisplayed': False,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'position': 1,
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
                'eventTime': '2026-01-10T01:31:22.974+0900',
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
                'sourceType': 'home_keep_shopping_ads',
                'domain': 'home',
                'isDisplayed': False,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'position': 5,
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
                'eventTime': '2026-01-10T01:31:22.975+0900',
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
                'sourceType': 'home_fbi,home_related_ads',
                'domain': 'home',
                'shownWidgetNumber': 1,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'pageName': 'home',
                'pageNum': 1,
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
                'eventTime': '2026-01-10T01:31:22.976+0900',
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
                'sourceType': 'home_related_product',
                'domain': 'home',
                'isDisplayed': False,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'position': 8,
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
                'eventTime': '2026-01-10T01:31:22.977+0900',
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
                'sourceType': 'home_personalized_bestseller_for_category',
                'domain': 'home',
                'isDisplayed': False,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'position': 15,
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
                'eventTime': '2026-01-10T01:31:22.979+0900',
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
                'sourceType': 'home_personalized',
                'domain': 'home',
                'isDisplayed': False,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'position': 14,
                'pageName': 'home',
                'pageNum': 6
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
                'eventTime': '2026-01-10T01:31:22.980+0900',
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
                'sourceType': 'home_fbi',
                'domain': 'home',
                'isDisplayed': False,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'position': 3,
                'pageName': 'home',
                'pageNum': 1
            },
            'extra': {
                'eventTime': 1767976277330
            }
        }
    ]
    
    return run_request(session, method, url, headers, body)
