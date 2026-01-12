import sys
import os
import json
import datetime
import random
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.common.utils import generate_common_payload


# Reference Data Index: 155
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '30255',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session, context: dict = None):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"

    headers = {
        'content-type': 'application/json; charset=utf-8',
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/4.9.3',
        'expect': ''  # [Fix] Disable 'Expect: 100-continue' to prevent proxy/server connection resets
    }

    if not context: context = {}

    # [Dynamic Preparation] Consuming UNIT_LOGS for Schema 13697 & 14741
    # -------------------------------------------------------------
    unit_logs = context.get('RESULT', {}).get('META', {}).get('UNIT_LOGS', [])
    
    # Defaults
    s13697_productIdList = "[]"
    s13697_itemIdList = "[]"
    s13697_vendorItemIdList = "[]"
    s13697_itemStartTime = "[]"
    s13697_itemEndTime = "[]"
    s13697_endItemEventTypeList = "[]"
    s13697_vendorItemCount = 0
    s13697_pageStartTime = int(datetime.datetime.now().timestamp() * 1000)
    s13697_pageEndTime = int(datetime.datetime.now().timestamp() * 1000) + 5000 # default +5s

    if unit_logs:
        # Extract Lists
        s13697_productIdList = str([int(log['data']['productId']) for log in unit_logs if log['data'].get('productId')])
        s13697_itemIdList = str([int(log['data']['itemId']) for log in unit_logs if log['data'].get('itemId')])
        s13697_vendorItemIdList = str([int(log['data']['vendorItemId']) for log in unit_logs if log['data'].get('vendorItemId')])
        s13697_vendorItemCount = len(unit_logs)

        # Simulate Timestamps
        # Assume user scrolls through them linearly. 
        # Start Time: Page Start + small offset per item
        # End Time: Page End (all visible until end) or partial
        
        start_ts_list = []
        end_ts_list = []
        event_type_list = []
        
        base_ts = s13697_pageStartTime + 500 # First item starts 500ms after page start
        
        for i in range(len(unit_logs)):
            # Start: staggered by ~150ms
            item_start = base_ts + (i * 150)
            start_ts_list.append([item_start])
            
            # End: assume they stay visible until page end or slightly before
            item_end = s13697_pageEndTime 
            end_ts_list.append([item_end])
            
            event_type_list.append(["SDP_VID"]) # Default event type seen in captures
        
        s13697_itemStartTime = str(start_ts_list)
        s13697_itemEndTime = str(end_ts_list)
        s13697_endItemEventTypeList = str(event_type_list)
        
        # Update Page End Time if calculated logic suggests longer duration
        final_item_start = start_ts_list[-1][0]
        if final_item_start > s13697_pageEndTime:
             s13697_pageEndTime = final_item_start + 1000 # Ensure end time is after last start
             
    # Prepare body definition


    body = [
        # ============================================================
        # Schema 18359: (Bypass - SDP 진입 로그)
        # Source: Not Found - API 응답에서 직접 추출
        # 용도: SDP 페이지 진입 시 전송되는 로그
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 18359,
                'schemaVersion': 1
            },
            # --------------------------------------------------------
            # [Bypass] 수집완료: 145에서 전체 추출하여 META에 저장
            # 원리: traverse_and_log_schemas()로 API 응답에서 추출
            # 경로: RESULT.META.PRODUCT.18359_1
            # --------------------------------------------------------
            'data': context.get('RESULT', {}).get('META', {}).get('PRODUCT', {}).get('18359_1', {}).get('data', {}),  # [Bypass|수집완료] ← RESULT.META.PRODUCT
            'extra': context.get('RESULT', {}).get('META', {}).get('PRODUCT', {}).get('18359_1', {}).get('extra', {})  # [Bypass|수집완료] ← RESULT.META.PRODUCT
        },
        # ============================================================
        # Schema 15987: ImplicitPageLeave (페이지 이탈)
        # Source: smali_classes22/com/coupang/mobile/implicitlogging/ImplicitPageLeave.smali
        # 용도: 페이지 이탈 시 로깅
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 15987,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'srp',                  # [Fixed] SRP 페이지
                'logCategory': 'view',            # [Fixed] 고정값
                'logType': 'modal',               # [Fixed] 고정값
                'pageName': 'srp',                # [Fixed] SRP 페이지
                'eventName': 'page_leave',        # [Fixed] 고정값
                'pvid': context.get('RESULT', {}).get('SEARCH', {}).get('srp_pvId')  # [Dynamic|수집완료] ← RESULT.SEARCH.srp_pvId
            },
            'extra': {}
        },
        # ============================================================
        # Schema 17062: ProductImageEnlargement (이미지 확대 로깅)
        # Source: smali_classes6/com/coupang/mobile/domain/advertising/logger/scheme/ProductImageEnlargement.smali
        # 용도: 이미지 확대/압축 성능 로깅 (서버측 필수 아님)
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 17062,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'cmg',                  # [Fixed] 고정값
                'logCategory': 'system',          # [Fixed] 고정값
                'logType': 'performance',         # [Fixed] 고정값
                'pageName': None,                 # [Fixed] 고정값 (null)
                'eventName': 'image_enlargement_logging',  # [Fixed] 고정값
                # --------------------------------------------------------
                # [Dynamic] 수집불가: 앱 내부 이미지 처리 정보
                # 원리: 앱이 이미지 로딩/압축 시 생성
                # --------------------------------------------------------
                'eventId': 'b35cb0a0-ed78-11f0-8b76-d328a895e0de',  # [Dynamic|수집불가] UUID 생성
                'definition': '657x657q90trim',   # [Dynamic|수집불가] 이미지 정의 스펙
                'compress': 'true',               # [Dynamic|수집불가] 압축 여부
                'ratio': '0.99847794'             # [Dynamic|수집불가] 압축 비율
            },
            'extra': {}
        },
        # ============================================================
        # Schema 14057: TimeToInteractImage (이미지 로딩 성능)
        # Source: smali_classes5/com/coupang/mobile/common/logger/internal/schema/TimeToInteractImage.smali
        # 용도: 이미지 로딩 성능 모니터링 (서버측 필수 아님)
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 14057,
                'schemaVersion': 2
            },
            'data': {
                'domain': 'search',               # [Fixed] 고정값
                'logCategory': 'impression',      # [Fixed] 고정값
                'logType': 'impression',          # [Fixed] 고정값
                'pageName': 'SearchFragment',     # [Fixed] 고정값
                'eventName': 'image_loads',       # [Fixed] 고정값
                # --------------------------------------------------------
                # [Dynamic] 수집완료: 검색 관련 정보
                # --------------------------------------------------------
                'searchId': context.get('RESULT', {}).get('ROOT', {}).get('searchId'),  # [Dynamic|수집완료] ← RESULT.ROOT.searchId
                'q': context.get('INPUT', {}).get('q'),  # [Dynamic|수집완료] ← INPUT.q
                'sdpVisitKey': None,              # [Dynamic|SRP에서null] SDP 방문 키
                # --------------------------------------------------------
                # [Dynamic] 수집불가: 앱 내부 이미지 로딩 성능
                # 원리: 앱이 이미지 로딩 시 측정
                # 현재: 하드코딩 (성능 시뮬레이션용)
                # --------------------------------------------------------
                'networkType': 'wifi',            # [Dynamic|DEVICE확장] 네트워크 타입
                'fileSizeList': '693888,803648,814784,4624,827776',  # [Dynamic|수집불가] 이미지 파일 크기 리스트
                'imageResolutionList': '417x416,433x464,439x464,34x34,464x446',  # [Dynamic|수집불가] 이미지 해상도 리스트
                'imageUrlList': 'https://thumbnail9.coupangcdn.com/thumbnails/remote/657x657q90trim/image/vendor_inventory/5e47/8d2e8bc32200b474bdf439f8fe02705fe1fd5e2d45b4a4bf3496a3a8f9e7.png.webp,https://thumbnail.coupangcdn.com/thumbnails/remote/657x657q90trim/image/vendor_inventory/image_audit/prod/1c6b2b3e-795b-48af-9b52-01993a5595e6_fixing_v2.png.webp,https://thumbnail.coupangcdn.com/thumbnails/remote/657x657q90trim/image/vendor_inventory/3b3a/29bcfec71c7f96c93b580e2df31da837e3779be4f7c74f953bd1d0535197.jpg.webp,https://image.coupangcdn.com/image/coupang/rds/icon/xxhdpi/rds_icon_similar_outline1702461081753.png,https://thumbnail.coupangcdn.com/thumbnails/remote/657x657q90trim/image/vendor_inventory/d5bb/1922703ddb30b2e92bdce03dcb318285547c6da0829d86c2cc9198b0dba7.png.webp',  # [Dynamic|수집불가] 이미지 URL 리스트
                'resultList': 'SUCCESS,SUCCESS,SUCCESS,SUCCESS,SUCCESS',  # [Dynamic|수집불가] 로딩 결과 리스트
                'itemIdList': 'null,27087300150,26462223016,null,27087300159',  # [Dynamic|수집불가] 아이템 ID 리스트
                'productIdList': 'null,9183773210,9024146312,null,9183773210',  # [Dynamic|수집불가] 상품 ID 리스트
                'vendorItemIdList': 'null,94055536143,93437504341,null,94055536145',  # [Dynamic|수집불가] 벤더아이템 ID 리스트
                'cacheTypeList': 'DATA_DISK_CACHE,DATA_DISK_CACHE,MEMORY_CACHE,MEMORY_CACHE,DATA_DISK_CACHE',  # [Dynamic|수집불가] 캐시 타입 리스트
                'sourceType': 'search_dco-ads,search_pup,search_pup,search_pup,search_pup',  # [Dynamic|수집불가] 소스 타입 리스트
                'imageDurationList': '25,138,0,0,28',  # [Dynamic|수집불가] 이미지 로딩 시간 리스트(ms)
                'rawByteSizeList': '64940,18216,-1,-1,22314'  # [Dynamic|수집불가] 원본 바이트 크기 리스트
            },
            'extra': {
                'rankList': 'null,6,2,null,3'     # [Dynamic|수집불가] 순위 리스트
            }
        },
        # ============================================================
        # Schema 137: PerformanceTti (TTI 성능 로깅 - searchHome)
        # Source: smali/com/coupang/mobile/common/tti/schema/PerformanceTti.smali
        # 용도: Time To Interactive 성능 모니터링 (서버측 필수 아님)
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 137,
                'schemaVersion': 12
            },
            'data': {
                'domain': 'tti',                  # [Fixed] 고정값
                'logCategory': 'system',          # [Fixed] 고정값
                'logType': 'performance',         # [Fixed] 고정값
                'pageName': 'srp',                # [Fixed] SRP 페이지
                'eventName': 'tti-logger',        # [Fixed] 고정값
                # --------------------------------------------------------
                # [Dynamic] 수집불가: 앱 내부 TTI 성능 측정
                # 원리: 앱이 화면 렌더링 완료까지 시간 측정
                # 현재: 하드코딩 (성능 시뮬레이션용)
                # --------------------------------------------------------
                'platformType': 'native',         # [Dynamic|수집불가] 플랫폼 타입
                'tti': 540,                       # [Dynamic|수집불가] Time To Interactive (ms)
                'bounced': False,                 # [Dynamic] 이탈 여부
                'screenType': 'searchHome',       # [Dynamic] 화면 타입
                'viewCreateTime': 7,              # [Dynamic] 뷰 생성 시간(ms)
                'apiResponseTime': 175,           # [Dynamic] API 응답 시간(ms)
                'viewBindingTime': 1,             # [Dynamic] 뷰 바인딩 시간(ms)
                'imageLoadingTime': 0,            # [Dynamic] 이미지 로딩 시간(ms)
                'networkState': 'wifi',           # [Dynamic] 네트워크 상태 ← 디바이스
                'carrier': 'unknown',             # [Dynamic] 통신사 ← 디바이스
                'webViewVersion': '131.0.6778.260',  # [Dynamic] WebView 버전 ← 디바이스
                'ixid': context.get('DEVICE', {}).get('ixid'),  # [Dynamic] Interaction ID
                'async': None,                    # [Dynamic] 비동기 여부
                'serverTime': None,               # [Dynamic] 서버 시간
                'domReady': None,                 # [Dynamic] DOM Ready 시간
                'applicationId': None,            # [Dynamic] 앱 ID
                'serverProcessingTime': None,     # [Dynamic] 서버 처리 시간
                'serverFetchingTime': None,       # [Dynamic] 서버 페칭 시간
                'responseSize': 2339,             # [Dynamic] 응답 크기(bytes)
                'akamaiToGatewayServiceTime': 6,  # [Dynamic] CDN→GW 시간(ms)
                'internalProcessingTime': 32,     # [Dynamic] 내부 처리 시간(ms)
                'transferTime': 143,              # [Dynamic] 전송 시간(ms)
                'imageCount': 0,                  # [Dynamic] 이미지 수
                'prepareApiTime': 25,             # [Dynamic] API 준비 시간(ms)
                'prepareImageTime': 0,            # [Dynamic] 이미지 준비 시간(ms)
                'maxImageSize': None,             # [Dynamic] 최대 이미지 크기
                'averageImageSize': None,         # [Dynamic] 평균 이미지 크기
                'parsingTime': 228,               # [Dynamic] 파싱 시간(ms)
                'pageVersion': None,              # [Dynamic] 페이지 버전
                'cdn': 'envoy',                   # [Dynamic] CDN 타입
                'viewUpdateTime': 0,              # [Dynamic] 뷰 업데이트 시간(ms)
                'gatewayProcessingTime': None,    # [Dynamic] 게이트웨이 처리 시간
                'responseTransferTime': 2,        # [Dynamic] 응답 전송 시간(ms)
                'apiBeforeFetchingTime': 0,       # [Dynamic] API 페칭 전 시간
                'apiAfterFetchingTime': 0         # [Dynamic] API 페칭 후 시간
            },
            'extra': {
                'api': '[{"key":"searchHome","time":175,"parse":228,"dispatch":1,"binding":1,"client_request_to_cdn":67,"client_request_to_gw":73,"gw_response_to_client":68,"response_transfer_time":2,"content_length":2339,"unzipped_size":21694}]',  # [Dynamic] API 성능 상세 JSON
                'image': '[]',                    # [Dynamic] 이미지 성능 상세 JSON
                'total': '430',                   # [Dynamic] 총 시간(ms)
                'categoryDepth': '',              # [Dynamic] 카테고리 깊이
                'campaignId': '',                 # [Dynamic] 캠페인 ID
                'signal': -1,                     # [Dynamic] 신호 강도
                'viewUpdateTime': 0,              # [Dynamic] 뷰 업데이트 시간
                'prepareApiTime': 25,             # [Dynamic] API 준비 시간
                'prepareImageTime': 0,            # [Dynamic] 이미지 준비 시간
                'maxImageUrl': '',                # [Dynamic] 최대 이미지 URL
                'isorganic': 'true'               # [Dynamic] 자연 검색 여부
            }
        },
        {
            'common': generate_common_payload(context),
            'meta': {
                # [Hardcoded] Decompiled: smali/com/coupang/mobile/common/tti/schema/PerformanceTti.smali
                'schemaId': 137,
                'schemaVersion': 12
            },
            'data': {
                'domain': 'tti',                  # [Fixed]
                'logCategory': 'system',          # [Fixed]
                'logType': 'performance',         # [Fixed]
                'pageName': 'srp',                # [Dynamic] 현재 페이지명
                'eventName': 'tti-logger',        # [Fixed]
                'platformType': 'native',         # [Dynamic] 플랫폼 타입
                'tti': 0,                         # [Dynamic] TTI (ms)
                'bounced': False,                 # [Dynamic] 이탈 여부
                'screenType': 'searchResult',     # [Dynamic] 화면 타입
                'viewCreateTime': 36,             # [Dynamic] 뷰 생성 시간(ms)
                'apiResponseTime': 0,             # [Dynamic] API 응답 시간(ms)
                'viewBindingTime': -9,            # [Dynamic] 뷰 바인딩 시간(ms)
                'imageLoadingTime': 0,            # [Dynamic] 이미지 로딩 시간(ms)
                'networkState': 'wifi',           # [Dynamic] 네트워크 상태 ← 디바이스
                'carrier': 'unknown',             # [Dynamic] 통신사 ← 디바이스
                'webViewVersion': '131.0.6778.260',  # [Dynamic] WebView 버전 ← 디바이스
                'ixid': context.get('DEVICE', {}).get('ixid'),  # [Dynamic] Interaction ID
                'async': None,                    # [Dynamic]
                'serverTime': None,               # [Dynamic]
                'domReady': None,                 # [Dynamic]
                'applicationId': None,            # [Dynamic]
                'serverProcessingTime': None,     # [Dynamic]
                'serverFetchingTime': None,       # [Dynamic]
                'responseSize': 0,                # [Dynamic] 응답 크기(bytes)
                'akamaiToGatewayServiceTime': None,  # [Dynamic]
                'internalProcessingTime': None,   # [Dynamic]
                'transferTime': None,             # [Dynamic]
                'imageCount': 0,                  # [Dynamic] 이미지 수
                'prepareApiTime': 0,              # [Dynamic]
                'prepareImageTime': 0,            # [Dynamic]
                'maxImageSize': None,             # [Dynamic]
                'averageImageSize': None,         # [Dynamic]
                'parsingTime': 0,                 # [Dynamic] 파싱 시간(ms)
                'pageVersion': None,              # [Dynamic]
                'cdn': 'none',                    # [Dynamic] CDN 타입
                'viewUpdateTime': 0,              # [Dynamic]
                'gatewayProcessingTime': None,    # [Dynamic]
                'responseTransferTime': 0,        # [Dynamic]
                'apiBeforeFetchingTime': 0,       # [Dynamic]
                'apiAfterFetchingTime': 0         # [Dynamic]
            },
            'extra': {
                'api': '[]',                      # [Dynamic] API 성능 상세 JSON
                'image': '[]',                    # [Dynamic] 이미지 성능 상세 JSON
                'total': '27',                    # [Dynamic] 총 시간(ms)
                'categoryDepth': '',              # [Dynamic]
                'campaignId': '',                 # [Dynamic]
                'signal': -1,                     # [Dynamic] 신호 강도
                'viewUpdateTime': 0,              # [Dynamic]
                'prepareApiTime': 0,              # [Dynamic]
                'prepareImageTime': 0,            # [Dynamic]
                'maxImageUrl': '',                # [Dynamic]
                'isorganic': 'true',              # [Dynamic] 자연 검색 여부
                'datasize': '611296'              # [Dynamic] 데이터 크기(bytes)
            }
        },
        {
            'common': generate_common_payload(context),
            'meta': {
                # [Hardcoded] Decompiled: smali/com/coupang/mobile/common/tti/schema/PerformanceTti.smali
                'schemaId': 137,
                'schemaVersion': 12
            },
            'data': {
                'domain': 'tti',                  # [Fixed]
                'logCategory': 'system',          # [Fixed]
                'logType': 'performance',         # [Fixed]
                'pageName': 'srp_comp',           # [Dynamic] 현재 페이지명 (srp_comp = SRP Complete)
                'eventName': 'tti-logger',        # [Fixed]
                'platformType': 'native',         # [Dynamic] 플랫폼 타입
                'tti': 1342,                      # [Dynamic] TTI (ms)
                'bounced': False,                 # [Dynamic] 이탈 여부
                'screenType': 'searchResult',     # [Dynamic] 화면 타입
                'viewCreateTime': 36,             # [Dynamic] 뷰 생성 시간(ms)
                'apiResponseTime': 855,           # [Dynamic] API 응답 시간(ms)
                'viewBindingTime': 40,            # [Dynamic] 뷰 바인딩 시간(ms)
                'imageLoadingTime': 142,          # [Dynamic] 이미지 로딩 시간(ms)
                'networkState': 'wifi',           # [Dynamic] 네트워크 상태 ← 디바이스
                'carrier': 'unknown',             # [Dynamic] 통신사 ← 디바이스
                'webViewVersion': '131.0.6778.260',  # [Dynamic] WebView 버전 ← 디바이스
                'ixid': context.get('DEVICE', {}).get('ixid'),  # [Dynamic] Interaction ID
                'async': None,                    # [Dynamic]
                'serverTime': None,               # [Dynamic]
                'domReady': None,                 # [Dynamic]
                'applicationId': None,            # [Dynamic]
                'serverProcessingTime': 644,      # [Dynamic] 서버 처리 시간(ms)
                'serverFetchingTime': 558,        # [Dynamic] 서버 페칭 시간(ms)
                'responseSize': 0,                # [Dynamic] 응답 크기(bytes)
                'akamaiToGatewayServiceTime': 6,  # [Dynamic] CDN→GW 시간(ms)
                'internalProcessingTime': 684,    # [Dynamic] 내부 처리 시간(ms)
                'transferTime': 171,              # [Dynamic] 전송 시간(ms)
                'imageCount': 2,                  # [Dynamic] 이미지 수
                'prepareApiTime': 43,             # [Dynamic] API 준비 시간(ms)
                'prepareImageTime': 1243,         # [Dynamic] 이미지 준비 시간(ms)
                'maxImageSize': 59910,            # [Dynamic] 최대 이미지 크기(bytes)
                'averageImageSize': 39063,        # [Dynamic] 평균 이미지 크기(bytes)
                'parsingTime': 169,               # [Dynamic] 파싱 시간(ms)
                'pageVersion': None,              # [Dynamic]
                'cdn': 'envoy',                   # [Dynamic] CDN 타입
                'viewUpdateTime': 126,            # [Dynamic] 뷰 업데이트 시간(ms)
                'gatewayProcessingTime': 40,      # [Dynamic] 게이트웨이 처리 시간(ms)
                'responseTransferTime': 6,        # [Dynamic] 응답 전송 시간(ms)
                'apiBeforeFetchingTime': 0,       # [Dynamic]
                'apiAfterFetchingTime': 0         # [Dynamic]
            },
            'extra': {
                'api': '[{"key":"searchResult","time":855,"parse":169,"dispatch":8,"binding":40,"client_request_to_cdn":66,"client_request_to_gw":72,"gw_response_to_client":92,"response_transfer_time":6,"content_length":0,"unzipped_size":611296}]',  # [Dynamic] API 성능 상세 JSON
                'image': '[{"key":"LegoSquareImage","time":138,"url":"https:\\/\\/thumbnail.coupangcdn.com\\/thumbnails\\/remote\\/657x657q90trim\\/image\\/vendor_inventory\\/image_audit\\/prod\\/1c6b2b3e-795b-48af-9b52-01993a5595e6_fixing_v2.png.webp","preload":"NONE","image_loading_end":"363271968","image_size":"18216","image_decoding":"22","image_loading_start":"363271830","after_decoding":"114","image_fetching":"0","before_fetching":"1","cacheType":"DATA_DISK_CACHE"},{"key":"LegoSquareImage","time":84,"url":"https:\\/\\/thumbnail.coupangcdn.com\\/thumbnails\\/remote\\/657x657q90trim\\/image\\/vendor_inventory\\/3b3a\\/29bcfec71c7f96c93b580e2df31da837e3779be4f7c74f953bd1d0535197.jpg.webp","preload":"NONE","image_loading_end":"363271972","image_size":"59910","image_decoding":"29","image_loading_start":"363271888","after_decoding":"53","image_fetching":"1","before_fetching":"1","cacheType":"DATA_DISK_CACHE"}]',  # [Dynamic] 이미지 성능 상세 JSON
                'total': '1117',                  # [Dynamic] 총 시간(ms)
                'categoryDepth': '',              # [Dynamic]
                'campaignId': '',                 # [Dynamic]
                'signal': -1,                     # [Dynamic] 신호 강도
                'viewUpdateTime': 126,            # [Dynamic]
                'prepareApiTime': 43,             # [Dynamic]
                'prepareImageTime': 1243,         # [Dynamic]
                'maxImageUrl': 'https://thumbnail.coupangcdn.com/thumbnails/remote/657x657q90trim/image/vendor_inventory/image_audit/prod/1c6b2b3e-795b-48af-9b52-01993a5595e6_fixing_v2.png.webp',  # [Dynamic] 최대 이미지 URL
                'pagesnapshottime': '0',          # [Dynamic] 페이지 스냅샷 시간
                'isorganic': 'true',              # [Dynamic] 자연 검색 여부
                'pagesnapshot': '{"domainPageArea":[{"viewName":"AppBarLayout","isHidden":false,"isZeroSize":false},{"viewName":"SearchResultHeaderViewRedesign","isHidden":false,"isZeroSize":true},{"viewName":"DcoHorizontalScrollContainerView","isHidden":false,"isZeroSize":false,"viewType":"DYNAMIC_TEMPLATE"},{"viewName":"LegoContainerView","isHidden":false,"isZeroSize":false,"viewType":"U_WIDGET"},{"viewName":"LegoContainerView","isHidden":false,"isZeroSize":false,"viewType":"U_WIDGET"},{"viewName":"TabMenu","isHidden":false,"isZeroSize":false},{"viewName":"BottomNudgingWithCloseButtonView","isHidden":false,"isZeroSize":false}],"domainPageName":"srp"}',  # [Dynamic] 페이지 스냅샷 JSON
                'preload_image_request': '[{"url":"https://thumbnail.coupangcdn.com/thumbnails/remote/657x657q90trim/image/vendor_inventory/image_audit/prod/1c6b2b3e-795b-48af-9b52-01993a5595e6_fixing_v2.png.webp","image_loading_start":363271658,"requested_resolution":"-2147483648x-2147483648"},{"url":"https://thumbnail.coupangcdn.com/thumbnails/remote/657x657q90trim/image/vendor_inventory/3b3a/29bcfec71c7f96c93b580e2df31da837e3779be4f7c74f953bd1d0535197.jpg.webp","image_loading_start":363271659,"requested_resolution":"-2147483648x-2147483648"},{"url":"https://thumbnail.coupangcdn.com/thumbnails/remote/657x657q90trim/image/vendor_inventory/3b3a/29bcfec71c7f96c93b580e2df31da837e3779be4f7c74f953bd1d0535197.jpg.webp","image_loading_start":363271659,"requested_resolution":"-2147483648x-2147483648"},{"url":"https://thumbnail.coupangcdn.com/thumbnails/remote/657x657q90trim/image/vendor_inventory/d5bb/1922703ddb30b2e92bdce03dcb318285547c6da0829d86c2cc9198b0dba7.png.webp","image_loading_start":363271659,"requested_resolution":"-2147483648x-2147483648"}]',  # [Dynamic] 프리로드 이미지 요청 JSON
                'viewholdertimedetails': '[{"Key":"com.coupang.mobile.commonui.widget.commonlist.viewholder.DefaultCommonViewHolder","ViewHolderCreationTime":0,"ViewHolderDataBindingTime":0},{"Key":"com.coupang.mobile.commonui.widget.commonlist.viewholder.DefaultCommonViewHolder","ViewHolderCreationTime":0,"ViewHolderDataBindingTime":0},{"Key":"com.coupang.mobile.domain.advertising.view.viewholder.DynamicTemplateVHFactoryImpl.VH","ViewHolderCreationTime":1,"ViewHolderDataBindingTime":39},{"Key":"com.coupang.mobile.commonui.rds.renderengine.viewholder.UWidgetViewHolderFactory.UWidgetVH","ViewHolderCreationTime":53,"ViewHolderDataBindingTime":26},{"Key":"com.coupang.mobile.commonui.rds.renderengine.viewholder.UWidgetViewHolderFactory.UWidgetVH","ViewHolderCreationTime":38,"ViewHolderDataBindingTime":12}]',  # [Dynamic] ViewHolder 시간 상세 JSON
                'timetotrackviewviewholdertimedetails': '1'  # [Dynamic]
            }
        },
        # ============================================================
        # Schema 13697: SrpBrowseDuration (SRP 브라우징 시간)
        # Source: smali_classes18/com/coupang/mobile/domain/search/monitoring/schema/SrpBrowseDuration.smali
        # 용도: SRP 페이지에서 상품 노출 시간 로깅 (중요)
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 13697,
                'schemaVersion': 2
            },
            'data': {
                'domain': 'SRP',                  # [Fixed] 고정값
                'logCategory': 'impression',      # [Fixed] 고정값
                'logType': 'impression',          # [Fixed] 고정값
                'pageName': 'srp',                # [Fixed] 고정값
                'eventName': 'srp_product_unit_exposure',  # [Fixed] 고정값
                # --------------------------------------------------------
                # [Dynamic] 수집완료: 검색 관련 정보
                # --------------------------------------------------------
                'query': context.get('INPUT', {}).get('q'),  # [Dynamic|수집완료] ← INPUT.q
                'searchId': context.get('RESULT', {}).get('ROOT', {}).get('searchId'),  # [Dynamic|수집완료] ← RESULT.ROOT.searchId
                'ixid': context.get('DEVICE', {}).get('ixid'),  # [Dynamic|수집완료] ← DEVICE.ixid
                # --------------------------------------------------------
                # [Dynamic] 수집불가: 앱 내부 노출 시간 측정
                # 원리: 앱이 스크롤 시 각 상품의 노출 시작/종료 시간 측정
                # 현재: 하드코딩 (노출 시뮬레이션용)
                # --------------------------------------------------------
                'productIdList': s13697_productIdList,            # [Dynamic|수집완료] 노출된 상품 ID 리스트 (from UNIT_LOGS)
                'itemIdList': s13697_itemIdList,                  # [Dynamic|수집완료] 노출된 아이템 ID 리스트 (from UNIT_LOGS)
                'vendorItemIdList': s13697_vendorItemIdList,      # [Dynamic|수집완료] 노출된 벤더아이템 ID 리스트 (from UNIT_LOGS)
                'pageStartTime': s13697_pageStartTime,            # [Dynamic|수집완료] 페이지 시작 타임스탬프
                'pageEndTime': s13697_pageEndTime,                # [Dynamic|수집완료] 페이지 종료 타임스탬프
                'itemStartTime': s13697_itemStartTime,            # [Dynamic|수집완료] 각 아이템 노출 시작 시간
                'itemEndTime': s13697_itemEndTime,                # [Dynamic|수집완료] 각 아이템 노출 종료 시간
                'endEventType': 'SDP_VID',                        # [Fixed] 종료 이벤트 타입
                'endItemEventTypeList': s13697_endItemEventTypeList, # [Dynamic|수집완료] 각 아이템 종료 이벤트 타입
                'vendorItemCount': s13697_vendorItemCount         # [Dynamic|수집완료] 노출된 벤더아이템 수
            },
            'extra': {}
        },
        # ============================================================
        # Schema 14741: SrpProductUnitImpression (Dynamic Generation)
        # Strategy: Log *all* visible items extracted by 128_G (Rank 0 to Target)
        # ============================================================
    ]

    # [Fix] Payload Chunking to avoid 64KB limit (Connection Reset)
    # The overhead schemas are constant. The unit logs (14741) add weight.
    # Strategy: Send overhead + first 3 unit logs in Batch 1.
    #           Send remaining unit logs in subsequent batches (max 5 per batch).
    
    overhead_schemas = body  # The list initialized above contains only overhead schemas so far
    
    # Generate all Unit Log Schemas first
    unit_log_schemas = []
    
    current_time = datetime.datetime.now()
    
    for i, log_entry in enumerate(unit_logs):
        # ... (Transformation logic copied from above) ...
        # Wait, I need to preserve the transformation logic.
        # I will cut the original code passed the body init, generate the schemas into unit_log_schemas list, then chunk.
        
        # Simulate sequential exposure (user scrolling)
        jitter = random.randint(20, 50) * (i + 1)
        event_time_dt = current_time + datetime.timedelta(milliseconds=jitter)
        event_time_str = event_time_dt.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + "+0900"
        
        schema_block = {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': log_entry['schemaId'],
                'schemaVersion': log_entry['version']
            },
            'data': log_entry['data'],
            'extra': log_entry['extra']
        }
        
        # [Patch] Schema 14741 Fidelity Fixes
        if str(log_entry['schemaId']) == '14741':
            d = schema_block['data']
            # 1. Boolean Type Fix
            bool_keys = [
                'isFreeReturn', 'isRocket', 'isCoupick', 'isBestReviewBadge', 'isBlueBadge', 
                'isTitleVisible', 'isSalesPriceVisible', 'isPddVisible', 'isOriginalPriceVisible',
                'isAdultProduct', 'isSoldOut', 'hasDiscount', 'starRating', 'imageCount'
            ]
            for k in bool_keys:
                if k in d:
                    val = str(d[k]).lower()
                    if val in ['true', 'yes', '1']: d[k] = True
                    elif val in ['false', 'no', '0']: d[k] = False
            
            # 2. Missing Fields
            if not d.get('viewType'):
                svt = context.get('RESULT', {}).get('SEARCH', {}).get('searchViewType', 'GRID_2')
                if 'GRID' in svt: d['viewType'] = 'BRICK_PRODUCT_UNIT_GRID_UPROTOCOL_M2'
                else: d['viewType'] = 'BRICK_PRODUCT_UNIT_LIST_UPROTOCOL_M2'
            
            if not d.get('source'): d['source'] = 'srp'
        
        schema_block['common']['eventTime'] = event_time_str
        if 'exposureTimestamp' in schema_block['data']: schema_block['data']['exposureTimestamp'] = event_time_str
        else: schema_block['data']['exposureTimestamp'] = event_time_str
        
        unit_log_schemas.append(schema_block)

    print(f"[156] Generated {len(unit_log_schemas)} Unit Schemas. Proceeding to Chunked Delivery.")

    # Chunking Logic
    CHUNK_SIZE = 3 # Conservative size (Overhead + 3 logs ~ 40KB?)
    
    # First Batch: Overhead + First Chunk
    first_chunk = unit_log_schemas[:CHUNK_SIZE]
    remaining_chunks = [unit_log_schemas[i:i + 5] for i in range(CHUNK_SIZE, len(unit_log_schemas), 5)] # Subsequent chunks can be larger as they have no overhead
    
    # 1. Send First Batch
    batch_1_body = overhead_schemas + first_chunk
    print(f"[156] Batch 1 Size: {len(json.dumps(batch_1_body))} bytes")
    
    # Jitter
    base_time = datetime.datetime.now()
    for item in batch_1_body:
        offset_ms = random.randint(1, 5)
        base_time += datetime.timedelta(milliseconds=offset_ms)
        item['common']['eventTime'] = base_time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "+0900"

    resp = run_request(session, method, url, headers, batch_1_body)
    
    # 2. Send Remaining Batches
    for idx, chunk in enumerate(remaining_chunks):
        print(f"[156] Batch {idx+2} Size: {len(json.dumps(chunk))} bytes")
        
        # Update common payload for new request time (optional but good)
        # We reuse the generated objects but common time was set. It is fine.
        
        run_request(session, method, url, headers, chunk)
        
    return resp
