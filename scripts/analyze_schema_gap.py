import json
import os
import glob
import sys
from collections import defaultdict

# Configurations
SCENARIOS_FILE = '/home/tech/v2_cp_app/scenarios.json'
CAPTURE_DIR = '/home/tech/v2_cp_app/captures'
PACKET_DIR = '/home/tech/v2_cp_app/logs/session/20260112' # Targeted Logs
# Wait, user said "/home/tech/v2_cp_app/captures/packet" contains the logs?
# The `list_dir` output shows directories like `204645_노트북_8099175514`.
# These look like simulation session logs.
# Let's assume the user COPIED the simulation logs to `captures/packet` or they ARE the simulation logs.
# The `list_dir` output matches the timestamped log directories we saw earlier (e.g. `20:46:45 ...`).
# So `captures/packet` contains the SIMULATION OUTPUT for each scenario.

TARGET_SCHEMAS = {
    '133_P': [15704, 116],
    '147_P': [124],     # Removed 2851
    '156_P': [14741],
    '179_P': [10, 11599]
}

def load_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return None

def find_capture_file(q, pid):
    # Find capture file matching "Keyword-PID-*.json"
    pattern = os.path.join(CAPTURE_DIR, f"{q.replace(' ', '_')}-{pid}-*.json")
    files = glob.glob(pattern)
    if files:
        return files[0]
    return None

def extract_schemas_from_log(log_path, target_schema_ids):
    schemas = []
    content = ""
    try:
        with open(log_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return []
        
    # Naive extraction: finding JSON blocks in body
    # The logs have "Body:\n[\n  {...}\n]" format usually.
    # We'll look for the JSON array after "Body:"
    import re
    # Match content between "Body:\n" and "\n\n=== RESPONSE"
    match = re.search(r'Body:\s*(\[.*?\])\s*=== RESPONSE', content, re.DOTALL)
    if match:
        try:
            json_str = match.group(1)
            data = json.loads(json_str)
            for item in data:
                sid = item.get('meta', {}).get('schemaId')
                if sid in target_schema_ids:
                    schemas.append(item)
        except:
            pass
            
    return schemas

def extract_schemas_from_capture(capture_path, target_schema_ids):
    schemas = []
    data = load_json(capture_path)
    if not data: return []
    
    for req in data.get('requests', []):
        if '/bulksubmit' in req.get('url', ''):
            payload = None
            # Case 1: 'body' key is already a parsed object/list (Native format)
            if 'body' in req:
                payload = req['body']
            # Case 2: HAR format with postData.text
            elif 'postData' in req:
                try:
                    text = req['postData'].get('text', '')
                    if text:
                        payload = json.loads(text)
                except: pass
            
            if payload and isinstance(payload, list):
                for item in payload:
                    sid = item.get('meta', {}).get('schemaId')
                    if sid in target_schema_ids:
                        schemas.append(item)
    return schemas

def compare_schemas(sim_schemas, cap_schemas, schema_id):
    # Retrieve the first matching schema for comparison (simplification)
    # Ideally should match by some ID, but for 1:1 scenarios usually ok.
    # For 14741 (unit logs), we might have many. We'll verify the structure of the FIRST one.
    
    sim_item = next((s for s in sim_schemas if s.get('meta', {}).get('schemaId') == schema_id), None)
    cap_item = next((s for s in cap_schemas if s.get('meta', {}).get('schemaId') == schema_id), None)
    
    if not sim_item:
        return f"MISSING in Simulation"
    if not cap_item:
        return f"MISSING in Capture"
        
    diffs = []
    
    # Compare Data
    sim_data = sim_item.get('data', {})
    cap_data = cap_item.get('data', {})
    
    # Check for missing keys in Sim
    for k, v in cap_data.items():
        if k not in sim_data:
            diffs.append(f"[data] Missing Key: {k} (Expected: {v})")
        elif str(sim_data[k]) != str(v):
            # Ignore dynamic fields
            if k in ['eventTime', 'logId', 'uuid', 'pcid', 'appSessionId', 'id', 'searchId', 'requestId', 'traceId']:
                continue
            # Ignore specific known dynamic values
            if str(v).startswith('${'): continue
            
            diffs.append(f"[data] Value Mismatch: {k} (Sim: {sim_data[k]} vs Cap: {v})")

    # Compare Extra
    sim_extra = sim_item.get('extra', {})
    cap_extra = cap_item.get('extra', {})
    
    for k, v in cap_extra.items():
        if k not in sim_extra:
            diffs.append(f"[extra] Missing Key: {k} (Expected: {v})")
        elif str(sim_extra[k]) != str(v):
             # Ignore dynamic fields
            if k in ['eventTime', 'logId', 'uuid', 'pcid', 'appSessionId']:
                continue
            diffs.append(f"[extra] Value Mismatch: {k} (Sim: {sim_extra[k]} vs Cap: {v})")
            
    if not diffs:
        return "MATCH"
    else:
        return "\n".join(diffs)

def analyze():
    scenarios = load_json(SCENARIOS_FILE)
    if not scenarios: return

    # Map packet dirs to scenarios?
    # Packet dirs are like `204645_노트북_8099175514`.
    # We can match by ProductID.
    packet_dirs = glob.glob(os.path.join(PACKET_DIR, '*'))
    pid_to_packet = {}
    for pdir in packet_dirs:
        # Extract PID from folder name
        try:
            name = os.path.basename(pdir)
            pid = name.split('_')[-1]
            pid_to_packet[pid] = pdir
        except: pass

    report = []
    report.append("# Bulksubmit Schema Gap Analysis Report")
    report.append(f"Analysis Date: {os.popen('date').read().strip()}")
    report.append(f"Scenarios: {len(scenarios)}")
    report.append("---")
    
    for sid, sdata in scenarios.items():
        q = sdata['q']
        pid = sdata['productId']
        desc = sdata['description']
        
        report.append(f"\n## {desc}")
        
        # 1. Find Simulation Packet Dir
        sim_dir = pid_to_packet.get(pid)
        if not sim_dir:
            report.append(f"- **Simulation Log**: NOT FOUND for PID {pid}")
            continue
            
        # 2. Find Capture File
        cap_file = find_capture_file(q, pid)
        if not cap_file:
            report.append(f"- **Capture File**: NOT FOUND for {q}-{pid}")
            continue

        report.append(f"- **Sim Dir**: `{os.path.basename(sim_dir)}`")
        report.append(f"- **Capture**: `{os.path.basename(cap_file)}`")
        
        # 3. Analyze per Key
        for step_key, schemas_ids in TARGET_SCHEMAS.items():
            report.append(f"\n### Step: {step_key}")
            
            # Identify log file
            # e.g. 133_P_v2_bulksubmit_srp_view_impression.log
            # We look for files starting with {step_key} in sim_dir
            log_files = glob.glob(os.path.join(sim_dir, f"{step_key}*.log"))
            if not log_files:
                report.append(f"- Log file not found for {step_key}")
                continue
            
            log_path = log_files[0]
            sim_schemas = extract_schemas_from_log(log_path, schemas_ids)
            cap_schemas = extract_schemas_from_capture(cap_file, schemas_ids)
            
            for sid in schemas_ids:
                res = compare_schemas(sim_schemas, cap_schemas, sid)
                if res == "MATCH":
                    report.append(f"- **Schema {sid}**: ✅ MATCH")
                elif "MISSING" in res:
                    report.append(f"- **Schema {sid}**: ❌ {res}")
                else:
                    report.append(f"- **Schema {sid}**: ⚠️ MISMATCH")
                    # Indent diffs
                    for line in res.split('\n'):
                        report.append(f"    - `{line}`")

    # Save Report
    with open('log_gap_analysis_v2.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))
    
    print("Report generated: log_gap_analysis_v2.md")

if __name__ == "__main__":
    analyze()
