import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 69
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '11725',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '11725',
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
                'eventTime': '2026-01-10T01:31:21.605+0900',
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
                'pageName': 'domain.home.presentation.view.MainActivity(HomeFragment)',
                'eventName': 'frame_rendering_metric',
                'totalFrameCount': 191,
                'totalSlowFrameCount': 117,
                'totalFrozenFrameCount': 0,
                'isTotalSlow': True,
                'totalAverageRenderingTime': 30,
                'idleFrameCount': 191,
                'idleSlowFrameCount': 117,
                'idleFrozenFrameCount': 0,
                'isIdleSlow': True,
                'isIdleFrozen': False,
                'idleAverageRenderingTime': 30,
                'scrollFrameCount': 0,
                'scrollSlowFrameCount': 0,
                'scrollFrozenFrameCount': 0,
                'isScrollSlow': None,
                'isScrollFrozen': None,
                'scrollAverageRenderingTime': None,
                'startTimeStamp': 1767976275251,
                'endTimeStamp': 1767976281604,
                'maximumFPS': None,
                'applicationId': 'com.coupang.mobile',
                'deviceName': 'SM-A165N',
                'buildType': 'prod',
                'osType': 'ANDROID',
                'sourceUserAgent': 'COUPANG|Android|15|9.0.4||null|f0b740d2-3447-3b2b-b118-d66257275f8f|Y|SM-A165N|f0b740d234472b2bb118d66257275f8f|25ede38a-c6e9-41b2-818a-aef7b5c17d0a|XXHDPI|17679762746194168937968||0||wifi|-1|||Asia/Seoul|c658d419f4d046cfb15f281769b15de7fbc66b30||1080|450|-1|1.0|true',
                'networkType': 'wifi',
                'isTotalFrozen': False,
                'screenType': None,
                'screenName': 'HomeFragment'
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
                'eventTime': '2026-01-10T01:31:21.607+0900',
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
                'feedId': 'feed-9a9e39785f9f4a17ababeaea86bb9bf8-1.33.107:gw_promotion',
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
                'eventTime': '2026-01-10T01:31:21.607+0900',
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
                'schemaId': 93,
                'schemaVersion': 1
            },
            'data': {
                'logType': 'impression',
                'pageNumber': None,
                'itemIds': None,
                'requestCategoryId': '/home_today_recommendation',
                'productTypes': None,
                'sectionId': None,
                'totalCount': -1,
                'pageName': 'home',
                'extraContents': None,
                'q': None,
                'searchId': None,
                'productIds': None,
                'domain': 'home',
                'eventName': 'impression_home',
                'rank': 34,
                'logCategory': 'impression',
                'filterType': None,
                'contentType': 'HOME'
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
                'eventTime': '2026-01-10T01:31:21.640+0900',
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
                'schemaId': 12936,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'member',
                'logCategory': 'system',
                'logType': 'debug',
                'pageName': 'login',
                'eventName': 'mobile_coupang_login_sdk_tracking_log',
                'message': 'AuthBridgeActivity: onCreate'
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
                'eventTime': '2026-01-10T01:31:21.672+0900',
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
                'schemaId': 12936,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'member',
                'logCategory': 'system',
                'logType': 'debug',
                'pageName': 'login',
                'eventName': 'mobile_coupang_login_sdk_tracking_log',
                'message': 'authorize'
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
                'eventTime': '2026-01-10T01:31:21.764+0900',
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
                'schemaId': 12936,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'member',
                'logCategory': 'system',
                'logType': 'debug',
                'pageName': 'login',
                'eventName': 'mobile_coupang_login_sdk_tracking_log',
                'message': 'browser: com.android.chrome'
            },
            'extra': {
                'version': '143.0.7499.146'
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
                'eventTime': '2026-01-10T01:31:21.822+0900',
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
                'schemaId': 12936,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'member',
                'logCategory': 'system',
                'logType': 'debug',
                'pageName': 'login',
                'eventName': 'mobile_coupang_login_sdk_tracking_log',
                'message': 'startAuth'
            },
            'extra': {
                'isWebView': 'false'
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
                'eventTime': '2026-01-10T01:31:22.062+0900',
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
                'schemaId': 12936,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'member',
                'logCategory': 'system',
                'logType': 'debug',
                'pageName': 'login',
                'eventName': 'mobile_coupang_login_sdk_tracking_log',
                'message': 'tab is shown'
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
                'eventTime': '2026-01-10T01:31:22.066+0900',
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
                'schemaId': 12936,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'member',
                'logCategory': 'system',
                'logType': 'debug',
                'pageName': 'login',
                'eventName': 'mobile_coupang_login_sdk_tracking_log',
                'message': 'tab has started loading'
            },
            'extra': {}
        }
    ]
    
    return run_request(session, method, url, headers, body)
