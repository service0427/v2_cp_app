# Schema Documentation for 156_P_v2_bulksubmit_srp_product_unit_impression.py

## 1. Schema 18359: Bypass (SDP Entry)
*   **APK Source**: N/A (Server-Side Injection via API Response - SDP Data)
*   **Logic**: Product API 응답 내 로깅 데이터 전송

| Field Path | Internal Source File | Variable / Extract Logic |
| :--- | :--- | :--- |
| `data` | `145_G_v1_PRODUCT_9024146312.py` | `context['RESULT']['META']['PRODUCT']['18359_1']` |

## 2. Schema 15987: ImplicitPageLeave
*   **APK Source**: `smali_classes22/com/coupang/mobile/implicitlogging/ImplicitPageLeave.smali`
*   **Logic**: Activity `onPause/onDestroy` 시점 로깅

| Field Path | Internal Source File | Variable / Extract Logic |
| :--- | :--- | :--- |
| `data.pvid` | `128_G_v3_SEARCH_products.py` | `context['RESULT']['SEARCH']['srp_pvId']` |

## 3. Schema 13697: SrpBrowseDuration
*   **APK Source**: `smali_classes18/com/coupang/mobile/domain/search/monitoring/schema/SrpBrowseDuration.smali`
*   **Logic**: `RecyclerView` 스크롤 리스너에서 아이템별 노출 시간 집계

| Field Path | Internal Source File | Variable / Extract Logic |
| :--- | :--- | :--- |
| `data.productIdList` | `156_P_v2_bulksubmit...py` | Aggregated from `UNIT_LOGS` |
| `data.itemStartTime` | `156_P_v2_bulksubmit...py` | Calculated (Index * 150ms) |

## 4. Schema 14741: SrpProductUnitImpression (**CORE**)
*   **APK Source**: `smali_classes18/com/coupang/mobile/domain/search/monitoring/schema/SrpProductUnitImpression.smali`
*   **Logic**: `ModuleBypass` + 클라이언트 수집 데이터

| Field Path | Internal Source File | Variable / Extract Logic |
| :--- | :--- | :--- |
| `data` | `128_G_v3_SEARCH_products.py` | `context['RESULT']['META']['UNIT_LOGS']` (Extract) |
| `data.viewType` | `156_P_v2_bulksubmit...py` | `searchViewType` based Patching |
| `data.productId` | `128_G_v3_SEARCH_products.py` | Extracted from `entityList` |
| `data.isRocket` | `128_G_v3_SEARCH_products.py` | Extracted from `entityList.badge` |

