
import requests
import sys
import os
import json

# Add project root to path
sys.path.append("/home/tech/v2_cp_app")

import importlib
test_module = importlib.import_module("lib.schedule.128_G_v3_SEARCH_products")
run = test_module.run

# Mock Context
context = {
    'INPUT': {
        'q': '호박식혜 달빛',
        'productId': '9183773210' # Example from log
    },
    'DEVICE': {
        'ixid': 'test-ixid-12345'
    },
    'RESULT': {
        'META': {'SEARCH': {}},
        'SEARCH': {},
        'ROOT': {}
    }
}

session = requests.Session()
# Run the script
run(session, context)

# Check if Schema 14741 exists in META
found = False
for key, val in context['RESULT']['META']['SEARCH'].items():
    if key.startswith('14741'):
        found = True
        print(f"Schema {key} found: {json.dumps(val, ensure_ascii=False)[:200]}...")

if not found:
    print("Schema 14741 NOT FOUND in context.")
else:
    print("Schema 14741 FOUND.")
