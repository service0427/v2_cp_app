import sys
import os
import json
import datetime

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.common.log_manager.scenario import ScenarioManager

def verify_cart_generation():
    print("Initializing ScenarioManager...")

    # Mock Context
    # This mimics the structure present when 179_P runs
    context = {
        "device": {
            "appCode": "coupang",
            "market": "KR",
             "osVersion": "15", 
             "model": "SM-A165N" 
        },
        "RESULT": {
            "SEARCH": {
                "srp_pvId": "TEST_PVID_12345"
            },
            "PRODUCT": {
                "sdp_traceId": "TEST_TRACE_123",
                "sdp_serverTime": 1736681055000,
                # In a real run, 145_G would populate this list
                "sdp_atc_click_schemas": [] 
            },
            # This is where 179_P normally falls back to if explicit schemas aren't found
            "META": {
                "PRODUCT": {
                    "10_77": {
                        "data": {
                            "productId": 12345,
                            "itemId": 67890,
                            "vendorItemId": 112233,
                            "quantity": 1,
                            "rank": 13,
                            "q": "샴푸",
                             "sdpVisitKey": "TEST_VISIT_KEY"
                        }
                    },
                    "11599_4": {
                         "data": {
                            "productId": 12345,
                            "quantity": 1
                         }
                    }
                }
            }
        },
        "INPUT": { # GenericSchema input wrapper would flatten this, but we'll manually prep INPUT for now
            "q": "샴푸",
            "sdpVisitKey": "TEST_VISIT_KEY",
            "searchId": "TEST_SEARCH_ID",
            "productId": 8208169672,
            "itemId": 14322466357,
            "vendorItemId": 81567090984,
            "quantity": 1,
            "srp_pvId": "TEST_PVID_12345",
            "sdp_traceId": "TEST_TRACE_123",
            "sdp_serverTime": 1736681055000,
            "price": 6110,
            "finalPrice": 6110,
            "rank": 13,
            "ratingCount": 100,
            "ratingAverage": 4.5,
            "searchRank": 1,
            "filterKey": "TEST_FILTER",
            "sourceType": "TEST_SOURCE",
            "itemProductId": 123,
            "offerCondition": "NEW",
            "isRlux": False,
            "isRocketMart": False,
            "rocketType": "Rocket",
            "isLoyaltyMember": False,
            "hasOptionTable": True,
            "brandId": 1234,
            "brandName": "TestBrand"
        }
    }

    manager = ScenarioManager(context)

    print("\nExecuting 'add_to_cart' scenario...")
    logs = manager.execute_scenario("add_to_cart")

    print(f"\nGenerated {len(logs)} logs.")
    
    # Verify each schema
    found_schemas = {10: False, 15989: False, 11599: False, 14044: False}
    
    for log in logs:
        schema_id = log.get('meta', {}).get('schemaId')
        print(f"\n[Schema {schema_id}]")
        print(json.dumps(log['data'], indent=2, ensure_ascii=False))
        
        if schema_id in found_schemas:
            found_schemas[schema_id] = True
            
            # Specific assertions
            if schema_id == 10:
                if log['data'].get('q') == "샴푸" and log['data'].get('sdpVisitKey') == "TEST_VISIT_KEY":
                     print("  ✅ Schema 10: Data mapping verified")
                else:
                     print("  ❌ Schema 10: Data mapping FAILED")
            
            if schema_id == 15989:
                if log['extra'].get('pvid') == "TEST_PVID_12345":
                     print("  ✅ Schema 15989: PVId verified")
                else:
                     print(f"  ❌ Schema 15989: PVId FAILED (Got {log['extra'].get('pvid')})")

            if schema_id == 11599:
                 if log['data'].get('sdpHandlerClickType') == 'add_to_cart':
                      print("  ✅ Schema 11599: Patch verified")
                 else:
                      print("  ❌ Schema 11599: Patch FAILED")

    print("\nSummary:")
    all_passed = True
    for sid, found in found_schemas.items():
        status = "FOUND" if found else "MISSING"
        print(f"Schema {sid}: {status}")
        if not found: all_passed = False

    if all_passed:
        print("\nSUCCESS: All schemas generated correctly.")
    else:
        print("\nFAILURE: Some schemas missing.")

if __name__ == "__main__":
    verify_cart_generation()
