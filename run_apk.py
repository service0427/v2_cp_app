#!/usr/bin/env python3
"""
APK 기반 자동화 실행기
======================

lib_apk 전용 독립 실행 스크립트
기존 lib/ 폴더에 영향 없음

사용법:
    python run_apk.py --q "검색어" --productId "상품ID" --vendorItemId "벤더ID" --itemId "아이템ID"
    python run_apk.py --limit 3
    python run_apk.py --test  # 테스트 모드 (mock context 사용)
"""

import os
import sys
import argparse
import importlib.util
import json
import datetime

from curl_cffi import requests

# lib_apk 경로 추가
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib_apk.utils import JA3_STRING
from lib_apk.device_profile import DEFAULT_PROFILE
import lib_apk.logger


def run_schedule():
    parser = argparse.ArgumentParser(description="APK-Based Coupang Action Scheduler")
    parser.add_argument("--limit", type=int, default=0, help="Limit number of steps to execute.")
    parser.add_argument("--log", action="store_true", help="Enable artifact logging.")
    parser.add_argument("--id", type=str, help="Scenario ID from config/scenarios.json")

    # Target Product Parameters
    parser.add_argument("--q", type=str, default="게이밍 의자", help="Search keyword")
    parser.add_argument("--productId", type=str, default="9221117836", help="Target product ID")
    parser.add_argument("--vendorItemId", type=str, default="87889515588", help="Vendor item ID")
    parser.add_argument("--itemId", type=str, default="23456789", help="Item ID")

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
                    print(f"[Run-APK] Loaded Scenario '{args.id}': {scenario_data.get('q')}")

                    if 'q' in scenario_data: args.q = scenario_data['q']
                    if 'productId' in scenario_data: args.productId = scenario_data['productId']
                    if 'vendorItemId' in scenario_data: args.vendorItemId = scenario_data['vendorItemId']
                    if 'itemId' in scenario_data: args.itemId = scenario_data['itemId']
                else:
                    print(f"[Run-APK] Warning: Scenario ID '{args.id}' not found")
            else:
                print(f"[Run-APK] Warning: scenarios.json not found")
        except Exception as e:
            print(f"[Run-APK] Error loading scenario: {e}")

    print("=" * 60)
    print("APK 기반 자동화 실행기 (lib_apk)")
    print("=" * 60)

    # Initialize Session
    session = requests.Session(ja3=JA3_STRING)

    # Timeout 적용
    original_request = session.request
    def timeouts_enforced_request(method, url, *a, **kw):
        if 'timeout' not in kw:
            kw['timeout'] = 10
        return original_request(method, url, *a, **kw)
    session.request = timeouts_enforced_request
    print("[Run-APK] Enforcing 10s timeout for all requests.")

    # Initialize Logger
    lib_apk.logger.init(args.log, {'q': args.q, 'productId': args.productId})

    # Build Context (초기값만 - 나머지는 step_128에서 서버로부터 받아옴)
    context = {
        'INPUT': {
            'q': args.q,
            'productId': args.productId,
            'vendorItemId': args.vendorItemId,
            'itemId': args.itemId,
        },
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
        'RESULT': {
            'ROOT': {},      # step_128에서 채워짐
            'TARGET': {},
            'SEARCH': {},    # step_128에서 채워짐
            'PRODUCT': {},
            'META': {'SEARCH': {}, 'PRODUCT': {}}
        }
        # srp_bypass_mandatory, srp_click_log_bypass는 step_128에서 서버로부터 추출
    }

    # Schedule Directory
    schedule_dir = os.path.join(os.path.dirname(__file__), "lib_apk", "schedule")
    if not os.path.exists(schedule_dir):
        print(f"Error: Schedule directory '{schedule_dir}' not found.")
        return

    # List step files (step_*.py)
    step_files = sorted([
        f for f in os.listdir(schedule_dir)
        if f.endswith(".py") and f.startswith("step_")
    ])

    print(f"Found {len(step_files)} steps in lib_apk/schedule.")

    count = 0
    for step_file in step_files:
        if args.limit > 0 and count >= args.limit:
            print(f"Reached limit of {args.limit} steps.")
            break

        step_name = step_file[:-3]  # remove .py

        if "_SKIP_" in step_name:
            print(f"\n[{step_name}] SKIPPED")
            continue

        print(f"\n[{step_name}] Executing...")

        # Dynamic Import
        file_path = os.path.join(schedule_dir, step_file)
        spec = importlib.util.spec_from_file_location(step_name, file_path)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if hasattr(module, "run"):
                try:
                    import inspect
                    sig = inspect.signature(module.run)
                    if len(sig.parameters) >= 2:
                        result = module.run(session, context)
                    else:
                        result = module.run(session)

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

    print("\n" + "=" * 60)
    print("실행 완료")
    print("=" * 60)

    # Context 저장
    if lib_apk.logger.LOG_BASE_DIR:
        try:
            context_log_file = os.path.join(lib_apk.logger.LOG_BASE_DIR, "context.log")
            with open(context_log_file, 'w', encoding='utf-8') as f:
                json.dump(context, f, indent=2, ensure_ascii=False)
            print(f"[Context] Saved to {context_log_file}")
        except Exception as e:
            print(f"[Context] Failed to save: {e}")


if __name__ == "__main__":
    run_schedule()
