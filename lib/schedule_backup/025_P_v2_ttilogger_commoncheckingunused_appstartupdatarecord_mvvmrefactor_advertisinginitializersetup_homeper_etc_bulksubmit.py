import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 24
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '14565',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '14565',
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
                'eventTime': '2026-01-10T01:31:16.130+0900',
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
                'schemaId': 137,
                'schemaVersion': 12
            },
            'data': {
                'domain': 'tti',
                'logCategory': 'system',
                'logType': 'performance',
                'pageName': 'intro',
                'eventName': 'tti-logger',
                'platformType': 'native',
                'tti': 806,
                'bounced': False,
                'screenType': None,
                'viewCreateTime': 116,
                'apiResponseTime': 201,
                'viewBindingTime': 78,
                'imageLoadingTime': 0,
                'networkState': 'wifi',
                'carrier': 'unknown',
                'webViewVersion': '131.0.6778.260',
                'ixid': '00014a5c-5554-5d91-02d6-a65fc4db903f',
                'async': None,
                'serverTime': None,
                'domReady': None,
                'applicationId': None,
                'serverProcessingTime': None,
                'serverFetchingTime': None,
                'responseSize': 4564,
                'akamaiToGatewayServiceTime': 19,
                'internalProcessingTime': 50,
                'transferTime': 347,
                'imageCount': 0,
                'prepareApiTime': 209,
                'prepareImageTime': 0,
                'maxImageSize': None,
                'averageImageSize': None,
                'parsingTime': 348,
                'pageVersion': None,
                'cdn': 'envoy',
                'viewUpdateTime': 0,
                'gatewayProcessingTime': None,
                'responseTransferTime': 1,
                'apiBeforeFetchingTime': 0,
                'apiAfterFetchingTime': 0
            },
            'extra': {
                'api': '[{"key":"intro","time":201,"parse":315,"dispatch":1,"binding":42,"client_request_to_cdn":104,"client_request_to_gw":109,"gw_response_to_client":73,"response_transfer_time":0,"content_length":2257,"unzipped_size":6260},{"key":"ablist","time":196,"parse":342,"dispatch":10,"binding":36,"client_request_to_cdn":-35,"client_request_to_gw":-21,"gw_response_to_client":173,"response_transfer_time":1,"content_length":2307,"unzipped_size":24328}]',
                'image': '[]',
                'total': '806',
                'categoryDepth': '',
                'campaignId': '',
                'signal': -1,
                'viewUpdateTime': 0,
                'prepareApiTime': 209,
                'prepareImageTime': 0,
                'maxImageUrl': ''
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
                'eventTime': '2026-01-10T01:31:16.131+0900',
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
                'schemaId': 19536,
                'schemaVersion': 1
            },
            'data': {
                'domain': None,
                'logCategory': 'system',
                'logType': 'performance',
                'pageName': 'com.coupang.mobile.domain.home.presentation.view.MainActivity',
                'eventName': None
            },
            'extra': {
                'isForegroundImportance': True,
                'importance': 100,
                'isFirstInstall': True,
                'isJumpBeforeHome': False,
                'source': 'splash_fragment_on_stop',
                'appStartType': 'cold',
                'coldLaunchCase': 'appVersionUpgrade',
                'isStartedFromBackground': True,
                'networkState': 'wifi',
                'splash_fragment_on_view_created': 797,
                'splash_fragment_on_start': 881,
                'splash_fragment_on_stop': 1613
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
                'eventTime': '2026-01-10T01:31:16.134+0900',
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
                'key': 'MPA-9746',
                'value': 'FastDeliveryMessageBoxVHFactory'
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
                'eventTime': '2026-01-10T01:31:16.142+0900',
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
                'schemaId': 17228,
                'schemaVersion': 8
            },
            'data': {
                'domain': 'CoupangAPP',
                'logCategory': 'system',
                'logType': 'performance',
                'pageName': 'com.coupang.mobile.domain.home.presentation.view.MainActivity',
                'applicationId': 'com.coupang.mobile',
                'eventName': 'app_startup_data_record',
                'introPageAppear': 877,
                'firstScreenDisplay': 573,
                'ffEnd': 1251,
                'abEnd': 1562,
                'introEnd': 1530,
                'introPageDisappear': 1613,
                'domainPageInit': 1622,
                'applicationCreated': 326,
                'mainActivityInitEnd': 541,
                'mainActivityCreated': 563,
                'enterMain': 93,
                'enterWillFinishLaunching': None,
                'leftWillFinishLaunching': None,
                'enterDidFinishLaunching': None,
                'networkState': 'wifi',
                'isAdSplash': False,
                'splashType': 0,
                'isStartedFromBackground': True,
                'isForegroundImportance': True,
                'modulesInitializerStart': 93,
                'modulesInitializerEnd': 326,
                'pageStartType': 'ORGANIC',
                'appStartType': 'cold',
                'introPageInit': None,
                'apiFetchingStart': 861,
                'apiFetchingEnd': 1596,
                'leftDidFinishLaunching': None,
                'splashExtendStart': 1571,
                'splashExtendEnd': 938,
                'isFirstInstall': True,
                'domainPageInitTime': 1622,
                'processEnvInitTime': 326,
                'containerSetupTime': 237,
                'introPageInitTime': 314,
                'apiFetchingTime': 735,
                'introPageTime': 736,
                'introPageTimeWithAd': 736,
                'gwPrepareTime': 9,
                'gwPrepareTimeWithAd': 9,
                'splashExtendTime': 0,
                'introPageDisappearTime': 1613,
                'splashTypeDesc': 'noSplash',
                'moduleInitialTime': 233,
                'homePageCreate': None,
                'isJumpBeforeHome': False,
                'bounced': False
            },
            'extra': {
                'importance': 100,
                'isFacebookRemoveEnable': False,
                'liveInitWhenNeed': False,
                'applicationWaitTime': 0,
                'introApiPrefetching': False,
                'splashFragmentOnStart': True,
                'introApiStart': 969,
                'ablistApiStart': 970,
                'introApiNetworkTime': 201,
                'ablistApiNetworkTime': 196,
                'obtainIntroDataSuccess': '',
                'startHome': {
                    'isSplashFragmentCreated': True
                },
                'preloadHomeC1ImageStart': 1598,
                'preloadHomeC1ImageEnd': 1599,
                'loadHomeFragment': 1603,
                'processIntent': 1605,
                'isSplashViewSimplified': False,
                'homeFragmentOnAttach': 1618,
                'applicationInitializers': '{"LoggingInitializer":5,"UnifiedPaymentInitializer":2,"AdvancedFirebaseInitializer":0,"ErrorCollectorInitializer":6,"StackManagerInitializer":0,"LogcatInitializer":0,"UnifiedEcommerceMemberInitializer":68,"DebugSettingInitializer":0,"EntranceServiceInitializer":10,"PlayerFrameworkInitializer":16,"FacebookInitializer":26,"FalconInitializer":0,"ImplicitInitializer":0,"MultiDataSourceMapInitializer":2,"ActivityOnCrashInitializer":0,"SecurityToolInitializer":0,"NotificationInitializer":0,"KakaoShareInitializer":5,"AppMonitoringPlatformInitializer":47,"SharedPreferenceInitializer":1,"MollyLoggerInitializer":1,"FeatureControlInitializer":0,"StartupTimeExperimentalInitializer":0,"WebViewInitializer":0,"AdvertisingInitializer":4,"InstallReferrerInitializer":4,"UnifiedAppInfoInitializer":1,"FirebaseInitializer":28,"ComponentHolderInitializer":0,"AppLifecycleInitializer":1,"UnifiedRegionInitializer":0,"LeakCanaryInitializer":0,"UnifiedMemberSdkInitializer":2,"RdsInitializer":0,"ImageLoaderInitializer":0,"NetworkInitializer":0,"FlipperInitializer":0}',
                'activityLifecycle': '{"SplashActivityInjectTime":15,"MainActivityCreateViewModelTime":4,"MainActivityStartTime":131,"SplashActivityStartTime":33,"MainActivityInjectTime":7}',
                'coldLaunchCase': 'appFirstInstall'
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
                'eventTime': '2026-01-10T01:31:16.144+0900',
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
                'featureName': 'USER_LANGUAGES_CONFIGURATION',
                'schemaName': 'feature_tracking',
                'additionalComment': None
            },
            'extra': {
                'System-Language': 'ko-KR',
                'Application-Language': 'ko-KR',
                'Activity-Language': 'ko-KR',
                'Market-Default-Language': 'ko-KR',
                'App-Language': 'ko-KR'
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
                'eventTime': '2026-01-10T01:31:16.233+0900',
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
                'schemaId': 15502,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'cmg',
                'logCategory': 'system',
                'logType': 'performance',
                'pageName': 'App',
                'eventName': 'advertising_initializer_setup',
                'launchId': 'AOS:1767976274728',
                'labels': 'app_version_9_0_4,com.coupang.mobile.common.multisourcemap.abtestmap.InternalABTestMapKey@e91dfe9_[A],com.coupang.mobile.common.multisourcemap.abtestmap.InternalABTestMapKey@1d5170f_[C],com.coupang.mobile.common.multisourcemap.abtestmap.InternalABTestMapKey@99f91a5_[C],com.coupang.mobile.common.multisourcemap.abtestmap.InternalABTestMapKey@856152b_[A],com.coupang.mobile.common.multisourcemap.abtestmap.InternalABTestMapKey@15c4d88_[B],com.coupang.mobile.common.multisourcemap.abtestmap.InternalABTestMapKey@31ca321_[C],com.coupang.mobile.common.multisourcemap.abtestmap.InternalABTestMapKey@96bb346_[A],com.coupang.mobile.common.multisourcemap.abtestmap.InternalABTestMapKey@284cbce_[A],com.coupang.mobile.common.multisourcemap.abtestmap.InternalABTestMapKey@92cba34_[B],com.coupang.mobile.common.multisourcemap.abtestmap.InternalABTestMapKey@ff505d_[A],com.coupang.mobile.common.multisourcemap.abtestmap.InternalABTestMapKey@c1fbdd2_[A],com.coupang.mobile.common.multisourcemap.abtestmap.InternalABTestMapKey@7c5fea3_[A],com.coupang.mobile.common.multisourcemap.abtestmap.InternalABTestMapKey@7f545a0_[A],com.coupang.mobile.common.multisourcemap.abtestmap.InternalABTestMapKey@531027a_[A],com.coupang.mobile.common.multisourcemap.abtestmap.InternalABTestMapKey@f5e7122_[A],com.coupang.mobile.common.multisourcemap.abtestmap.InternalABTestMapKey@3fab7b3_[A],com.coupang.mobile.common.multisourcemap.abtestmap.InternalABTestMapKey@d2af170_[A],com.coupang.mobile.common.multisourcemap.abtestmap.InternalABTestMapKey@d791ce9_[A]'
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
                'eventTime': '2026-01-10T01:31:16.298+0900',
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
                'schemaId': 13315,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'home',
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'home',
                'eventName': 'home_permission_notice_nudge_impression'
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
                'eventTime': '2026-01-10T01:31:16.299+0900',
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
                'schemaId': 5907,
                'schemaVersion': 2
            },
            'data': {
                'logType': 'platform',
                'isTalkBackOn': False,
                'isScreenReaderEnabled': False,
                'domain': 'sdp',
                'eventName': 'talk_back_user_check',
                'logCategory': 'system',
                'pageName': 'home'
            },
            'extra': {
                'packages': '[]'
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
                'eventTime': '2026-01-10T01:31:16.521+0900',
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
                'pageNumber': '_S1',
                'itemIds': '',
                'requestCategoryId': '/home_today_recommendation',
                'productTypes': '',
                'sectionId': None,
                'totalCount': None,
                'pageName': 'home',
                'extraContents': 'HOME_C1_CATEGORY:11D,9D',
                'q': None,
                'searchId': None,
                'productIds': '',
                'domain': 'home',
                'eventName': 'impression_home',
                'rank': None,
                'logCategory': 'impression',
                'filterType': None,
                'contentType': 'ult'
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
                'eventTime': '2026-01-10T01:31:16.590+0900',
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
                'extraContent': 'HOME_C1_CATEGORY:11D',
                'trAid': 'home_C1',
                'totalCount': 10,
                'pageName': 'list',
                'domain': 'list',
                'trCid': '865323',
                'viewType': 'NONE_CLICK_IMAGE_PAGER',
                'eventName': 'impression_ad',
                'rank': 0,
                'logCategory': 'impression',
                'eventGroup': 'HOME_C1',
                'contentType': 'WHATS_NEW',
                'targetUrl': 'coupang://list?linkcode=413777&channel=home_C1'
            },
            'extra': {}
        }
    ]
    
    return run_request(session, method, url, headers, body)
