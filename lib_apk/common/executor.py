"""
APK 기반 HTTP 요청 실행기
=========================

lib_apk 전용 독립 executor
"""

from curl_cffi import requests
from lib_apk.logger import log_transaction
import inspect
import os


def run_request(session: requests.Session, method: str, url: str, headers: dict, body=None, step_name: str = None):
    """
    Common request executor for APK-based schedule modules.
    """
    if step_name is None:
        try:
            frame = inspect.currentframe().f_back
            filename = frame.f_code.co_filename
            step_name = os.path.splitext(os.path.basename(filename))[0]
        except Exception:
            step_name = "unknown_step"

    session.headers.clear()

    if "content-length" in headers:
        del headers["content-length"]

    session.headers.update(headers)

    print(f"[APK:{step_name}] {method} {url[:60]}...")
    try:
        if body is not None:
            if isinstance(body, (dict, list)):
                response = session.request(method, url, json=body)
            else:
                response = session.request(method, url, data=body)
        else:
            response = session.request(method, url)

        print(f"      Status: {response.status_code}")

        log_transaction(
            method=method,
            url=url,
            req_headers=dict(session.headers),
            req_body=body,
            resp_status=response.status_code,
            resp_headers=dict(response.headers),
            resp_body=response.text,
            step_name=step_name
        )
        return response
    except Exception as e:
        print(f"      Error: {e}")
        return None
