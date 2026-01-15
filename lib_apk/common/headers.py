"""
APK 기반 헤더 빌더 모듈
======================

lib_apk 전용 독립 헤더 빌더
"""

from typing import Dict
from lib_apk.device_profile import DeviceProfile


class HeaderBuilder:
    """
    API별 헤더 빌더
    """

    LJC_TEMPLATE = {
        "content-type": "application/json; charset=utf-8",
        "accept-encoding": "gzip",
        "user-agent": "okhttp/4.9.3"
    }

    @staticmethod
    def build_ljc_headers(device: DeviceProfile = None) -> Dict[str, str]:
        """
        LJC API용 헤더 생성 (POST 요청)
        """
        return HeaderBuilder.LJC_TEMPLATE.copy()
