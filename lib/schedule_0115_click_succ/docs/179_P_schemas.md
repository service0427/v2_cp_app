# Schema Documentation for 179_P_v2_bulksubmit_add_to_cart.py

## 1. Schema 15989: PageInteraction
*   **APK Source**: `smali_classes2/com/coupang/mobile/implicitlogging/PageInteraction.smali`
*   **Logic**: 사용자 터치/인터랙션 발생 시 로깅

| Field Path | Internal Source File | Variable / Extract Logic |
| :--- | :--- | :--- |
| `extra.pvid` | `128_G_v3_SEARCH_products.py` | `context['RESULT']['SEARCH']['srp_pvId']` |

## 2. Schema 10: SdpAddToCart (**CORE**)
*   **APK Source**: `smali_classes4/com/coupang/mobile/commonui/widget/schema/SdpAddToCart.smali`
*   **Logic**: `BottomButton` 위젯 클릭 리스너

| Field Path | Internal Source File | Variable / Extract Logic |
| :--- | :--- | :--- |
| `data` | `145_G_v1_PRODUCT_9024146312.py` | `sdp_atc_click_schemas[id=10]` (API Extract) |
| `data.currentWidget` | `179_P_v2_bulksubmit...py` | Patch: `bottom_button` |
| `data.toggleViewType` | `179_P_v2_bulksubmit...py` | Patch: `srp_grid` |

## 3. Schema 11599: QuantityPickerLogging
*   **APK Source**: `smali_classes18/com/coupang/mobile/domain/sdp/util/QuantityPickerLoggingListener.smali`
*   **Logic**: 수량 선택 다이얼로그 (Bottom Sheet) 로깅

| Field Path | Internal Source File | Variable / Extract Logic |
| :--- | :--- | :--- |
| `data` | `145_G_v1_PRODUCT_9024146312.py` | `sdp_atc_click_schemas[id=11599]` (API Extract) |
| `data.sdpHandlerClickType` | `179_P_v2_bulksubmit...py` | Patch: `add_to_cart` |

## 4. Schema 14044: ImplicitClick
*   **APK Source**: `smali_classes22/com/coupang/mobile/implicitlogging/ImplicitClick.smali`
*   **Logic**: 일반적인 `View.OnClickListener` 래핑

| Field Path | Internal Source File | Variable / Extract Logic |
| :--- | :--- | :--- |
| `data.traceId` | `145_G_v1_PRODUCT_9024146312.py` | `sdp_traceId` (API Extract) |
| `data.serverTime` | `145_G_v1_PRODUCT_9024146312.py` | `sdp_serverTime` (API Extract) |

