"""
APK 기반 로거 모듈
==================

lib_apk 전용 독립 로거
"""

import os
import datetime
import json

LOG_ENABLED = True
ARTIFACTS_ENABLED = False
LOG_FILE_PATH = None
LOG_BASE_DIR = None
CONTEXT_INFO = {}


def init(enable_artifacts: bool, context: dict):
    global LOG_ENABLED, ARTIFACTS_ENABLED, LOG_FILE_PATH, CONTEXT_INFO, LOG_BASE_DIR

    LOG_ENABLED = True
    ARTIFACTS_ENABLED = enable_artifacts
    CONTEXT_INFO = context

    today = datetime.datetime.now().strftime('%Y%m%d')

    if not os.path.exists("logs_apk"):
        os.makedirs("logs_apk")
    LOG_FILE_PATH = f"logs_apk/daily_log_{today}.txt"
    print(f"[Logger-APK] Daily Logging Active: {LOG_FILE_PATH}")

    if ARTIFACTS_ENABLED:
        timestamp = datetime.datetime.now().strftime('%H%M%S')
        q_safe = context.get('q', 'unknown').replace(' ', '_')
        if len(q_safe) > 20:
            q_safe = q_safe[:20]

        daily_artifact_dir = f"logs_apk/session/{today}/{timestamp}_{q_safe}"

        if not os.path.exists(daily_artifact_dir):
            os.makedirs(daily_artifact_dir, exist_ok=True)
        LOG_BASE_DIR = daily_artifact_dir
        print(f"[Logger-APK] Artifact Logging Enabled: {LOG_BASE_DIR}")
    else:
        LOG_BASE_DIR = None


def log_transaction(method, url, req_headers, req_body, resp_status, resp_headers, resp_body, step_name=None):
    if not LOG_ENABLED or not LOG_FILE_PATH:
        return None

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    q = CONTEXT_INFO.get('q', 'Unknown')
    pid = CONTEXT_INFO.get('productId', 'Unknown')

    log_line = f"[{timestamp}] [APK] [Keyword: {q}] [Product: {pid}] [Step: {step_name or 'Unknown'}] [Status: {resp_status}]"

    try:
        with open(LOG_FILE_PATH, "a", encoding="utf-8") as f:
            f.write(log_line + "\n")

        if LOG_BASE_DIR:
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

            if resp_body:
                try:
                    log_data["response"]["body"] = json.loads(resp_body)
                except:
                    log_data["response"]["body"] = resp_body

            step_filename = f"{step_name}.log" if step_name else f"unknown_step_{timestamp}.log"
            artifact_path = os.path.join(LOG_BASE_DIR, step_filename)

            with open(artifact_path, "w", encoding="utf-8") as f:
                json.dump(log_data, f, indent=2, ensure_ascii=False)

        return LOG_FILE_PATH

    except Exception as e:
        print(f"[Logger-APK] Failed to write log: {e}")
        return None
