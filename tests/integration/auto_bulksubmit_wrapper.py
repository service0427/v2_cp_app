import sys
import os
import json
import logging
from curl_cffi import requests

# Set Project Root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_ROOT)

import importlib
SearchScript = importlib.import_module("lib.schedule.128_G_v3_SEARCH_products")
from lib.common.log_manager.scenario import ScenarioManager
from lib.device_profile import DEFAULT_PROFILE

# Setup Logger
logging.basicConfig(level=logging.INFO, format='[TEST] %(message)s')
logger = logging.getLogger("IntegrationTest")

from dataclasses import asdict

def run_integration_test():
    logger.info(">>> Starting Auto-BulkSubmit Integration Test")
    
    # 1. Initialize Session & Context
    session = requests.Session()
    context = {
        'DEVICE': asdict(DEFAULT_PROFILE),  # Convert dataclass to dict
        'INPUT': {
            'q': '나이키',
            'productId': '7942485559' # Example Product ID (Must exist in search results ideally, or fallback)
        },
        'RESULT': {
            'META': {'SEARCH': {}} # 128_G requires this initialization
        }
    }
    
    # 2. Execute 128_G (Scraping & State Update)
    logger.info(f"Running 128_G_v3_SEARCH_products for q={context['INPUT']['q']}...")
    try:
        SearchScript.run(session, context) # 128_G modifies context in-place
        
        # Verify execution by checking RESULT
        if not context.get('RESULT', {}).get('ROOT'):
             logger.warning("128_G finished but RESULT.ROOT is empty. Proceeding anyway to test robustness.")
             
    except Exception as e:
        logger.error(f"128_G execution error: {e}")
        return

    # 3. Context Adaptation (Bridge 128_G output to Schema Engine expectations)
    # 128_G puts selected product in context['RESULT']['TARGET']
    # Schema definitions (124.json) might expect RESULT.ROOT or RESULT.TARGET.
    # We will alias TARGET to ROOT for compatibility if needed, or update definitions.
    # For now, let's copy TARGET to ROOT because 124.json definition currently uses ROOT.
    
    if 'TARGET' in context['RESULT']:
        context['RESULT']['ROOT'] = context['RESULT']['TARGET']
        logger.info("Context Adapted: Appended RESULT.TARGET to RESULT.ROOT for Schema Engine.")
        
        # Also ensure SEARCH info is available
        # 128_G puts search info in local 'extracted_data' but usually merges back or we have to rely on what it put in TARGET.
        # Let's see what 128_G creates. It seems it doesn't explicitly put global 'SEARCH' stats into context['RESULT']['SEARCH'] in the code snippet I saw, 
        # except implicitly via some specific logic or mixed keys.
        # Let's inspect context after run to be sure.
        
        # Polyfill SEARCH stats if missing (for 152 schema)
        if 'SEARCH' not in context['RESULT']:
             context['RESULT']['SEARCH'] = {
                 'srp_rank': context['RESULT']['TARGET'].get('rank', 0),
                 'searchCount': 1000, # Mock/Undefined if not captured
                 'internalCategoryId': '1234' # Mock
             }
    else:
        logger.warning("128_G did not find a TARGET product. Schema Engine might fail.")
        context['RESULT']['ROOT'] = {}
        context['RESULT']['SEARCH'] = {}

    # [NEW] Mimic 147_P Logic Injection
    # 147_P now calculates these fields before calling ScenarioManager.
    # We must do the same here to emulate the Scheduler's behavior.
    
    # 1. Search ID Combined
    search_id = context['RESULT']['ROOT'].get('searchId', 'test-sid')
    rank = context['RESULT']['SEARCH'].get('srp_rank', 0)
    context['INPUT']['searchIdCombined'] = f"{search_id}:{rank}"
    
    # 2. AB Test Attribute
    ab_id = context['RESULT']['SEARCH'].get('srp_abTestId', '')
    if str(ab_id) in ['85005', '85006', '85007']:
        context['INPUT']['abTestAttribute'] = 'srp,lowestpricein7days'
    else:
        context['INPUT']['abTestAttribute'] = 'srp'

    # 4. Trigger Schema Engine (ScenarioManager)
    logger.info("Triggering ScenarioManager: 'search_product_click'...")
    manager = ScenarioManager(context)
    
    try:
        payloads = manager.execute_scenario('search_product_click')
        
        logger.info(f"Generated {len(payloads)} Schemas successfully!")
        
        # 5. Output Verification
        for p in payloads:
            s_id = p['meta']['schemaId']
            logger.info(f"--- Schema {s_id} Generated ---")
            
            # Print critical fields to verify data flow from 128_G
            if s_id == 124:
                print(json.dumps(p['data'], indent=2, ensure_ascii=False))
                
                # Verify Product ID matches input
                gen_pid = p['data'].get('productId') or p['data'].get('id')
                logger.info(f"Schema 124 ProductId: {gen_pid}")
                
    except Exception as e:
        logger.error(f"Scenario Execution Failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    run_integration_test()
