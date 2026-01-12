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

    # Search/SDP API 공통 템플릿 (cmapi.coupang.com)
    SEARCH_TEMPLATE = {
        "x-coupang-font-scale": "1.0",
        "run-mode": "production",
        "x-coupang-app-request": "true",
        "x-view-name": "/search",
        "x-coupang-target-market": "KR",
        "x-coupang-app-name": "coupang",
        "x-cp-app-id": "com.coupang.mobile",
        "x-coupang-origin-region": "KR",
        "x-coupang-accept-language": "ko-KR",
        "accept-encoding": "gzip"
    }

    # LJC API 템플릿 (ljc.coupang.com)
    # 실제 캡처 기준: 4개 헤더만 사용
    LJC_TEMPLATE = {
        "content-type": "application/json; charset=utf-8",
        "accept-encoding": "gzip",
        "user-agent": "okhttp/4.9.3"
    }

    @staticmethod
    def build_search_headers(device: DeviceProfile, view_name: str = "/search") -> Dict[str, str]:
        """
        Search/SDP API용 헤더 생성 (GET 요청)

        Args:
            device: DeviceProfile 인스턴스
            view_name: x-view-name 값 (기본: "/search")

        Returns:
            완전한 헤더 딕셔너리
        """
        headers = HeaderBuilder.SEARCH_TEMPLATE.copy()
        ts = int(time.time() * 1000)

        # 동적 값 설정
        headers["x-timestamp"] = str(ts)
        headers["x-cp-app-req-time"] = str(ts + 100)  # 약간의 지연
        headers["x-cmg-dco"] = device.get_cmg_dco()
        headers["coupang-app"] = device.get_coupang_app_header()
        headers["user-agent"] = device.get_user_agent()
        headers["x-trace-ix-id"] = device.generate_trace_id()
        headers["x-view-name"] = view_name

        # X-Signature 생성 (핵심!)
        headers["x-signature"] = device.generate_signature(ts)

        return headers

    @staticmethod
    def build_ljc_headers(device: DeviceProfile = None) -> Dict[str, str]:
        """
        LJC API용 헤더 생성 (POST 요청)

        실제 캡처 기준: 간단한 4개 헤더만 사용
        - content-type
        - content-length (자동)
        - accept-encoding
        - user-agent

        Args:
            device: DeviceProfile 인스턴스 (현재 미사용, 향후 확장용)

        Returns:
            헤더 딕셔너리
        """
        return HeaderBuilder.LJC_TEMPLATE.copy()

    @staticmethod
    def build_post_headers(device: DeviceProfile, view_name: str = "/search") -> Dict[str, str]:
        """
        POST 요청용 헤더 생성 (bulksubmit 등)

        Args:
            device: DeviceProfile 인스턴스
            view_name: x-view-name 값

        Returns:
            완전한 헤더 딕셔너리
        """
        headers = HeaderBuilder.build_search_headers(device, view_name)
        headers["content-type"] = "application/json; charset=utf-8"
        return headers
