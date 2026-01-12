import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 73
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '12607',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '12607',
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
                'eventTime': '2026-01-10T01:31:23.001+0900',
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
                'sourceType': 'home_promotion',
                'domain': 'home',
                'isDisplayed': False,
                'eventName': 'home_page_information',
                'logCategory': 'impression',
                'position': 13,
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
                'eventTime': '2026-01-10T01:31:23.011+0900',
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
                'eventTime': '2026-01-10T01:31:23.017+0900',
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
                'fileSizeList': '2203200,484416,484416,2203200,1088640,484416,2203200',
                'imageResolutionList': '1080x510,348x348,348x348,1080x510,1080x252,348x348,1080x510',
                'imageUrlList': 'https://thumbnail.coupangcdn.com/thumbnails/remote/mlow/image/bannerunit/bannerunit_30b7d476-431c-4a1f-85b1-5905d3060335.png,https://thumbnail8.coupangcdn.com/thumbnails/remote/292x292q65ex/image/vendor_inventory/image_audit/prod/b97749d6-381a-4214-97d8-f49117ffad82_fixing_v2.png,https://thumbnail4.coupangcdn.com/thumbnails/remote/292x292q65ex/image/vendor_inventory/0687/262255e9b0244679bf5d2d3983b420d4b7eae8547130f0259a198974a77e.jpg,https://image12.coupangcdn.com/image/ccm/banner/354b89f843f33bcd91dac21fcd7797ae.jpg,https://thumbnail.coupangcdn.com/thumbnails/remote/mhigh/image/displayitem/displayitem_e22090e3-4316-450d-947d-de613bfbd913.jpg,https://thumbnail4.coupangcdn.com/thumbnails/remote/292x292q65ex/image/vendor_inventory/669c/cb45a0d94f7efac2426033308861bed66ab79d2b3deb423f6c2ba34f22f5.jpg,https://img5a.coupangcdn.com/image/ccm/banner/5e48de838a1444fe0b8259e03fd9821e.png',
                'resultList': 'SUCCESS,SUCCESS,SUCCESS,SUCCESS,SUCCESS,SUCCESS,SUCCESS',
                'itemIdList': None,
                'productIdList': None,
                'vendorItemIdList': None,
                'sdpVisitKey': None,
                'searchId': None,
                'q': None,
                'cacheTypeList': 'DATA_DISK_CACHE,MEMORY_CACHE,MEMORY_CACHE,REMOTE,MEMORY_CACHE,MEMORY_CACHE,REMOTE',
                'sourceType': 'gateway_banner-list,gateway_dco-ads,gateway_dco-ads,gateway_banner-list,gateway_banner,gateway_dco-ads,gateway_banner-list',
                'imageDurationList': '151,0,0,448,1,0,428',
                'rawByteSizeList': '108300,-1,-1,142583,15459,-1,58662'
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
                'eventTime': '2026-01-10T01:31:23.022+0900',
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
                'pageName': 'home',
                'eventName': 'tti-logger',
                'platformType': 'native',
                'tti': 1016,
                'bounced': False,
                'screenType': 'TODAY_RECOMMENDATIONS',
                'viewCreateTime': 156,
                'apiResponseTime': 200,
                'viewBindingTime': 7,
                'imageLoadingTime': 570,
                'networkState': 'wifi',
                'carrier': 'unknown',
                'webViewVersion': '131.0.6778.260',
                'ixid': '00014a5c-875e-3c7d-1f06-c3ccfdbb073c',
                'async': None,
                'serverTime': None,
                'domReady': None,
                'applicationId': None,
                'serverProcessingTime': 53,
                'serverFetchingTime': 51,
                'responseSize': 11059,
                'akamaiToGatewayServiceTime': 7,
                'internalProcessingTime': 59,
                'transferTime': 141,
                'imageCount': 12,
                'prepareApiTime': -22,
                'prepareImageTime': 446,
                'maxImageSize': 108300,
                'averageImageSize': 29441,
                'parsingTime': 4,
                'pageVersion': None,
                'cdn': 'envoy',
                'viewUpdateTime': 86,
                'gatewayProcessingTime': 6,
                'responseTransferTime': 0,
                'apiBeforeFetchingTime': 0,
                'apiAfterFetchingTime': 0
            },
            'extra': {
                'api': '[{"key":"","time":200,"parse":4,"dispatch":171,"binding":7,"client_request_to_cdn":66,"client_request_to_gw":73,"gw_response_to_client":68,"response_transfer_time":0,"content_length":11059,"unzipped_size":88507}]',
                'image': '[{"key":"C1_IMAGE","time":152,"url":"bannerunit\\/bannerunit_30b7d476-431c-4a1f-85b1-5905d3060335.png","preload":"NONE","image_loading_end":"363236868","doAnimate":"false","image_size":"108300","image_decoding":"61","image_loading_start":"363236716","after_decoding":"41","image_fetching":"1","before_fetching":"49","cacheType":"DATA_DISK_CACHE"},{"key":"CATEGORY","time":170,"url":"coupang\\/home\\/icons\\/3d\\/icon_coupang_play_3d_v3.png","preload":"NONE","image_loading_end":"363236897","image_size":"19579","image_decoding":"30","image_loading_start":"363236727","after_decoding":"9","image_fetching":"118","before_fetching":"6","cdn_cache_status":"Hit from cloudfront","cacheType":"REMOTE"},{"key":"CATEGORY","time":255,"url":"coupang\\/home\\/icons\\/3d\\/icon_jikgu_3d_v3.png","preload":"NONE","image_loading_end":"363236984","image_size":"28106","image_decoding":"23","image_loading_start":"363236729","after_decoding":"3","image_fetching":"199","before_fetching":"5","cdn_cache_status":"Hit from cloudfront","cacheType":"REMOTE"},{"key":"CATEGORY","time":222,"url":"coupang\\/home\\/icons\\/3d\\/icon_fresh_3d_v3.png","preload":"NONE","image_loading_end":"363236956","image_size":"31096","image_decoding":"19","image_loading_start":"363236734","after_decoding":"10","image_fetching":"173","before_fetching":"1","cdn_cache_status":"Hit from cloudfront","cacheType":"REMOTE"},{"key":"CATEGORY","time":258,"url":"coupang\\/home\\/icons\\/3d\\/icon_rlux_3d_v3.png","preload":"NONE","image_loading_end":"363236995","image_size":"25430","image_decoding":"31","image_loading_start":"363236737","after_decoding":"4","image_fetching":"193","before_fetching":"1","cdn_cache_status":"Hit from cloudfront","cacheType":"REMOTE"},{"key":"CATEGORY","time":244,"url":"coupang\\/home\\/icons\\/3d\\/icon_eats_3d_v3.png","preload":"NONE","image_loading_end":"363236984","image_size":"19732","image_decoding":"20","image_loading_start":"363236740","after_decoding":"6","image_fetching":"190","before_fetching":"3","cdn_cache_status":"Hit from cloudfront","cacheType":"REMOTE"},{"key":"CATEGORY","time":254,"url":"coupang\\/home\\/icons\\/3d\\/icon_coupang_play_3d_v3.png","preload":"NONE","image_loading_end":"363236996","image_size":"20107","image_decoding":"5","image_loading_start":"363236742","after_decoding":"6","image_fetching":"235","before_fetching":"1","cdn_cache_status":"Hit from cloudfront","cacheType":"REMOTE"},{"key":"CATEGORY","time":344,"url":"coupang\\/home\\/icons\\/3d\\/icon_jikgu_3d_v3.png","preload":"NONE","image_loading_end":"363237093","image_size":"21430","image_decoding":"22","image_loading_start":"363236749","after_decoding":"30","image_fetching":"279","before_fetching":"3","cdn_cache_status":"Hit from cloudfront","cacheType":"REMOTE"},{"key":"CATEGORY","time":343,"url":"coupang\\/home\\/icons\\/3d\\/icon_fresh_3d_v3.png","preload":"NONE","image_loading_end":"363237095","image_size":"15373","image_decoding":"6","image_loading_start":"363236752","after_decoding":"7","image_fetching":"316","before_fetching":"4","cdn_cache_status":"Hit from cloudfront","cacheType":"REMOTE"},{"key":"CATEGORY","time":392,"url":"coupang\\/home\\/icons\\/3d\\/icon_rlux_3d_v3.png","preload":"NONE","image_loading_end":"363237147","image_size":"20410","image_decoding":"12","image_loading_start":"363236755","after_decoding":"2","image_fetching":"370","before_fetching":"1","cdn_cache_status":"Hit from cloudfront","cacheType":"REMOTE"},{"key":"CATEGORY","time":492,"url":"coupang\\/home\\/icons\\/3d\\/icon_eats_3d_v3.png","preload":"NONE","image_loading_end":"363237250","image_size":"28278","image_decoding":"10","image_loading_start":"363236758","after_decoding":"0","image_fetching":"461","before_fetching":"3","cdn_cache_status":"Hit from cloudfront","cacheType":"REMOTE"},{"key":"LIST_BANNER","time":526,"url":"displayitem\\/displayitem_e22090e3-4316-450d-947d-de613bfbd913.jpg","preload":"NONE","image_loading_end":"363237286","doAnimate":"false","image_size":"15459","image_decoding":"20","image_loading_start":"363236760","after_decoding":"16","image_fetching":"462","before_fetching":"8","cdn_cache_status":"Hit from cloudfront","cacheType":"REMOTE"}]',
                'total': '360',
                'categoryDepth': '',
                'campaignId': '',
                'signal': -1,
                'viewUpdateTime': 86,
                'prepareApiTime': -22,
                'prepareImageTime': 446,
                'maxImageUrl': 'displayitem/displayitem_e22090e3-4316-450d-947d-de613bfbd913.jpg',
                'starttype': 'ORGANIC',
                'pagesnapshottime': '1',
                'isorganic': 'true',
                'splashnudgeactiontype': 'loginPrompt',
                'pagesnapshot': '{"domainPageArea":[{"viewName":"ListEmptyView","isHidden":false,"isZeroSize":false},{"viewName":"LoadingFooterView","isHidden":false,"isZeroSize":true},{"viewName":"ImageGroupFullyRecyclerPagerView","isHidden":false,"isZeroSize":false,"viewType":"NONE_CLICK_IMAGE_PAGER"},{"viewName":"QuickCategoryGridView","isHidden":false,"isZeroSize":false,"viewType":"QUICK_GRID_CATEGORY"},{"viewName":"BannerView","isHidden":false,"isZeroSize":false,"viewType":"LIST_BANNER"},{"viewName":"LoadingFooterView","isHidden":false,"isZeroSize":true},{"viewName":"AppBarLayout","isHidden":false,"isZeroSize":false},{"viewName":"TabMenu","isHidden":false,"isZeroSize":false}],"domainPageName":"home"}',
                'appstarttime': '1734',
                'splashnudgecontenttype': 'TARGET_PROMOTION',
                'withsplashnudge': 'true'
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
                'eventTime': '2026-01-10T01:31:23.049+0900',
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
                'message': 'tab has finished loading'
            },
            'extra': {}
        }
    ]
    
    return run_request(session, method, url, headers, body)
