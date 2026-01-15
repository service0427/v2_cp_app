import json
import re
import sys

def extract_schemas_from_capture(file_path):
    schemas = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for req in data.get('requests', []):
                if 'bulksubmit' in req.get('path', '') or 'bulksubmit' in req.get('url', ''):
                    # Check body
                    body = req.get('body')
                    if isinstance(body, list):
                        for item in body:
                            meta = item.get('meta', {})
                            if 'schemaId' in meta:
                                schemas.add(meta['schemaId'])
                    elif isinstance(body, str):
                         # sometimes body is stringified json? unlikely for bulksubmit but possible
                         pass
    except Exception as e:
        print(f"Error reading capture: {e}")
    return schemas

def extract_schemas_from_log(file_path):
    schemas = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Log format is custom blocks. We look for 'req_body' in logs for 'bulksubmit' URLs
        # Regex or simple parsing?
        # The log file seems to be '=== Header ===\n JSON' blocks.
        # Let's split by '=== ['
        
        blocks = re.split(r'=== \[.*?\] .*? ===', content)
        for block in blocks:
            if not block.strip(): continue
            try:
                # Find JSON part
                json_start = block.find('{')
                if json_start == -1: continue
                json_str = block[json_start:]
                entry = json.loads(json_str)
                
                req = entry.get('request', {})
                url = req.get('url', '')
                if 'bulksubmit' in url:
                    body = req.get('body')
                    if body and isinstance(body, list):
                        for item in body:
                            meta = item.get('meta', {})
                            if 'schemaId' in meta:
                                schemas.add(meta['schemaId'])
            except json.JSONDecodeError:
                continue
            except Exception:
                continue
                
    except Exception as e:
        print(f"Error reading log: {e}")
    return schemas

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compare Schemas')
    parser.add_argument('--real', required=True, help='Path to real capture JSON')
    parser.add_argument('--log', required=True, help='Path to simulation Log')
    args = parser.parse_args()

    real_path = args.real
    log_path = args.log

    print(f"Comparing:")
    print(f"  Real: {real_path}")
    print(f"  Log : {log_path}")

    real_schemas = extract_schemas_from_capture(real_path)
    log_schemas = extract_schemas_from_log(log_path)

    print(f"Real Schemas: {sorted(list(real_schemas))}")
    print(f"Log Schemas:  {sorted(list(log_schemas))}")

    missing = real_schemas - log_schemas
    extra = log_schemas - real_schemas

    print(f"Missing in Log: {sorted(list(missing))}")
    print(f"Extra in Log:   {sorted(list(extra))}")
