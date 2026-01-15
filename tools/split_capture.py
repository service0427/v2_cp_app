#!/usr/bin/env python3
import json
import os
import sys
import argparse
from urllib.parse import urlparse, parse_qs
from datetime import datetime

# =============================================================================
# Helper: Extract Key Data from Scenarios
# =============================================================================

def extract_search_data(request, response_body):
    """
    Type 128 (Search): GET .../products?
    Extract: keyword (from URL), searchId (from Response)
    """
    try:
        url = request.get('url', '')
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        
        # Keyword extraction logic: filter=KEYWORD:encoded|...
        # Example: filter=KEYWORD:%EB%85%B8%ED%8A%B8%EB%B6%81|...
        filter_param = params.get('filter', [''])[0]
        keyword = "unknown_keyword"
        if 'KEYWORD:' in filter_param:
            # Extract between KEYWORD: and |
            start = filter_param.find('KEYWORD:') + len('KEYWORD:')
            end = filter_param.find('|', start)
            if end == -1: end = len(filter_param)
            keyword = filter_param[start:end]
            # URL Decode is handled by parse_qs but 'filter' value itself might need extra handling if it was double encoded or raw. 
            # Actually parse_qs decodes the value of 'filter'. 
            # But the value inside 'KEYWORD:...' usually comes URL-encoded in the capture.
            # Let's simple unquote it just in case.
            from urllib.parse import unquote
            keyword = unquote(keyword)

        search_id = None
        if response_body and isinstance(response_body, dict):
             r_data = response_body.get('rData', {})
             # searchId might be in rData directly or deeper
             # Based on previous analysis (128_G...py):
             # searchId = extracted_data.get('searchId')
             # It seems typically at the top level of rData for V3 search
             search_id = r_data.get('searchId')

        return {
            'type': '128_SEARCH',
            'keyword': keyword,
            'searchId': search_id,
            'ts': request.get('ts')
        }
    except Exception as e:
        # print(f"Error parsing 128: {e}")
        return None

def extract_click_data(request):
    """
    Type 147 (Click): POST /api/v2/bulksubmit with Schema 124
    Extract: searchId, productId
    """
    try:
        body = request.get('body')
        if not body or not isinstance(body, list): return None
        
        found_schema = False
        search_id = None
        product_id = None
        
        for log in body:
            meta = log.get('meta', {})
            data = log.get('data', {})
            schema_id = str(meta.get('schemaId'))
            
            if schema_id == '124':
                found_schema = True
                # Extract searchId and productId
                search_id = data.get('searchId')
                product_id = data.get('productId')
                # If valid data found, break or continue? Usually one click per request.
                if search_id and product_id: break
        
        if found_schema and search_id and product_id:
             return {
                'type': '147_CLICK',
                'searchId': search_id,
                'productId': product_id,
                'ts': request.get('ts')
            }
        elif found_schema:
             # Schema found but missing ID might be interesting to log
             return {
                'type': '147_CLICK',
                'searchId': search_id,
                'productId': product_id,
                'ts': request.get('ts')
             }
        return None
    except Exception as e:
        return None

def identify_request_type(req, resp_body):
    """
    Classify request into one of the 6 types.
    Returns: (TypeString, MetadataDict)
    """
    method = req.get('method', '')
    url = req.get('url', '')
    path = req.get('path', '')
    body = req.get('body')
    
    # helper for bulksubmit schema checking
    def has_schema(body_list, schema_ids):
        if not isinstance(body_list, list): return False
        for item in body_list:
            sid = str(item.get('meta', {}).get('schemaId', ''))
            if sid in schema_ids: return True
        return False

    # 1. SEARCH (128)
    if method == 'GET' and '/products' in path and 'filter=KEYWORD' in url:
        data = extract_search_data(req, resp_body)
        if data and data['searchId']:
            return '128_SEARCH', data
            
    # 2. DETAIL (145)
    # URL pattern: .../sdp/v2/platform/products/{id}
    # Targeted native API call.
    if method == 'GET' and '/sdp/v2/platform/products/' in path:
        # Extract ProductId from Path
        try:
            # /path/.../products/9221117836?...
            parts = path.split('/products/')
            if len(parts) > 1:
                # 9221117836?searchId=...
                pid_part = parts[1]
                # remove query params matching if any (though path usually has param in split capturing, sometimes logic varies)
                # In this specific split utility, 'path' might include query depending on parsing.
                # But logical splitting usually splits by slash. 
                # Let's simple split by '?' just in case.
                pid = pid_part.split('?')[0].split('/')[0]
                return '145_DETAIL', {'productId': pid, 'ts': req.get('ts')}
        except:
             pass

    # 3. BULKSUBMIT Handlers
    if method == 'POST' and 'bulksubmit' in path:
        if has_schema(body, ['124']):
            # CLICK (147)
            # We re-parse to get details
            clicked = extract_click_data(req)
            if clicked: return '147_CLICK', clicked
            
        if has_schema(body, ['10']):
            # CART (179) - Schema 10 is SdpAddToCart
            return '179_CART', {'ts': req.get('ts')}
            
        if has_schema(body, ['13697', '14741']):
            # UNIT IMPRESSION (156)
            return '156_UNIT_IMP', {'ts': req.get('ts')}
            
        if has_schema(body, ['15704', '116']):
            # VIEW IMPRESSION (133)
            return '133_VIEW_IMP', {'ts': req.get('ts')}

    return 'UNKNOWN', None

# =============================================================================
# Formatter
# =============================================================================

def format_log_entry(req, resp):
    """
    Format request/response into the target text format.
    """
    # Reconstruct Request Line
    method = req.get('method')
    url = req.get('url')
    
    out = []
    out.append("=== REQUEST ===")
    out.append(f"{method} {url}")
    out.append("Headers:")
    if req.get('headers'):
        for k, v in req.get('headers').items():
            out.append(f"  {k}: {v}")
    
    # Request Body
    if req.get('body'):
        out.append("Body:")
        out.append(json.dumps(req['body'], indent=2, ensure_ascii=False))
    elif req.get('body_raw'):
        out.append("Body:")
        out.append(req['body_raw'])
        
    out.append("")
    out.append("=== RESPONSE ===")
    if resp:
        out.append(f"Status: {resp.get('status')}")
        out.append("Headers:")
        if resp.get('headers'):
            for k, v in resp.get('headers').items():
                out.append(f"  {k}: {v}")
        out.append("Body:")
        if resp.get('body'):
            out.append(json.dumps(resp['body'], indent=2, ensure_ascii=False))
    else:
        out.append("Status: (No Response Parsed)")
        
    return "\n".join(out)

# =============================================================================
# Main Logic
# =============================================================================

def process_capture(input_file, output_base):
    print(f"Loading capture: {input_file}")
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    requests = data.get('requests', [])
    
    # 1. Indexing (Pair Req/Resp) using Queue
    # Key: (host, path) -> List[RequestObject] (FIFO queue)
    pending_requests = {}
    paired_events = []
    
    unpaired_req_count = 0
    unpaired_resp_count = 0

    for item in requests:
        # Normalize Key: (host, path)
        host = item.get('host', '')
        path = item.get('path', '')
        key = (host, path)
        
        if item.get('type') == 'response':
            # Try to pop matching request
            if key in pending_requests and pending_requests[key]:
                req = pending_requests[key].pop(0)
                paired_events.append({'req': req, 'resp': item})
            else:
                # Orphan response
                unpaired_resp_count += 1
        else:
            # Request
            if key not in pending_requests:
                pending_requests[key] = []
            pending_requests[key].append(item)
            
    # Handle remaining pending requests (no response captured)
    for key, req_list in pending_requests.items():
        for req in req_list:
             paired_events.append({'req': req, 'resp': None})
             unpaired_req_count += 1

    print(f"Paired {len(paired_events)} events. (Unpaired Reqs: {unpaired_req_count}, Unpaired Resps: {unpaired_resp_count})")
    
    # Sort paired events by Request Timestamp to ensure chronological processing
    paired_events.sort(key=lambda x: x['req'].get('ts', 0))
    
    # 2. Classification & Context Building
    
    # 2. Classification & Context Building
    
    sessions = {} # searchId -> SearchContext
    
    # Logic: Items after a Click belong to that Click until a new Click occurs? 
    # Or strictly by Timestamp?
    # Simple strategy: Current active interaction.
    current_search_context = None
    current_interaction = None
    
    # Buffer for Detail events that might arrive BEFORE the Click log (due to batching)
    pending_details = []
    
    # Validation counters
    search_count = 0
    interaction_count = 0
    
    for event in paired_events:
        req = event['req']
        resp = event.get('resp')
        resp_body = resp.get('body') if resp else None
        
        type_str, meta = identify_request_type(req, resp_body)
        data = meta
        
        event['type'] = type_str
        event['data'] = meta # Use 'data' to match loop usage
        
        if type_str == '128_SEARCH':
            sid = meta.get('searchId')
            # Fix: Ensure sid is string
            if sid:
                current_search_context = {
                    'searchId': sid,
                    'keyword': data.get('keyword', 'UNKNOWN'),
                    'events': [event], 
                    'interactions': [], 
                    'impressions': [], 
                    # pending_details is handled globally, but we could scope it here if we wanted.
                    # But for now, global 'pending_details' logic is fine.
                }
                sessions[sid] = current_search_context
                search_count += 1
                
        elif type_str == '133_VIEW_IMP' or type_str == '156_UNIT_IMP':
            if current_search_context:
                current_search_context['impressions'].append(event)
                
        elif type_str == '147_CLICK':
            sid = data.get('searchId')
            pid = data.get('productId')
            
            # Find context
            ctx = sessions.get(sid)
            if not ctx and current_search_context:
                 # Fallback to current if searchId missing or not found
                 ctx = current_search_context
            
            if ctx:
                # Create new interaction
                interaction = {
                    'productId': pid,
                    'click_event': event,
                    'detail_events': [],
                    'cart_events': []
                }
                ctx['interactions'].append(interaction)
                current_interaction = interaction
                interaction_count += 1
                
                # Check pending details for this product
                claimed_indexes = []
                for i, p_item in enumerate(pending_details):
                    if p_item['pid'] == str(pid): # string comparison
                        interaction['detail_events'].append(p_item['event'])
                        claimed_indexes.append(i)
                
                # Remove claimed
                for i in sorted(claimed_indexes, reverse=True):
                    pending_details.pop(i)

        elif type_str == '145_DETAIL':
            pid = data.get('productId')
            
            # If current interaction matches this product, attach immediately
            if current_interaction and str(current_interaction['productId']) == str(pid):
                current_interaction['detail_events'].append(event)
            else:
                # Buffer it (Case: Detail happened before Click log)
                pending_details.append({'pid': str(pid), 'event': event})

        elif type_str == '179_CART':
            # Attach to current interaction
            if current_interaction:
                current_interaction['cart_events'].append(event)
            else:
                pass
                
    # 3. Output Generation
    print(f"Found {len(sessions)} Search Contexts.")
    print(f"Found {interaction_count} Product Interactions.")
    
    for ctx in sessions.values():
        keyword = ctx['keyword']
        
        for idx, interaction in enumerate(ctx['interactions']):
            pid = interaction['productId']
            
            # Format Folder Name: Keyword_ProductId
            # Sanitize keyword
            safe_keyword = "".join([c if c.isalnum() else "_" for c in keyword])
            folder_name = f"{safe_keyword}_{pid}"
            
            # Timestamp for 'session/YYYYMMDD/HHMMSS'
            # Use Click TS (or Detail TS if click missing timestamp?)
            ts = None
            if interaction.get('click_event'):
                ts = interaction['click_event']['req'].get('ts')
            
            if not ts: # Fallback if click event or its timestamp is missing
                # Try to get from first detail event if available
                if interaction['detail_events']:
                    ts = interaction['detail_events'][0]['req'].get('ts')
                else:
                    # Default to current time or 0 if no timestamp found
                    ts = datetime.now().timestamp() 
                
            dt = datetime.fromtimestamp(ts)
            date_str = dt.strftime("%Y%m%d")
            time_str = dt.strftime("%H%M%S")
            
            session_dir = os.path.join(output_base, f"{safe_keyword}_{pid}", "session", date_str, time_str)
            os.makedirs(session_dir, exist_ok=True)
            
            print(f"Generating logs in: {session_dir}")
            
            # Helper to write file
            def write_log(filename, event):
                path = os.path.join(session_dir, filename)
                content = format_log_entry(event['req'], event['resp'])
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
    
            # Write Context Logs (Search + Impressions)
            # Accessing context from 'ctx' directly
            # Search
            if ctx.get('events'): # Should be list
                 write_log("128_G_v3_SEARCH_products.log", ctx['events'][0])
            
            # Impressions
            view_imp_count = 0
            unit_imp_count = 0
            for evt in ctx['impressions']:
                etype = evt['type']
                if etype == '133_VIEW_IMP':
                    view_imp_count += 1
                    suffix = f"_{view_imp_count}" if view_imp_count > 1 else ""
                    write_log(f"133_P_v2_bulksubmit_srp_view_impression{suffix}.log", evt)
                elif etype == '156_UNIT_IMP':
                    unit_imp_count += 1
                    suffix = f"_{unit_imp_count}" if unit_imp_count > 1 else ""
                    write_log(f"156_P_v2_bulksubmit_srp_product_unit_impression{suffix}.log", evt)
    
            # Write Interaction Logs
            write_log("147_P_v2_bulksubmit_click_search_product.log", interaction['click_event'])
            
            for i, evt in enumerate(interaction['detail_events']):
                 suffix = f"_{i+1}" if i > 0 else ""
                 write_log(f"145_G_v1_PRODUCT{suffix}.log", evt)
                 
            for i, evt in enumerate(interaction['cart_events']):
                 suffix = f"_{i+1}" if i > 0 else ""
                 write_log(f"179_P_v2_bulksubmit_add_to_cart{suffix}.log", evt)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='Path to input JSON capture file')
    parser.add_argument('--output', required=True, help='Base path for output directories')
    args = parser.parse_args()
    
    process_capture(args.input, args.output)
