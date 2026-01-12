import os
import datetime
import json
import time
from urllib.parse import urlparse
from curl_cffi import requests

# --- Configuration ---
DATA_FILE = "requests_data.json"

# Logging is now handled by lib.logger


import argparse
import importlib.util
from lib.utils import JA3_STRING
from lib.device_profile import DEFAULT_PROFILE
import lib.capture_parser
import lib.logger
import lib.proxy_manager

# --- Execution ---
def run_schedule():
    parser = argparse.ArgumentParser(description="Coupang App Action Scheduler")
    parser.add_argument("--limit", type=int, default=0, help="Limit number of steps to execute.")
    parser.add_argument("--log", action="store_true", help="Enable daily consolidated logging.")

    parser.add_argument("--capture_file", type=str, help="Path to capture file for dynamic scenario execution.")
    parser.add_argument("--id", type=str, help="Scenario ID from scenarios.json (e.g. 'test1')")
    parser.add_argument("--proxy", action="store_true", help="Enable dynamic SOCKS5 proxy.")

    # Target Product Parameters
    parser.add_argument("--q", type=str, default="호박식혜 달빛", help="Search keyword")
    parser.add_argument("--productId", type=str, default="9183773210", help="Target product ID")
    parser.add_argument("--vendorItemId", type=str, default="94055536143", help="Vendor item ID")
    parser.add_argument("--itemId", type=str, default="27087300150", help="Item ID")

    args = parser.parse_args()

    # Load Scenario from JSON if --id is provided
    if args.id:
        try:
            scenario_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config', 'scenarios.json')
            if os.path.exists(scenario_path):
                with open(scenario_path, 'r', encoding='utf-8') as f:
                    scenarios = json.load(f)
                
                if args.id in scenarios:
                    scenario_data = scenarios[args.id]
                    print(f"[Run] Loaded Scenario '{args.id}'")
                    
                    if 'q' in scenario_data: args.q = scenario_data['q']
                    if 'productId' in scenario_data: args.productId = scenario_data['productId']
                    if 'vendorItemId' in scenario_data: args.vendorItemId = scenario_data['vendorItemId']
                    if 'itemId' in scenario_data: args.itemId = scenario_data['itemId']
                else:
                    print(f"[Run] Warning: Scenario ID '{args.id}' not found in scenarios.json")
            else:
                print(f"[Run] Warning: scenarios.json not found at {scenario_path}")
        except Exception as e:
            print(f"[Run] Error loading scenarios.json: {e}")
    
    # Initialize Session
    session = requests.Session(ja3=JA3_STRING)
    
    # Proxy Setup
    if args.proxy:
        # import lib.proxy_manager  <-- Moved to top level to avoid UnboundLocalError
        proxy_url = lib.proxy_manager.get_random_proxy()
        if proxy_url:
            session.proxies = {"http": proxy_url, "https": proxy_url}
            print(f"[Run] Using Proxy: {proxy_url}")
        else:
            print("[Run] Failed to get proxy. Proceeding without proxy (or should we fail?).")
            # User instruction implies using it if --proxy is present. If failed, maybe warn?
            # Proceeding without proxy might reveal IP. Let's strictly warn.
            print("[Run] WARNING: proceeding DIRECTLY without proxy!")

    # Timeout Configuration (Global hint via wrapping? or modifying generic request?)
    # curl_cffi Session objects don't enforce a default timeout on methods easily unless we override them.
    # Let's override session.request to enforce timeout=10 if not specified.
    
    original_request = session.request
    def timeouts_enforced_request(method, url, *args, **kwargs):
        if 'timeout' not in kwargs:
            kwargs['timeout'] = 10
        return original_request(method, url, *args, **kwargs)
    session.request = timeouts_enforced_request
    print("[Run] Enforcing 10s timeout for all requests.")

    # Initialize Logger (New Daily Strategy)
    # enable_artifacts = args.log (Daily Text Log is always ON)
    lib.logger.init(args.log, {'q': args.q, 'productId': args.productId})



    # Modular Schedule Execution
    schedule_dir = os.path.join(os.path.dirname(__file__), "lib", "schedule")
    if not os.path.exists(schedule_dir):
        print(f"Error: Schedule directory '{schedule_dir}' not found.")
        return

    # List all step files (e.g., 001_entrance.py)
    step_files = sorted([
        f for f in os.listdir(schedule_dir) 
        if f.endswith(".py") and f[0].isdigit()
    ])

    print(f"Found {len(step_files)} steps in schedule.")
    
    count = 0
    context = {
        # 사용자 입력값 (CLI Arguments)
        'INPUT': {
            'q': args.q,
            'productId': args.productId,
            'vendorItemId': args.vendorItemId,
            'itemId': args.itemId,
        },

        # 디바이스 프로필 (generate_common_payload & headers에서 사용)
        'DEVICE': {
            'model': DEFAULT_PROFILE.model,
            'os_version': DEFAULT_PROFILE.os_version,
            'width': DEFAULT_PROFILE.width,
            'height': DEFAULT_PROFILE.height,
            'pcid': DEFAULT_PROFILE.pcid,
            'app_session_id': DEFAULT_PROFILE.app_session_id,
            'device_uuid': DEFAULT_PROFILE.device_uuid,
            'ixid': DEFAULT_PROFILE.ixid,
            'dpi': DEFAULT_PROFILE.dpi,
            'dpi_level': DEFAULT_PROFILE.dpi_level,
            'android_id': DEFAULT_PROFILE.android_id,
            'install_timestamp': DEFAULT_PROFILE.install_timestamp,
            'device_hash': DEFAULT_PROFILE.device_hash,
        },

        # 결과 저장소
        'RESULT': {
            'ROOT': {},      # API 호출에 필요한 필수 값 (productId, searchId, sdpVisitKey 등)
            'TARGET': {},    # 타겟 상품 정보 (productId, itemId, rank, name, price 등)
            'SEARCH': {},    # SRP 페이지 전체 메타데이터 (srp_* 포함)
            'PRODUCT': {},   # SDP 페이지 전체 메타데이터 (sdp_* 포함)
            'META': {'SEARCH': {}, 'PRODUCT': {}}
        }
    }
    
    for step_file in step_files:
        if args.limit > 0 and count >= args.limit:
            print(f"Reached limit of {args.limit} steps.")
            break

        step_name = step_file[:-3] # remove .py
        
        if "_SKIP_" in step_name:
            print(f"\n[{step_name}] SKIPPED (Filename Strategy)")
            continue
            
        print(f"\n[{step_name}] Executing...")
        # display_context = {'INPUT': context['INPUT'], 'DEVICE': context['DEVICE']}
        # print(f"[Context] {json.dumps(display_context, indent=2, ensure_ascii=False)}")
        
        # Dynamic Import
        file_path = os.path.join(schedule_dir, step_file)
        spec = importlib.util.spec_from_file_location(step_name, file_path)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            if hasattr(module, "run"):
                try:
                    # Check if run accepts 2 arguments (session, context) or just 1 (session)
                    import inspect
                    sig = inspect.signature(module.run)
                    if len(sig.parameters) >= 2:
                        result = module.run(session, context)
                    else:
                        result = module.run(session)
                    
                    # Update context if result is a dict
                    if isinstance(result, dict):
                        context.update(result)
                        
                    count += 1
                except Exception as e:
                    print(f"[{step_name}] Failed: {e}")
                    import traceback
                    traceback.print_exc()
                    print(f"[{step_name}] Critical failure. Stopping execution.")
                    break
            else:
                print(f"[{step_name}] Error: 'run(session)' function not found.")
        else:
            print(f"[{step_name}] Error: Could not load module.")

    # Save context to log file
    try:
        # Only save context log if valid LOG_BASE_DIR exists (logging enabled)
        if lib.logger.LOG_BASE_DIR:
            context_log_file = os.path.join(lib.logger.LOG_BASE_DIR, "context.log")
            with open(context_log_file, 'w', encoding='utf-8') as f:
                json.dump(context, f, indent=2, ensure_ascii=False)
            print(f"\n[Context] Saved to {context_log_file}")
    except Exception as e:
        print(f"[Context] Failed to save: {e}")




if __name__ == "__main__":
    run_schedule()
