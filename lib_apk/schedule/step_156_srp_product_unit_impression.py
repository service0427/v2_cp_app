"""
APK 기반 SRP 상품 노출 로깅
===========================

용도: 검색 결과에서 개별 상품이 화면에 노출될 때 로깅
- 스크롤하면서 각 상품이 보일 때마다 전송
- 서버가 어떤 상품이 실제로 노출되었는지 추적
"""

import datetime
import random
from curl_cffi import requests

from lib_apk.common.executor import run_request
from lib_apk.common.utils import generate_common_payload


def run(session: requests.Session, context: dict = None):
    """
    APK 기반 상품 단위 노출 로깅

    전송 스키마:
    1. Schema 13839 (SrpProductUnitImpression) - 각 상품별 노출
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

    # 128에서 추출한 visible_items 사용
    visible_items = context.get('visible_items', [])

    if not visible_items:
        print("[156_APK] No visible items to log")
        return {}

    body = []

    for item in visible_items:
        # Bypass 스키마 사용 (서버가 제공)
        bypass_schema = item.get('bypass_schema', {})

        if bypass_schema:
            schema_entry = {
                'common': generate_common_payload(context),
                'meta': {
                    'schemaId': bypass_schema.get('id', 13839),
                    'schemaVersion': bypass_schema.get('version', 16)
                },
                'data': bypass_schema.get('mandatory', {}),
                'extra': bypass_schema.get('extra', {})
            }
            body.append(schema_entry)

    if not body:
        print("[156_APK] No bypass schemas found")
        return {}

    print(f"[156_APK] Logging {len(body)} product impressions")

    # 타임스탬프 적용
    base_time = datetime.datetime.now()
    for item in body:
        offset_ms = random.randint(1, 5)
        base_time += datetime.timedelta(milliseconds=offset_ms)
        item['common']['eventTime'] = base_time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "+0900"

    return run_request(session, method, url, headers, body)
