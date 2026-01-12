import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 139
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '14484',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '14484',
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
                'eventTime': '2026-01-10T01:31:52.103+0900',
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
                'schemaId': 4262,
                'schemaVersion': 1
            },
            'data': {
                'logType': 'platform',
                'domain': 'common',
                'eventName': 'invalid_server_response',
                'logCategory': 'system',
                'stackTrace': 'com.coupang.mobile.common.dto.search.filter.shortcutbar.FilterShortcutBar.getType(SourceFile:5) com.coupang.mobile.domain.search.domain.impl.filter.RequestStaticFiltersUseCaseImpl.k(SourceFile:26) com.coupang.mobile.domain.search.domain.impl.filter.RequestStaticFiltersUseCaseImpl.f(SourceFile:1) com.coupang.mobile.domain.search.domain.impl.filter.RequestStaticFiltersUseCaseImpl$attachEmitterToCallback$1.onFilterLoad(SourceFile:95) com.coupang.mobile.common.domainmodel.product.interactor.ProductFilterInteractor$HttpCallback.a(SourceFile:83) com.coupang.mobile.common.domainmodel.product.interactor.ProductFilterInteractor$HttpCallback.onResponse(SourceFile:3) com.coupang.mobile.network.core.callback.CallbackManager.h(SourceFile:19) com.coupang.mobile.network.core.parts.VolleyNetworkParts$ResponseBridge.onResponse(SourceFile:15) com.coupang.mobile.network.core.VolleyRequest.deliverResponse(SourceFile:3) com.android.volley.ExecutorDelivery$ResponseDeliveryRunnable.run(SourceFile:31) android.os.Handler.handleCallback(Handler.java:959) android.os.Handler.dispatchMessage(Handler.java:100) android.os.Looper.loopOnce(Looper.java:257) android.os.Looper.loop(Looper.java:342) android.app.ActivityThread.main(ActivityThread.java:9638) java.lang.reflect.Method.invoke(Native Method) com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:619) com.android.internal.os.ZygoteInit.main(ZygoteInit.java:929)'
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
                'eventTime': '2026-01-10T01:31:52.126+0900',
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
                'schemaId': 2466,
                'schemaVersion': 8
            },
            'data': {
                'domain': 'filter',
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'list',
                'eventName': 'impression_shortcut',
                'viewType': 'SERVICE_SHORTCUT',
                'filterValues': 'ROCKET_DELIVERY',
                'q': '호박식혜 달빛',
                'domainType': 'SRP',
                'brandName': None,
                'categoryId': None,
                'searchId': '0797993d22350',
                'categoryType': None,
                'filterGroupValue': 'SERVICE',
                'filterTitles': '로켓배송',
                'numVisibleItems': None,
                'numScrolledToItems': None,
                'campaignId': None,
                'filterGroupTitle': '',
                'selectedFilters': '',
                'selectedFilterValues': '',
                'isRluxInTop20': False,
                'srpType': None,
                'isRlux': None,
                'isFarfetch': None
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
                'eventTime': '2026-01-10T01:31:52.133+0900',
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
                'schemaId': 4262,
                'schemaVersion': 1
            },
            'data': {
                'logType': 'platform',
                'domain': 'common',
                'eventName': 'invalid_server_response',
                'logCategory': 'system',
                'stackTrace': 'com.coupang.mobile.common.dto.search.filter.shortcutbar.FilterShortcutBar.getType(SourceFile:5) com.coupang.mobile.commonui.filter.FilterViewManager.b(SourceFile:22) com.coupang.mobile.commonui.filter.FilterViewManager.f(SourceFile:116) com.coupang.mobile.commonui.filter.FilterViewController.onFilterDataLoadCompleted(SourceFile:9) com.coupang.mobile.domain.search.presentation.viewmodel.filter.SearchFilterViewModel.updateFilterRelatedView(SourceFile:259) com.coupang.mobile.domain.search.presentation.viewmodel.filter.SearchFilterViewModel.S(SourceFile:33) com.coupang.mobile.domain.search.presentation.viewmodel.filter.SearchFilterViewModel.i(SourceFile:1) com.coupang.mobile.domain.search.presentation.viewmodel.filter.h.accept(SourceFile:1) io.reactivex.rxjava3.internal.observers.ConsumerSingleObserver.onSuccess(SourceFile:8) autodispose2.AutoDisposingSingleObserverImpl.onSuccess(SourceFile:21) io.reactivex.rxjava3.internal.operators.single.SingleObserveOn$ObserveOnSingleObserver.run(SourceFile:15) io.reactivex.rxjava3.android.schedulers.HandlerScheduler$ScheduledRunnable.run(SourceFile:3) android.os.Handler.handleCallback(Handler.java:959) android.os.Handler.dispatchMessage(Handler.java:100) android.os.Looper.loopOnce(Looper.java:257) android.os.Looper.loop(Looper.java:342) android.app.ActivityThread.main(ActivityThread.java:9638) java.lang.reflect.Method.invoke(Native Method) com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:619) com.android.internal.os.ZygoteInit.main(ZygoteInit.java:929)'
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
                'eventTime': '2026-01-10T01:31:52.142+0900',
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
                'schemaId': 10384,
                'schemaVersion': 1
            },
            'data': {
                'logType': 'impression',
                'q': '호박식혜 달빛',
                'searchId': '0797993d22350',
                'domain': 'srp',
                'eventName': 'srp_unitprice_including_deliveryfee_toggle_impression',
                'logCategory': 'impression',
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
                'eventTime': '2026-01-10T01:31:52.158+0900',
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
                'schemaId': 4262,
                'schemaVersion': 1
            },
            'data': {
                'logType': 'platform',
                'domain': 'common',
                'eventName': 'invalid_server_response',
                'logCategory': 'system',
                'stackTrace': 'com.coupang.mobile.common.dto.search.filter.shortcutbar.FilterShortcutBar.getType(SourceFile:5) com.coupang.mobile.commonui.filter.FilterViewManager.e(SourceFile:22) com.coupang.mobile.commonui.filter.FilterViewManager.f(SourceFile:133) com.coupang.mobile.commonui.filter.FilterViewController.onFilterDataLoadCompleted(SourceFile:9) com.coupang.mobile.domain.search.presentation.viewmodel.filter.SearchFilterViewModel.updateFilterRelatedView(SourceFile:259) com.coupang.mobile.domain.search.presentation.viewmodel.filter.SearchFilterViewModel.S(SourceFile:33) com.coupang.mobile.domain.search.presentation.viewmodel.filter.SearchFilterViewModel.i(SourceFile:1) com.coupang.mobile.domain.search.presentation.viewmodel.filter.h.accept(SourceFile:1) io.reactivex.rxjava3.internal.observers.ConsumerSingleObserver.onSuccess(SourceFile:8) autodispose2.AutoDisposingSingleObserverImpl.onSuccess(SourceFile:21) io.reactivex.rxjava3.internal.operators.single.SingleObserveOn$ObserveOnSingleObserver.run(SourceFile:15) io.reactivex.rxjava3.android.schedulers.HandlerScheduler$ScheduledRunnable.run(SourceFile:3) android.os.Handler.handleCallback(Handler.java:959) android.os.Handler.dispatchMessage(Handler.java:100) android.os.Looper.loopOnce(Looper.java:257) android.os.Looper.loop(Looper.java:342) android.app.ActivityThread.main(ActivityThread.java:9638) java.lang.reflect.Method.invoke(Native Method) com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:619) com.android.internal.os.ZygoteInit.main(ZygoteInit.java:929)'
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
                'eventTime': '2026-01-10T01:31:52.161+0900',
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
                'logType': 'impression',
                'q': '호박식혜 달빛',
                'searchId': '0797993d22350',
                'domain': 'srp',
                'eventName': 'ab_test_exposure',
                'abGroup': 'A',
                'logCategory': 'impression',
                'pageName': 'srp',
                'abTestId': '92685'
            },
            'extra': {
                'listSingleFilters': '',
                'numberConsolidatedFilters': 1,
                'listOtherFilters': 'DRAWER FILTER,ROCKET_DELIVERY',
                'listGroupFilters': ''
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
                'eventTime': '2026-01-10T01:31:52.163+0900',
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
                'schemaId': 150,
                'schemaVersion': 8
            },
            'data': {
                'logType': 'impression',
                'filterValues': None,
                'dawnDeliveryEnabled': False,
                'domainType': 'SRP',
                'filterGroup': None,
                'isRluxEnable': False,
                'rocketOverseaEnabled': 'false',
                'pageName': 'list',
                'isFilterSelected': None,
                'searchId': '0797993d22350',
                'cateID': None,
                'eventName': 'exposed_filter_view',
                'logCategory': 'impression',
                'rocketMartEnabled': None,
                'samedayDeliveryEnabled': False,
                'rocketLuxuryEnabled': None,
                'campaignId': None,
                'selectedServiceShortcuts': None,
                'q': '호박식혜 달빛',
                'filterTitles': '로켓배송',
                'hasCavenue': False,
                'domain': 'list',
                'rocketDeliveryEnabled': None,
                'rocketWowEnabled': 'false',
                'filterType': 'rocket',
                'categoryId': None
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
                'eventTime': '2026-01-10T01:31:52.174+0900',
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
                'schemaId': 83,
                'schemaVersion': 5
            },
            'data': {
                'logType': 'impression',
                'domainType': 'SRP',
                'pageName': 'list',
                'attributeId': 'attr_12757,attr_8460,attr_12700,attr_12777,attr_12805,attr_11022,attr_11210,attr_7663,attr_11411,attr_1133,attr_13394,attr_7823,attr_7637,attr_12808',
                'q': '호박식혜 달빛',
                'actionType': None,
                'searchId': '0797993d22350',
                'service': 'ROCKET_DELIVERY,FREE_DELIVERY',
                'domain': 'list',
                'eventName': 'filter_expose',
                'logCategory': 'impression',
                'attribute': None,
                'filterType': None,
                'category': None,
                'filterTypes': 'ATTRIBUTE,RATING,CATEGORY,SORT_KEY,BRAND_KEY,SERVICE,PRICE_RANGE,OFFER_CONDITION,DISCOUNT',
                'brand': None
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
                'eventTime': '2026-01-10T01:31:52.277+0900',
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
                'schemaId': 19454,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'list',
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'list',
                'eventName': 'impression_view_type_list',
                'categoryId': None,
                'sectionName': None,
                'searchId': '0797993d22350',
                'isFarfetch': None,
                'isRlux': None
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
                'eventTime': '2026-01-10T01:31:52.338+0900',
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
                'schemaId': 11318,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'tti',
                'logCategory': 'system',
                'logType': 'performance',
                'pageName': 'srp',
                'eventName': 'filter_exposed_tti',
                'serverFetchingTime': None,
                'responseSize': 43642,
                'apiResponseTime': 356,
                'ixid': '00014a64-c789-e809-f2ce-1e1abf3ab649',
                'carrier': 'unknown',
                'networkState': 'wifi',
                'imageLoadingTime': 0,
                'viewBindingTime': 240,
                'viewCreateTime': 0,
                'bounced': False,
                'jsonParsingTime': 181,
                'tti': 783
            },
            'extra': {
                'api': '[{"key":"\\/modular\\/v1\\/endpoints\\/152\\/v3\\/search-filter?clientType=SRP&filter=KEYWORD%3A%ED%98%B8%EB%B0%95%EC%8B%9D%ED%98%9C+%EB%8B%AC%EB%B9%9B%7CCCID%3AALL%7CENABLE_ASYNC%3ACATEGORY%7CGET_FILTER%3ANONE%7CEXTRAS%3Achannel%2Fuser@SEARCH&keywordTypes=FOOD&searchId=0797993d22350&totalCount=640&ccidActivated=false&top20HasLuxury=false&keywordLeafInternalCategoryId=58799&exposePremiumBrandShortcutFilter=true&version=V2","time":356,"parse":181,"dispatch":5,"binding":3}]',
                'total': 783,
                'categoryDepth': None,
                'signal': -1,
                'viewUpdateTime': 0,
                'prepareApiTime': 5,
                'prepareImageTime': 0,
                'dataSize': 43642
            }
        }
    ]
    
    return run_request(session, method, url, headers, body)
