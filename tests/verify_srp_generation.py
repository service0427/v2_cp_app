import sys
import os
import json
import logging
from dataclasses import asdict

# Set Project Root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

from lib.common.log_manager.scenario import ScenarioManager
from lib.device_profile import DEFAULT_PROFILE

# Setup Logger
logging.basicConfig(level=logging.INFO, format='[VERIFY] %(message)s')
logger = logging.getLogger("VerifySRP")

def run_test():
    logger.info(">>> Verifying SRP View Impression Log Generation")
    
    # Mock Context (as if produced by 128_G)
    context = {
        'DEVICE': asdict(DEFAULT_PROFILE),
        'INPUT': { 'q': '나이키' },
        'RESULT': {
            'ROOT': {
                'searchId': 'test_search_id_123',
                'searchCount': 50000,
                'keywordType': 'BRAND_KEYWORD'
            },
            'SEARCH': {
                'srp_pvId': 'test_pv_id_999',
                'widgetTotalCount': 35,
                'widgetTypeCount': 5,
                'widgetDistribution': '{"U_WIDGET": 30}',
                'searchViewType': 'GRID_2',
                'isCoupick': True,
                'rankOfCoupick': 3,
                'filterKeys': 'brand:nike',
                'filterType': 'brand'
            }
        }
    }
    
    manager = ScenarioManager(context)
    payloads = manager.execute_scenario('srp_view_impression')
    
    logger.info(f"Generated {len(payloads)} schemas.")
    
    # Check Schemas
    required_ids = [116, 17211, 15704, 11965]
    found_ids = [p['meta']['schemaId'] for p in payloads]
    
    logger.info(f"IDs Found: {found_ids}")
    
    for rid in required_ids:
        if rid not in found_ids:
            logger.error(f"Missing Schema {rid}!")
        else:
            # Inspection
            schema = next(p for p in payloads if p['meta']['schemaId'] == rid)
            logger.info(f"--- Schema {rid} Data ---")
            print(json.dumps(schema['data'], indent=2, ensure_ascii=False))

if __name__ == "__main__":
    run_test()
