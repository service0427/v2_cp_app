import json
import os
import uuid
import time
import hashlib
from typing import Dict

# JA3 Fingerprint
JA3_STRING = "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,16-10-43-51-17613-5-65281-35-11-0-65037-18-23-45-13-27,4588-29-23-24,0"

# Signature Utils
def get_current_timestamp() -> str:
    return str(int(time.time() * 1000))


def generate_x_signature(timestamp: str, pcid: str) -> str:
    """
    X-Signature 헤더 값 생성 (PcidVerification 알고리즘)

    알고리즘:
        X-Signature = SHA256(timestamp + pcid.takeLast(pcid.last().digitToInt())).toHex()

    단계별:
        1. pcid.last()         → PCID 마지막 문자 (예: "1")
        2. digitToInt()        → 정수 변환 (예: 1)
        3. pcid.takeLast(n)    → 마지막 n자 추출 (예: "1")
        4. timestamp + suffix  → 문자열 연결 (예: "17676005711021")
        5. SHA256().toHex()    → 64자 lowercase hex

    출처: com/coupang/mobile/common/network/PcidVerification.kt (Line 41-44)
    검증: 캡처 59건 100% 일치

    Args:
        timestamp: X-Timestamp 값 (밀리초, 문자열)
        pcid: coupang-app 헤더 12번째 필드

    Returns:
        64자 hex 문자열 (SHA256 결과)
    """
    if not pcid or not timestamp:
        raise ValueError("timestamp and pcid are required")

    # pcid.last().digitToInt() - PCID 마지막 문자를 정수로 변환
    last_char = pcid[-1]
    if not last_char.isdigit():
        raise ValueError(f"PCID last character must be a digit, got: {last_char}")

    n = int(last_char)

    # pcid.takeLast(n) - 마지막 n자 추출
    suffix = pcid[-n:] if n > 0 else ''

    # SHA256(timestamp + suffix)
    input_bytes = (timestamp + suffix).encode('utf-8')
    hash_result = hashlib.sha256(input_bytes).hexdigest()

    return hash_result








