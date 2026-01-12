import json
import subprocess
import time
import sys
import os

def run_all():
    if not os.path.exists('scenarios.json'):
        print("scenarios.json not found")
        return

    try:
        with open('scenarios.json', 'r', encoding='utf-8') as f:
            scenarios = json.load(f)
    except Exception as e:
        print(f"Error loading scenarios.json: {e}")
        return

    # Sort keys numerically
    try:
        keys = sorted(scenarios.keys(), key=lambda x: int(x))
    except ValueError:
        # Fallback if non-integer keys exist (shouldn't happen based on known structure)
        keys = sorted(scenarios.keys())
    
    print(f"Found {len(keys)} scenarios to execute.")
    print(f"Scenario IDs: {', '.join(keys)}")
    
    success_count = 0
    fail_count = 0
    
    for sid in keys:
        desc = scenarios[sid].get('description', '')
        print(f"\n[{time.strftime('%H:%M:%S')}] ==================================================")
        print(f"Executing Scenario ID: {sid} >> {desc}")
        print(f"==================================================")
        
        cmd = [sys.executable, 'run.py', '--id', sid]
        
        try:
            # Run synchronously
            result = subprocess.run(cmd, check=False) 
            if result.returncode != 0:
                print(f"!!! Error executing Scenario {sid} (Exit Code: {result.returncode})")
                fail_count += 1
            else:
                print(f"Scenario {sid} completed successfully.")
                success_count += 1
        except Exception as e:
            print(f"Failed to run scenario {sid}: {e}")
            fail_count += 1
            
        time.sleep(1) # Brief pause

    print(f"\n\nAll scenarios execution finished.")
    print(f"Total: {len(keys)}, Success: {success_count}, Failed: {fail_count}")

if __name__ == "__main__":
    run_all()
