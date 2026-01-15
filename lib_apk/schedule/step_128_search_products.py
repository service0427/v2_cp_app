"""
APK 기반 검색 API
==================

핵심: 서버가 제공하는 bypass 스키마를 추출하여 context에 저장
- clickSchemas → srp_click_log_bypass
- commonBypassLogParams.mandatory → srp_bypass_mandatory

이후 스텝에서 이 bypass 데이터를 사용하여 스키마 자동 생성
"""

import time
import json
from urllib.parse import quote_plus
from curl_cffi import requests

from lib_apk.common.executor import run_request
from lib_apk.device_profile import DeviceProfile


def run(session: requests.Session, context: dict = None):
    """
    검색 API 호출 및 bypass 스키마 추출

    APK 원리:
    1. 서버가 clickSchemas, commonBypassLogParams 반환
    2. 클라이언트는 bypass 템플릿의 빈 값을 mandatory에서 채움
    3. bulksubmit으로 전송
    """
    method = "GET"

    encoded_keyword = quote_plus(context['INPUT']['q'])
    url = f"https://cmapi.coupang.com/v3/products?filter=KEYWORD:{encoded_keyword}|CCID:ALL|EXTRAS:channel/user|GET_FILTER:NONE|SINGLE_ENTITY:TRUE@SEARCH&preventingRedirection=false&resultType=default&ccidActivated=false&referrerPage=HOME"

    # 디바이스 프로필 생성
    device = DeviceProfile(
        model=context['DEVICE']['model'],
        os_version=context['DEVICE']['os_version'],
        width=context['DEVICE']['width'],
        height=context['DEVICE']['height'],
        pcid=context['DEVICE']['pcid'],
        app_session_id=context['DEVICE']['app_session_id'],
        ixid=context['DEVICE']['ixid'],
        android_id=context['DEVICE'].get('android_id', ''),
        dpi=context['DEVICE'].get('dpi', '450'),
        dpi_level=context['DEVICE'].get('dpi_level', 'XXHDPI'),
    )

    ts = int(time.time() * 1000)

    headers = {
        'x-timestamp': str(ts),
        'coupang-app': device.get_coupang_app_header(),
        'x-coupang-font-scale': '1.0',
        'run-mode': 'production',
        'x-coupang-app-request': 'true',
        'baggage': 'enable-upstream-tti-info=true',
        'x-cp-app-req-time': str(ts + 100),
        'x-view-name': '/search',
        'x-coupang-target-market': 'KR',
        'x-coupang-app-name': 'coupang',
        'x-cp-app-id': 'com.coupang.mobile',
        'x-cmg-dco': device.get_cmg_dco(),
        'x-coupang-origin-region': 'KR',
        'x-signature': device.generate_signature(ts),
        'x-coupang-accept-language': 'ko-KR',
        'x-trace-ix-id': device.generate_trace_id(),
        'user-agent': device.get_user_agent(),
        'accept-encoding': 'gzip'
    }

    # 헤더 저장
    context['DEVICE']['coupangAppHeader'] = headers.get('coupang-app', '')
    context['DEVICE']['userAgent'] = headers.get('user-agent', '')

    response = run_request(session, method, url, headers, None)

    if response and response.status_code == 200:
        try:
            data = response.json()
            r_data = data.get('rData', {})
            entity_list = r_data.get('entityList', [])

            # === 타겟 상품 찾기 ===
            selected_product = None
            selected_entity_wrapper = None
            target_rank = 0

            for i, entity_wrapper in enumerate(entity_list):
                if i > 100:
                    break

                display_item = None
                entity = entity_wrapper.get('entity', {})

                if 'widget' in entity:
                    display_item = entity.get('widget', {}).get('metadata', {}).get('displayItem')
                if not display_item:
                    display_item = entity_wrapper.get('displayItem')
                if not display_item:
                    display_item = entity.get('displayItem')

                if display_item:
                    p_id = str(display_item.get('id', ''))
                    if p_id == context['INPUT']['productId']:
                        selected_product = display_item
                        selected_entity_wrapper = entity_wrapper
                        target_rank = i
                        print(f"[128_APK] FOUND TARGET: {p_id} at Rank {i}")
                        break

            if not selected_product:
                print(f"[128_APK] Target {context['INPUT']['productId']} not found, using first item")
                for i, entity_wrapper in enumerate(entity_list[:50]):
                    entity = entity_wrapper.get('entity', {})
                    display_item = entity.get('widget', {}).get('metadata', {}).get('displayItem')
                    if not display_item:
                        display_item = entity_wrapper.get('displayItem')
                    if display_item:
                        selected_product = display_item
                        selected_entity_wrapper = entity_wrapper
                        target_rank = i
                        break

            if not selected_product:
                raise RuntimeError("[128_APK] No product found in search results")

            # === RESULT 업데이트 ===
            context['RESULT']['ROOT'] = {
                'productId': str(selected_product.get('id', '')),
                'itemId': str(selected_product.get('itemId', '')),
                'vendorItemId': str(selected_product.get('vendorItemId', '')),
                'itemProductId': str(selected_product.get('itemProductId', 4)),
                'searchId': '',
                'searchCount': r_data.get('totalCount', 0),
            }

            context['RESULT']['SEARCH'] = {
                'srp_rank': target_rank,
                'searchViewType': 'GRID_2',
                'internalCategoryId': '',
            }

            # === APK 핵심: Bypass 스키마 추출 ===
            # 1. clickSchemas에서 Schema 124 추출
            def find_click_schema(obj, target_id="124"):
                if isinstance(obj, dict):
                    if 'clickSchemas' in obj and isinstance(obj['clickSchemas'], list):
                        for s in obj['clickSchemas']:
                            s_id = str(s.get('id', '') or s.get('schemaId', ''))
                            if s_id == target_id:
                                return s
                    for v in obj.values():
                        res = find_click_schema(v, target_id)
                        if res:
                            return res
                elif isinstance(obj, list):
                    for item in obj:
                        res = find_click_schema(item, target_id)
                        if res:
                            return res
                return None

            click_schema_124 = find_click_schema(selected_entity_wrapper, "124")
            if click_schema_124:
                context['srp_click_log_bypass'] = click_schema_124
                print(f"[128_APK] Extracted clickSchema 124: {list(click_schema_124.keys())}")
            else:
                print(f"[128_APK] No clickSchema 124 found")

            # 2. commonBypassLogParams.mandatory 추출
            entity_inner = selected_entity_wrapper.get('entity', {})
            widget = entity_inner.get('widget', {})
            metadata = widget.get('metadata', {})
            bypass_params = metadata.get('commonBypassLogParams', {})
            mandatory_params = bypass_params.get('mandatory', {})

            if mandatory_params:
                context['srp_bypass_mandatory'] = mandatory_params
                print(f"[128_APK] Extracted bypass mandatory: {list(mandatory_params.keys())}")

                # internalCategoryId 추출
                if 'internalCategoryId' in mandatory_params:
                    context['RESULT']['SEARCH']['internalCategoryId'] = str(mandatory_params['internalCategoryId'])
            else:
                print(f"[128_APK] No bypass mandatory found")

            # === visible_items 추출 (156용) ===
            visible_items = []
            end_rank = min(max(4, target_rank + 5), 100)

            for i, entity_wrapper in enumerate(entity_list[:end_rank]):
                entity = entity_wrapper.get('entity', {})
                display_item = entity.get('widget', {}).get('metadata', {}).get('displayItem')
                if not display_item:
                    display_item = entity_wrapper.get('displayItem')
                if not display_item:
                    continue

                # bypass 스키마 추출
                item_bypass = find_click_schema(entity_wrapper, "13839")  # SrpProductUnitImpression

                visible_items.append({
                    'rank': i,
                    'productId': str(display_item.get('id', '')),
                    'itemId': str(display_item.get('itemId', '')),
                    'vendorItemId': str(display_item.get('vendorItemId', '')),
                    'bypass_schema': item_bypass
                })

            context['visible_items'] = visible_items
            print(f"[128_APK] Extracted {len(visible_items)} visible items")

            print(f"[128_APK] Search completed. Target: {context['RESULT']['ROOT']['productId']}")

        except Exception as e:
            print(f"[128_APK] Extraction Error: {e}")
            import traceback
            traceback.print_exc()
            raise e
    else:
        status = response.status_code if response else "None"
        raise RuntimeError(f"[128_APK] Request Failed. Status: {status}")

    return {}
