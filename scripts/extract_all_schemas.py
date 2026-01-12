import os
import json

LOG_DIR = "/home/tech/v2_cp_app/logs/session/20260112/004353-backup"
OUTPUT_FILE = "/home/tech/v2_cp_app/logs/session/20260112/004353-backup/ALL_META.log"

def extract_schemas(obj, results):
    """Recursively find all schemas in response"""
    if isinstance(obj, dict):
        # Check for bypass schemas
        if 'bypass' in obj:
            bypass = obj['bypass']
            if isinstance(bypass, dict):
                if 'exposureSchema' in bypass:
                    store_schema(bypass['exposureSchema'], results)
                if 'clickSchemas' in bypass:
                    for s in bypass['clickSchemas']:
                        store_schema(s, results)

        # Check direct schema keys
        if 'exposureSchema' in obj:
            store_schema(obj['exposureSchema'], results)
        if 'clickSchemas' in obj and isinstance(obj['clickSchemas'], list):
            for s in obj['clickSchemas']:
                store_schema(s, results)

        # Recurse
        for k, v in obj.items():
            if isinstance(v, (dict, list)):
                extract_schemas(v, results)

    elif isinstance(obj, list):
        for item in obj:
            extract_schemas(item, results)

def store_schema(schema, results):
    """Store schema with composite key"""
    if not isinstance(schema, dict):
        return

    s_id = str(schema.get('id', ''))
    if not s_id:
        s_id = str(schema.get('schemaId', ''))
    version = str(schema.get('version', ''))

    if s_id and version:
        meta_key = f"{s_id}_{version}"
        results[meta_key] = {
            'data': schema.get('mandatory', {}),
            'extra': schema.get('extra', {})
        }

def extract_json_from_log(content):
    """Extract JSON from log file (after === RESPONSE ===)"""
    marker = "=== RESPONSE ==="
    if marker in content:
        response_part = content.split(marker, 1)[1]
        # Find first { or [
        for i, c in enumerate(response_part):
            if c in '{[':
                return response_part[i:]
    return None

def main():
    all_meta = {}

    # Get all log files
    log_files = sorted([f for f in os.listdir(LOG_DIR) if f.endswith('.log') and f[0].isdigit()])

    for log_file in log_files:
        file_path = os.path.join(LOG_DIR, log_file)
        file_num = log_file.split('_')[0]  # e.g., "017"

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Skip if no clickSchemas
            if 'clickSchemas' not in content and 'exposureSchema' not in content:
                continue

            json_str = extract_json_from_log(content)
            if not json_str:
                continue

            data = json.loads(json_str)
            schemas = {}
            extract_schemas(data, schemas)

            if schemas:
                all_meta[file_num] = {
                    'file': log_file,
                    'schemas': schemas
                }
                print(f"[{file_num}] Found {len(schemas)} schemas: {list(schemas.keys())}")

        except Exception as e:
            print(f"[{log_file}] Error: {e}")

    # Save ALL_META.log
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(all_meta, f, indent=2, ensure_ascii=False)

    print(f"\nSaved to {OUTPUT_FILE}")
    print(f"Total files with schemas: {len(all_meta)}")

if __name__ == "__main__":
    main()
