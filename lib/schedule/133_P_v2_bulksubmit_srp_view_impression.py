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
                # [Dynamic] 수집가능: SRP API rData.entityList 분석
                # 원리: entityList 순회하며 entity.type별 개수 집계
                # 현재: 하드코딩 (앱 내부 파싱 결과)
                # --------------------------------------------------------
                'widgetTotalCount': 30,         # [Dynamic|수집가능] entityList.length
                'widgetTypeCount': 3,           # [Dynamic|수집가능] unique(entity.type).length
                'widgetDistribution': '{"DYNAMIC_TEMPLATE":3,"U_WIDGET":26,"AB_TRACKING":1}',  # [Dynamic|수집가능] JSON.stringify(typeCount)
                'analyzeDuration': 2            # [Dynamic|수집불가] 앱 내부 파싱 시간, 랜덤 1~10ms 대체
            },
            'extra': {}
        },
        # ============================================================
        # Schema 9854: CommonCheckingAbnormalApi (에러 로깅 - TOP)
        # Source: smali_classes5/com/coupang/mobile/common/logger/internal/schema/CommonCheckingAbnormalApi.smali
        # 용도: 앱 내부 API 에러 감지 로그 (서버측 필수 아님)
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 9854,
                'schemaVersion': 2
            },
            'data': {
                'domain': 'search',             # [Fixed] 고정값
                'logCategory': 'system',        # [Fixed] 고정값
                'logType': 'error',             # [Fixed] 고정값
                'pageName': 'search',           # [Fixed] 고정값
                'eventName': 'abnormal_api',    # [Fixed] 고정값
                # --------------------------------------------------------
                # [Dynamic] 수집불가: 앱 내부 에러 감지 로직
                # 원리: 앱이 API 응답 파싱 중 에러 발생 시 생성
                # 현재: 하드코딩 (에러 시뮬레이션용)
                # --------------------------------------------------------
                'abnormalLevel': 'component',   # [Dynamic|수집불가] 앱 내부 에러 레벨
                'abnormalSubLevel': 'title',    # [Dynamic|수집불가] 앱 내부 에러 서브레벨
                'requestParam': None,           # [Dynamic|수집불가] 요청 파라미터
                'requestURL': 'https://cmapi.coupang.com/v3/products',  # [Fixed] 고정 URL
                'fullRequestURL': context.get('RESULT', {}).get('SEARCH', {}).get('SEARCH_URL')  # [Dynamic|수집완료] ← RESULT.SEARCH.SEARCH_URL
            },
            'extra': {
                # --------------------------------------------------------
                # [Dynamic] 수집불가: 앱 내부 에러 상세 정보
                # --------------------------------------------------------
                'errorType': 'DYNAMIC_TEMPLATE',              # [Dynamic|수집불가] 에러 타입
                'viewType': 'SRP_TOP_DYNAMIC_TEMPLATE',       # [Dynamic|수집불가] 에러 발생 위치
                'errorMessage': 'APP_SRP_TOP_BANNER: variableMap',  # [Dynamic|수집불가] 에러 메시지
                'vendorItemIds': ['']                         # [Dynamic|수집불가] 관련 상품 ID
            }
        },
        # ============================================================
        # Schema 9854: CommonCheckingAbnormalApi (에러 로깅 - MID)
        # Source: 위와 동일
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 9854,
                'schemaVersion': 2
            },
            'data': {
                'domain': 'search',             # [Fixed] 고정값
                'logCategory': 'system',        # [Fixed] 고정값
                'logType': 'error',             # [Fixed] 고정값
                'pageName': 'search',           # [Fixed] 고정값
                'eventName': 'abnormal_api',    # [Fixed] 고정값
                'abnormalLevel': 'component',   # [Dynamic|수집불가] 앱 내부 에러 레벨
                'abnormalSubLevel': 'title',    # [Dynamic|수집불가] 앱 내부 에러 서브레벨
                'requestParam': None,           # [Dynamic|수집불가] 요청 파라미터
                'requestURL': 'https://cmapi.coupang.com/v3/products',  # [Fixed] 고정 URL
                'fullRequestURL': context.get('RESULT', {}).get('SEARCH', {}).get('SEARCH_URL')  # [Dynamic|수집완료] ← RESULT.SEARCH.SEARCH_URL
            },
            'extra': {
                'errorType': 'DYNAMIC_TEMPLATE',              # [Dynamic|수집불가] 에러 타입
                'viewType': 'SRP_MID_DYNAMIC_TEMPLATE',       # [Dynamic|수집불가] 에러 발생 위치 (MID)
                'errorMessage': 'APP_SRP_MID_BANNER: variableMap',  # [Dynamic|수집불가] 에러 메시지
                'vendorItemIds': ['']                         # [Dynamic|수집불가] 관련 상품 ID
            }
        },
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
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 116,
                'schemaVersion': 23
            },
            'data': {
                'domain': 'srp',                  # [Fixed] 고정값
                'logCategory': 'view',            # [Fixed] 고정값
                'logType': 'page',                # [Fixed] 고정값
                'pageName': 'srp',                # [Fixed] 고정값
                'eventName': None,                # [Fixed] 고정값 (null)
                # --------------------------------------------------------
                # [Dynamic] 수집완료: 검색 관련 필수 정보
                # --------------------------------------------------------
                'q': context.get('INPUT', {}).get('q'),                           # [Dynamic|수집완료] ← INPUT.q
                'searchId': context.get('RESULT', {}).get('ROOT', {}).get('searchId'),            # [Dynamic|수집완료] ← RESULT.ROOT.searchId
                'searchCount': context.get('RESULT', {}).get('ROOT', {}).get('searchCount'),      # [Dynamic|수집완료] ← RESULT.ROOT.searchCount (rData.totalCount)
                'keywordType': context.get('RESULT', {}).get('ROOT', {}).get('keywordType'),      # [Dynamic|수집완료] ← RESULT.ROOT.keywordType (128에서 추출)
                'ixid': context.get('DEVICE', {}).get('ixid'),                     # [Dynamic|수집완료] ← DEVICE.ixid
                # --------------------------------------------------------
                # [Dynamic] 수집가능: SRP API 응답에서 추출 가능
                # 원리: rData 파싱 시 추가 필드 추출
                # --------------------------------------------------------
                'channel': 'user',                # [Dynamic|수집가능] API 요청 파라미터 EXTRAS:channel/user
                'filterKeys': '',                 # [Dynamic|수집가능] rData.filterKey (미적용시 빈값)
                'filterType': '',                 # [Dynamic|수집가능] rData.filterType (미적용시 빈값)
                'isCoupick': context.get('RESULT', {}).get('SEARCH', {}).get('isCoupick', False),                   # [Dynamic|수집완료] 128_G에서 추출
                'rankOfCoupick': context.get('RESULT', {}).get('SEARCH', {}).get('rankOfCoupick', -1),              # [Dynamic|수집완료] 128_G에서 추출
                'brandId': None,                  # [Dynamic|수집가능] 브랜드 검색 시 brandId
                # --------------------------------------------------------
                # [Dynamic] DEVICE 확장 필요: 디바이스 정보 추가 수집
                # 원리: DEVICE 객체에 dpi, fontScale 등 추가
                # --------------------------------------------------------
                'dpi': '450',                     # [Dynamic|DEVICE확장] DEVICE.dpi
                'deviceFontScale': '1.0',         # [Dynamic|DEVICE확장] DEVICE.fontScale
                'appliedFontScale': '1.0',        # [Dynamic|DEVICE확장] DEVICE.appliedFontScale
                'systemFontScale': '1.0',         # [Dynamic|DEVICE확장] DEVICE.systemFontScale
                # --------------------------------------------------------
                # [Dynamic] 앱설정: 사용자 앱 설정값 (기본값 유지)
                # --------------------------------------------------------
                'searchViewType': context.get('RESULT', {}).get('SEARCH', {}).get('searchViewType', 'GRID_2'),       # [Dynamic|수집완료] 128_G에서 추출
                'turnoffAutosave': False,         # [Dynamic|앱설정] 자동저장 끄기 여부
                # --------------------------------------------------------
                # [Dynamic] 관리필요: 네비게이션 경로 관리
                # 원리: context에 navigationHistory 필드 추가
                # --------------------------------------------------------
                'previousPage': None,             # [Dynamic|관리필요] 이전 페이지 경로
                'referralPage': None,             # [Dynamic|관리필요] 레퍼럴 페이지 경로
                # --------------------------------------------------------
                # [Dynamic] 수집불가: 앱 내부 상태/A/B 테스트
                # --------------------------------------------------------
                'isGenderTabTest': False,         # [Dynamic|수집불가] 성별탭 A/B 테스트
                'hasSeeOtherRocketItem': None,    # [Dynamic|수집불가] 앱 내부 UI 상태
                'isFromRecoHintKeyword': False,   # [Dynamic|수집불가] 추천 힌트 키워드 여부
                'isCcidPriceSelect': None,        # [Dynamic|수집불가] CCID 가격 선택 여부
                'multiImageItemIds': None,        # [Dynamic|수집불가] 멀티이미지 상품 ID
                'hasProdWColorChips': False,      # [Dynamic|수집불가] 컬러칩 여부
                'hasProdWColorTexts': False,      # [Dynamic|수집불가] 컬러텍스트 여부
                'hasProdOTLink': False,           # [Dynamic|수집불가] OT 링크 여부
                'subChannel': None,               # [Dynamic|수집불가] 서브채널
                'sourceType': None,               # [Dynamic|수집불가] 소스타입
                'selectedTheme': None,            # [Dynamic|수집불가] 선택된 테마
                'subSourceType': None,            # [Dynamic|수집불가] 서브소스타입
                'channelPremium': None,           # [Dynamic|수집불가] 프리미엄 채널
                'midFilterKeys': None,            # [Dynamic|수집불가] 미드필터 키
                # --------------------------------------------------------
                # [Dynamic] 로그인필요: 로그인 상태에서만 확인 가능
                # --------------------------------------------------------
                'isLoyaltyMember': False,         # [Dynamic|로그인필요] 와우 멤버십 여부
                'rank': None,                     # [Dynamic|수집불가] 순위
                # --------------------------------------------------------
                # [Dynamic] 외부SDK: 외부 SDK 연동 필요 (수집 불가)
                # --------------------------------------------------------
                'ga': None,                       # [Dynamic|외부SDK] Google Analytics ID
                'fbc': None,                      # [Dynamic|외부SDK] Facebook Click ID
                'fbp': None                       # [Dynamic|외부SDK] Facebook Pixel ID
            },
            'extra': {
                # --------------------------------------------------------
                # [Dynamic] 수집완료/DEVICE확장
                # --------------------------------------------------------
                'parentView': '/home',            # [Dynamic|관리필요] 부모 뷰 경로
                'pvId': context.get('RESULT', {}).get('SEARCH', {}).get('srp_pvId'),                    # [Dynamic|수집완료] ← RESULT.SEARCH.srp_pvId
                'dpi': 'XHDPI'                    # [Dynamic|DEVICE확장] DPI 레벨 (LDPI/MDPI/HDPI/XHDPI/XXHDPI)
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
