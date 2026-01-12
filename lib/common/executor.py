from curl_cffi import requests
from lib.logger import log_transaction
import inspect
import os

def run_request(session: requests.Session, method: str, url: str, headers: dict, body=None, step_name: str = None):
    """
    Common request executor for schedule modules.
    Handles header updates, request execution, logging, and error handling.
    """
    if step_name is None:
        try:
            # Get the caller's frame
            frame = inspect.currentframe().f_back
            # Get the filename of the caller
            filename = frame.f_code.co_filename
            # Extract step name from filename (e.g. /path/to/003_bulksubmit.py -> 003_bulksubmit)
            step_name = os.path.splitext(os.path.basename(filename))[0]
        except Exception:
            step_name = "unknown_step"
    # Update Session Headers
    session.headers.clear()
    
    # Remove content-length to let the library calculate it correctly
    if "content-length" in headers:
        del headers["content-length"]
        
    session.headers.update(headers)
    
    print(f"[{step_name}] {method} {url[:60]}...")
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
