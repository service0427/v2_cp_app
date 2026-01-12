import json
import os
import re
import sys
from urllib.parse import urlparse

# Ensure project root is in path to import lib
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib.device_profile import DEFAULT_PROFILE

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "requests_data.json")
SCHEDULE_DIR = os.path.join(BASE_DIR, "lib", "schedule")

TEMPLATE = """import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: {index}
# Method: {method}
#
# Original Headers (Comparison):
# ------------------------------
{original_headers}
# ------------------------------

def run(session: requests.Session):
    url = "{url}"
    method = "{method}"
    
    headers = {headers_repr}
    
    body = {body_repr}
    
    return run_request(session, method, url, headers, body)
"""

class RawCode:
    def __init__(self, code):
        self.code = code
    def __repr__(self):
        return self.code

def pretty_repr(obj, indent=0):
    """
    Custom pretty printer that handles RawCode and formats dicts/lists nicely.
    """
    indent_str = "    " * indent
    next_indent_str = "    " * (indent + 1)
    
    if isinstance(obj, dict):
        if not obj:
            return "{}"
        items = []
        for k, v in obj.items():
            formatted_v = pretty_repr(v, indent + 1)
            items.append(f'{next_indent_str}{repr(k)}: {formatted_v}')
        return "{\n" + ",\n".join(items) + f"\n{indent_str}}}"
    
    elif isinstance(obj, list):
        if not obj:
            return "[]"
        items = []
        for item in obj:
            formatted_item = pretty_repr(item, indent + 1)
            items.append(f'{next_indent_str}{formatted_item}')
        return "[\n" + ",\n".join(items) + f"\n{indent_str}]"
    
    elif isinstance(obj, RawCode):
        return obj.code
        
    else:
        return repr(obj)

def replace_with_profile(data):
    if isinstance(data, dict):
        return {k: replace_with_profile(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [replace_with_profile(v) for v in data]
    elif isinstance(data, str):
        # Direct matches
        if data == DEFAULT_PROFILE.model:
            return RawCode("DEFAULT_PROFILE.model")
        if data == DEFAULT_PROFILE.user_agent:
            return RawCode("DEFAULT_PROFILE.user_agent")
        if data == DEFAULT_PROFILE.os_version:
             return RawCode("DEFAULT_PROFILE.os_version")
        if data == DEFAULT_PROFILE.app_version_name:
             return RawCode("DEFAULT_PROFILE.app_version_name")
        if data == DEFAULT_PROFILE.pcid:
             return RawCode("DEFAULT_PROFILE.pcid")
        if data == DEFAULT_PROFILE.uuid:
             return RawCode("DEFAULT_PROFILE.uuid")
        if data == f"{DEFAULT_PROFILE.width}x{DEFAULT_PROFILE.height}":
             return RawCode('f"{DEFAULT_PROFILE.width}x{DEFAULT_PROFILE.height}"')

        # Substring replacements (e.g. for coupang-app header)
        # Check if the string contains the PCID or UUID
        if DEFAULT_PROFILE.pcid in data or DEFAULT_PROFILE.uuid in data:
            # We need to construct an f-string representation
            # Escape existing braces for f-string
            safe_data = data.replace("{", "{{").replace("}", "}}")
            # Replace PCID with {DEFAULT_PROFILE.pcid}
            replaced_data = safe_data.replace(DEFAULT_PROFILE.pcid, "{DEFAULT_PROFILE.pcid}")
            
            # Replace UUID with {DEFAULT_PROFILE.uuid}
            if DEFAULT_PROFILE.uuid in replaced_data:
                replaced_data = replaced_data.replace(DEFAULT_PROFILE.uuid, "{DEFAULT_PROFILE.uuid}")
            
            # Helper for no-dash UUID if constructed from same logic
            uuid_no_dash = DEFAULT_PROFILE.uuid.replace("-", "")
            if uuid_no_dash in replaced_data:
                # We can't easily reference a variable for no-dash unless we add it to profile
                # But for now, let's just leave it or construct it if we want perfection.
                # User asked for 'f0b740d2-3447-3b2b-b118-d66257275f8f' specifically.
                # If the no-dash version appears, it might be better to replace it with 
                # {DEFAULT_PROFILE.uuid.replace('-', '')}
                replaced_data = replaced_data.replace(uuid_no_dash, "{DEFAULT_PROFILE.uuid.replace('-', '')}")

            # Also try to replace other variable parts within this string if possible
            if DEFAULT_PROFILE.model in replaced_data:
                 replaced_data = replaced_data.replace(DEFAULT_PROFILE.model, "{DEFAULT_PROFILE.model}")
            if DEFAULT_PROFILE.os_version in replaced_data:
                 replaced_data = replaced_data.replace(DEFAULT_PROFILE.os_version, "{DEFAULT_PROFILE.os_version}")
            if DEFAULT_PROFILE.app_version_name in replaced_data:
                 replaced_data = replaced_data.replace(DEFAULT_PROFILE.app_version_name, "{DEFAULT_PROFILE.app_version_name}")
            if DEFAULT_PROFILE.timezone in replaced_data:
                 replaced_data = replaced_data.replace(DEFAULT_PROFILE.timezone, "{DEFAULT_PROFILE.timezone}")
            if DEFAULT_PROFILE.density_dpi_name in replaced_data:
                 replaced_data = replaced_data.replace(DEFAULT_PROFILE.density_dpi_name, "{DEFAULT_PROFILE.density_dpi_name}")
            
            # Numeric values as strings
            if str(DEFAULT_PROFILE.width) in replaced_data:
                 replaced_data = replaced_data.replace(str(DEFAULT_PROFILE.width), "{DEFAULT_PROFILE.width}")
            if str(DEFAULT_PROFILE.height) in replaced_data:
                 replaced_data = replaced_data.replace(str(DEFAULT_PROFILE.height), "{DEFAULT_PROFILE.height}")
            if str(DEFAULT_PROFILE.density) in replaced_data:
                 replaced_data = replaced_data.replace(str(DEFAULT_PROFILE.density), "{DEFAULT_PROFILE.density}")
                 
            return RawCode(f"f'{replaced_data}'")
            
    elif isinstance(data, int):
        if data == DEFAULT_PROFILE.width:
             pass 
        if data == DEFAULT_PROFILE.app_version_code:
             return RawCode("DEFAULT_PROFILE.app_version_code")
             
    return data

def sanitize_filename(url, index):
    parsed = urlparse(url)
    path = parsed.path
    if not path or path == "/":
        name = "root"
    else:
        # Extract last part or meaningful name
        parts = [p for p in path.split('/') if p]
        if parts:
            name = parts[-1]
        else:
            name = "unknown"
            
    # Clean invalid chars
    name = re.sub(r'[^a-zA-Z0-9_]', '_', name)
    
    # Add index prefix (1-based for file name usually, but user used 001 for index 0)
    # 001_entrance (Index 0)
    # 002_variable_templates (Index 1)
    # So file prefix is Index + 1
    file_idx = index + 1
    filename = f"{file_idx:03d}_{name}.py"
    return filename

def generate():
    if not os.path.exists(SCHEDULE_DIR):
        os.makedirs(SCHEDULE_DIR)
        
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
        
    print(f"Found {len(data)} requests.")
    
    for i, req in enumerate(data):
        # Skip 0 and 1 as they are already customized/implemented
        if i < 2:
            continue
            
        # Filename Generation Logic
        # Format: {index:03d}_{PREFIX}_{name}.py
        file_idx = i + 1
        
        headers = req.get('headers', {})
        body = req.get('body')

        # Determine Prefix (SKIP or METHOD)
        skip_indices = [66, 167, 187]
        if file_idx in skip_indices:
             prefix = "S"
        else:
             # prefix = req['method'].upper()
             m = req['method'].upper()
             if m == "GET":
                 prefix = "G"
             elif m == "POST":
                 prefix = "P"
             else:
                 prefix = m # Fallback

        # Sanitize Name
        parsed = urlparse(req['url'])
        path = parsed.path
        if not path or path == "/":
            name = "root"
        else:
            parts = [p for p in path.split('/') if p]
            name = parts[-1] if parts else "unknown"
        name = re.sub(r'[^a-zA-Z0-9_]', '_', name)
        
        # Determine Version (v2, v3, etc.)
        version = ""
        if "/v1/" in path:
            version = "v1"
        elif "/v2/" in path:
            version = "v2"
        elif "/v3/" in path:
            version = "v3"
        elif "/v4/" in path:
            version = "v4"

        # Determine Action (MAIN, SEARCH, PRODUCT)
        action = ""
        if "/home/main" in path:
            action = "MAIN"
        elif re.search(r'/products/\d+', path) or "sdp" in path:
            action = "PRODUCT"
        elif "search" in path or ("products" in path):
            action = "SEARCH"

        # Extract Event Names (for bulksubmit/tracking)
        event_names = []
        if body:
            if isinstance(body, list):
                for item in body:
                    if isinstance(item, dict) and 'data' in item:
                        e_name = item['data'].get('eventName')
                        if e_name:
                            event_names.append(e_name)
            elif isinstance(body, dict):
                 if 'data' in body:
                    e_name = body['data'].get('eventName')
                    if e_name:
                        event_names.append(e_name)
        
        # Construct Filename
        parts_list = [f"{file_idx:03d}", prefix]
        if version:
            parts_list.append(version)
        if action:
            parts_list.append(action)
        
        # Add events
        if event_names:
            # Sanitize and join
            sanitized_events = [re.sub(r'[^a-zA-Z0-9]', '', e) for e in event_names]
            events_str = "_".join(sanitized_events)
            
            # Truncate if too long (max 100 chars for events part)
            if len(events_str) > 100:
                events_str = events_str[:100] + "_etc"
                
            if events_str:
                parts_list.append(events_str)

        parts_list.append(name)
        
        filename = "_".join(parts_list) + ".py"
        filepath = os.path.join(SCHEDULE_DIR, filename)
        
        step_name = filename[:-3]

        
        # Inject Profile Vars - REVERTED to hardcoded as requested
        # headers_processed = replace_with_profile(headers)
        # body_processed = replace_with_profile(body)
        headers_processed = headers
        body_processed = body
        
        # Prepare Original Headers for Comment
        original_headers_repr = pretty_repr(headers, indent=0)
        # Add comment hash to every line
        original_headers_commented = "\n".join([f"# {line}" for line in original_headers_repr.split('\n')])

        content = TEMPLATE.format(
            index=i,
            method=req['method'],
            url=req['url'],
            original_headers=original_headers_commented,
            headers_repr=pretty_repr(headers_processed, indent=1), # Start indentation at 1 level
            body_repr=pretty_repr(body_processed, indent=1)
        )
        
        with open(filepath, 'w') as f:
            f.write(content)
            
        print(f"Generated: {filename}")

if __name__ == "__main__":
    generate()
