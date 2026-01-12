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

def run(session: requests.Session, context: dict = None):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"

    headers = {
        'content-type': 'application/json; charset=utf-8',
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/4.9.3'
    }

    if not context: context = {}

    if not context: context = {}

    # [Patch] Schema 124 preparation
    # Bypass schema often lacks client-side context (q, searchId, etc.)
    # We match the server schema but MUST inject client-side known values.
    bypass_124 = context.get('srp_click_log_bypass', {})
    fallback_124 = context.get('RESULT', {}).get('META', {}).get('SEARCH', {}).get('124_53', {})
    
    schema_124_data = (bypass_124.get('mandatory') or fallback_124.get('data') or {}).copy()
    
    # Inject Missing Keys
    if not schema_124_data.get('q'):
        schema_124_data['q'] = context.get('INPUT', {}).get('q')
        
    if not schema_124_data.get('internalCategoryId'):
        schema_124_data['internalCategoryId'] = context.get('RESULT', {}).get('SEARCH', {}).get('internalCategoryId') # From 128_G
        
    if not schema_124_data.get('id'):
         schema_124_data['id'] = context.get('RESULT', {}).get('ROOT', {}).get('productId')
         
    if not schema_124_data.get('itemProductId'):
         schema_124_data['itemProductId'] = 4 # Default for most products
         
    if not schema_124_data.get('searchViewType'):
         schema_124_data['searchViewType'] = context.get('RESULT', {}).get('SEARCH', {}).get('searchViewType', 'GRID_2')

    # Ensure rank is present
    if not schema_124_data.get('rank'):
        schema_124_data['rank'] = context.get('RESULT', {}).get('SEARCH', {}).get('srp_rank')

    body = [
        # ============================================================
        # Schema 15989: PageInteraction (페이지 인터랙션)
        # Source: smali_classes2/com/coupang/mobile/implicitlogging/PageInteraction.smali
        # 용도: 페이지 내 사용자 인터랙션 로깅
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 15989,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'srp',                  # [Fixed] SRP 페이지
                'logCategory': 'event',           # [Fixed] 고정값
                'logType': 'processing',          # [Fixed] 고정값
                'pageName': 'srp',                # [Fixed] SRP 페이지
                'eventName': 'page_interact'      # [Fixed] 고정값
            },
            'extra': {
                'pvid': context.get('RESULT', {}).get('SEARCH', {}).get('srp_pvId')  # [Dynamic|수집완료] ← RESULT.SEARCH.srp_pvId
            }
        },
        # ============================================================
        # Schema 7960: FeatureTracking (기능 추적 - SDP 이동 시작)
        # Source: smali/com/coupang/mobile/common/abtest/schema/FeatureTracking.smali
        # 용도: MVVM 리팩토링 마이그레이션 추적
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 7960,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'android',              # [Fixed] 고정값
                'logCategory': 'system',          # [Fixed] 고정값
                'logType': 'debug',               # [Fixed] 고정값
                'pageName': 'mvvm refactor',      # [Fixed] 고정값
                'eventName': 'mvvm refactor',     # [Fixed] 고정값
                # --------------------------------------------------------
                # [Hardcoded] 수집불가: 앱 내부 마이그레이션 추적
                # 원리: 앱 빌드 시 결정되는 기능명
                # --------------------------------------------------------
                'featureName': 'MoveToSdpMigration',  # [Hardcoded|수집불가] 기능명
                'schemaName': 'move_to_sdp',      # [Hardcoded|수집불가] 스키마명
                'additionalComment': 'start'      # [Hardcoded|수집불가] 시작 표시
            },
            'extra': {}
        },
        # ============================================================
        # Schema 124: SrpProductClick (SRP 상품 클릭 - 핵심)
        # Source: smali_classes18/com/coupang/mobile/domain/search/monitoring/schema/SrpProductClick.smali
        # 용도: 검색 결과에서 상품 클릭 로깅 (중요)
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 124,
                'schemaVersion': 53
            },
            # --------------------------------------------------------
            # [Bypass] 수집완료: 128에서 선택된 상품의 Bypass Schemas를 우선 사용
            # 원리: 128_G에서 srp_click_log_bypass에 저장한 정확한 스키마 사용
            # Fallback: RESULT.META.SEARCH (기존 로직)
            # --------------------------------------------------------
            # --------------------------------------------------------
            # [Bypass] 수집완료: 128에서 선택된 상품의 Bypass Schemas를 우선 사용
            # 원리: 128_G에서 srp_click_log_bypass에 저장한 정확한 스키마 사용
            # Fallback: RESULT.META.SEARCH (기존 로직)
            # Patch: q, internalCategoryId 등 Context 정보 강제 주입
            # --------------------------------------------------------
            'data': schema_124_data,
            'extra': {
                **(context.get('srp_click_log_bypass', {}).get('extra', {}) or context.get('RESULT', {}).get('META', {}).get('SEARCH', {}).get('124_53', {}).get('extra', {})),
                'currentView': '/search_list',
                'eventReferrer': 'click_search_list'
            }
        },
        # ============================================================
        # Schema 7598: CommonCheckingUnused (미사용 기능 체크)
        # Source: smali/com/coupang/mobile/common/logger/internal/schema/CommonCheckingUnused.smali
        # 용도: 앱 내부 기능 사용 추적 (서버측 필수 아님)
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 7598,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'common',               # [Fixed] 고정값
                'logCategory': 'system',          # [Fixed] 고정값
                'logType': 'platform',            # [Fixed] 고정값
                'pageName': '',                   # [Fixed] 고정값 (빈값)
                'eventName': 'common_checking_unused',  # [Fixed] 고정값
                # --------------------------------------------------------
                # [Hardcoded] 수집불가: 앱 내부 기능 ID
                # --------------------------------------------------------
                'key': 'MPA_3281',                # [Hardcoded|수집불가] 기능 ID
                'value': 'getSelectedParamsString - has filter data'  # [Hardcoded|수집불가] UseCase명
            },
            'extra': {}
        },
        # ============================================================
        # Schema 7960: FeatureTracking (기능 추적 - FBI PUP 마이그레이션)
        # Source: smali/com/coupang/mobile/common/abtest/schema/FeatureTracking.smali
        # 용도: SDP 전환 시 상품 정보 전달 (중요)
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 7960,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'android',              # [Fixed] 고정값
                'logCategory': 'system',          # [Fixed] 고정값
                'logType': 'debug',               # [Fixed] 고정값
                'pageName': 'mvvm refactor',      # [Fixed] 고정값
                'eventName': 'mvvm refactor',     # [Fixed] 고정값
                'featureName': 'fbi_pup_migration',  # [Hardcoded|수집불가] 기능명
                'schemaName': None,               # [Hardcoded|수집불가] 스키마명
                'additionalComment': None         # [Hardcoded|수집불가] 추가 코멘트
            },
            'extra': {
                # --------------------------------------------------------
                # [Dynamic] SDP 전환 시 전달되는 상품 정보
                # 원리: SRP에서 클릭한 상품 정보를 SDP로 전달
                # --------------------------------------------------------
                'KEY_RATING_HIGHLIGHT': 'true',                    # [Fixed] 고정값
                'sdp.requestParams': '{}',                         # [Fixed] 고정값
                'KEY_PICK_TYPE': 'COU_PICK' if context.get('RESULT', {}).get('SEARCH', {}).get('srp_isCoupick') else None,  # [Dynamic|수집완료] COU_PICK 여부
                'sdp.sub.discount': '0.0',                         # [Fixed] 고정값
                'sdp.sub.price': '0',                              # [Fixed] 고정값
                'sdp.previousViewType': context.get('RESULT', {}).get('SEARCH', {}).get('searchViewType', 'GRID_2'),  # [Dynamic|수집완료] ← RESULT.SEARCH.searchViewType
                'KEY_PRODUCT_ID': context.get('RESULT', {}).get('ROOT', {}).get('productId'),              # [Dynamic|수집완료] ← RESULT.ROOT.productId
                'KEY_THUMBNAIL_IMAGE': context.get('RESULT', {}).get('SEARCH', {}).get('srp_imageUrl'),    # [Dynamic|수집완료] ← RESULT.SEARCH.srp_imageUrl
                'KEY_SALE_PRICE': context.get('RESULT', {}).get('SEARCH', {}).get('srp_finalPrice', '26,990원'),  # [Dynamic|수집완료] ← RESULT.SEARCH.srp_finalPrice
                'KEY_RATING_COUNT': context.get('RESULT', {}).get('SEARCH', {}).get('srp_ratingCount', '(1)'),    # [Dynamic|수집완료] ← RESULT.SEARCH.srp_ratingCount
                'KEY_SIMILAR_SEARCH_KEYWORD_TYPE': context.get('RESULT', {}).get('ROOT', {}).get('keywordType', 'FOOD'),  # [Dynamic|수집완료] ← RESULT.ROOT.keywordType
                'sdp.productImageScaleType': context.get('RESULT', {}).get('SEARCH', {}).get('srp_scaleType', 'FIT_CENTER'),  # [Dynamic|수집완료] ← RESULT.SEARCH.srp_scaleType
                'KEY_ITEM_PRODUCT_ID': context.get('RESULT', {}).get('ROOT', {}).get('itemProductId', '4'),  # [Dynamic|수집완료] ← RESULT.ROOT.itemProductId
                'KEY_RATING_AVERAGE': context.get('RESULT', {}).get('SEARCH', {}).get('srp_ratingAverage', '4.0'),  # [Dynamic|수집완료] ← RESULT.SEARCH.srp_ratingAverage
                'sdp.o.price': context.get('RESULT', {}).get('SEARCH', {}).get('srp_originalPrice', '32,000원'),  # [Dynamic|수집완료] ← RESULT.SEARCH.srp_originalPrice
                'KEY_PRODUCT_NAME': context.get('RESULT', {}).get('SEARCH', {}).get('srp_productName'),     # [Dynamic|수집완료] ← RESULT.SEARCH.srp_productName
                'KEY_FILTER_KEY': context.get('RESULT', {}).get('SEARCH', {}).get('filterKey', ''),         # [Dynamic|수집가능] ← RESULT.SEARCH.filterKey
                'sdp.egiftPromotion': 'false',                     # [Fixed] 고정값
                'KEY_SEARCH_COUNT': str(context.get('RESULT', {}).get('ROOT', {}).get('searchCount', '0')),  # [Dynamic|수집완료] ← RESULT.ROOT.searchCount
                'sdp.discount': context.get('RESULT', {}).get('SEARCH', {}).get('srp_discountRate', '15%'),  # [Dynamic|수집완료] ← RESULT.SEARCH.srp_discountRate
                'KEY_ITEM_ID': context.get('RESULT', {}).get('ROOT', {}).get('itemId'),                     # [Dynamic|수집완료] ← RESULT.ROOT.itemId
                'sdp.previousActivity': 'SearchRedesignActivity',  # [Fixed] 고정값
                'KEY_VENDOR_ITEM_ID': context.get('RESULT', {}).get('ROOT', {}).get('vendorItemId'),        # [Dynamic|수집완료] ← RESULT.ROOT.vendorItemId
                'sdp.toggleViewType': 'srp_grid',                  # [Fixed] 고정값
                'KEY_RANK': str(context.get('RESULT', {}).get('SEARCH', {}).get('srp_rank', '0')),          # [Dynamic|수집완료] ← RESULT.SEARCH.srp_rank
                'KEY_SEARCH_RANK': str(int(context.get('RESULT', {}).get('SEARCH', {}).get('srp_rank', '0') or '0') + 1),  # [Dynamic|수집완료] rank + 1 (1-based)
                'KEY_SEARCH_KEYWORD': context.get('INPUT', {}).get('q'),                                    # [Dynamic|수집완료] ← INPUT.q
                'KEY_SEARCH_ID': context.get('RESULT', {}).get('ROOT', {}).get('searchId'),                 # [Dynamic|수집완료] ← RESULT.ROOT.searchId
                'sdp.mvp': '11',                                   # [Fixed] 고정값
                'KEY_SOURCE_TYPE': 'search'                        # [Fixed] 고정값
            }
        },
        # ============================================================
        # Schema 9453: FrameRenderingMetric (프레임 렌더링 성능)
        # Source: smali_classes2/com/coupang/mobile/monitoring/schema/FrameRenderingMetric.smali
        # 용도: 화면 렌더링 성능 모니터링 (서버측 필수 아님)
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 9453,
                'schemaVersion': 2
            },
            'data': {
                'domain': 'AMP',                  # [Fixed] 고정값
                'logCategory': 'system',          # [Fixed] 고정값
                'logType': 'performance',         # [Fixed] 고정값
                # --------------------------------------------------------
                # [Dynamic] 수집불가: 앱 내부 렌더링 성능 측정
                # 원리: 앱이 UI 렌더링 시 프레임 카운트/시간 측정
                # 현재: 하드코딩 (성능 시뮬레이션용)
                # --------------------------------------------------------
                'pageName': 'domain.search.presentation.view.search.SearchRedesignActivity(SearchFragment)',  # [Dynamic|수집불가] 페이지명
                'eventName': 'frame_rendering_metric',  # [Fixed] 고정값
                'totalFrameCount': 262,           # [Dynamic|수집불가] 전체 프레임 수
                'totalSlowFrameCount': 150,       # [Dynamic|수집불가] 느린 프레임 수
                'totalFrozenFrameCount': 0,       # [Dynamic|수집불가] 멈춘 프레임 수
                'isTotalSlow': True,              # [Dynamic|수집불가] 전체 느림 여부
                'totalAverageRenderingTime': 28,  # [Dynamic|수집불가] 평균 렌더링 시간(ms)
                'idleFrameCount': 262,            # [Dynamic|수집불가] 유휴 프레임 수
                'idleSlowFrameCount': 150,        # [Dynamic|수집불가] 유휴 느린 프레임 수
                'idleFrozenFrameCount': 0,        # [Dynamic|수집불가] 유휴 멈춘 프레임 수
                'isIdleSlow': True,               # [Dynamic|수집불가] 유휴 느림 여부
                'isIdleFrozen': False,            # [Dynamic|수집불가] 유휴 멈춤 여부
                'idleAverageRenderingTime': 28,   # [Dynamic|수집불가] 유휴 평균 렌더링 시간
                'scrollFrameCount': 0,            # [Dynamic|수집불가] 스크롤 프레임 수
                'scrollSlowFrameCount': 0,        # [Dynamic|수집불가] 스크롤 느린 프레임 수
                'scrollFrozenFrameCount': 0,      # [Dynamic|수집불가] 스크롤 멈춘 프레임 수
                'isScrollSlow': None,             # [Dynamic|수집불가] 스크롤 느림 여부
                'isScrollFrozen': None,           # [Dynamic|수집불가] 스크롤 멈춤 여부
                'scrollAverageRenderingTime': None,  # [Dynamic|수집불가] 스크롤 평균 렌더링 시간
                'startTimeStamp': 1767976287501,  # [Dynamic|수집불가] 시작 타임스탬프
                'endTimeStamp': 1767976316727,    # [Dynamic|수집불가] 종료 타임스탬프
                'maximumFPS': None,               # [Dynamic|수집불가] 최대 FPS
                'applicationId': 'com.coupang.mobile',  # [Fixed] 고정값
                'deviceName': context.get('DEVICE', {}).get('model', 'SM-A165N'),  # [Dynamic|수집완료] ← DEVICE.model
                'buildType': 'prod',              # [Fixed] 고정값
                'osType': 'ANDROID',              # [Fixed] 고정값
                'sourceUserAgent': context.get('DEVICE', {}).get('coupangAppHeader', ''),  # [Dynamic|DEVICE확장] UA 전체 ← context.DEVICE.coupangAppHeader
                'networkType': 'wifi',            # [Dynamic|DEVICE확장] 네트워크 타입
                'isTotalFrozen': False,           # [Dynamic|수집불가] 전체 멈춤 여부
                'screenType': None,               # [Dynamic|수집불가] 화면 타입
                'screenName': 'SearchFragment'    # [Fixed] 화면명
            },
            'extra': {}
        },
        # ============================================================
        # Schema 152: SrpProductRankingImpression (검색 순위 노출)
        # Source: smali_classes18/com/coupang/mobile/domain/search/monitoring/schema/SrpProductRankingImpression.smali
        # 용도: 검색 결과 순위 노출 로깅
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 152,
                'schemaVersion': 4
            },
            'data': {
                'domain': 'srp',                  # [Fixed] 고정값
                'logCategory': 'impression',      # [Fixed] 고정값
                'logType': 'impression',          # [Fixed] 고정값
                'pageName': 'srp',                # [Fixed] 고정값
                'eventName': 'impression_ranking',  # [Fixed] 고정값
                'domainType': 'SRP',              # [Fixed] 고정값
                # --------------------------------------------------------
                # [Dynamic] 수집완료: 검색 관련 정보
                # --------------------------------------------------------
                'searchId': f"{context.get('RESULT', {}).get('ROOT', {}).get('searchId')}:{context.get('RESULT', {}).get('SEARCH', {}).get('srp_rank', 0)}",  # [Fixed] searchId:rank
                'q': context.get('INPUT', {}).get('q'),  # [Dynamic|수집완료] ← INPUT.q
                'totalCount': context.get('RESULT', {}).get('ROOT', {}).get('searchCount'),  # [Dynamic|수집완료] ← RESULT.ROOT.searchCount
                # --------------------------------------------------------
                # [Dynamic] 수집가능: 현재 노출 순위
                # 원리: 스크롤 위치에 따라 현재 노출 중인 상품 순위
                # --------------------------------------------------------
                'rank': int(context.get('RESULT', {}).get('SEARCH', {}).get('srp_rank', 0)),  # [Dynamic|수집완료] 현재 노출 순위 ← RESULT.SEARCH.srp_rank
                'recommendationCount': None,      # [Dynamic|수집불가] 추천 수
                'channel': 'user',                # [Dynamic|수집가능] 검색 채널
                'subChannel': None,               # [Dynamic|수집불가] 서브채널
                'sourceType': None                # [Dynamic|수집불가] 소스타입
            },
            'extra': {}
        },
        # ============================================================
        # Schema 11942: AbTestExposureLog (A/B 테스트 노출)
        # Source: smali_classes5/com/coupang/mobile/commonui/gnb/schema/AbTestExposureLog.smali
        # 용도: A/B 테스트 노출 로깅 (중요)
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 11942,
                'schemaVersion': 6
            },
            # --------------------------------------------------------
            # [Bypass] 수집완료: 128에서 전체 추출하여 META에 저장
            # 원리: traverse_and_log_schemas()로 API 응답에서 추출
            # 경로: RESULT.META.SEARCH.11942_6
            # --------------------------------------------------------
            'data': context.get('RESULT', {}).get('META', {}).get('SEARCH', {}).get('11942_6', {}).get('data', {}),  # [Bypass|수집완료] ← RESULT.META.SEARCH
            'extra': {}
        }
    ]

    # Apply dynamic injection with timestamp jitter
    base_time = datetime.datetime.now()
    for item in body:
        # Add 1-5ms offset
        offset_ms = random.randint(1, 5)
        base_time += datetime.timedelta(milliseconds=offset_ms)
        item['common']['eventTime'] = base_time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "+0900"


    return run_request(session, method, url, headers, body)
