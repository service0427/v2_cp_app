import sys
import os
import json
import datetime
import random
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.common.utils import generate_common_payload


# Reference Data Index: 178
# Method: POST

def run(session: requests.Session, context: dict = None):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/4.9.3'
    }

    if not context: context = {}

    # -------------------------------------------------------------------------
    # [NEW] Data-Driven Schema Engine (ScenarioManager)
    # -------------------------------------------------------------------------
    # attribution context preparation ensuring sdpVisitKey and searchId are propagated
    # logic mimics APK state transfer from SRP -> SDP
    # -------------------------------------------------------------------------
    from lib.common.log_manager.scenario import ScenarioManager
    
    # Prepare INPUT layer for GenericSchema mapping
    # We explicitly map keys from the RESULT (Context) to INPUT (Schema Interface)
    input_data = context.get('INPUT', {})
    
    # 1. Attribute: sdpVisitKey (Critical for linking Cart to Visit)
    # Source: 145_G Extraction (RESULT.ROOT.sdpVisitKey)
    if 'sdpVisitKey' not in input_data:
        input_data['sdpVisitKey'] = context.get('RESULT', {}).get('ROOT', {}).get('sdpVisitKey')

    # 2. Attribute: searchId (Critical for linking Cart to Search)
    # Source: SRP Context (RESULT.ROOT.searchId)
    if 'searchId' not in input_data:
        input_data['searchId'] = context.get('RESULT', {}).get('ROOT', {}).get('searchId')

    # 3. Attribute: q (Search Query)
    if 'q' not in input_data:
        input_data['q'] = context.get('RESULT', {}).get('INPUT', {}).get('q') or input_data.get('q')

    # 4. Attribute: Product Info
    if 'productId' not in input_data:
        input_data['productId'] = context.get('RESULT', {}).get('ROOT', {}).get('productId')
    if 'itemId' not in input_data:
         input_data['itemId'] = context.get('RESULT', {}).get('ROOT', {}).get('itemId')
    if 'vendorItemId' not in input_data:
         input_data['vendorItemId'] = context.get('RESULT', {}).get('ROOT', {}).get('vendorItemId')

    # 5. Attribute: PVID (Page View Link)
    if 'srp_pvId' not in input_data:
         input_data['srp_pvId'] = context.get('RESULT', {}).get('SEARCH', {}).get('srp_pvId')

    # Update Context with enriched INPUT
    context['INPUT'] = input_data

    # Instantiate Manager with Full Context
    manager = ScenarioManager(context)

    # Execute 'add_to_cart' Scenario
    # This generates Schema 10, 15989, 11599, 14044 with dynamic injection
    body = manager.execute_scenario("add_to_cart")

    if not body:
        print("[179] Warning: ScenarioManager returned empty body.")
        return None

    return run_request(session, method, url, headers, body)
