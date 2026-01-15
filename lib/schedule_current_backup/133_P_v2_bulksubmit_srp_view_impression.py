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

# Reference Data Index: 132
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '10621',
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
        'user-agent': 'okhttp/4.9.3'
    }

    if not context: context = {}

    body = [
        # ============================================================
        # Schema 17211: TtiWidgetMonitorLog (위젯 모니터링)
        # Source: smali_classes5/com/coupang/mobile/commonui/filter/tti/schema/TtiWidgetMonitorLog.smali
        # APK ParseTimeInterceptor.e() 메서드 로직 기반 동적 계산
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 17211,
                'schemaVersion': 2
            },
            'data': {
                'domain': 'srp',                # [Fixed] 고정값
                'logCategory': 'system',        # [Fixed] 고정값
                'logType': 'debug',             # [Fixed] 고정값
                'pageName': None,               # [Fixed] 고정값 (null)
                'eventName': None,              # [Fixed] 고정값 (null)
                # --------------------------------------------------------
                # [Dynamic] 수집완료: 128에서 calculate_widget_stats()로 계산
                # 원리: entityList 순회하며 commonViewType별 개수 집계
                # 경로: RESULT.SEARCH.widgetTotalCount/widgetTypeCount/widgetDistribution
                # --------------------------------------------------------
                'widgetTotalCount': context.get('RESULT', {}).get('SEARCH', {}).get('widgetTotalCount', 0),      # [Dynamic|수집완료] ← RESULT.SEARCH
                'widgetTypeCount': context.get('RESULT', {}).get('SEARCH', {}).get('widgetTypeCount', 0),        # [Dynamic|수집완료] ← RESULT.SEARCH
                'widgetDistribution': context.get('RESULT', {}).get('SEARCH', {}).get('widgetDistribution', '{}'),  # [Dynamic|수집완료] ← RESULT.SEARCH
                'analyzeDuration': random.randint(1, 10)  # [Dynamic] 앱 내부 파싱 시간, 랜덤 1~10ms
            },
            'extra': {}
        },
        # ============================================================
        # ============================================================
        # Schema 9854: CommonCheckingAbnormalApi (Dynamic Extraction)
        # Source: smali_classes5/com/coupang/mobile/common/logger/internal/schema/CommonCheckingAbnormalApi.smali
        # App internal error logging for Dynamic Templates (SRP_TOP, SRP_MID, etc.)
        # ============================================================
        *[
            {
                'common': generate_common_payload(context),
                'meta': {
                    'schemaId': 9854,
                    'schemaVersion': 2
                },
                'data': {
                    'domain': 'search',
                    'logCategory': 'system',
                    'logType': 'error',
                    'pageName': 'search',
                    'eventName': 'abnormal_api',
                    'abnormalLevel': 'component',
                    'abnormalSubLevel': 'title',
                    'requestParam': None,
                    'requestURL': 'https://cmapi.coupang.com/v3/products',
                    # [Dynamic] fullRequestURL from SEARCH result
                    'fullRequestURL': context.get('RESULT', {}).get('SEARCH', {}).get('SEARCH_URL')
                },
                'extra': {
                    'errorType': 'DYNAMIC_TEMPLATE',
                    'viewType': t['viewType'],
                    # Error Message format: APP_{placementName}: variableMap
                    'errorMessage': f"APP_{t['placementName']}: variableMap",
                    'vendorItemIds': ['']
                }
            }
            for t in context.get('RESULT', {}).get('SEARCH', {}).get('dynamic_templates', [])
        ],
        # ============================================================
        # Schema 11965: CspUnavailableEvent (CSP 에러 이벤트)
        # Source: smali_classes5/com/coupang/mobile/common/abtest/schema/CspUnavailableEvent.smali
        # 용도: 앱 내부 렌더링 에러 로그 (서버측 필수 아님)
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 11965,
                'schemaVersion': 15
            },
            'data': {
                'domain': '-',                                # [Fixed] 고정값
                'logCategory': 'system',                      # [Fixed] 고정값
                'logType': 'error',                           # [Fixed] 고정값
                # --------------------------------------------------------
                # [Dynamic] 수집불가: 앱 내부 렌더링 에러 정보
                # 원리: 앱이 UI 렌더링 중 필요한 위젯 타입을 찾지 못할 때 발생
                # 현재: 하드코딩 (에러 시뮬레이션용)
                # --------------------------------------------------------
                'pageName': 'SearchFragment',                 # [Fixed] 페이지명 고정
                'eventName': 'product',                       # [Fixed] 이벤트명 고정
                'domainName': 'search',                       # [Fixed] 도메인명 고정
                'errorDescription': 'PRODUCT_VITAMIN Type is not exist',  # [Dynamic|수집불가] 앱 내부 에러
                'errorName': 'requiredViewTypeNotExist',      # [Dynamic|수집불가] 앱 내부 에러명
                'eventType': 'render',                        # [Fixed] 렌더링 이벤트
                'source': 'server',                           # [Fixed] 소스 = 서버
                'errorType': 'apiError'                       # [Fixed] API 에러
            },
            'extra': {}
        },
        # ============================================================
        # Schema 15704: SrpPaginationView (SRP 페이지 뷰 - 핵심)
        # Source: smali_classes18/com/coupang/mobile/domain/search/monitoring/schema/SrpPaginationView.smali
        # 용도: 검색 결과 페이지 노출 로깅 (중요)
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 15704,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'srp',                  # [Fixed] 고정값
                'logCategory': 'view',            # [Fixed] 고정값
                'logType': 'page',                # [Fixed] 고정값
                'pageName': 'srp',                # [Fixed] 고정값
                'eventName': 'srp_view_impression',  # [Fixed] 고정값
                # --------------------------------------------------------
                # [Dynamic] 수집완료: 검색 관련 필수 정보
                # --------------------------------------------------------
                'q': context.get('INPUT', {}).get('q'),                           # [Dynamic|수집완료] ← INPUT.q
                'searchId': context.get('RESULT', {}).get('ROOT', {}).get('searchId'),            # [Dynamic|수집완료] ← RESULT.ROOT.searchId (128에서 추출)
                'rootSearchId': context.get('RESULT', {}).get('ROOT', {}).get('searchId'),        # [Dynamic|수집완료] 첫 검색은 searchId와 동일
                # --------------------------------------------------------
                # [Dynamic] 관리필요: 페이지네이션 시 이전 searchId 저장
                # 원리: context에 previousSearchId 필드 추가하여 관리
                # --------------------------------------------------------
                'previousRootSearchId': ''        # [Dynamic|관리필요] 이전 검색 ID (첫 검색=빈값)
            },
            'extra': {}
        },
        # ============================================================
        # Schema 116: SrpPageView (SRP 상세 페이지 뷰 - 핵심)
        # Source: smali_classes18/com/coupang/mobile/domain/search/monitoring/schema/SrpPageView.smali
        # 용도: 검색 결과 페이지 상세 로깅 (가장 중요)
        # 필드 순서: 원본 캡처 기준 정렬
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 116,
                'schemaVersion': 23
            },
            'data': {
                # === 기본 메타 ===
                'domain': 'srp',
                'logCategory': 'view',
                'logType': 'page',
                'pageName': 'srp',
                'eventName': None,
                # === 검색 정보 (원본 순서) ===
                'q': context.get('INPUT', {}).get('q'),
                'channel': 'user',
                'filterKeys': '',
                'searchViewType': context.get('RESULT', {}).get('SEARCH', {}).get('searchViewType', 'GRID_2'),
                'searchId': context.get('RESULT', {}).get('ROOT', {}).get('searchId'),
                'searchCount': context.get('RESULT', {}).get('ROOT', {}).get('searchCount'),
                'isCoupick': context.get('RESULT', {}).get('SEARCH', {}).get('isCoupick', False),
                'rankOfCoupick': context.get('RESULT', {}).get('SEARCH', {}).get('rankOfCoupick', -1),
                'keywordType': context.get('RESULT', {}).get('ROOT', {}).get('keywordType', ''),
                # === A/B 테스트 & UI 상태 ===
                'isGenderTabTest': False,
                'hasSeeOtherRocketItem': None,
                'previousPage': None,
                'referralPage': None,
                'isFromRecoHintKeyword': False,
                'isCcidPriceSelect': None,
                'multiImageItemIds': None,
                # === 로그인/멤버십 ===
                'isLoyaltyMember': False,
                'rank': None,
                # === 디바이스 정보 ===
                'ixid': context.get('DEVICE', {}).get('ixid'),
                'dpi': context.get('DEVICE', {}).get('dpi', '450'),
                'deviceFontScale': '1.0',
                # === 컬러칩/UI 옵션 ===
                'hasProdWColorChips': False,
                'hasProdWColorTexts': False,
                'turnoffAutosave': False,
                'hasProdOTLink': False,
                # === 채널/소스 ===
                'subChannel': None,
                'sourceType': None,
                'selectedTheme': None,
                'subSourceType': None,
                'channelPremium': None,
                # === 필터 ===
                'filterType': '',
                'appliedFontScale': '1.0',
                'systemFontScale': '1.0',
                'midFilterKeys': None,
                # === 외부 SDK ===
                'ga': None,
                'fbc': None,
                'fbp': None,
                'brandId': None
            },
            'extra': {
                'parentView': '/home',
                'pvId': context.get('RESULT', {}).get('SEARCH', {}).get('srp_pvId'),
                'dpi': context.get('DEVICE', {}).get('dpi_level', 'XHDPI')
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
                # 원리: 앱 빌드 시 결정되는 고정값
                # --------------------------------------------------------
                'key': '59701',                   # [Hardcoded|수집불가] 기능 ID
                'value': 'AddImageToRecentKeywordUseCase'  # [Hardcoded|수집불가] UseCase명
            },
            'extra': {}
        },
        # ============================================================
        # Schema 11942: AbTestExposureLog (A/B 테스트 노출 #1)
        # Source: smali_classes5/com/coupang/mobile/commonui/gnb/schema/AbTestExposureLog.smali
        # 용도: A/B 테스트 노출 로깅 (중요)
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 11942,
                'schemaVersion': 8
            },
            'data': {
                'domain': 'srp',                  # [Fixed] 고정값
                'logCategory': 'impression',      # [Fixed] 고정값
                'logType': 'impression',          # [Fixed] 고정값
                'pageName': 'srp',                # [Fixed] 고정값
                'eventName': 'ab_test_exposure',  # [Fixed] 고정값
                # --------------------------------------------------------
                # [Dynamic] 수집완료: 검색 관련
                # --------------------------------------------------------
                'searchId': context.get('RESULT', {}).get('ROOT', {}).get('searchId'),            # [Dynamic|수집완료] ← RESULT.ROOT.searchId
                # --------------------------------------------------------
                # [Dynamic] 수집가능: A/B 테스트 정보
                # 원리: SRP API 응답의 bypass.extra.abTestIds/abGroups에서 추출
                # 128에서 첫번째만 추출중, 전체 리스트 저장하면 다중 로깅 가능
                # 현재: 하드코딩 (88343/B)
                # --------------------------------------------------------
                'abTestId': '88343',              # [Dynamic|수집가능] ← bypass.extra.abTestIds[0]
                'abGroup': 'B',                   # [Dynamic|수집가능] ← bypass.extra.abGroups[0]
                # --------------------------------------------------------
                # [Dynamic] SRP에서 null: 상품/세션 관련 (SDP에서 사용)
                # --------------------------------------------------------
                'productId': None,                # [Dynamic|SRP에서null] 상품 ID
                'itemId': None,                   # [Dynamic|SRP에서null] 아이템 ID
                'vendorItemId': None,             # [Dynamic|SRP에서null] 벤더아이템 ID
                'sdpVisitKey': None,              # [Dynamic|SRP에서null] SDP 방문키
                'extraAttribute': None,           # [Dynamic|SRP에서null] 추가 속성
                'cartSessionId': None,            # [Dynamic|SRP에서null] 장바구니 세션 ID
                'cartId': None,                   # [Dynamic|SRP에서null] 장바구니 ID
                'checkoutId': None,               # [Dynamic|SRP에서null] 결제 ID
                'categoryId': None,               # [Dynamic|SRP에서null] 카테고리 ID
                'categoryType': None,             # [Dynamic|SRP에서null] 카테고리 타입
                'campaignId': None,               # [Dynamic|SRP에서null] 캠페인 ID
                'toggleViewType': None,           # [Dynamic|SRP에서null] 토글뷰 타입
                'widgetPosition': None,           # [Dynamic|SRP에서null] 위젯 위치
                'subSourceType': None,            # [Dynamic|SRP에서null] 서브소스 타입
                'requestId': None,                # [Dynamic|SRP에서null] 요청 ID
                'q': None,                        # [Dynamic|SRP에서null] 검색어 (여기선 null)
                'exposureCase': None,             # [Dynamic|SRP에서null] 노출 케이스
                'premiumCategory': None,          # [Dynamic|SRP에서null] 프리미엄 카테고리
                'isBadDiscount': None,            # [Dynamic|SRP에서null] 불량 할인 여부
                'isNoDiscount': None              # [Dynamic|SRP에서null] 할인 없음 여부
            },
            'extra': {
                'domainName': 'SRP'               # [Fixed] 고정값
            }
        },
        # ============================================================
        # Schema 11942: AbTestExposureLog (A/B 테스트 노출 #2)
        # Source: 위와 동일
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 11942,
                'schemaVersion': 8
            },
            'data': {
                'domain': 'srp',                  # [Fixed] 고정값
                'logCategory': 'impression',      # [Fixed] 고정값
                'logType': 'impression',          # [Fixed] 고정값
                'pageName': 'srp',                # [Fixed] 고정값
                'eventName': 'ab_test_exposure',  # [Fixed] 고정값
                'searchId': context.get('RESULT', {}).get('ROOT', {}).get('searchId'),            # [Dynamic|수집완료] ← RESULT.ROOT.searchId
                # --------------------------------------------------------
                # [Dynamic] 수집가능: 두번째 A/B 테스트
                # 원리: abTestIds/abGroups 리스트의 두번째 값
                # 현재: 하드코딩 (88344/A)
                # --------------------------------------------------------
                'abTestId': '88344',              # [Dynamic|수집가능] ← bypass.extra.abTestIds[1]
                'abGroup': 'A',                   # [Dynamic|수집가능] ← bypass.extra.abGroups[1]
                'productId': None,                # [Dynamic|SRP에서null]
                'itemId': None,                   # [Dynamic|SRP에서null]
                'vendorItemId': None,             # [Dynamic|SRP에서null]
                'sdpVisitKey': None,              # [Dynamic|SRP에서null]
                'extraAttribute': None,           # [Dynamic|SRP에서null]
                'cartSessionId': None,            # [Dynamic|SRP에서null]
                'cartId': None,                   # [Dynamic|SRP에서null]
                'checkoutId': None,               # [Dynamic|SRP에서null]
                'categoryId': None,               # [Dynamic|SRP에서null]
                'categoryType': None,             # [Dynamic|SRP에서null]
                'campaignId': None,               # [Dynamic|SRP에서null]
                'toggleViewType': None,           # [Dynamic|SRP에서null]
                'widgetPosition': None,           # [Dynamic|SRP에서null]
                'subSourceType': None,            # [Dynamic|SRP에서null]
                'requestId': None,                # [Dynamic|SRP에서null]
                'q': None,                        # [Dynamic|SRP에서null]
                'exposureCase': None,             # [Dynamic|SRP에서null]
                'premiumCategory': None,          # [Dynamic|SRP에서null]
                'isBadDiscount': None,            # [Dynamic|SRP에서null]
                'isNoDiscount': None              # [Dynamic|SRP에서null]
            },
            'extra': {
                'domainName': 'SRP'               # [Fixed] 고정값
            }
        },
        # ============================================================
        # Schema 12636: (Bypass - 전체 동적 주입)
        # Source: Not Found - API 응답에서 직접 추출
        # 용도: 서버 제공 스키마 그대로 전송
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 12636,
                'schemaVersion': 1
            },
            # --------------------------------------------------------
            # [Bypass] 수집완료: 128에서 전체 추출하여 META에 저장
            # 원리: traverse_and_log_schemas()로 API 응답에서 추출
            # 경로: RESULT.META.SEARCH.12636_1
            # --------------------------------------------------------
            'data': context.get('RESULT', {}).get('META', {}).get('SEARCH', {}).get('12636_1', {}).get('data', {}),   # [Bypass|수집완료] ← RESULT.META.SEARCH
            'extra': context.get('RESULT', {}).get('META', {}).get('SEARCH', {}).get('12636_1', {}).get('extra', {})  # [Bypass|수집완료] ← RESULT.META.SEARCH
        }
    ]

    # Fix eventTime collision and apply dynamic injection
    base_time = datetime.datetime.now()

    for item in body:
        # Add 1-5ms offset
        offset_ms = random.randint(1, 5)
        base_time += datetime.timedelta(milliseconds=offset_ms)
        item['common']['eventTime'] = base_time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "+0900"


    return run_request(session, method, url, headers, body)
