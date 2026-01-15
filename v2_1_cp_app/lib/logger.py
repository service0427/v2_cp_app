import os
import datetime
from urllib.parse import urlparse
import json

# --- Logging Setup ---
# --- Logging Setup ---
LOG_ENABLED = True  # Always enable daily text logging by default
ARTIFACTS_ENABLED = False
LOG_FILE_PATH = None
LOG_BASE_DIR = None  # Needed for artifacts (SEARCH.log, etc.)
CONTEXT_INFO = {}

def init(enable_artifacts: bool, context: dict):
    global LOG_ENABLED, ARTIFACTS_ENABLED, LOG_FILE_PATH, CONTEXT_INFO, LOG_BASE_DIR
    
    # Always ON for Daily Text Log
    LOG_ENABLED = True 
    ARTIFACTS_ENABLED = enable_artifacts
    CONTEXT_INFO = context
    
    today = datetime.datetime.now().strftime('%Y%m%d')
    
    # 1. Setup Daily Text Log (Always)
    if not os.path.exists("logs"):
        os.makedirs("logs")
    LOG_FILE_PATH = f"logs/daily_log_{today}.txt"
    print(f"[Logger] Daily Logging Active: {LOG_FILE_PATH}")

    # 2. Setup Artifacts Directory (Optional, via --log)
    if ARTIFACTS_ENABLED:
        # Create a unique session directory to avoid overwriting
        timestamp = datetime.datetime.now().strftime('%H%M%S')
        q_safe = context.get('q', 'unknown').replace(' ', '_')
         # Truncate if too long
        if len(q_safe) > 20: q_safe = q_safe[:20]
        
        daily_artifact_dir = f"logs/session/{today}/{timestamp}_{q_safe}"
        
        if not os.path.exists(daily_artifact_dir):
                os.makedirs(daily_artifact_dir, exist_ok=True)
        LOG_BASE_DIR = daily_artifact_dir
        print(f"[Logger] Artifact Logging Enabled: {LOG_BASE_DIR}")
    else:
        LOG_BASE_DIR = None 
        # Note: We don't print "Disabled" for artifacts to avoid noise, 
        # or maybe print it to be clear.
        # print("[Logger] Artifacts Disabled (Use --log to save JSONs)")

def set_log_dir_suffix(suffix):
    pass # Deprecated in favor of init()

def log_transaction(method, url, req_headers, req_body, resp_status, resp_headers, resp_body, step_name=None):
    if not LOG_ENABLED or not LOG_FILE_PATH:
        return None
    

    q = CONTEXT_INFO.get('q', 'Unknown')
    pid = CONTEXT_INFO.get('productId', 'Unknown')
    
    # Simplified One-Line Log
    # [TIME] [Keyword: ...] [Product: ...] [Step: ...] [Status: ...]

    
    try:
        # Microsecond timestamp (3 digits)
        now = datetime.datetime.now()
        timestamp = now.strftime('%Y-%m-%d %H:%M:%S') + f".{now.microsecond // 1000:03d}"
        
        q = CONTEXT_INFO.get('q', 'Unknown')
        pid = CONTEXT_INFO.get('productId', 'Unknown')
        
        # Simplified One-Line Log
        # [TIME] [Keyword: ...] [Product: ...] [Step: ...] [Status: ...]
        log_line = f"[{timestamp}] [Keyword: {q}] [Product: {pid}] [Step: {step_name or 'Unknown'}] [Status: {resp_status}]"
        
        # 1. Write to Daily Summary Log (Original)
        with open(LOG_FILE_PATH, "a", encoding="utf-8") as f:
            f.write(log_line + "\n")
            
        # 2. Write Detailed Artifact Log (if enabled)
        if LOG_BASE_DIR:
            # 2-1. Generate Summary Log (Time | Status | URL)
            summary_path = os.path.join(LOG_BASE_DIR, "Summary_Log.txt")
            summary_line = f"{timestamp} | {resp_status} | {url}"
            with open(summary_path, "a", encoding="utf-8") as f:
                f.write(summary_line + "\n")

            # Construct JSON structure for jq compatibility
            log_data = {
                "timestamp": timestamp,
                "context": {
                    "keyword": q,
                    "productId": pid,
                    "step": step_name or "Unknown"
                },
                "request": {
                    "method": method,
                    "url": url,
                    "headers": dict(req_headers) if req_headers else {},
                    "body": None
                },
                "response": {
                    "status": resp_status,
                    "headers": dict(resp_headers) if resp_headers else {},
                    "body": None
                }
            }

            # Handle Request Body
            if req_body:
                try:
                    if isinstance(req_body, (dict, list)):
                        log_data["request"]["body"] = req_body
                    elif isinstance(req_body, str):
                        try:
                            log_data["request"]["body"] = json.loads(req_body)
                        except:
                            log_data["request"]["body"] = req_body
                    else:
                        log_data["request"]["body"] = str(req_body)
                except:
                    log_data["request"]["body"] = str(req_body)

            # Handle Response Body
            if resp_body:
                try:
                    # Try to parse as JSON first
                    log_data["response"]["body"] = json.loads(resp_body)
                except:
                    # If text/html, keep as string but truncate if excessively large?
                    # User wants full logs mostly, but let's be safe. 
                    # Actually, for jq, string is fine.
                    log_data["response"]["body"] = resp_body

            # [Unified Log Only] Append to consolidated session log
            # User requested to disable individual logs and keep only the unified one.
            unified_path = os.path.join(LOG_BASE_DIR, "Action_Log.log")
            try:
                with open(unified_path, "a", encoding="utf-8") as f:
                    f.write(f"=== [{step_name}] {timestamp} ===\n")
                    json.dump(log_data, f, indent=2, ensure_ascii=False)
                    f.write("\n\n")
            except Exception as e:
                print(f"[Logger] Failed to write unified log: {e}")

        return LOG_FILE_PATH
    except Exception as e:
        print(f"[Logger] Failed to write log: {e}")
        return None

def log_bypass_schema(module_prefix, schema):
    """
    Logs bypass schema if logging is enabled.
    """
    if not LOG_ENABLED or not LOG_FILE_PATH:
        return None

    try:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        s_id = schema.get('id')
        s_ver = schema.get('version')
        
        # Simple Audit Line for Bypass
        log_line = f"[{timestamp}] [BYPASS] [Step: {module_prefix}] [ID: {s_id}] [Ver: {s_ver}]"
        
        with open(LOG_FILE_PATH, "a", encoding="utf-8") as f:
            f.write(log_line + "\n")
            
        return LOG_FILE_PATH
            
    except Exception as e:
        print(f"[Logger] Warning: Failed to log bypass schema: {e}")
    return None
