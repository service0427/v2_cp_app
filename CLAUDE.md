# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Language Policy

- **전용 언어**: 한국어 (Korean)
- 모든 대화, 주석, 문서는 **한국어**로 작성

## Project Overview

쿠팡(Coupang) 앱 API 자동화 프로젝트. **현재 개발 진행 중**.

**핵심 개발 워크플로우**:
1. `captures/` 폴더에 실제 쿠팡 앱의 HTTP 요청을 캡처한 JSON 파일 저장
2. 캡처 파일을 분석하여 `lib/schedule/` 모듈 작성
3. `run.py`가 schedule 모듈들을 순차 실행하여 앱 동작 재현

**자동화 방식**:
1. **HTTP API 방식** (`run.py`): `curl-cffi`를 사용한 API 레벨 자동화 - **주력 개발 중**
2. **ADB 방식** (`run_coupang_bot.py`, `run_naver_bot.py`): ADB를 통한 UI 자동화

## Commands

```bash
# HTTP API 자동화 실행
python run.py --q "검색어" --productId "상품ID" --vendorItemId "벤더ID" --itemId "아이템ID"
python run.py --limit 10                    # 처음 10개 스텝만 실행
python run.py --capture_file captures/xxx   # 캡처 파일에서 파라미터 추출

# ADB 자동화 실행
python run_coupang_bot.py --steps 3 --toggle-ip   # 쿠팡 봇 3회 반복 (IP 토글)
python run_naver_bot.py --steps 5                  # 네이버 봇 5회 반복

# 의존성 설치
pip install -r requirements.txt   # curl-cffi, beautifulsoup4
```

## Architecture

### HTTP API 자동화 (lib/)

```
lib/
├── schedule/           # 현재 활성 스텝 모듈 (개발 중)
├── schedule_backup/    # 전체 스텝 백업 (참조용)
├── common/executor.py  # HTTP 요청 실행 유틸 (run_request)
├── device_profile.py   # 디바이스 프로필 (DeviceProfile 클래스)
├── utils.py           # JA3 핑거프린트, StateManager, 시그니처 생성
├── capture_parser.py  # 캡처 파일 파싱 (q, productId, itemId, vendorItemId 추출)
└── logger.py          # 로깅 (LOG_BASE_DIR 사용)
```

**Schedule 모듈 작성 규칙**:
- 파일명: `{순번}_{타입}_{버전}_{설명}.py`
  - 타입: `G` = GET, `P` = POST, `S` = 기타
  - 예: `128_G_v3_SEARCH_products.py`, `133_P_v2_bulksubmit_srp_view_impression.py`
- `_SKIP_` 포함 시 자동 스킵
- 필수 함수: `run(session, context)` 또는 `run(session)`
- `lib/common/executor.py`의 `run_request()` 사용하여 요청 실행

**현재 구현된 주요 스텝** (`lib/schedule/`):
- `128_G_v3_SEARCH_products.py`: 검색 API (SRP)
- `133_P_v2_bulksubmit_srp_view_impression.py`: SRP 노출 로깅
- `145_G_v1_PRODUCT_*.py`: 상품 상세 API (SDP)
- `147_P_v2_bulksubmit_click_search_product.py`: 상품 클릭 로깅
- `156_P_v2_bulksubmit_srp_product_unit_impression.py`: 상품 단위 노출 로깅
- `179_P_v2_bulksubmit_add_to_cart.py`: 장바구니 추가

**Context 구조**:
```python
context = {
    'INPUT': {'q', 'productId', 'vendorItemId', 'itemId'},  # CLI 입력값
    'DEVICE': {'model', 'os_version', 'pcid', 'ixid', ...}, # 디바이스 정보
    'RESULT': {
        'ROOT': {},      # API 호출 필수값 (searchId, productId 등)
        'TARGET': {},    # 타겟 상품 정보
        'SEARCH': {},    # SRP 페이지 데이터
        'PRODUCT': {},   # SDP 페이지 데이터
        'META': {}       # 스키마 데이터
    }
}
```

### ADB 자동화 (adb_coupang_automation/, adb_naver_automation/)

```
adb_*/
├── core/
│   ├── engine.py       # AutomationEngine (ADB 명령 래퍼: tap, swipe, dump_ui)
│   ├── lifecycle.py    # AppLifecycle (앱 시작/종료, 네트워크, 권한)
│   ├── identity.py     # IdentityManager (기기 식별자 로테이션)
│   └── network_manager.py
├── modules/
│   ├── onboarding.py   # 온보딩 자동화
│   ├── interaction.py  # 스크롤, 탭 상호작용
│   ├── keyboard.py     # 한글 입력 (perform_hangul_typing)
│   ├── search_input.py # 검색창 조작
│   └── search_results.py # SERP 탐색, 상품 선택
└── utils/
```

**실행 흐름 (run_*_bot.py)**:
1. Identity Rotation → 2. App Launch (Data Clear) → 3. Onboarding → 4. Search Input → 5. Result Selection → 6. Product Interaction

## Development Workflow

**캡처 → 분석 → 모듈 작성 → 테스트** 사이클:

1. **캡처**: 실제 앱 사용 시 HTTP 요청을 `captures/capture_YYYYMMDD_HHMMSS.json`으로 저장
2. **파싱**: `capture_parser.py`가 캡처에서 검색어(`q`), `productId`, `itemId`, `vendorItemId` 추출
3. **모듈 작성**: 캡처된 요청을 `lib/schedule/` 모듈로 구현
4. **실행**: `python run.py --capture_file captures/xxx.json`으로 시나리오 재현

**captures/ 폴더**:
- 실제 쿠팡 앱의 HTTP 트래픽 캡처본 (JSON)
- 파일명에 검색어 포함 가능 (예: `capture_20260112_150945-소파.json`)

## Key Technical Details

- **TLS 핑거프린트**: `lib/utils.py`의 `JA3_STRING` 사용
- **디바이스 UUID 생성**: Java의 `UUID.nameUUIDFromBytes` 호환 (`lib/device_profile.py`)
- **로그 저장**: `lib.logger.LOG_BASE_DIR` 하위에 `SEARCH.log`, `context.log` 등 저장
- **IP 토글**: WireGuard VPN 제어 (`lifecycle.toggle_ip`)

## Working Principles

- 사용자 주도: 명시적 지시 없이 독단적 판단 금지
- 기술 스택: `curl-cffi` 기반
