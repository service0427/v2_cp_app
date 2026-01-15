#!/usr/bin/env python3
"""
APK 기반 스키마 vs 캡처 기반 스키마 비교 테스트
"""

import json
from datetime import datetime

# Mock context
mock_context = {
    'INPUT': {
        'q': '게이밍 의자',
        'productId': '9221117836',
        'vendorItemId': '87889515588',
        'itemId': '23456789'
    },
    'DEVICE': {
        'pcid': 'test-pcid-123',
        'ixid': 'test-ixid-456',
        'model': 'SM-A165N',
        'os_version': '14',
        'dpi': '450',
        'dpi_level': 'XHDPI'
    },
    'RESULT': {
        'ROOT': {
            'productId': '9221117836',
            'vendorItemId': '87889515588',
            'itemId': '23456789',
            'itemProductId': '4',
            'searchId': 'search-id-test',
            'searchCount': 1500,
            'keywordType': 'GENERAL'
        },
        'SEARCH': {
            'srp_rank': 5,
            'searchViewType': 'GRID_2',
            'internalCategoryId': '102942',
            'isCoupick': False,
            'rankOfCoupick': -1,
            'srp_productName': '게이밍 의자 테스트',
            'srp_finalPriceString': '129,000원',
            'srp_imageUrl': 'https://example.com/image.jpg'
        },
        'META': {
            'SEARCH': {
                '124_53': {
                    'data': {
                        'domain': 'srp',
                        'pageName': 'srp'
                    },
                    'extra': {}
                }
            }
        }
    },
    'srp_bypass_mandatory': {
        'q': '게이밍 의자',
        'internalCategoryId': '102942',
        'id': '9221117836',
        'itemProductId': '4',
        'searchRank': 5
    },
    'srp_click_log_bypass': {
        'mandatory': {
            'domain': 'srp',
            'pageName': 'srp',
            'q': '게이밍 의자',
            'productId': '9221117836'
        },
        'extra': {
            'beacon': 'test-beacon'
        }
    }
}


def test_apk_based():
    """APK 기반 모듈 테스트"""
    print("=" * 60)
    print("APK 기반 스키마 테스트")
    print("=" * 60)

    import sys
    sys.path.insert(0, '/home/tech/v2_cp_app')

    # 수동 테스트
    from lib.common.utils import generate_common_payload

    # Schema 124 구성 (APK 기반)
    schema_124_data = mock_context.get('srp_click_log_bypass', {}).get('mandatory', {}).copy()
    bypass_mandatory = mock_context.get('srp_bypass_mandatory', {})

    if not schema_124_data.get('q'):
        schema_124_data['q'] = bypass_mandatory.get('q')
    if not schema_124_data.get('internalCategoryId'):
        schema_124_data['internalCategoryId'] = bypass_mandatory.get('internalCategoryId')

    apk_payload = {
        'common': generate_common_payload(mock_context),
        'meta': {
            'schemaId': 124,
            'schemaVersion': 53
        },
        'data': schema_124_data,
        'extra': {
            'currentView': '/search_list',
            'eventReferrer': 'click_search_list'
        }
    }

    print("\n[APK 기반] Schema 124 페이로드:")
    print(f"  schemaId: {apk_payload['meta']['schemaId']}")
    print(f"  schemaVersion: {apk_payload['meta']['schemaVersion']}")
    print(f"  data.q: {apk_payload['data'].get('q')}")
    print(f"  data.productId: {apk_payload['data'].get('productId')}")
    print(f"  data.internalCategoryId: {apk_payload['data'].get('internalCategoryId')}")
    print(f"  extra: {apk_payload['extra']}")

    # 전체 body 크기 비교
    apk_body = [apk_payload]
    print(f"\n[APK 기반] 전송 스키마 수: {len(apk_body)}")

    return apk_body


def test_capture_based():
    """캡처 기반 모듈 (기존) 참조"""
    print("\n" + "=" * 60)
    print("캡처 기반 스키마 (기존 147 파일)")
    print("=" * 60)

    # 기존 147 파일의 스키마 수
    # Schema 7960 x2, 124, 7598, 9453, 152, 11942 = 7개
    print("\n[캡처 기반] 전송 스키마 수: 7개 (7960 x2, 124, 7598, 9453, 152, 11942)")
    print("  - Schema 7960: FeatureTracking (fbi_pup_migration)")
    print("  - Schema 124: SrpProductClick (핵심)")
    print("  - Schema 7598: CommonCheckingUnused")
    print("  - Schema 9453: FrameRenderingMetric")
    print("  - Schema 152: SrpProductRankingImpression")
    print("  - Schema 11942: AbTestExposureLog")


def main():
    print("\n" + "=" * 60)
    print("APK 기반 vs 캡처 기반 비교")
    print("=" * 60)

    apk_body = test_apk_based()
    test_capture_based()

    print("\n" + "=" * 60)
    print("결론")
    print("=" * 60)
    print("""
APK 기반 접근법:
  - 필수 스키마만 전송 (Schema 124)
  - 서버가 제공한 bypass 템플릿 활용
  - 불필요한 앱 내부 로깅 스키마 제거 (7598, 9453 등)

캡처 기반 접근법:
  - 실제 앱과 동일하게 모든 스키마 전송
  - 타이밍까지 재현 (1-5ms 간격)
  - 더 높은 Fidelity, 더 많은 데이터

권장:
  - 서버 로직에 필수인 스키마만 알면 APK 기반이 효율적
  - 완벽한 재현이 필요하면 캡처 기반 유지
""")


if __name__ == '__main__':
    main()
