import json
import glob
import os

# Find latest 128 log
log_files = glob.glob("logs/session/*/*/*128_G_v3_SEARCH_products.log")
if not log_files:
    print("No log file found")
    exit(1)
latest_log = max(log_files, key=os.path.getctime)
print(f"Inspecting {latest_log}")

with open(latest_log, 'r') as f:
    content = f.read()

# Extract JSON body
try:
    start_idx = content.find('{', content.find('Body:'))
    json_str = content[start_idx:]
    data = json.loads(json_str)
except Exception as e:
    print(f"Failed to parse JSON: {e}")
    exit(1)

def find_display_item(obj, path=""):
    if isinstance(obj, dict):
        if 'displayItem' in obj and 'id' in obj['displayItem']:
            print(f"Found displayItem at {path} -> ID: {obj['displayItem']['id']}")
            return
        for k, v in obj.items():
            find_display_item(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            find_display_item(item, f"{path}[{i}]")

if 'rData' in data:
    find_display_item(data['rData']['entityList'], "rData.entityList")
else:
    print("No rData")
