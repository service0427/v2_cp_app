
import os
import json
import glob
from datetime import datetime

TARGET_DIR = "/home/tech/v2_cp_app/logs/session/20260113/123438_게이밍_의자"
OUTPUT_FILE = os.path.join(TARGET_DIR, "Synthesized_Action_Log.log")

def read_json_safe(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return None

def main():
    entries = []
    
    # 1. 133_P (SRP View) -> Step 02
    path_133 = os.path.join(TARGET_DIR, "133_P_v2_bulksubmit_srp_view_impression.log")
    if os.path.exists(path_133):
        data = read_json_safe(path_133)
        if data:
            entries.append({
                "ts": data.get("timestamp", "0000-00-00 00:00:00"),
                "step": "02_Log_Search_Impression",
                "data": data
            })

    # 2. 147_P (Click) -> Step 03
    path_147 = os.path.join(TARGET_DIR, "147_P_v2_bulksubmit_click_search_product.log")
    if os.path.exists(path_147):
        data = read_json_safe(path_147)
        if data:
            entries.append({
                "ts": data.get("timestamp", "0000-00-00 00:00:00"),
                "step": "03_Log_Product_Click",
                "data": data
            })

    # 3. 156_P (Impression) -> Step 05
    path_156 = os.path.join(TARGET_DIR, "156_P_v2_bulksubmit_srp_product_unit_impression.log")
    if os.path.exists(path_156):
        data = read_json_safe(path_156)
        if data:
            entries.append({
                "ts": data.get("timestamp", "0000-00-00 00:00:00"),
                "step": "05_Log_Product_Impression",
                "data": data
            })
            
    # 4. 179_P (Add To Cart) -> Step XX (Not standard flow usually?)
    path_179 = os.path.join(TARGET_DIR, "179_P_v2_bulksubmit_add_to_cart.log")
    if os.path.exists(path_179):
        data = read_json_safe(path_179)
        if data:
            entries.append({
                "ts": data.get("timestamp", "0000-00-00 00:00:00"),
                "step": "Add_To_Cart",
                "data": data
            })

    # Sort by timestamp
    entries.sort(key=lambda x: x['ts'])

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        for entry in entries:
            f.write(f"=== [{entry['step']}] {entry['ts']} ===\n")
            json.dump(entry['data'], f, indent=2, ensure_ascii=False)
            f.write("\n\n")

    print(f"Synthesized log written to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
