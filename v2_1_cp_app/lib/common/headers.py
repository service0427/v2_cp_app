"""
헤더 빌더 모듈

Search API, SDP API, LJC API 등에 사용되는 헤더를 동적으로 생성합니다.
v1_cp_app의 HeaderBuilder 로직 기반.
"""
import time
from typing import Dict
from lib.device_profile import DeviceProfile


class HeaderBuilder:
    """
    API별 헤더 빌더
    """

    # LJC API 템플릿 (ljc.coupang.com)
    # 실제 캡처 기준: 4개 헤더만 사용
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
