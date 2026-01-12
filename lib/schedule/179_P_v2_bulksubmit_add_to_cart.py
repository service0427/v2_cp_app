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


# Reference Data Index: 178
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

    # Prepare ATC Schemas from explicit extraction (Handlebar priority)
    atc_schemas = context.get('RESULT', {}).get('PRODUCT', {}).get('sdp_atc_click_schemas', [])
    
    def get_schema_from_list(schemas, target_id):
        for s in schemas:
            s_id = str(s.get('id', ''))
            if not s_id: s_id = str(s.get('schemaId', ''))
            if s_id == str(target_id):
                return s
        return None

    schema_10 = get_schema_from_list(atc_schemas, 10)
    schema_11599 = get_schema_from_list(atc_schemas, 11599)

    schema_10 = get_schema_from_list(atc_schemas, 10)
    schema_11599 = get_schema_from_list(atc_schemas, 11599)

    # [Patch] Schema 10 Preparation
    schema_10_data = (schema_10.get('mandatory', {}) if schema_10 else context.get('RESULT', {}).get('META', {}).get('PRODUCT', {}).get('10_77', {}).get('data', {})).copy()

    # Fix widget name mismatch: handlebar -> bottom_button (if capture dictates)
    if schema_10_data.get('currentWidget') == 'handlebar':
         schema_10_data['currentWidget'] = 'bottom_button'

    # Fix toggleViewType: search -> srp_grid (ATC 액션에 적합한 값)
    if schema_10_data.get('toggleViewType') == 'search':
         schema_10_data['toggleViewType'] = 'srp_grid'

    # [Patch] Schema 11599 Preparation
    schema_11599_data = (schema_11599.get('mandatory', {}) if schema_11599 else context.get('RESULT', {}).get('META', {}).get('PRODUCT', {}).get('11599_4', {}).get('data', {})).copy()

    # Fix sdpHandlerClickType: cancel -> add_to_cart (장바구니 담기 액션)
    if schema_11599_data.get('sdpHandlerClickType') == 'cancel':
         schema_11599_data['sdpHandlerClickType'] = 'add_to_cart'

    body = [
        # ============================================================
        # Schema 15989: PageInteraction (페이지 인터랙션)
        # Source: smali_classes2/com/coupang/mobile/implicitlogging/PageInteraction.smali
        # 용도: SDP 페이지 내 사용자 인터랙션 로깅
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 15989,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'sdp',                  # [Fixed] SDP 페이지
                'logCategory': 'event',           # [Fixed] 고정값
                'logType': 'processing',          # [Fixed] 고정값
                'pageName': 'sdp',                # [Fixed] SDP 페이지
                'eventName': 'page_interact'      # [Fixed] 고정값
            },
            'extra': {
                'pvid': context.get('RESULT', {}).get('SEARCH', {}).get('srp_pvId')  # [Dynamic|수집완료] ← RESULT.SEARCH.srp_pvId
            }
        },
        # ============================================================
        # Schema 10: SdpAddToCart (장바구니 담기 - 핵심)
        # Source: smali_classes4/com/coupang/mobile/commonui/widget/schema/SdpAddToCart.smali
        # 용도: 장바구니 담기 버튼 클릭 로깅 (가장 중요)
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 10,
                'schemaVersion': 77
            },
            # --------------------------------------------------------
            # [Bypass] 수집완료: 145에서 선택된 버튼(Handlebar)의 스키마 우선 사용
            # 원리: 145_G에서 sdp_atc_click_schemas에 추출된 정확한 스키마 사용
            # Fallback: RESULT.META.PRODUCT (기존 로직)
            # --------------------------------------------------------
            # --------------------------------------------------------
            # [Bypass] 수집완료: 145에서 선택된 버튼(Handlebar)의 스키마 우선 사용
            # 원리: 145_G에서 sdp_atc_click_schemas에 추출된 정확한 스키마 사용
            # Fallback: RESULT.META.PRODUCT (기존 로직)
            # Patch: currentWidget Name Alignment (handlebar -> bottom_button)
            # --------------------------------------------------------
            'data': schema_10_data,
            'extra': {
                'eventReferrer': 'sdp_click_duration',  # [Dynamic|관리필요] 이벤트 참조자
                'currentView': '/search_list'     # [Dynamic|관리필요] 이전 뷰 경로
            }
        },
        # ============================================================
        # Schema 11599: QuantityPickerLogging (수량 선택 로깅)
        # Source: smali_classes18/com/coupang/mobile/domain/sdp/util/QuantityPickerLoggingListener.smali
        # 용도: 수량 선택 시 로깅
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 11599,
                'schemaVersion': 4
            },
            # --------------------------------------------------------
            # [Bypass] 수집완료: 145에서 선택된 버튼(Handlebar)의 스키마 우선 사용
            # 원리: 145_G에서 sdp_atc_click_schemas에 추출된 정확한 스키마 사용
            # Fallback: RESULT.META.PRODUCT (기존 로직)
            # --------------------------------------------------------
            'data': schema_11599_data,  
            'extra': {
                'eventReferrer': 'add_to_cart',   # [Dynamic|관리필요] 이벤트 참조자
                'currentView': '/search_list'     # [Dynamic|관리필요] 이전 뷰 경로
            }
        },
        # ============================================================
        # Schema 14044: ImplicitClick (암묵적 클릭 로깅)
        # Source: smali_classes22/com/coupang/mobile/implicitlogging/ImplicitClick.smali
        # 용도: 버튼 클릭 상세 로깅
        # ============================================================
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 14044,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'sdp',                  # [Fixed] SDP 페이지
                'logCategory': 'event',           # [Fixed] 고정값
                'logType': 'click',               # [Fixed] 고정값
                'pageName': 'sdp',                # [Fixed] SDP 페이지
                'eventName': '',                  # [Fixed] 고정값 (빈값)
                # --------------------------------------------------------
                # [Dynamic] 수집완료: 페이지뷰 ID
                # --------------------------------------------------------
                'pvid': context.get('RESULT', {}).get('SEARCH', {}).get('srp_pvId'),  # [Dynamic|수집완료] ← RESULT.SEARCH.srp_pvId
                # --------------------------------------------------------
                # [Dynamic] 수집가능: SDP API 응답에서 추출 가능
                # 원리: 145에서 SDP API 응답 파싱 시 추가 필드 추출
                # --------------------------------------------------------
                'traceId': context.get('RESULT', {}).get('PRODUCT', {}).get('sdp_traceId', '3bc42af30268f9137afa534259b804e3'),  # [Dynamic|수집가능] ← RESULT.PRODUCT.sdp_traceId
                'serverTime': int(datetime.datetime.now().timestamp() * 1000),  # [Dynamic|수집가능] ← RESULT.PRODUCT.sdp_serverTime
                # --------------------------------------------------------
                # [Fixed] 하드코딩: 장바구니 버튼 고정 정보
                # --------------------------------------------------------
                'widgetName': 'SECTION_ATF_BOTTOM_BUTTONS',  # [Fixed] 위젯명 (ATF = Above The Fold)
                'sectionName': None,              # [Fixed] 섹션명 (null)
                'componentName': 'BOTTOM_BUTTON', # [Fixed] 컴포넌트명
                'checked': False                  # [Fixed] 체크 여부
            },
            'extra': {
                'widgetId': '',                   # [Fixed] 위젯 ID (빈값)
                'id': '장바구니 담기',             # [Fixed] 버튼 라벨
                'index': 0,                       # [Fixed] 인덱스
                'eventReferrer': 'handler_click'  # [Fixed] 이벤트 참조자
            }
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
