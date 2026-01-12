import json
import glob
import os
import sys

# Ensure lib is in path (Parent directory)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib.capture_parser import parse_capture_file

SCENARIOS_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config', 'scenarios.json')
CAPTURE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'captures')

def populate_scenarios():
    capture_files = sorted(glob.glob(os.path.join(CAPTURE_DIR, '*.json')), key=os.path.getctime)
    
    scenarios = {}
    idx = 0
    
    print(f"Found {len(capture_files)} capture files.")
    
    for filepath in capture_files:
        print(f"Parsing {filepath}...")
        try:
            data = parse_capture_file(filepath)
            if data and data.get('q') and data.get('productId'):
                scenario_id = str(idx)
                
                # Check for duplicates? or just add all?
                # The user want "all files checked", so we add all valid ones.
                
                scenarios[scenario_id] = {
                    "q": data['q'],
                    "productId": data['productId'],
                    "vendorItemId": data.get('vendorItemId', ''),
                    "itemId": data.get('itemId', '')
                }
                idx += 1
            else:
                print(f"Skipping {filepath}: Missing critical data (q or productId)")
        except Exception as e:
            print(f"Error parsing {filepath}: {e}")
            
    with open(SCENARIOS_FILE, 'w', encoding='utf-8') as f:
        json.dump(scenarios, f, indent=4, ensure_ascii=False)
        
    print(f"Successfully wrote {len(scenarios)} scenarios to {SCENARIOS_FILE}")

if __name__ == "__main__":
    populate_scenarios()
