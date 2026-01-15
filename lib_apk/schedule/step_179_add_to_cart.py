"""
APK 기반 장바구니 추가 로깅
============================

용도: 상품을 장바구니에 추가할 때 로깅
- Schema 12345 (AddToCart)
"""

import datetime
import random
from curl_cffi import requests

from lib_apk.common.executor import run_request
from lib_apk.common.utils import generate_common_payload


def run(session: requests.Session, context: dict = None):
    """
    APK 기반 장바구니 추가 로깅

    전송 스키마:
    1. Schema (AddToCart) - 장바구니 추가 이벤트
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

    # 장바구니 추가 bypass 스키마 사용
    add_cart_bypass = context.get('add_cart_bypass', {})

    if not add_cart_bypass:
        print("[179_APK] No add_cart_bypass found in context")
        return {}

    schema_data = add_cart_bypass.get('mandatory', {}).copy()

    # 필수 필드 보강
    product_info = context.get('RESULT', {}).get('PRODUCT', {})
    root_info = context.get('RESULT', {}).get('ROOT', {})

    if not schema_data.get('productId'):
        schema_data['productId'] = root_info.get('productId')

    if not schema_data.get('vendorItemId'):
        schema_data['vendorItemId'] = root_info.get('vendorItemId')

    if not schema_data.get('itemId'):
        schema_data['itemId'] = root_info.get('itemId')

    print(f"[179_APK] AddToCart: productId={schema_data.get('productId')}")

    body = [
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': add_cart_bypass.get('id', 0),
                'schemaVersion': add_cart_bypass.get('version', 1)
            },
            'data': schema_data,
            'extra': add_cart_bypass.get('extra', {})
        }
    ]

    # 타임스탬프 적용
    base_time = datetime.datetime.now()
    for item in body:
        offset_ms = random.randint(1, 5)
        base_time += datetime.timedelta(milliseconds=offset_ms)
        item['common']['eventTime'] = base_time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "+0900"

    return run_request(session, method, url, headers, body)
