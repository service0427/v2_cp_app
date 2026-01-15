import sys
import os
import json
import logging

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.log_manager.scenario import ScenarioManager

# Mock Context
mock_context = {
    'DEVICE': {
        'pcid': 'TEST_PCID_12345',
        'model': 'Galaxy S24',
        'os_version': '14',
        'device_uuid': 'TEST_UUID_9999',
        'app_session_id': 'TEST_SESSION_8888',
        'width': 1080,
        'height': 2400
    },
    'INPUT': {
        'q': '나이키'
    },
    'RESULT': {
        'ROOT': {
            'productId': '123456789',
            'searchId': 'SEARCH_ID_111',
            'itemId': '987654321',
            'vendorItemId': '55555'
        },
        'SEARCH': {
            'srp_rank': 1,
            'internalCategoryId': '123',
            'searchCount': 1000,
            'srp_ratingAverage': 4.5
        }
    },
    'PERFORMANCE': {
        'totalFrameCount': 120
    }
}

def test_engine():
    print(">>> Testing Data-Driven Schema Engine...")
    
    manager = ScenarioManager(mock_context)
    payloads = manager.execute_scenario('search_product_click')
    
    print(f"\n[Generated {len(payloads)} Logs]")
    
    for i, p in enumerate(payloads):
        schema_id = p['meta']['schemaId']
        print(f"\n--- Log #{i+1} (Schema {schema_id}) ---")
        print(json.dumps(p, indent=2, ensure_ascii=False))
        
        # Validation
        if schema_id == 124:
            assert p['data']['q'] == '나이키', "Schema 124 'q' mismatch"
            assert p['data']['productId'] == '123456789', "Schema 124 'productId' mismatch"
            print("✅ Schema 124 Validated")
        elif schema_id == 152:
            assert p['data']['rank'] == 1, "Schema 152 'rank' mismatch"
            print("✅ Schema 152 Validated")
        elif schema_id == 9453:
            assert p['data']['totalFrameCount'] == 120, "Schema 9453 'totalFrameCount' mismatch"
            print("✅ Schema 9453 Validated")

if __name__ == "__main__":
    test_engine()
