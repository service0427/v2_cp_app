import os
import sys
import glob
import importlib
import traceback
from curl_cffi import requests
from lib import logger

# Project Root Setup
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(PROJECT_ROOT)

def main():
    # Force CWD to be the project root so "logs/" is created in v2_1_cp_app/logs/
    os.chdir(PROJECT_ROOT)
    print(f"[V2.1] Starting Execution from: {PROJECT_ROOT}")
    print(f"[V2.1] CWD set to: {os.getcwd()}")
    
    # 1. Initialize Logger
    # Context can be enriched later.
    logger.init(enable_artifacts=True, context={'q': 'V2.1_Replication', 'productId': 'N/A'})
    
    # 2. Initialize Session
    session = requests.Session(impersonate="chrome124")
    
    # 3. Load Schedule Scripts
    schedule_dir = os.path.join(PROJECT_ROOT, "lib", "schedule")
    scripts = sorted(glob.glob(os.path.join(schedule_dir, "*.py")))
    
    print(f"[V2.1] Found {len(scripts)} scripts in schedule.")
    
    # 4. Execute Sequentially
    for script_path in scripts:
        script_name = os.path.basename(script_path)
        
        # Skip __init__.py or non-script files
        if not script_name.endswith(".py") or script_name == "__init__.py":
            continue
            
        print(f"\n>>> [Executing] {script_name} ...")
        
        try:
            # Dynamic Import
            module_name = f"lib.schedule.{script_name[:-3]}"
            module = importlib.import_module(module_name)
            
            # Run 'run' function if exists
            if hasattr(module, "run"):
                module.run(session)
            else:
                print(f"!!! [Warning] No 'run' function found in {script_name}")
                
        except Exception as e:
            print(f"!!! [Error] Blocked at {script_name}: {e}")
            traceback.print_exc()
            # Decide: Continue or Stop? User said "Total Replication", typically we might want to see how far it goes, 
            # but usually a crash in one might affect headers for next. 
            # For now, we continue to verify the whole chain.
            
    print("\n[V2.1] Execution Finished.")

if __name__ == "__main__":
    main()
