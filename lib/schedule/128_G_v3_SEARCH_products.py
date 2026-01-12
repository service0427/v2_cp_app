import sys
import os
import json
import time
import urllib.parse
from urllib.parse import quote
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.common.headers import HeaderBuilder
from lib.device_profile import DEFAULT_PROFILE, DeviceProfile
import lib.logger


# Reference Data Index: 127
# Method: GET
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'x-timestamp': '1767976309414',
#     'coupang-app': 'COUPANG|Android|15|9.0.4||null|f0b740d2-3447-3b2b-b118-d66257275f8f|Y|SM-A165N|f0b740d234472b2bb118d66257275f8f|25ede38a-c6e9-41b2-818a-aef7b5c17d0a|XXHDPI|17679762746194168937968||0||wifi|-1|||Asia/Seoul|c658d419f4d046cfb15f281769b15de7fbc66b30||1080|450|-1|1.0|true',
#     'x-coupang-font-scale': '1.0',
#     'run-mode': 'production',
#     'x-coupang-app-request': 'true',
#     'x-cp-app-req-time': '1767976310499',
#     'x-view-name': '/search',
#     'x-coupang-target-market': 'KR',
#     'x-coupang-app-name': 'coupang',
#     'x-cp-app-id': 'com.coupang.mobile',
#     'x-cmg-dco': '1767946318000',
#     'x-coupang-origin-region': 'KR',
#     'x-signature': '9dd7e6b266cb37c66ded3b39e353bb2901992e8dc1a17635a954cc93e9e9c900',
#     'x-coupang-accept-language': 'ko-KR',
#     'x-trace-ix-id': '00014a5f-2f79-23fb-e384-abdc292008d4',
#     'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 15; SM-A165N Build/AP3A.240905.015.A2)',
#     'accept-encoding': 'gzip'
# }
# ------------------------------

def run(session: requests.Session, context: dict = None):
    method = "GET"

    # Encode keyword for URL
    encoded_keyword = quote(context['INPUT']['q'], safe='')

    # Build URL dynamically
    url = f"https://cmapi.coupang.com/v3/products?filter=KEYWORD:{encoded_keyword}|CCID:ALL|EXTRAS:channel/user|GET_FILTER:NONE|SINGLE_ENTITY:TRUE@SEARCH&preventingRedirection=false&resultType=default&ccidActivated=false&referrerPage=HOME"

    # ========================================
    # 동적 헤더 생성 (v1 로직 적용)
    # ========================================

    # DeviceProfile 인스턴스 생성 (context의 DEVICE 정보 사용)
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

    # HeaderBuilder로 동적 헤더 생성
    headers = HeaderBuilder.build_search_headers(device, view_name="/search")

    # Store dynamic headers in context for later reuse (e.g., sourceUserAgent in 147_P)
    context['DEVICE']['coupangAppHeader'] = headers.get('coupang-app', '')
    context['DEVICE']['userAgent'] = headers.get('user-agent', '')

    body = None

    response = run_request(session, method, url, headers, body)

    if response and response.status_code == 200:
        try:
            data = response.json()

            # Save raw API response to SEARCH.log
            try:
                if lib.logger.LOG_BASE_DIR:
                    search_log_file = os.path.join(lib.logger.LOG_BASE_DIR, "SEARCH.log")
                    with open(search_log_file, "w", encoding="utf-8") as f:
                        json.dump(data, f, indent=2, ensure_ascii=False)
                    print(f"[128] Saved raw API response to {search_log_file}")
            except Exception as e:
                print(f"[128] Failed to save SEARCH.log: {e}")

            r_data = data.get('rData', {})

            extracted_data = {}

            # Extract searchId
            # Strategy 1: Check rData.requestUris (URL params) - Most reliable
            request_uris = r_data.get('requestUris', {})
            for uri_key, uri_val in request_uris.items():
                if isinstance(uri_val, str) and 'searchId=' in uri_val:
                    # Extract searchId from URL
                    try:
                        parsed = urllib.parse.urlparse(uri_val)
                        query_params = urllib.parse.parse_qs(parsed.query)
                        if 'searchId' in query_params:
                            extracted_data['searchId'] = query_params['searchId'][0]
                            break
                    except:
                        pass
            
            if 'searchId' not in extracted_data:
                # Fallback logic for searchId
                entity_list = r_data.get('entityList', [])
                for entity in entity_list:
                    display_item = entity.get('displayItem')
                    if display_item and 'searchId' in display_item:
                         extracted_data['searchId'] = display_item['searchId']
                         break
            
            # Extract totalCount
            if 'totalCount' in r_data:
                extracted_data['searchCount'] = r_data['totalCount']

            # Set Context Variables
            extracted_data['q'] = context['INPUT']['q']
            extracted_data['ixid'] = context['DEVICE']['ixid']
            extracted_data['SEARCH_URL'] = url
            extracted_data['ENCODED_KEYWORD'] = encoded_keyword
            
            # [Added] Initialize Schema 116 fields
            extracted_data['searchViewType'] = 'GRID_2' # Default
            extracted_data['srp_isCoupick'] = False
            extracted_data['srp_rankOfCoupick'] = -1

            
            # Product Selection Logic
            entity_list = r_data.get('entityList', [])
            selected_product = None
            selected_entity_wrapper = None
            
            if entity_list:
                # First pass: Look for TARGET product
                for i, entity_wrapper in enumerate(entity_list):
                    if i > 100: break # check deeper for target
                    
                    display_item = None
                    entity = entity_wrapper.get('entity', {})
                    if 'widget' in entity:
                        display_item = entity.get('widget', {}).get('metadata', {}).get('displayItem')
                    if not display_item: display_item = entity_wrapper.get('displayItem')
                    if not display_item: display_item = entity.get('displayItem')
                    
                    if display_item:
                        p_id = str(display_item.get('id', ''))
                        if p_id == context['INPUT']['productId']:
                            selected_product = display_item
                            selected_entity_wrapper = entity_wrapper
                            extracted_data['srp_rank'] = str(i) # 0-based or 1-based? Usually 0 in lists, but searchRank often 1-based. Let's use i and potentially adjust in client.
                            print(f"[128] FOUND TARGET PRODUCT: {p_id} at Rank {i}")
                            break
                            
                # Second pass: Fallback to first valid item if target not found
                if not selected_product:
                    print(f"[128] Target product {context['INPUT']['productId']} not found. Falling back to first item.")
                    for i, entity_wrapper in enumerate(entity_list):
                        if i > 50: break
                        display_item = None
                        entity = entity_wrapper.get('entity', {})
                        if 'widget' in entity:
                            display_item = entity.get('widget', {}).get('metadata', {}).get('displayItem')
                        if not display_item: display_item = entity_wrapper.get('displayItem')
                        if not display_item: display_item = entity.get('displayItem')
                        
                        if display_item:
                            selected_product = display_item
                            selected_entity_wrapper = entity_wrapper
                            extracted_data['srp_rank'] = str(i)
                            print(f"[128] Fallback Product Rank: {i}")
                            break
            
            # [Added] Extract global SRP state (viewType, Coupick Rank)
            if entity_list:
                for i, entity_wrapper in enumerate(entity_list):
                    entity = entity_wrapper.get('entity', {})
                    widget = entity.get('widget', {})
                    
                    # 1. Search View Type (Find 'currentTemplate')
                    # Location: entity.widget.currentTemplate OR entity.widget.metadata.currentTemplate
                    if 'currentTemplate' in widget:
                        extracted_data['searchViewType'] = widget['currentTemplate']
                    elif 'metadata' in widget and 'currentTemplate' in widget['metadata']:
                         extracted_data['searchViewType'] = widget['metadata']['currentTemplate']
                    
                    # 2. Coupick Analysis (First item with isCoupick=True)
                    # Check displayItem from various locations
                    d_item = None
                    if 'displayItem' in entity: d_item = entity['displayItem']
                    elif 'widget' in entity and 'displayItem' in entity.get('widget', {}).get('metadata', {}):
                         d_item = entity['widget']['metadata']['displayItem']
                    elif 'displayItem' in entity_wrapper: d_item = entity_wrapper['displayItem']
                    
                    if d_item and d_item.get('isCoupick') is True:
                         if extracted_data['srp_rankOfCoupick'] == -1:
                             extracted_data['srp_isCoupick'] = True
                             extracted_data['srp_rankOfCoupick'] = i
                             # Don't break immediately if we want to scan all for viewType, 
                             # but usually viewType is consistent. 
                             # We continue to ensure we find viewType if it appears later.

            
            if selected_product:
                p_id = str(selected_product.get('id'))
                item_id = str(selected_product.get('itemId'))
                vendor_item_id = str(selected_product.get('vendorItemId'))

                print(f"[128] Selected Product: {p_id}, Item: {item_id}, VendorItem: {vendor_item_id}")

                # RESULT > TARGET: 타겟 상품 정보를 별도로 분리 저장
                context['RESULT']['TARGET'] = {
                    'productId': p_id,
                    'itemId': item_id,
                    'vendorItemId': vendor_item_id,
                    'itemProductId': str(selected_product.get('itemProductId', 4)),
                    'rank': extracted_data.get('srp_rank', '0'),
                    'productName': extracted_data.get('srp_productName', ''),
                    'finalPrice': extracted_data.get('srp_finalPrice', ''),
                    'originalPrice': extracted_data.get('srp_originalPrice', ''),
                    'discountRate': extracted_data.get('srp_discountRate', ''),
                    'ratingAverage': extracted_data.get('srp_ratingAverage', ''),
                    'ratingCount': extracted_data.get('srp_ratingCount', ''),
                    'imageUrl': extracted_data.get('srp_imageUrl', ''),
                    'scaleType': extracted_data.get('srp_scaleType', ''),
                }

                # extracted_data에도 유지 (호환성)
                extracted_data['productId'] = p_id
                extracted_data['itemId'] = item_id
                extracted_data['vendorItemId'] = vendor_item_id
                extracted_data['itemProductId'] = str(selected_product.get('itemProductId', 4))
                
                # [Hybrid Hydration] Extract additional attributes for 156_P
                if selected_entity_wrapper:
                     # 0. isAds (Ad Icon)
                     # Check if 'isAds' is true at entity level
                     extracted_data['srp_isAds'] = str(selected_entity_wrapper.get('entity', {}).get('isAds', 'false')).lower()

                     # 1. isFreeReturn
                     extracted_data['srp_isFreeReturn'] = str(selected_entity_wrapper.get('displayItem', {}).get('isFreeReturn', 'False'))
                     
                     # 2. Badges (rocketType, isRocket, etc.)
                     badges = selected_entity_wrapper.get('badges', [])
                     extracted_data['srp_badges'] = str(badges) # Raw list string
                     
                     # Parse badges for specific flags
                     extracted_data['srp_isRocket'] = 'False'
                     extracted_data['srp_rocketType'] = ''
                     for badge in badges:
                         if 'rocket' in str(badge).lower():
                             extracted_data['srp_isRocket'] = 'True'
                             extracted_data['srp_rocketType'] = 'ROCKET_DELIVERY' # Example fallback
                             break
                             
                              
                     # 3. isCoupick (Per Item - for selected product context, kept as string for compatibility if needed)
                     # But for Schema 116 we use the global extracted_data['srp_isCoupick'] (bool)
                     extracted_data['srp_isCoupick_str'] = str(selected_entity_wrapper.get('displayItem', {}).get('isCoupick', 'False'))
                     
                     # 4. [Component Scraper] Extract logging data from widget components
                     # Many fields like ratingCountString, promiseDeliveryDate are visible here
                     try:
                         entity = selected_entity_wrapper.get('entity', {})
                         widget_data = entity.get('widget', {}).get('data', {})
                         
                         for comp_key, comp_val in widget_data.items():
                             if isinstance(comp_val, dict):
                                 # Check logging > mandatory
                                 logging_mandatory = comp_val.get('data', {}).get('logging', {}).get('mandatory', {})
                                 if logging_mandatory:
                                     for k, v in logging_mandatory.items():
                                         # Map specific keys to srp_ prefixed vars
                                         if k in ['ratingCountString', 'ratingAverageString', 'promiseDeliveryDate', 
                                                  'originalPriceString', 'salesPricePrefix', 'finalPriceString', 'unitPrice']:
                                             extracted_data[f'srp_{k}'] = str(v)
                                             
                                 # Check logging > loggingValue (e.g. for Benefits)
                                 logging_val = comp_val.get('data', {}).get('logging', {}).get('loggingValue')
                                 if logging_val:
                                     # Heuristic: Check ID or Key to guess what it is
                                     if 'Benefit' in comp_key or 'Benefit' in str(comp_val.get('id', '')):
                                         extracted_data['srp_productDeliveryBenefitGroup'] = str(logging_val)
                                         
                     except Exception as e:
                         print(f"[128] Component Scraping Failed: {e}")

                     # [Gap Analysis Fix] Extract Search Metadata (Schema 116/124)
                     # 1. SearchViewType & InternalCategoryId & Coupick
                     try:
                         search_view_type = "LIST" # Default
                         is_coupick = False
                         rank_of_coupick = -1
                         internal_category_id = ''
                         
                         extracted_data['searchViewType'] = search_view_type # Init
                         extracted_data['isCoupick'] = is_coupick
                         extracted_data['rankOfCoupick'] = rank_of_coupick
                         
                         if 'entityList' in r_data:
                             # A. Scan for Coupick & ViewType
                             for idx, ent in enumerate(r_data.get('entityList', [])):
                                 # refined searchViewType from template
                                 tpl = ent.get('template', '').upper()
                                 if 'GRID' in tpl:
                                     search_view_type = "GRID_2"
                                 
                                 # refined Coupick
                                 # Check badges list for 'COU_PICK' string or dict
                                 ent_badges = ent.get('badges', [])
                                 # Some badges are dicts, some strings. Handle both.
                                 has_coupick_badge = False
                                 for b in ent_badges:
                                     if isinstance(b, str) and 'COU_PICK' in b: has_coupick_badge = True
                                     elif isinstance(b, dict) and 'COU_PICK' in str(b): has_coupick_badge = True
                                     
                                 if has_coupick_badge:
                                     if not is_coupick: # Capture first occurrence
                                         is_coupick = True
                                         rank_of_coupick = idx
                                 
                                 # B. Extract internalCategoryId from first valid product
                                 if not internal_category_id:
                                     # Try extracting from displayItem or entity data
                                     e_item = ent.get('displayItem') or ent.get('entity', {}).get('displayItem')
                                     if e_item:
                                         cat_id = e_item.get('categoryId') # Direct
                                         if not cat_id:
                                              # sibling or ancestors? difficult.
                                              # Try logging data if available
                                              pass
                                         if cat_id: internal_category_id = str(cat_id)

                             # Update context
                             extracted_data['searchViewType'] = search_view_type
                             extracted_data['isCoupick'] = is_coupick
                             extracted_data['rankOfCoupick'] = rank_of_coupick
                             extracted_data['internalCategoryId'] = internal_category_id
                             extracted_data['q'] = context['INPUT']['q']
                             
                             print(f"[128_G] Metadata Extracted: valid_q={extracted_data['q']}, ViewType={search_view_type}, Coupick={is_coupick}@{rank_of_coupick}, CatID={internal_category_id}")
                             
                     except Exception as e:
                         print(f"[128_G] Metadata Extraction Failed: {e}")

                     # [Bypass Extraction] Scan selected entity for Click Schemas (ID 124)
                     # This ensures we use the exact schema provided by the server for the click event.
                     try:
                         context['srp_click_log_bypass'] = None
                         def find_click_schema(obj, target_id="124"):
                             if isinstance(obj, dict):
                                 if 'clickSchemas' in obj and isinstance(obj['clickSchemas'], list):
                                     for s in obj['clickSchemas']:
                                         s_id = str(s.get('id', ''))
                                         if not s_id: s_id = str(s.get('schemaId', ''))
                                         if s_id == target_id:
                                             return s
                                 for k, v in obj.items():
                                     res = find_click_schema(v, target_id)
                                     if res: return res
                             elif isinstance(obj, list):
                                 for item in obj:
                                     res = find_click_schema(item, target_id)
                                     if res: return res
                             return None

                         click_schema_124 = find_click_schema(selected_entity_wrapper, "124")
                         if click_schema_124:
                             print(f"[128] Found Bypass Click Schema 124 for selected product.")
                             context['srp_click_log_bypass'] = click_schema_124
                         else:
                             print(f"[128] No Bypass Click Schema 124 found in selected entity.")
                     except Exception as e:
                         print(f"[128] Bypass Schema Extraction Failed: {e}")
                # [Neighbor Logging & Scroll Path] Extract Visible Items for 156_P
                # Strategy: Log items from Rank 0 down to the Target Rank (plus a small buffer).
                # This mimics the "Scroll Path" where the user sees top items before reaching the target.
                
                visible_items = []
                target_rank_int = int(extracted_data.get('srp_rank', '0'))
                
                # Determine range: Always include Top 4 (0-3), extend if target is deeper.
                # e.g., if Target is Rank 10, we want 0..12 to simulate scroll.
                # Max range cap: 300 (effectively unlimited for normal use, but verified for deep scrolls)
                # User verification: "Check if all 100 are passed" -> We must support >100.
                end_rank = min(max(4, target_rank_int + 5), 300)
                
                print(f"[128] Extraction Range: Rank 0 to {end_rank} (Target Rank: {target_rank_int})")

                for i, entity_wrapper in enumerate(entity_list[:end_rank]):
                    try:
                        # Basic Info
                        display_item = None
                        entity = entity_wrapper.get('entity', {})
                        if 'widget' in entity:
                             display_item = entity.get('widget', {}).get('metadata', {}).get('displayItem')
                        if not display_item: display_item = entity_wrapper.get('displayItem')
                        if not display_item: display_item = entity.get('displayItem')

                        if not display_item: continue

                        item_data = {
                            'rank': str(i),
                            'itemId': str(display_item.get('itemId', '')),
                            'vendorItemId': str(display_item.get('vendorItemId', '')),
                            'productId': str(display_item.get('id', '')),
                            'srp_isAds': str(entity.get('isAds', 'false')).lower(),
                            'srp_isFreeReturn': str(display_item.get('isFreeReturn', 'False')),
                            'srp_isFreeReturn': str(display_item.get('isFreeReturn', 'False')),
                            'srp_badges': str(entity_wrapper.get('badges', [])),
                            'srp_isCoupick': str(display_item.get('isCoupick', 'False')),
                            'srp_rocketType': '',
                            'srp_isRocket': 'False',
                            'srp_finalPriceString': '',
                            'srp_ratingCountString': '',
                            'srp_ratingAverageString': '0.0', # Default
                            'srp_promiseDeliveryDate': '',
                            'srp_originalPriceString': '',
                            'srp_salesPricePrefix': '',
                            'srp_unitPrice': '',
                            'srp_unitPrice': '',
                            'srp_productDeliveryBenefitGroup': '',
                            'srp_extra_raw': {}
                        }

                        # Rocket Type
                        for badge in entity_wrapper.get('badges', []):
                             if 'rocket' in str(badge).lower():
                                 item_data['srp_isRocket'] = 'True'
                                 item_data['srp_rocketType'] = 'ROCKET_DELIVERY'
                                 break
                        
                        # Component Scraper (Reuse logic)
                        try:
                            widget_data = entity.get('widget', {}).get('data', {})
                            for comp_val in widget_data.values():
                                if isinstance(comp_val, dict):
                                    logging_mandatory = comp_val.get('data', {}).get('logging', {}).get('mandatory', {})
                                    if logging_mandatory:
                                        for k, v in logging_mandatory.items():
                                            if k in ['ratingCountString', 'ratingAverageString', 'promiseDeliveryDate', 
                                                     'originalPriceString', 'salesPricePrefix', 'finalPriceString', 'unitPrice']:
                                                item_data[f'srp_{k}'] = str(v)
                                    
                                    logging_val = comp_val.get('data', {}).get('logging', {}).get('loggingValue')
                                    if logging_val:
                                         if 'Benefit' in str(comp_val.get('id', '')):
                                             item_data['srp_productDeliveryBenefitGroup'] = str(logging_val)

                                    # [156_P Fix] Extract extraLoggingValues for Schema 14741 Fidelity
                                    extra_logging = comp_val.get('data', {}).get('logging', {}).get('extraLoggingValues')
                                    if extra_logging and isinstance(extra_logging, dict):
                                         item_data['srp_extra_raw'].update(extra_logging)
                        except: pass
                        
                        visible_items.append(item_data)
                    except Exception as e:
                        print(f"[128] Failed to extract visible item {i}: {e}")
                
                extracted_data['visible_items'] = visible_items
                print(f"[128] Extracted {len(visible_items)} visible items for Schema 14741 logging.")

                # Save selected product details to separate log
                # Save selected product details to separate log
                try:
                    if lib.logger.LOG_BASE_DIR:
                        log_file = os.path.join(lib.logger.LOG_BASE_DIR, "128_G_v3_SEARCH_select_products.log")
                        with open(log_file, "w", encoding="utf-8") as f:
                             # Dump the full wrapper if available for context, else just the product
                             data_to_log = selected_entity_wrapper if selected_entity_wrapper else selected_product
                             json.dump(data_to_log, f, indent=2, ensure_ascii=False)
                        print(f"[128] Saved selected product details to {log_file}")
                except Exception as e:
                    print(f"[128] Failed to save separate log: {e}")

                # Log all bypass schemas found in the response
                from lib.logger import log_bypass_schema

                from lib.logger import log_bypass_schema

                def traverse_and_log_schemas(obj):
                    if isinstance(obj, dict):
                        # Heuristic: If it looks like a schema, store it.
                        # A schema usually has 'id' (or 'schemaId'), 'version', and 'mandatory'.
                        # 'bypass' usually contains 'exposureSchema' or 'clickSchemas'.
                        
                        # 1. Check for 'exclusion' patterns (if any)? No, catch all for now.
                        
                        # Check Standard Bypass Keys
                        if 'bypass' in obj:
                            bypass = obj['bypass']
                            if isinstance(bypass, dict):
                                if 'exposureSchema' in bypass:
                                     store_schema_in_context(bypass['exposureSchema'])
                                if 'clickSchemas' in bypass:
                                     for s in bypass['clickSchemas']:
                                         store_schema_in_context(s)

                        # Check generic keys like 'exposureSchema' or 'clickSchemas' appearing directly (e.g. inside logging)
                        if 'exposureSchema' in obj:
                             store_schema_in_context(obj['exposureSchema'])
                        if 'clickSchemas' in obj and isinstance(obj['clickSchemas'], list):
                             for s in obj['clickSchemas']:
                                 store_schema_in_context(s)
                                 
                        # Recursively search children
                        for k, v in obj.items():
                            if isinstance(v, (dict, list)):
                                traverse_and_log_schemas(v)
                                
                    elif isinstance(obj, list):
                        for item in obj:
                            traverse_and_log_schemas(item)

                def store_schema_in_context(schema):
                    if not isinstance(schema, dict): return

                    s_id = str(schema.get('id', ''))
                    if not s_id: s_id = str(schema.get('schemaId', ''))
                    version = str(schema.get('version', ''))

                    if s_id and version:
                        # Build composite key: schemaId_version
                        meta_key = f"{s_id}_{version}"

                        # Store in RESULT > META with data/extra format
                        context['RESULT']['META']['SEARCH'][meta_key] = {
                            'data': schema.get('mandatory', {}),
                            'extra': schema.get('extra', {})
                        }

                traverse_and_log_schemas(r_data)

                # [Hydration] Schema 14741 (SrpProductUnitImpression)
                # Server returns empty template. We must hydrate it with client-side data.
                # Find the schema in context
                hydration_target_key = None
                for key in context['RESULT']['META']['SEARCH'].keys():
                    if key.startswith('14741_'):
                        hydration_target_key = key
                        break

                if hydration_target_key and 'visible_items' in extracted_data:
                    # Prepare a clean list for Unit Impression Logs
                    if 'UNIT_LOGS' not in context['RESULT']['META']:
                        context['RESULT']['META']['UNIT_LOGS'] = []

                    base_schema_data = context['RESULT']['META']['SEARCH'][hydration_target_key]['data']
                    base_schema_extra = context['RESULT']['META']['SEARCH'][hydration_target_key].get('extra', {})

                    # Iterate over ALL visible items (including the target itself)
                    for item in extracted_data['visible_items']:
                        # Create a deep copy for this item's log
                        import copy
                        schema_data = copy.deepcopy(base_schema_data)
                        schema_extra = copy.deepcopy(base_schema_extra)

                        # ============================================================
                        # 1. Basic IDs (Required)
                        # ============================================================
                        schema_data['productId'] = str(item.get('productId', ''))
                        schema_data['itemId'] = str(item.get('itemId', ''))
                        schema_data['vendorItemId'] = str(item.get('vendorItemId', ''))
                        schema_data['searchId'] = extracted_data.get('searchId', '')
                        schema_data['q'] = extracted_data.get('q', '')
                        schema_data['query'] = extracted_data.get('q', '')
                        schema_data['ixid'] = context.get('DEVICE', {}).get('ixid', '')

                        # ============================================================
                        # 2. Ranking & Display
                        # ============================================================
                        rank = str(item.get('rank', '0'))
                        schema_data['rank'] = rank
                        # searchRank is typically rank + 1 (1-based) or kept as 0-based index?
                        # App logs show rank 1 has searchRank 0. Let's align with observed data.
                        # Actually, usually searchRank is 0-based index of organic items.
                        # For simplicity, we can use rank as rough proxy or item.get('searchRank') if captured.
                        schema_data['searchRank'] = str(max(0, int(rank) - 1)) # Approx heuristic based on observation

                        for k, v in list(schema_data.items()):
                            if isinstance(v, str) and v.startswith('${'):
                                if 'is' in k.lower() or k.startswith('has'):
                                    schema_data[k] = 'False'
                                elif 'Count' in k or 'Number' in k or 'price' in k.lower():
                                    schema_data[k] = '0'
                                else:
                                    schema_data[k] = ''

                            if isinstance(v, str) and v.startswith('${'):
                                schema_extra[k] = ''
                        
                        # [156_P Fix] Hydrate Extra from extracted extraLoggingValues
                        if item.get('srp_extra_raw'):
                            # Filter out 'None' strings or actual None
                            cleaned_extra = {k: v for k, v in item['srp_extra_raw'].items() if v is not None}
                            schema_extra.update(cleaned_extra)

                        # ============================================================
                        # 4. Product Display Data (from item wrapper)
                        # ============================================================
                        schema_data['isAds'] = 'true' if item.get('isAds') else ''
                        schema_data['adIcon'] = 'true' if item.get('isAds') else ''
                        
                        # Pricing
                        if item.get('salesPrice'):
                            schema_data['salesPrice'] = str(item['salesPrice'])
                            schema_data['isSalesPriceVisible'] = 'true'
                        if item.get('finalPrice'):
                            schema_extra['finalPrice'] = str(item['finalPrice'])
                            
                        # Badges & Delivery
                        if item.get('isRocket'):
                            schema_data['rocketType'] = 'ROCKET' # Default
                            if item.get('rocketType'):
                                 schema_data['rocketType'] = item['rocketType'] 
                        
                        schema_data['isFreeDelivery'] = 'true' if item.get('isFreeDelivery') else ''

                        # Rating
                        if item.get('ratingCount'):
                            schema_data['ratingCountString'] = f"({item['ratingCount']})"
                            schema_extra['ratingCount'] = f"({item['ratingCount']})"
                        
                        if item.get('rating'):
                            schema_data['ratingAverageString'] = str(item['rating'])
                            schema_extra['ratingAverage'] = str(item['rating'])

                        # Promise Date
                        if item.get('promiseDate'):
                            schema_data['promiseDeliveryDate'] = item['promiseDate']
                            schema_extra['pddMessage'] = item['promiseDate']
                            schema_data['isPddVisible'] = 'true'

                        # ============================================================
                        # 5. Append to UNIT_LOGS list
                        # ============================================================
                        context['RESULT']['META']['UNIT_LOGS'].append({
                            'schemaId': 14741,
                            'version': 36,
                            'data': schema_data,
                            'extra': schema_extra
                        })
                    
                print(f"[128] Hydrated {len(context['RESULT']['META'].get('UNIT_LOGS', []))} Unit Impression Logs.")


            # Export the exact URL used for 133
            extracted_data['searchRequestUrl'] = url

            # RESTORED: Check for pvId and keywordType in rData (Recursive Search)
            def find_keys(obj, path=""):
                results = {}
                if isinstance(obj, dict):
                    for k, v in obj.items():
                        if k.lower() == 'pvid' and 'pvid' not in results:
                            results['pvid'] = v
                        if k == 'keywordType' and 'keywordType' not in results:
                             results['keywordType'] = v
                        
                        if isinstance(v, (dict, list)):
                            child_res = find_keys(v, f"{path}.{k}" if path else k)
                            results.update(child_res)
                elif isinstance(obj, list):
                    for i, item in enumerate(obj):
                        child_res = find_keys(item, f"{path}[{i}]")
                        results.update(child_res)
                return results

            found_keys = find_keys(r_data)
            found_pvid = found_keys.get('pvid')
            found_keyword_type = found_keys.get('keywordType')

            if found_keyword_type:
                extracted_data['keywordType'] = str(found_keyword_type)
            else:
                extracted_data['keywordType'] = 'FOOD' # Default fallback


            # RESTORED: Extract AB Test ID and Group
            srp_ab_test_id = None
            srp_ab_group = None

            def find_ab_data(obj):
                if isinstance(obj, dict):
                    # Look for extraLoggingValues which often contains both
                    if 'extraLoggingValues' in obj:
                        extra = obj['extraLoggingValues']
                        if 'abTestIds' in extra and 'abGroups' in extra:
                            return extra['abTestIds'], extra['abGroups']
                    
                    for k, v in obj.items():
                        if isinstance(v, (dict, list)):
                            res = find_ab_data(v)
                            if res: return res
                elif isinstance(obj, list):
                    for item in obj:
                        res = find_ab_data(item)
                        if res: return res
                return None

            ab_data = find_ab_data(r_data)
            if ab_data:
                ids = str(ab_data[0]).split(',')
                groups = str(ab_data[1]).split(',')
                
                if ids and groups and len(ids) > 0:
                    extracted_data['srp_abTestId'] = ids[0].strip()
                    if len(groups) >= 1:
                        extracted_data['srp_abGroup'] = groups[0].strip()
                    else:
                        extracted_data['srp_abGroup'] = 'NOT_APPLICABLE'

                    print(f"[128] Found AB Test: {extracted_data.get('srp_abTestId')} / {extracted_data.get('srp_abGroup')}")

            # found_pvid is already extracted above by find_keys
            if found_pvid:
                extracted_data['srp_pvId'] = str(found_pvid)
            else:
                 # Generate random pvId for SRP (Client-side generation)
                 import random
                 random_pv_id = str(random.randint(10000000, 99999999))
                 extracted_data['srp_pvId'] = random_pv_id
                 print(f"[128] Generated Client-side SRP pvId: {random_pv_id}")
            
            extracted_data['searchRequestUrl'] = url

            # Store in RESULT > SEARCH (전체 SRP 데이터)
            context['RESULT']['SEARCH'] = extracted_data

            print(f"[128] Extracted Data: {list(extracted_data.keys())}")
            print(f"[128] RESULT.TARGET: {context['RESULT'].get('TARGET', {})}")

            # RESULT > ROOT: API 호출에 필요한 필수 값들
            context['RESULT']['ROOT'] = {
                'productId': extracted_data.get('productId'),
                'itemId': extracted_data.get('itemId'),
                'vendorItemId': extracted_data.get('vendorItemId'),
                'itemProductId': extracted_data.get('itemProductId'),
                'searchId': extracted_data.get('searchId'),
                'searchCount': extracted_data.get('searchCount'),
                'keywordType': extracted_data.get('keywordType'),
            }
            print(f"[128] RESULT.ROOT: {context['RESULT'].get('ROOT', {})}")
            return {}

        except Exception as e:
            print(f"[128] Extraction Error: {e}")
            raise e

    else:
        # response is None or status != 200
        status = response.status_code if response else "None"
        error_msg = f"[128] Request Failed. Status: {status}"
        print(error_msg)
        raise RuntimeError(error_msg)

    return {}
