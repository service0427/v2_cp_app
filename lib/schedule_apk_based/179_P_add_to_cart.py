"""
APK 기반 장바구니 추가 로깅
===========================

용도: 상품을 장바구니에 추가할 때 로깅
"""

import sys
import os
import datetime
import random
from curl_cffi import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.common.utils import generate_common_payload


def run(session: requests.Session, context: dict = None):
    """
    APK 기반 장바구니 추가 로깅

    전송 스키마:
    1. Schema 163 (SdpAddToCart) - 장바구니 추가 이벤트
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
    # Schema 163: SdpAddToCart
    # APK: smali_classes16/com/coupang/mobile/domain/sdp/monitoring/schema/SdpAddToCart.smali
    # Fixed: logCategory=event, logType=click, eventName=add_to_cart
    # ============================================================

    body = [
        {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': 163,
                'schemaVersion': 17
            },
            'data': {
                # Fixed values (APK에서 추출)
                'domain': 'sdp',
                'logCategory': 'event',
                'logType': 'click',
                'pageName': 'sdp',
                'eventName': 'add_to_cart',

                # Dynamic values
                'productId': context.get('RESULT', {}).get('ROOT', {}).get('productId'),
                'vendorItemId': context.get('RESULT', {}).get('ROOT', {}).get('vendorItemId'),
                'itemId': context.get('RESULT', {}).get('ROOT', {}).get('itemId'),
                'itemProductId': context.get('RESULT', {}).get('ROOT', {}).get('itemProductId'),
                'quantity': 1,
                'channel': 'user',
                'sourceType': 'search',
                'q': context.get('INPUT', {}).get('q'),
                'searchId': context.get('RESULT', {}).get('ROOT', {}).get('searchId'),
            },
            'extra': {
                'currentView': '/sdp',
                'eventReferrer': 'click_add_to_cart'
            }
        }
    ]

    print(f"[179_APK] AddToCart: productId={context.get('RESULT', {}).get('ROOT', {}).get('productId')}")

    # 타임스탬프 적용
    base_time = datetime.datetime.now()
    for item in body:
        offset_ms = random.randint(1, 5)
        base_time += datetime.timedelta(milliseconds=offset_ms)
        item['common']['eventTime'] = base_time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "+0900"

    return run_request(session, method, url, headers, body)
