# Schema Documentation for 133_P_v2_bulksubmit_srp_view_impression.py

## 1. Schema 17211: TtiWidgetMonitorLog
*   **APK Source**: `smali_classes5/com/coupang/mobile/commonui/filter/tti/schema/TtiWidgetMonitorLog.smali`
*   **Logic**: `ParseTimeInterceptor.e()` (Dynamic Calculation)

| Field Path | Internal Source File | Variable / Extract Logic |
| :--- | :--- | :--- |
| `data.widgetTotalCount` | `128_G_v3_SEARCH_products.py` | `context['RESULT']['SEARCH']['widgetTotalCount']` |
| `data.widgetTypeCount` | `128_G_v3_SEARCH_products.py` | `context['RESULT']['SEARCH']['widgetTypeCount']` |
| `data.widgetDistribution` | `128_G_v3_SEARCH_products.py` | `context['RESULT']['SEARCH']['widgetDistribution']` |
| `data.analyzeDuration` | `133_P_v2_bulksubmit...py` | `random.randint(1, 10)` (Simulated) |

## 2. Schema 9854: CommonCheckingAbnormalApi
*   **APK Source**: `smali_classes5/com/coupang/mobile/common/logger/internal/schema/CommonCheckingAbnormalApi.smali`
*   **Logic**: `DynamicTemplate` 렌더링 에러 (Error Logging)

| Field Path | Internal Source File | Variable / Extract Logic |
| :--- | :--- | :--- |
| `data.fullRequestURL` | `128_G_v3_SEARCH_products.py` | `context['RESULT']['SEARCH']['SEARCH_URL']` |
| `extra.viewType` | `128_G_v3_SEARCH_products.py` | `dynamic_templates[i]['viewType']` |
| `extra.errorMessage` | `128_G_v3_SEARCH_products.py` | `f"APP_{placementName}: variableMap"` |

## 3. Schema 15704: SrpPaginationView
*   **APK Source**: `smali_classes18/com/coupang/mobile/domain/search/monitoring/schema/SrpPaginationView.smali`
*   **Logic**: SRP 페이지네이션/뷰 노출 로깅

| Field Path | Internal Source File | Variable / Extract Logic |
| :--- | :--- | :--- |
| `data.q` | `128_G_v3_SEARCH_products.py` | `context['INPUT']['q']` |
| `data.searchId` | `128_G_v3_SEARCH_products.py` | `context['RESULT']['ROOT']['searchId']` |
| `data.rootSearchId` | `128_G_v3_SEARCH_products.py` | `context['RESULT']['ROOT']['searchId']` |

## 4. Schema 116: SrpPageView (**CORE**)
*   **APK Source**: `smali_classes18/com/coupang/mobile/domain/search/monitoring/schema/SrpPageView.smali`
*   **Logic**: `SrpViewModel`에서 페이지 로드 시 생성

| Field Path | Internal Source File | Variable / Extract Logic |
| :--- | :--- | :--- |
| `data.q` | `128_G_v3_SEARCH_products.py` | `context['INPUT']['q']` |
| `data.searchViewType` | `128_G_v3_SEARCH_products.py` | `context['RESULT']['SEARCH']['searchViewType']` |
| `data.searchId` | `128_G_v3_SEARCH_products.py` | `context['RESULT']['ROOT']['searchId']` |
| `data.searchCount` | `128_G_v3_SEARCH_products.py` | `context['RESULT']['ROOT']['searchCount']` |
| `data.isCoupick` | `128_G_v3_SEARCH_products.py` | `context['RESULT']['SEARCH']['isCoupick']` |
| `data.rankOfCoupick` | `128_G_v3_SEARCH_products.py` | `context['RESULT']['SEARCH']['rankOfCoupick']` |
| `data.keywordType` | `128_G_v3_SEARCH_products.py` | `context['RESULT']['ROOT']['keywordType']` |
| `data.ixid` | `User Config` | `context['DEVICE']['ixid']` |
| `extra.pvId` | `128_G_v3_SEARCH_products.py` | `context['RESULT']['SEARCH']['srp_pvId']` |
| `extra.dpi` | `User Config` | `context['DEVICE']['dpi_level']` |

## 5. Schema 12636: Bypass
*   **APK Source**: N/A (Server-Side Injection via API Response)
*   **Logic**: API 응답 내 `bypass` 필드 그대로 전송

| Field Path | Internal Source File | Variable / Extract Logic |
| :--- | :--- | :--- |
| `data` | `128_G_v3_SEARCH_products.py` | `Result.META.SEARCH.12636_1.data` (API Extract) |
| `extra` | `128_G_v3_SEARCH_products.py` | `Result.META.SEARCH.12636_1.extra` (API Extract) |

