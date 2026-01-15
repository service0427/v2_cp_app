"""
APK 기반 Click Search Product 스키마
=====================================

APK 분석 결과:
- bulksubmit은 세트가 아니라 타이밍 기반 (10개 OR 500ms)
- 각 스키마는 독립적으로 큐에 추가됨
- 필수 스키마만 전송하면 됨

핵심 스키마: 124 (SrpProductClick)
- eventName: click_search_product
- 용도: SRP에서 상품 클릭 시 로깅
"""

import datetime
import random
from curl_cffi import requests

from lib_apk.common.executor import run_request
from lib_apk.common.utils import generate_common_payload


def run(session: requests.Session, context: dict = None):
    """
    APK 기반 상품 클릭 로깅

    전송 스키마:
    1. Schema 124 (SrpProductClick) - 필수, 핵심
    """
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"

    headers = {
        'content-type': 'application/json; charset=utf-8',
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/4.9.3'
    }

    if not context:
        context = {}

    # ============================================================
    # Schema 124: SrpProductClick
    # APK: smali_classes18/com/coupang/mobile/domain/search/monitoring/schema/SrpProductClick.smali
    # ID: 124, Version: 38
    # Fixed: logCategory=event, logType=click, eventName=click_search_product
    # ============================================================

    # Bypass 스키마 우선 사용 (서버가 제공한 템플릿)
    bypass_124 = context.get('srp_click_log_bypass', {})
    fallback_124 = context.get('RESULT', {}).get('META', {}).get('SEARCH', {}).get('124_53', {})

    # data 필드 구성
    schema_124_data = (bypass_124.get('mandatory') or fallback_124.get('data') or {}).copy()

    # 필수 필드 주입 (commonBypassLogParams.mandatory에서)
    bypass_mandatory = context.get('srp_bypass_mandatory', {})

    # APK 분석: 클라이언트가 bypass 템플릿의 빈 필드를 mandatory에서 채움
    if not schema_124_data.get('q'):
        schema_124_data['q'] = bypass_mandatory.get('q') or context.get('INPUT', {}).get('q')

    if not schema_124_data.get('internalCategoryId') or schema_124_data.get('internalCategoryId') == '':
        schema_124_data['internalCategoryId'] = bypass_mandatory.get('internalCategoryId') or \
            context.get('RESULT', {}).get('SEARCH', {}).get('internalCategoryId', '')

    if not schema_124_data.get('id'):
        schema_124_data['id'] = bypass_mandatory.get('id') or \
            context.get('RESULT', {}).get('ROOT', {}).get('productId')

    if not schema_124_data.get('itemProductId'):
        schema_124_data['itemProductId'] = bypass_mandatory.get('itemProductId') or \
            context.get('RESULT', {}).get('ROOT', {}).get('itemProductId', '4')

    if not schema_124_data.get('searchViewType'):
        schema_124_data['searchViewType'] = context.get('RESULT', {}).get('SEARCH', {}).get('searchViewType', 'GRID_2')

    if not schema_124_data.get('rank'):
        schema_124_data['rank'] = bypass_mandatory.get('searchRank') or \
            context.get('RESULT', {}).get('SEARCH', {}).get('srp_rank')

    print(f"[147_APK] Schema 124: q={schema_124_data.get('q')}, id={schema_124_data.get('id')}, rank={schema_124_data.get('rank')}")

    body = [
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 124,
                'schemaVersion': 53  # 서버 버전 사용 (APK는 38이지만 서버는 53)
            },
            'data': schema_124_data,
            'extra': {
                **(bypass_124.get('extra', {}) or fallback_124.get('extra', {})),
                'currentView': '/search_list',
                'eventReferrer': 'click_search_list'
            }
        }
    ]

    # 타임스탬프 적용
    base_time = datetime.datetime.now()
    for item in body:
        offset_ms = random.randint(1, 5)
        base_time += datetime.timedelta(milliseconds=offset_ms)
        item['common']['eventTime'] = base_time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "+0900"

    return run_request(session, method, url, headers, body)
