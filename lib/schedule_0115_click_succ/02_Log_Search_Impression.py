import sys
import os
import json
import datetime
import random
import time
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE, DeviceProfile
from lib.common.utils import generate_common_payload

# Combined Log Script: Post-Search Logs
# Aggregates:
# - 131_P (List Click / Misc)
# - 133_P (SRP View)
# - 156_P (SRP Product Unit Impressions)

def run(session: requests.Session, context: dict):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    # 1. Header & Device Setup
    if context and 'DEVICE' in context:
        device = DeviceProfile(
            model=context['DEVICE'].get('model', DEFAULT_PROFILE.model),
            os_version=context['DEVICE'].get('os_version', DEFAULT_PROFILE.os_version),
            width=context['DEVICE'].get('width', DEFAULT_PROFILE.width),
            height=context['DEVICE'].get('height', DEFAULT_PROFILE.height),
            pcid=context['DEVICE'].get('pcid', DEFAULT_PROFILE.pcid),
            app_session_id=context['DEVICE'].get('app_session_id', DEFAULT_PROFILE.app_session_id),
            ixid=context['DEVICE'].get('ixid', DEFAULT_PROFILE.ixid),
            android_id=context['DEVICE'].get('android_id', DEFAULT_PROFILE.android_id)
        )
    else:
        device = DEFAULT_PROFILE

    headers = {
        'content-type': 'application/json; charset=utf-8',
        'accept-encoding': 'gzip',
        'user-agent': device.get_okhttp_user_agent(),
        'expect': '' 
    }
    
    # 2. Prepare Common Data
    payload_common = generate_common_payload(context)
    q = context['INPUT'].get('q', '')
    import uuid
    request_id = str(uuid.uuid4())

    # Helper
    def make_item(schema_id, schema_ver, data_override=None, meta_override=None, extra_override=None):
        base_data = {
            'common': payload_common,
            'meta': {'schemaId': schema_id, 'schemaVersion': schema_ver},
            'data': {},
            'extra': {}
        }
        if meta_override:
            base_data['meta'].update(meta_override)
        if data_override:
            base_data['data'].update(data_override)
        if extra_override:
            base_data['extra'].update(extra_override)
        return base_data

    body = []

    # =========================================================================
    # PART 0: System Logs (App Start / Env) - Added 01/14 Gap Analysis
    # =========================================================================
    # 3-7 day random install timestamp for stability
    days_ago = random.randint(3, 7)
    install_ts = int(time.time() * 1000) - (days_ago * 24 * 60 * 60 * 1000)
    
    body.extend([
        # Schema 6515: amp_initialize (Platform Info)
        make_item(6515, 1, {
            'domain': 'amp', 'logCategory': 'system', 'logType': 'platform', 'pageName': 'none',
            'eventName': 'amp_initialize', 'applicationId': 'com.coupang.mobile',
            'clientVersion': '0.37.5' # Hardcoded from Real Capture
        }),
        
        # Schema 13550: deviceTotalMemory (Performance)
        make_item(13550, 1, {
            'domain': 'cmg', 'logCategory': 'system', 'logType': 'performance', 'pageName': None,
            'eventName': 'deviceTotalMemory', 'totalMemory': 5 # 5GB or Bucket?
        }),
        
        # Schema 19536: Performance / Launch
        make_item(19536, 1, {
            'domain': None, 'logCategory': 'system', 'logType': 'performance', 'pageName': '',
            'eventName': None
        }, meta_override={'schemaId': 19536}, extra_override={
            'isForegroundImportance': True, 'importance': 100, 'isFirstInstall': True,
            'isJumpBeforeHome': False, 'source': 'goto_StartLocaleSelection', 'appStartType': 'cold',
            'coldLaunchCase': 'appVersionUpgrade', 'isStartedFromBackground': True, 'networkState': 'wifi'
        }),
        
        # Schema 15617: check_token_migration (Auth)
        make_item(15617, 1, {
            'domain': 'member', 'logCategory': 'system', 'logType': 'debug', 'pageName': 'login',
            'eventName': 'check_token_migration_target', 'isLogin': False, 'hasAuthToken': False
        }, meta_override={'schemaId': 15617}, extra_override={'backupEnable': False})
    ])

    # =========================================================================
    # PART 1: 131_P (Misc Search Logs)
    # =========================================================================
    body.extend([
        # Schema 3894: search_autocomplete_keyword
        make_item(3894, 9, {
            'domain': 'srp', 'logCategory': 'impression', 'logType': 'impression', 'pageName': 'srp',
            'eventName': 'search_autocomplete_keyword', 'requestId': request_id, 'qPos': '1-9',
            'prefix': q, 'filters': None, 'filterKeys': '', 'hasCavenue': None, 'types': None,
            'subTypes': None, 'hasRecent': False, 'autoKeywords': '', 'officialBrand': '',
            'isRlux': False, 'brandId': 0
        }, meta_override={'schemaId': 3894}),
        
        # Schema 120: click_search_list (CRITICAL)
        make_item(120, 4, {
            'domain': 'srp', 'logCategory': 'event', 'logType': 'click', 'pageName': 'srp',
            'eventName': 'click_search_list', 'q': q, 'channel': None
        }),
        
        # Schema 7761: Recommendation
        make_item(7761, 1, {
            'logType': 'impression', 'numVisibleKeywords': 5, 'domain': 'srp',
            'eventName': 'search_home_fresh_recommended_keyword', 'searchHomeVersion': 'V2',
            'logCategory': 'impression', 'recoKeywords': '핫도그,연두부,슬라이스치즈', 'pageName': 'srp'
        })
    ])

    # =========================================================================
    # PART 2: 133_P (SRP View Logs)
    # =========================================================================
    search_res = context.get('RESULT', {}).get('SEARCH', {})
    root_res = context.get('RESULT', {}).get('ROOT', {})
    
    body.extend([
        # Schema 17211: TtiWidgetMonitorLog
        make_item(17211, 2, {
            'domain': 'srp', 'logCategory': 'system', 'logType': 'debug', 'pageName': None, 'eventName': None,
            'widgetTotalCount': search_res.get('widgetTotalCount', 0),
            'widgetTypeCount': search_res.get('widgetTypeCount', 0),
            'widgetDistribution': search_res.get('widgetDistribution', '{}'),
            'analyzeDuration': random.randint(1, 10)
        }),
        
        # Schema 9854 (Dynamic Templates)
        *[make_item(9854, 2, {
            'domain': 'search', 'logCategory': 'system', 'logType': 'error', 'pageName': 'search',
            'eventName': 'abnormal_api', 'requestURL': 'https://cmapi.coupang.com/v3/products',
            'fullRequestURL': search_res.get('SEARCH_URL')
        }) for t in search_res.get('dynamic_templates', [])],
        
        # Schema 15704: SrpPaginationView
        make_item(15704, 1, {
            'domain': 'srp', 'logCategory': 'view', 'logType': 'page', 'pageName': 'srp',
            'eventName': 'srp_view_impression',
            'q': q, 'searchId': root_res.get('searchId'), 'rootSearchId': root_res.get('searchId'),
            'previousRootSearchId': ''
        }),
        
        # Schema 116: SrpPageView (CRITICAL)
        make_item(116, 23, {
            'domain': 'srp', 'logCategory': 'view', 'logType': 'page', 'pageName': 'srp',
            'q': q, 'channel': 'user', 'searchId': root_res.get('searchId'),
            'searchCount': root_res.get('searchCount'),
            'isCoupick': search_res.get('isCoupick', False),
            'rankOfCoupick': search_res.get('rankOfCoupick', -1),
            'keywordType': root_res.get('keywordType', ''),
            'isGenderTabTest': False
        })
    ])

    # =========================================================================
    # PART 3: 156_P (Product Impressions & Unit Logs)
    # =========================================================================
    # Process UNIT_LOGS from Context
    unit_logs = context.get('RESULT', {}).get('META', {}).get('UNIT_LOGS', [])
    
    # 3.2 Generate Unit Logs (Schema 14741 - Neighbor Logging)
    # Critical for Anti-Abuse: Proves we rendered items around the target.
    for i, item in enumerate(unit_logs):
        # Data is already hydrated in 128_G
        item_data = item.get('data', {})
        item_extra = item.get('extra', {})
        
        # [Dynamic Layout Logic]
        # Calculate viewType from template map
        # Remove these temporary fields so they don't pollute the final log
        current_template = item_data.pop('currentTemplate', 'LIST') 
        template_map = item_data.pop('template', {})
        
        # Logic: Use current_template to look up the source string in template_map
        target_template_key = current_template
        
        # Override for testing/fidelity (can be extended to check context config)
        # if context.get('force_grid_3'): target_template_key = 'GRID_3'

        if template_map and target_template_key in template_map:
            source_string = template_map[target_template_key].get('source', '')
            if source_string.startswith('layoutMap://'):
                new_view_type = source_string.replace('layoutMap://', '')
                item_data['viewType'] = new_view_type
        
        body.extend([
            make_item(14741, 1, item_data, meta_override={'schemaId': 14741}, extra_override=item_extra)
        ])

    # 3.3 Product Impression Metadata (Schema 13697)
    # Summarized impression data for the page viewfaults
    s13697_data = {} # Defaults
    if unit_logs:
        s13697_productIdList = str([int(log['data']['productId']) for log in unit_logs if log['data'].get('productId')])
        s13697_itemIdList = str([int(log['data']['itemId']) for log in unit_logs if log['data'].get('itemId')])
        s13697_vendorItemIdList = str([int(log['data']['vendorItemId']) for log in unit_logs if log['data'].get('vendorItemId')])
        
        # Simulation of Timing
        now_ts = int(datetime.datetime.now().timestamp() * 1000)
        page_start = now_ts
        page_end = now_ts + 5000
        start_ts_list = []
        end_ts_list = []
        event_type_list = []
        base_ts = page_start + 500
        
        for i in range(len(unit_logs)):
            step_jitter = random.randint(120, 280)
            item_start = base_ts + step_jitter
            base_ts = item_start
            start_ts_list.append([item_start])
            item_end = page_end + random.randint(-500, 500)
            end_ts_list.append([item_end])
            event_type_list.append(["SDP_VID"])
            
        final_start = start_ts_list[-1][0] if start_ts_list else page_end
        if final_start > page_end: page_end = final_start + 1000
        
        s13697_data = {
            'productIdList': s13697_productIdList,
            'itemIdList': s13697_itemIdList,
            'vendorItemIdList': s13697_vendorItemIdList,
            'pageStartTime': page_start,
            'pageEndTime': page_end,
            'itemStartTime': str(start_ts_list),
            'itemEndTime': str(end_ts_list),
            'endEventType': 'SDP_VID',
            'endItemEventTypeList': str(event_type_list),
            'vendorItemCount': len(unit_logs)
        }

    body.extend([
        # Schema 18359: Bypass Logs
        make_item(18359, 1, 
            data_override=context.get('RESULT', {}).get('META', {}).get('PRODUCT', {}).get('18359_1', {}).get('data', {}),
            meta_override=context.get('RESULT', {}).get('META', {}).get('PRODUCT', {}).get('18359_1', {}).get('extra', {})
        ),
        
        # Schema 15987: Page Leave
        make_item(15987, 1, {
            'domain': 'srp', 'logCategory': 'view', 'logType': 'modal', 'pageName': 'srp',
            'eventName': 'page_leave', 'pvid': search_res.get('srp_pvId')
        }),
        
        # Schema 13697: Browse Duration (Calculated above)
        make_item(13697, 2, {
            'domain': 'SRP', 'logCategory': 'impression', 'logType': 'impression', 'pageName': 'srp',
            'eventName': 'srp_product_unit_exposure',
            'query': q, 'searchId': root_res.get('searchId'), 'ixid': device.ixid,
            **s13697_data
        })
    ])

    return run_request(session, method, url, headers, body)
