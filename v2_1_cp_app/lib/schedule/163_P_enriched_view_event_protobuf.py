import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 162
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/x-protobuf',
#     'content-length': '525',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://mercury.coupang.com/enriched-view-event-protobuf"
    method = "POST"
    
    headers = {
        'content-type': 'application/x-protobuf',
        'content-length': '525',
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/4.9.3'
    }
    
    body = '\n\x01\n\x07ANDROID\x12\x059.0.4*$b35cb0a0-ed78-11f0-9037-1d228fab5ce70\x0fB\x00J\x00R\x02\x12\x00Z(\x08机3\x12\x04show\x19\\(\\?"\x06\x08\x01\x10\x03*\x06\x08\x01\x10\x030\x01Z(\x08机3\x12\x04show\x19\x00\x00\x00\x00\x00\x00?"\x06\x08\x01\x10\x03*\x06\x08\x01\x10\x030\x02Z\x0f\x08机3\x12\x04hide0\x01b){"resolution":{"width":384,"height":832}}j\x1717679762746194168937968\n\x02\n\x07ANDROID\x12\x059.0.4*$b35cb0a0-ed78-11f0-8b76-d328a895e0de0\x13:\x046765B\x00J\x00R\x08\x12\x06\x08\x05\x10\x05Z(\x08机3\x12\x04show\x19\x00\x00\x00\x00\x00\x00?"\x06\x08\x03\x10\x01*\x06\x08\x03\x10\x010\x01Z(\x08机3\x12\x04show\x19q=\nףp?"\x06\x08\x03\x10\x01*\x06\x08\x03\x10\x010\x02Z\'\x08机3\x12\x04show\x19(\\?"\x06\x08\x03\x10\x01*\x05\x08\x03\x10:0\x03Z\x0f\x08机3\x12\x04hide0\x01b){"resolution":{"width":384,"height":832}}j\x1717679762746194168937968'
    
    return run_request(session, method, url, headers, body)
