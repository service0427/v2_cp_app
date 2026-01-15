#!/usr/bin/env python3
import json
import os
import sys
import argparse
from urllib.parse import urlparse, parse_qs, unquote
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
        
        filter_param = params.get('filter', [''])[0]
        keyword = "unknown_keyword"
        if 'KEYWORD:' in filter_param:
            start = filter_param.find('KEYWORD:') + len('KEYWORD:')
            end = filter_param.find('|', start)
            if end == -1: end = len(filter_param)
            keyword = filter_param[start:end]
            keyword = unquote(keyword)

        search_id = None
        if response_body and isinstance(response_body, dict):
             r_data = response_body.get('rData', {})
             search_id = r_data.get('searchId')

        return {
            'type': '128_SEARCH',
            'keyword': keyword,
            'searchId': search_id,
            'ts': request.get('ts')
        }
    except Exception as e:
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
                search_id = data.get('searchId')
                product_id = data.get('productId')
                if search_id and product_id: break
        
        if found_schema and search_id and product_id:
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
    Classify request into one of the known types or return GENERIC.
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
    if method == 'GET' and '/sdp/v2/platform/products/' in path:
        try:
            parts = path.split('/products/')
            if len(parts) > 1:
                pid = parts[1].split('?')[0].split('/')[0]
                return '145_DETAIL', {'productId': pid, 'ts': req.get('ts')}
        except:
             pass

    # 3. BULKSUBMIT Handlers
    if method == 'POST' and 'bulksubmit' in path:
        if has_schema(body, ['124']):
            clicked = extract_click_data(req)
            if clicked: return '147_CLICK', clicked
        if has_schema(body, ['10']):
            return '179_CART', {'ts': req.get('ts')}
        if has_schema(body, ['13697', '14741']):
            return '156_UNIT_IMP', {'ts': req.get('ts')}
        if has_schema(body, ['15704', '116']):
            return '133_VIEW_IMP', {'ts': req.get('ts')}
            
    return 'GENERIC', {'method': method, 'path': path, 'ts': req.get('ts')}

# =============================================================================
# Formatter
# =============================================================================

def format_log_entry(req, resp):
    method = req.get('method')
    url = req.get('url')
    
    out = []
    out.append("=== REQUEST ===")
    out.append(f"{method} {url}")
    out.append("Headers:")
    if req.get('headers'):
        for k, v in req.get('headers').items():
            out.append(f"  {k}: {v}")
    
    if req.get('body'):
        out.append("Body:")
        try:
            out.append(json.dumps(req['body'], indent=2, ensure_ascii=False))
        except:
             out.append(str(req['body']))
    elif req.get('body_raw'):
        out.append("Body (Raw):")
        # Truncate if too long (e.g. image)
        if len(req['body_raw']) > 1000:
             out.append(req['body_raw'][:1000] + "... (TRUNCATED)")
        else:
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
            try:
                out.append(json.dumps(resp['body'], indent=2, ensure_ascii=False))
            except:
                 out.append(str(resp['body']))
        elif resp.get('body_raw'):
             if len(resp['body_raw']) > 1000:
                 out.append(resp['body_raw'][:1000] + "... (TRUNCATED)")
             else:
                 out.append(resp['body_raw'])
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
    print(f"Loaded {len(requests)} requests from JSON.")
    
    # 1. Indexing (Pair Req/Resp)
    pending_requests = {}
    paired_events = []
    
    for item in requests:
        host = item.get('host', '')
        path = item.get('path', '')
        key = (host, path)
        
        if item.get('type') == 'response':
            if key in pending_requests and pending_requests[key]:
                req = pending_requests[key].pop(0)
                paired_events.append({'req': req, 'resp': item})
            else:
                pass # Orphan response
        else:
            if key not in pending_requests:
                pending_requests[key] = []
            pending_requests[key].append(item)
            
    # Handle pending requests
    for key, req_list in pending_requests.items():
        for req in req_list:
             paired_events.append({'req': req, 'resp': None})

    print(f"Total Paired Events: {len(paired_events)}")
    paired_events.sort(key=lambda x: x['req'].get('ts', 0))
    
    # 2. Sequential Processing & Grouping
    # We want to keep folder structure: Keyword_ProductId/session/Date/Time
    # But now we capture ALL logs.
    
    sessions = {} # searchId -> SearchContext
    current_search_context = None
    current_interaction = None
    
    # Buffer for events before the first search (App Launch, Intro, etc.)
    initial_buffer = []

    for event in paired_events:
        req = event['req']
        resp = event.get('resp')
        resp_body = resp.get('body') if resp else None
        
        type_str, meta = identify_request_type(req, resp_body)
        data = meta
        
        event['type'] = type_str
        event['data'] = meta
        
        # Decide Context Switching
        if type_str == '128_SEARCH':
            sid = meta.get('searchId')
            if sid:
                # NEW SESSION START
                new_ctx = {
                    'searchId': sid,
                    'keyword': data.get('keyword', 'UNKNOWN'),
                    'events': [], # Search & Generic events
                    'interactions': []
                }
                
                # If we have initial buffered events (Pre-Search), attach them here
                if initial_buffer:
                    # Prepend initial events
                    new_ctx['events'].extend(initial_buffer)
                    initial_buffer = [] # Clear buffer so it's not added again
                
                # Add this search event itself
                new_ctx['events'].append(event)
                
                sessions[sid] = new_ctx
                current_search_context = new_ctx
                current_interaction = None # Reset interaction on new search
                continue

        elif type_str == '147_CLICK':
            # NEW INTERACTION START
            sid = data.get('searchId')
            pid = data.get('productId')
            
            # Allow linking to previous session if sid matches, else use current
            ctx = sessions.get(sid)
            if not ctx: ctx = current_search_context
            
            # Create new interaction
            interaction = {
                'productId': pid,
                'events': [] # Click & subsequent generic/detail events
            }
            # Initialize with this click event
            interaction['events'].append(event)
            
            if ctx:
                ctx['interactions'].append(interaction)
                current_interaction = interaction
                current_search_context = ctx # Ensure we are on this context
            else:
                # Click without search context? Should ideally not happen in this flow or go to buffer
                # But typically means we track it generally if no search yet
                initial_buffer.append(event)
                
            continue
            
        # Logic for other events (Specific or Generic)
        if current_search_context:
            if current_interaction:
                # If we are inside an interaction (Product Clicked), everything goes here
                # UNLESS it's a new search (handled above)
                current_interaction['events'].append(event)
            else:
                # If we are in a search session but not yet clicked (or returned to list)
                current_search_context['events'].append(event)
        else:
            # No search session yet -> Add to buffer
            initial_buffer.append(event)


    # 3. Output Generation
    print(f"Generating full capture logs in {output_base}")
    
    for sid, ctx in sessions.items():
        if not ctx['events'] and not ctx['interactions']:
            continue
            
        keyword = ctx['keyword']
        
        # Determine Main folder name
        # If there are interactions, pick the first one's PID for folder name (closest to original logic)
        # If no interactions, just Keyword_None
        pid_label = "General"
        if ctx['interactions']:
            pid_label = ctx['interactions'][0]['productId']
            
        safe_keyword = "".join([c if c.isalnum() else "_" for c in keyword])
        folder_name = f"{safe_keyword}_{pid_label}"
        
        # Determine Timestamp (first event in session)
        first_ts = 0
        if ctx['events']:
            first_ts = ctx['events'][0]['req'].get('ts', 0)
        elif ctx['interactions']:
            first_ts = ctx['interactions'][0]['events'][0]['req'].get('ts', 0)
            
        if first_ts == 0: first_ts = datetime.now().timestamp()
            
        dt = datetime.fromtimestamp(first_ts)
        date_str = dt.strftime("%Y%m%d")
        time_str = dt.strftime("%H%M%S")
        
        session_dir = os.path.join(output_base, f"{safe_keyword}_{pid_label}", "session_full", date_str, time_str)
        os.makedirs(session_dir, exist_ok=True)
        
        print(f"  -> {session_dir}")
        seq = 1
        
        def write_event(evt):
            nonlocal seq
            type_label = evt['type']
            # Simplify label for generic
            if type_label == 'GENERIC':
                method = evt['data']['method']
                path = evt['data']['path']
                # clean path
                path_clean = path.split('?')[0].replace('/', '_')
                if len(path_clean) > 50: path_clean = path_clean[:50]
                if not path_clean: path_clean = "_root"
                filename = f"{seq:03d}_{method}{path_clean}.log"
            else:
                # Keep known names but add seq
                filename = f"{seq:03d}_{type_label}.log"
                
            path = os.path.join(session_dir, filename)
            content = format_log_entry(evt['req'], evt['resp'])
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            seq += 1

        # 1. Write Pre-Interaction Events (Search, View Imp, Generics)
        for evt in ctx['events']:
            write_event(evt)
            
        # 2. Write Interaction Events
        for interaction in ctx['interactions']:
            # Maybe add a separator file or just sequence? Sequence is enough.
            for evt in interaction['events']:
                 write_event(evt)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='Path to input JSON capture file')
    parser.add_argument('--output', required=True, help='Base path for output directories')
    args = parser.parse_args()
    
    process_capture(args.input, args.output)
