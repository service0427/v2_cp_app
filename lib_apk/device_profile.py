from dataclasses import dataclass, field
import uuid
import time
import random
import hashlib
from typing import Dict

from lib.utils import generate_x_signature


def java_name_uuid_from_bytes(name_bytes: bytes) -> str:
    """
    Java의 java.util.UUID.nameUUIDFromBytes(byte[] name)와 동일한 로직을 구현합니다.
    MD5 해시를 구한 뒤, version(3)과 variant(2 - IETF/Leach-Salz) 비트를 설정합니다.
    """
    m = hashlib.md5()
    m.update(name_bytes)
    md5_bytes = bytearray(m.digest())
    
    # Java UUID.nameUUIDFromBytes implementation details:
    # md5Bytes[6] &= 0x0f;  /* clear version        */
    # md5Bytes[6] |= 0x30;  /* set to version 3     */
    # md5Bytes[8] &= 0x3f;  /* clear variant        */
    # md5Bytes[8] |= 0x80;  /* set to IETF variant  */
    
    md5_bytes[6] &= 0x0f
    md5_bytes[6] |= 0x30
    md5_bytes[8] &= 0x3f
    md5_bytes[8] |= 0x80
    
    return str(uuid.UUID(bytes=bytes(md5_bytes)))

@dataclass
class DeviceProfile:
    # Required fields (used in context)
    model: str
    os_version: str
    width: int
    height: int
    pcid: str
    app_session_id: str
    ixid: str
    android_id: str
    dpi: str = "450"
    dpi_level: str = "XXHDPI"
    device_uuid: str = field(init=False)
    device_hash: str = field(init=False)
    app_version: str = "9.0.4"
    build_id: str = "AP3A.240905.015.A2"
    # 앱 설치 시점 타임스탬프 (cmg_dco용)
    install_timestamp: int = field(default=0)

    def __post_init__(self):
        # android_id를 기반으로 device_uuid 자동 생성
        # Coupang App은 ANDROID_ID(UTF-8)를 바이트로 변환 후 UUID.nameUUIDFromBytes()를 호출함
        if self.android_id:
            self.device_uuid = java_name_uuid_from_bytes(self.android_id.encode('utf-8'))
        else:
            self.device_uuid = str(uuid.uuid4())

        # device_hash 생성: SHA1(uuid|model|pcid)
        device_info = f"{self.device_uuid}|{self.model}|{self.pcid}"
        self.device_hash = hashlib.sha1(device_info.encode()).hexdigest()

        # install_timestamp 기본값 설정 (1~7일 전)
        if self.install_timestamp == 0:
            days_ago = random.randint(1, 7) * 24 * 60 * 60 * 1000
            self.install_timestamp = int(time.time() * 1000) - days_ago

    def get_coupang_app_header(self) -> str:
        """
        coupang-app 헤더 문자열 생성

        형식 (28개 필드, pipe 구분):
        COUPANG|Android|{OS}|{VER}||{FCM}|{UUID}|Y|{MODEL}|{UUID_NO_DASH}|{AD_ID}|XXHDPI|{PCID}||0||wifi|-1|||Asia/Seoul|{HASH}||{W}|{DPI}|-1|1.0|true
        """
        uuid_no_dash = self.device_uuid.replace('-', '')

        parts = [
            "COUPANG",              # 0
            "Android",              # 1
            self.os_version,        # 2
            self.app_version,       # 3
            "",                     # 4
            "null",                 # 5 (FCM token - null for non-login)
            self.device_uuid,       # 6
            "Y",                    # 7
            self.model,             # 8
            uuid_no_dash,           # 9
            self.app_session_id,    # 10 (ad_track_id 위치에 app_session_id)
            self.dpi_level,         # 11
            self.pcid,              # 12 ★ PCID (x-signature 계산에 사용)
            "",                     # 13
            "0",                    # 14
            "",                     # 15
            "wifi",                 # 16
            "-1",                   # 17
            "",                     # 18
            "",                     # 19
            "Asia/Seoul",           # 20
            self.device_hash,       # 21
            "",                     # 22
            str(self.width),        # 23
            self.dpi,               # 24
            "-1",                   # 25
            "1.0",                  # 26
            "true"                  # 27
        ]
        return "|".join(parts)

    def get_user_agent(self) -> str:
        """Dalvik User-Agent (Search/SDP API용)"""
        return f"Dalvik/2.1.0 (Linux; U; Android {self.os_version}; {self.model} Build/{self.build_id})"

    def get_okhttp_user_agent(self) -> str:
        """OkHttp User-Agent (LJC API용)"""
        return "okhttp/4.9.3"

    def get_cmg_dco(self) -> str:
        """x-cmg-dco 헤더 값 (앱 설치 시점 타임스탬프)"""
        return str(self.install_timestamp)

    def generate_signature(self, timestamp: int) -> str:
        """
        X-Signature 생성

        Args:
            timestamp: 현재 타임스탬프 (밀리초)

        Returns:
            64자 hex 서명 문자열
        """
        return generate_x_signature(str(timestamp), self.pcid)

    def generate_trace_id(self) -> str:
        """x-trace-ix-id 헤더 값 (세션 ixid)"""
        return self.ixid

# Helper function to generate random android_id (16 hex chars)
def generate_android_id():
    return "".join([random.choice("0123456789abcdef") for _ in range(16)])


def generate_pcid() -> str:
    """PCID 생성: timestamp(13자리) + random(10자리)"""
    return str(int(time.time() * 1000)) + "".join([str(random.randint(0, 9)) for _ in range(10)])


def create_device_profile(model: str = "SM-A165N") -> DeviceProfile:
    """
    새 DeviceProfile 인스턴스 생성

    매 호출마다 새로운 pcid, app_session_id, ixid 생성
    """
    return DeviceProfile(
        model=model,
        os_version="15",
        width=1080,
        height=2340,
        pcid=generate_pcid(),
        app_session_id=str(uuid.uuid4()),
        ixid=str(uuid.uuid4()),
        android_id=generate_android_id(),
        dpi="450",
        dpi_level="XXHDPI"
    )


# 기본 프로필 (모듈 로드 시 1회 생성 - run.py에서 context에 저장됨)
DEFAULT_PROFILE = create_device_profile("SM-A165N")
