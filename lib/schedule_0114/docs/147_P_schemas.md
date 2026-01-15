# Schema Documentation for 147_P_v2_bulksubmit_click_search_product.py

## 1. Schema 7960: FeatureTracking (FBI PUP Migration) (**CORE**)
*   **APK Source**: `smali/com/coupang/mobile/common/abtest/schema/FeatureTracking.smali`
*   **Logic**: SDP 전환 시 `ImageVO` 객체누수(Object Leak) 버그 포함

| Field Path | Internal Source File | Variable / Extract Logic |
| :--- | :--- | :--- |
| `extra.KEY_PICK_TYPE` | `128_G_v3_SEARCH_products.py` | `context['RESULT']['SEARCH']['srp_isCoupick']` |
| `extra.sdp.previousViewType` | `128_G_v3_SEARCH_products.py` | `context['RESULT']['SEARCH']['searchViewType']` |
| `extra.KEY_PRODUCT_ID` | `128_G_v3_SEARCH_products.py` | `context['RESULT']['ROOT']['productId']` |
| `extra.KEY_THUMBNAIL_IMAGE` | `147_P_v2_bulksubmit...py` | `f"com...ImageVO@{random_hash}"` (Bug Copy) |
| `extra.KEY_SALE_PRICE` | `128_G_v3_SEARCH_products.py` | `context['RESULT']['SEARCH']['srp_finalPriceString']` |
| `extra.KEY_RATING_COUNT` | `128_G_v3_SEARCH_products.py` | `context['RESULT']['SEARCH']['srp_ratingCountString']` |
| `extra.KEY_SEARCH_COUNT` | `128_G_v3_SEARCH_products.py` | `context['RESULT']['ROOT']['searchCount']` |
| `extra.KEY_SEARCH_ID` | `128_G_v3_SEARCH_products.py` | `context['RESULT']['ROOT']['searchId']` |
| `extra.KEY_SEARCH_RANK` | `147_P_v2_bulksubmit...py` | `int(rank) + 1` |

## 2. Schema 124: SrpProductClick (**CORE**)
*   **APK Source**: `smali_classes18/com/coupang/mobile/domain/search/monitoring/schema/SrpProductClick.smali`
*   **Logic**: `ModuleBypass` 데이터와 클라이언트 컨텍스트 병합

| Field Path | Internal Source File | Variable / Extract Logic |
| :--- | :--- | :--- |
| `data` (Base) | `128_G_v3_SEARCH_products.py` | `context['srp_click_log_bypass']['mandatory']` |
| `data.q` | `128_G_v3_SEARCH_products.py` | `bypass_mandatory['q']` or `INPUT.q` |
| `data.internalCategoryId` | `128_G_v3_SEARCH_products.py` | `bypass_mandatory['internalCategoryId']` |
| `data.id` | `128_G_v3_SEARCH_products.py` | `bypass_mandatory['id']` or `ROOT.productId` |
| `data.itemProductId` | `128_G_v3_SEARCH_products.py` | `bypass_mandatory['itemProductId']` |
| `data.rank` | `128_G_v3_SEARCH_products.py` | `bypass_mandatory['searchRank']` or `SEARCH.srp_rank` |
| `extra` | `128_G_v3_SEARCH_products.py` | `context['srp_click_log_bypass']['extra']` |

## 3. Schema 152: SrpProductRankingImpression
*   **APK Source**: `smali_classes18/com/coupang/mobile/domain/search/monitoring/schema/SrpProductRankingImpression.smali`
*   **Logic**: 스크롤 시 화면에 노출된 상품의 랭킹 로깅

| Field Path | Internal Source File | Variable / Extract Logic |
| :--- | :--- | :--- |
| `data.searchId` | `147_P_v2_bulksubmit...py` | `f"{searchId}:{rank}"` |
| `data.totalCount` | `128_G_v3_SEARCH_products.py` | `context['RESULT']['ROOT']['searchCount']` |
| `data.rank` | `128_G_v3_SEARCH_products.py` | `context['RESULT']['SEARCH']['srp_rank']` |

## 4. Schema 11942: AbTestExposureLog (AbTest)
*   **APK Source**: `smali_classes5/com/coupang/mobile/commonui/gnb/schema/AbTestExposureLog.smali`
*   **Logic**: `AbTestManager`에서 실험군 노출 시 로깅

| Field Path | Internal Source File | Variable / Extract Logic |
| :--- | :--- | :--- |
| `data.extraAttribute` | `147_P_v2_bulksubmit...py` | `abTestId` check (`85005` etc) |
| `data.abGroup` | `128_G_v3_SEARCH_products.py` | `context['RESULT']['SEARCH']['srp_abGroup']` |
| `data.abTestId` | `128_G_v3_SEARCH_products.py` | `context['RESULT']['SEARCH']['srp_abTestId']` |

