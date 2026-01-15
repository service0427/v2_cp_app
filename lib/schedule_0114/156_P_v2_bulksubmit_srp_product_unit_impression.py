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
            # Start: staggered by random variable (120ms ~ 280ms) to mimic human scroll
            # jitter = base_ts + (i * 150) -> [OLD] Robotic
            step_jitter = random.randint(120, 280)
            item_start = base_ts + step_jitter
            base_ts = item_start # Accumulate time naturally
            
            start_ts_list.append([item_start])
            
            # End: Variable duration instead of fixed page end
            # Some items actully scroll OFF screen? For now assume valid until end, but randomize end slightly
            item_end = s13697_pageEndTime + random.randint(-500, 500)
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
