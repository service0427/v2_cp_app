import os
import datetime
import json
import time
from urllib.parse import urlparse
from curl_cffi import requests

# --- Configuration ---
DATA_FILE = "requests_data.json"

import argparse
import importlib.util
from lib.utils import JA3_STRING
from lib.device_profile import DEFAULT_PROFILE

# --- Execution ---
def run_schedule():
    parser = argparse.ArgumentParser(description="Coupang App Action Scheduler (Test - schedule_backup)")
    parser.add_argument("--limit", type=int, default=0, help="Limit number of steps to execute.")

    # Target Product Parameters
    parser.add_argument("--q", type=str, default="호박식혜 달빛", help="Search keyword")
    parser.add_argument("--productId", type=str, default="9183773210", help="Target product ID")
    parser.add_argument("--vendorItemId", type=str, default="94055536143", help="Vendor item ID")
    parser.add_argument("--itemId", type=str, default="27087300150", help="Item ID")

    args = parser.parse_args()

    # Initialize Session
    session = requests.Session(ja3=JA3_STRING)

    # Use schedule_backup directory
    schedule_dir = os.path.join(os.path.dirname(__file__), "lib", "schedule_backup")
    if not os.path.exists(schedule_dir):
        print(f"Error: Schedule directory '{schedule_dir}' not found.")
        return

    # List all step files (e.g., 001_entrance.py)
    step_files = sorted([
        f for f in os.listdir(schedule_dir)
        if f.endswith(".py") and f[0].isdigit()
    ])

    print(f"[TEST MODE] Using schedule_backup directory")
    print(f"Found {len(step_files)} steps in schedule.")

    count = 0
    context = {
        # CLI Arguments
        'q': args.q,
        'productId': args.productId,
        'vendorItemId': args.vendorItemId,
        'itemId': args.itemId,

        # Device Profile (used in generate_common_payload & headers)
        'model': DEFAULT_PROFILE.model,
        'os_version': DEFAULT_PROFILE.os_version,
        'width': DEFAULT_PROFILE.width,
        'height': DEFAULT_PROFILE.height,
        'pcid': DEFAULT_PROFILE.pcid,
        'app_session_id': DEFAULT_PROFILE.app_session_id,
        'device_uuid': DEFAULT_PROFILE.device_uuid,
        'ixid': DEFAULT_PROFILE.ixid,

        # Result Storage
        'SEARCH_RESULT': {},
        'PRODUCT_RESULT': {},
        'TARGET_RESULT': {},
        'META_RESULT': {'SEARCH': {}, 'PRODUCT': {}}
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
        display_context = {k: v for k, v in context.items() if not k.endswith('_RESULT')}
        print(f"[Context] {json.dumps(display_context, indent=2, ensure_ascii=False)}")

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
            else:
                print(f"[{step_name}] Error: 'run(session)' function not found.")
        else:
            print(f"[{step_name}] Error: Could not load module.")

    # Save META_RESULT to log file
    if context.get('META_RESULT'):
        try:
            import lib.logger
            meta_log_file = os.path.join(lib.logger.LOG_BASE_DIR, "META_TEST.log")
            with open(meta_log_file, 'w', encoding='utf-8') as f:
                json.dump(context['META_RESULT'], f, indent=2, ensure_ascii=False)
            print(f"\n[META] Saved to {meta_log_file}")
        except Exception as e:
            print(f"[META] Failed to save: {e}")


if __name__ == "__main__":
    run_schedule()
