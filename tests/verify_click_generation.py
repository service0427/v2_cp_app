import sys
import os
import json
import logging

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.common.log_manager.manager import LogManager
from lib.common.log_manager.scenario import ScenarioManager

def verify_click_generation():
    print("Initializing ScenarioManager...")
    
    # Mock Context mimicking APK state after Search
    context = {
        'INPUT': {
            'q': '소파',
            'productId': 9158522812,
            'searchId': 'a458560f645321',  # Critical attribution
            'itemId': 26975668679,
            'vendorItemId': 93944527930,
            'itemProductId': 4,
            'rank': 27,
            # [Simulate 147_P Logic Injection]
            'searchIdCombined': 'a458560f645321:27',
            'abTestAttribute': 'srp,lowestpricein7days'
        },
        'RESULT': {
            'ROOT': {
                'productId': 9158522812,
                'searchId': 'a458560f645321',
                'itemId': 26975668679,
                'vendorItemId': 93944527930,
                'itemProductId': 4,
                'searchCount': 1000,
                'keywordType': 'FOOD'
            },
            'SEARCH': {
                'srp_rank': 27,
                'srp_finalPriceString': '539,750원',
                'srp_ratingCountString': '2',
                'srp_scaleType': 'FIT_CENTER',
                'srp_ratingAverage': '5.0',
                'srp_originalPrice': '890,000원',
                'srp_productName': '아이보리 소파',
                'srp_discountRate': '39%',
                'srp_abTestId': '85005',
                'srp_abGroup': 'A',
                'filterKey': 'GENDER_TAB:0',
                'searchViewType': 'GRID_2',
                'srp_isCoupick': True
            },
            'META': {
                'SEARCH': {
                    '124_53': {
                        'data': {}
                    }
                }
            }
        },
        'DEVICE': {
            'model': 'SM-A165N'
        }
    }

    # Initialize Manager
    manager = ScenarioManager(context)
    
    print("\nExecuting 'search_product_click' scenario...")
    logs = manager.execute_scenario("search_product_click")
    
    print(f"\nGenerated {len(logs)} logs.\n")
    
    # Validation Logic
    expected_schemas = {7960, 124, 7598, 9453, 152, 11942}
    found_schemas = set()
    
    for log in logs:
        meta = log.get('meta', {})
        schema_id = meta.get('schemaId')
        found_schemas.add(schema_id)
        
        print(f"[Schema {schema_id}]")
        print(json.dumps(log.get('data', {}), indent=2, ensure_ascii=False))
        
        # Verify Attribution Fields
        data = log.get('data', {})
        extra = log.get('extra', {})
        
        if schema_id == 7960:
            if extra.get('KEY_SEARCH_ID') == 'a458560f645321':
                print("  ✅ Schema 7960: SearchID verified")
            else:
                print(f"  ❌ Schema 7960: SearchID Mismatch ({extra.get('KEY_SEARCH_ID')})")

        if schema_id == 124:
            if data.get('searchId') == 'a458560f645321':
                print("  ✅ Schema 124: SearchID verified")
            else:
                print(f"  ❌ Schema 124: SearchID Mismatch ({data.get('searchId')})")
                
        if schema_id == 152:
            # 152 format: searchId:rank
            expected_sid_rank = 'a458560f645321:27'
            if data.get('searchId') == expected_sid_rank:
                 print("  ✅ Schema 152: SearchID:Rank verified")
            else:
                 print(f"  ❌ Schema 152: SearchID Mismatch ({data.get('searchId')})")

    print("\nSummary:")
    missing = expected_schemas - found_schemas
    if not missing:
        print("SUCCESS: All schemas generated correctly.")
    else:
        print(f"FAILURE: Missing schemas: {missing}")
        for s_id in found_schemas:
            print(f"Found: {s_id}")

if __name__ == "__main__":
    verify_click_generation()
