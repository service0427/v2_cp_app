import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 85
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '8929',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '8929',
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
                'eventTime': '2026-01-10T01:31:27.319+0900',
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
                'domain': 'home',
                'logCategory': 'event',
                'logType': 'processing',
                'pageName': 'home',
                'eventName': 'page_interact'
            },
            'extra': {
                'pvId': '53603966'
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
                'eventTime': '2026-01-10T01:31:27.338+0900',
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
                'pageName': 'recommendation',
                'eventName': 'ads_latency',
                'widgetRanking': -1,
                'placementId': 126,
                'adType': 'APP_GATEWAY_PROMOTION',
                'networkType': 'wifi',
                'apiLatency': -1,
                'waitingTime': -1,
                'renderingLatency': 158,
                'totalLatency': 158,
                'launchId': 'AOS:1767976274728',
                'totalImageLoadingLatency': 1,
                'avgImageLoadingLatency': 0,
                'minImageLoadingLatency': 0,
                'maxImageLoadingLatency': 0,
                'imageCount': 3,
                'viewCreationLatency': 83
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
                'eventTime': '2026-01-10T01:31:27.409+0900',
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
                'schemaId': 18,
                'schemaVersion': 8
            },
            'data': {
                'domain': None,
                'logCategory': 'event',
                'logType': 'click',
                'pageName': None,
                'eventName': 'click_top_gnb_search',
                'categoryId': None,
                'categoryType': None,
                'eventGroup': 'top_gnb',
                'parentView': '/home',
                'ifHintExists': False,
                'trafficName': None,
                'sectionName': None,
                'searchId': None,
                'targetKeyword': None,
                'checkoutWithWow': None,
                'isRlux': None,
                'isFarfetch': None,
                'vendorItemId': None,
                'itemId': None,
                'productId': None,
                'sdpVisitKey': None,
                'q': None,
                'premiumCategory': None,
                'brandId': 0,
                'isUnified': None,
                'isScrolled': None
            },
            'extra': {
                'currentView': '/home_today_recommendation',
                'eventReferrer': 'home_permission_notice_nudge_click'
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
                'eventTime': '2026-01-10T01:31:27.435+0900',
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
                'schemaId': 1431,
                'schemaVersion': 48
            },
            'data': {
                'logType': 'impression',
                'abtests': '',
                'trAid': 'home_gw_promotion',
                'discountBadgeItems': 'p242330134_i769680772_v4943442439,p8386793628_i24543142643_v91257614679,p9065194258_i26619385818_v87540504882,p8512576777_i24641603417_v91684285671,p8795096974_i25216819522_v92213254126,p8203956490_i25381462492_v92375478913,p335684414_i1071074440_v5560900464,p7581762134_i20077394571_v87102949387,p8591705334_i24911526050_v91942241690,p7525821319_i24292763730_v89015631516,p8795912216_i25607043982_v92597613018,p9041675610_i26529025051_v93503202809,p7520747858_i19724753613_v86974488036,p8873962377_i25992780653_v91444090806,p8384928020_i24233777927_v91250909561,p7581062742_i20012468594_v86974318670,p6541171114_i14564599431_v81806851049,p8617261019_i24998496969_v92003685878',
                'templateId': '6552',
                'pageName': 'recommendation',
                'rocketWowType': 'p242330134_i769680772_v4943442439_null,p8386793628_i24543142643_v91257614679_null,p9065194258_i26619385818_v87540504882_null,p8512576777_i24641603417_v91684285671_null,p8795096974_i25216819522_v92213254126_null,p8203956490_i25381462492_v92375478913_null,p335684414_i1071074440_v5560900464_null,p7581762134_i20077394571_v87102949387_null,p8665516765_i25150727752_v92149225105_null,p8591705334_i24911526050_v91942241690_null,p7525821319_i24292763730_v89015631516_null,p8795912216_i25607043982_v92597613018_null,p8734611566_i25382915351_v92376866980_null,p9041675610_i26529025051_v93503202809_null,p7520747858_i19724753613_v86974488036_null,p8873962377_i25992780653_v91444090806_null,p8384928020_i24233777927_v91250909561_null,p7581062742_i20012468594_v86974318670_null,p6541171114_i14564599431_v81806851049_null,p8617261019_i24998496969_v92003685878_null',
                'renderStyle': 'feed_carousel',
                'hasQatc': '',
                'feedId': 'feed-58fb7e16f92b480e87e6b1a9d5f7010c-1.33.107:gw_promotion',
                'isSeeMore': False,
                'sourceType': 'home_gw_promotion',
                'numVisibleItems': 3,
                'numScrolledToItemsList': '',
                'domain': 'home',
                'eventName': 'gw_promotion',
                'rank': 1,
                'logCategory': 'impression',
                'rocketType': 'p242330134_i769680772_v4943442439_null,p8386793628_i24543142643_v91257614679_null,p9065194258_i26619385818_v87540504882_null,p8512576777_i24641603417_v91684285671_rocket_merchant_v3,p8795096974_i25216819522_v92213254126_null,p8203956490_i25381462492_v92375478913_rocket_merchant_v3,p335684414_i1071074440_v5560900464_null,p7581762134_i20077394571_v87102949387_null,p8665516765_i25150727752_v92149225105_rocket_merchant_v3,p8591705334_i24911526050_v91942241690_rocket_merchant_v3,p7525821319_i24292763730_v89015631516_null,p8795912216_i25607043982_v92597613018_rocket_merchant_v3,p8734611566_i25382915351_v92376866980_null,p9041675610_i26529025051_v93503202809_rocket_merchant_v3,p7520747858_i19724753613_v86974488036_rocket_merchant_v3,p8873962377_i25992780653_v91444090806_null,p8384928020_i24233777927_v91250909561_null,p7581062742_i20012468594_v86974318670_rocket_merchant_v3,p6541171114_i14564599431_v81806851049_null,p8617261019_i24998496969_v92003685878_null',
                'items': 'p242330134_i769680772_v4943442439,p8386793628_i24543142643_v91257614679,p9065194258_i26619385818_v87540504882,p8512576777_i24641603417_v91684285671,p8795096974_i25216819522_v92213254126,p8203956490_i25381462492_v92375478913,p335684414_i1071074440_v5560900464,p7581762134_i20077394571_v87102949387,p8665516765_i25150727752_v92149225105,p8591705334_i24911526050_v91942241690,p7525821319_i24292763730_v89015631516,p8795912216_i25607043982_v92597613018,p8734611566_i25382915351_v92376866980,p9041675610_i26529025051_v93503202809,p7520747858_i19724753613_v86974488036,p8873962377_i25992780653_v91444090806,p8384928020_i24233777927_v91250909561,p7581062742_i20012468594_v86974318670,p6541171114_i14564599431_v81806851049,p8617261019_i24998496969_v92003685878'
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
                'eventTime': '2026-01-10T01:31:27.621+0900',
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
                'schemaId': 2202,
                'schemaVersion': 4
            },
            'data': {
                'logType': 'impression',
                'targetKeyword': None,
                'ifHintExists': None,
                'systemFontScale': '1.0',
                'domain': 'srp',
                'eventName': 'search_home',
                'searchHomeVersion': 'v2',
                'logCategory': 'impression',
                'appliedFontScale': '1.0',
                'pageName': 'srp',
                'selectedTheme': None,
                'selectedFilter': None
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
                'eventTime': '2026-01-10T01:31:27.625+0900',
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
                'schemaId': 14042,
                'schemaVersion': 2
            },
            'data': {
                'domain': 'srp',
                'logCategory': 'view',
                'logType': 'modal',
                'pageName': 'srp',
                'eventName': 'page_view',
                'pvid': '70757900'
            },
            'extra': {}
        }
    ]
    
    return run_request(session, method, url, headers, body)
