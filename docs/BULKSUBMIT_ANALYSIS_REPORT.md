# Bulksubmit Schema Analysis Report

**분석 대상**: 25개 키워드 원본 패킷 데이터 vs 현재 구현
**분석 일자**: 2026-01-12

---

## 요약 (Executive Summary)

| 파일 | 스키마 수 | 심각 이슈 | 개선 필요 | 정상 |
|------|----------|----------|----------|------|
| 133_P | 8 | 0 | 3 | 5 |
| 147_P | 7 | 1 | 2 | 4 |
| 156_P | 7 | 1 | 2 | 4 |
| 179_P | 4 | 1 | 1 | 2 |

---

## 1. 133_P_v2_bulksubmit_srp_view_impression.py

### 발견된 스키마 (원본 캡처)
- 116_v23, 11942_v8, 11965_v15, 12636_v1, 15704_v1, 17211_v2, 7598_v1, 9854_v2

### 분석 결과

#### [OK] Schema 116_v23 (SrpPageView) - 핵심 스키마
| 필드 | 원본 | 현재 구현 | 상태 |
|------|------|----------|------|
| q | DYNAMIC | context.INPUT.q | OK |
| searchId | DYNAMIC | context.RESULT.ROOT.searchId | OK |
| searchCount | DYNAMIC | context.RESULT.ROOT.searchCount | OK |
| keywordType | DYNAMIC | context.RESULT.ROOT.keywordType | OK |
| ixid | DYNAMIC | context.DEVICE.ixid | OK |
| searchViewType | CONSTANT=LIST | 하드코딩 GRID_2 | **개선필요** |
| isCoupick | CONSTANT=False | context.RESULT.SEARCH.srp_isCoupick | OK |
| rankOfCoupick | CONSTANT=-1 | context.RESULT.SEARCH.srp_rankOfCoupick | OK |

**개선사항**:
- `searchViewType`: 원본은 항상 `LIST`인데, 현재는 `GRID_2` 하드코딩. 128_G에서 추출하도록 되어있지만, 원본 값이 LIST임을 확인 필요.

#### [OK] Schema 11942_v8 (AbTestExposureLog)
| 필드 | 원본 | 현재 구현 | 상태 |
|------|------|----------|------|
| abTestId | DYNAMIC (88343, 88344) | 하드코딩 88343, 88344 | **개선필요** |
| abGroup | DYNAMIC (A, B) | 하드코딩 A, B | **개선필요** |
| searchId | DYNAMIC | context.RESULT.ROOT.searchId | OK |

**개선사항**:
- `abTestId`, `abGroup`: 현재 하드코딩되어 있음. 128_G bypass.extra.abTestIds/abGroups에서 동적 추출 필요.

#### [OK] Schema 12636_v1 (Bypass)
- 현재 구현: `context.RESULT.META.SEARCH.12636_1` 에서 전체 bypass
- **상태**: OK - 서버 제공 스키마 그대로 전송

#### [OK] Schema 15704_v1 (SrpPaginationView)
- 모든 필드 정상 매핑

#### [OK] Schema 17211_v2, 7598_v1, 9854_v2, 11965_v15
- 시스템/에러 로깅 스키마 - 하드코딩 허용

---

## 2. 147_P_v2_bulksubmit_click_search_product.py

### 발견된 스키마 (원본 캡처)
- 11942_v6, 124_v53, 152_v4, 15989_v1, 7598_v1, 7960_v1, 9453_v2

### 분석 결과

#### [CRITICAL] Schema 124_v53 (SrpProductClick) - 핵심 스키마
| 필드 | 원본 | 현재 구현 | 상태 |
|------|------|----------|------|
| salePrice | CONSTANT=0 | 하드코딩 0 | **심각** |
| productId | DYNAMIC | bypass 사용 | OK |
| itemId | DYNAMIC | bypass 사용 | OK |
| vendorItemId | DYNAMIC | bypass 사용 | OK |
| deliveryBadge | DYNAMIC (4종) | bypass 사용 | OK |
| rocketType | DYNAMIC | bypass 사용 | OK |
| searchRank | DYNAMIC | bypass 사용 | OK |

**심각 이슈**:
- `salePrice`: 원본에서 항상 0으로 기록됨. 이는 원본 앱의 버그일 가능성 있음. 현재 구현도 동일하게 0.
- 실제로는 가격 정보가 있어야 정상인데, 원본 캡처와 동일하게 0으로 전송 중.

**Extra 필드 분석** (원본 기준):
| 필드 | 원본 | 현재 구현 | 상태 |
|------|------|----------|------|
| ratingCount | DYNAMIC (예: "(17)", "(1,701)") | bypass | OK |
| deliveryBadge | DYNAMIC | bypass | OK |
| abGroups | DYNAMIC | bypass | OK |
| abTestIds | DYNAMIC | bypass | OK |
| catalogBrandName | DYNAMIC | bypass | OK |
| highlightedKeywordsAvailable | DYNAMIC | bypass | OK |

#### [OK] Schema 11942_v6 (AbTestExposureLog)
- 현재 구현: bypass 사용
- **이슈**: 원본에서 `logCategory`, `logType` 필드 확인 필요
- 세션 로그에서 success: false 발생 가능성 있음

#### [OK] Schema 152_v4 (SrpProductRankingImpression)
| 필드 | 원본 | 현재 구현 | 상태 |
|------|------|----------|------|
| searchId | DYNAMIC (format: "searchId:rank") | 동일 형식 | OK |
| rank | DYNAMIC | context.RESULT.SEARCH.srp_rank | OK |
| totalCount | DYNAMIC | context.RESULT.ROOT.searchCount | OK |

#### [개선필요] Schema 7960_v1 (FeatureTracking) - Extra 필드
| 필드 | 원본 | 현재 구현 | 상태 |
|------|------|----------|------|
| KEY_PRODUCT_NAME | CONSTANT=None | None | **문제** |
| KEY_THUMBNAIL_IMAGE | CONSTANT=None | context.RESULT.SEARCH.srp_imageUrl | **불일치** |
| KEY_SALE_PRICE | CONSTANT="26,990원" | 하드코딩 | OK (원본도 상수) |
| KEY_RATING_COUNT | CONSTANT="(1)" | 하드코딩 | OK (원본도 상수) |
| KEY_RATING_AVERAGE | CONSTANT="4.0" | 하드코딩 | OK (원본도 상수) |
| sdp.discount | CONSTANT="15%" | 하드코딩 | OK |
| sdp.previousViewType | CONSTANT="LIST" | GRID_2 | **불일치** |

**개선사항**:
- `KEY_THUMBNAIL_IMAGE`: 원본은 항상 None, 현재는 동적 추출 시도 - 불필요한 처리
- `sdp.previousViewType`: 원본은 LIST, 현재는 GRID_2

---

## 3. 156_P_v2_bulksubmit_srp_product_unit_impression.py

### 발견된 스키마 (원본 캡처)
- 13697_v2, 137_v12, 14057_v2, 14741_v36, 15987_v1, 17062_v1, 18359_v1

### 분석 결과

#### [CRITICAL] Schema 14741_v36 (SrpProductUnitImpression) - 284 샘플
**심각 이슈**: 대부분의 필드가 빈 문자열("")로 기록됨

원본 데이터 분석:
```
[DATA FIELDS - 빈값으로 기록되는 필드들]
adIcon, anchorPrice, appliedCcidPrice, attributedTitle, badges, brandId,
deliveryBadge, discountRate, finalPriceString, rating, ratingAverage,
ratingCount, rocketType, unitname1, unitname2, vendorName... (100개 이상)
```

**실제 값이 있는 필드**:
| 필드 | 원본 | 현재 구현 | 상태 |
|------|------|----------|------|
| productId | DYNAMIC (246종) | UNIT_LOGS에서 추출 | OK |
| itemId | DYNAMIC (275종) | UNIT_LOGS에서 추출 | OK |
| vendorItemId | DYNAMIC (275종) | UNIT_LOGS에서 추출 | OK |
| q | DYNAMIC | context.INPUT.q | OK |
| searchId | DYNAMIC | context.RESULT.ROOT.searchId | OK |
| rank | DYNAMIC (0-31) | UNIT_LOGS에서 추출 | OK |
| exposureTimestamp | DYNAMIC | 동적 생성 | OK |
| ixid | DYNAMIC | context.DEVICE.ixid | OK |

**Extra 필드 (실제 값 존재)**:
| 필드 | 원본 | 현재 구현 | 상태 |
|------|------|----------|------|
| abGroups | DYNAMIC (64종) | UNIT_LOGS | 확인필요 |
| abTestIds | DYNAMIC (44종) | UNIT_LOGS | 확인필요 |
| catalogBrandName | DYNAMIC (165종) | UNIT_LOGS | 확인필요 |
| finalTitle | DYNAMIC (274종) | UNIT_LOGS | 확인필요 |
| priceInfo | DYNAMIC (271종) | UNIT_LOGS | 확인필요 |
| ratingCount | DYNAMIC (229종) | UNIT_LOGS | 확인필요 |

**결론**: 현재 구현은 UNIT_LOGS에서 hydration하는 방식으로 되어있음. 128_G에서 UNIT_LOGS가 올바르게 추출되고 있는지 검증 필요.

#### [OK] Schema 13697_v2 (SrpBrowseDuration)
| 필드 | 원본 | 현재 구현 | 상태 |
|------|------|----------|------|
| productIdList | DYNAMIC | UNIT_LOGS에서 추출 | OK |
| itemIdList | DYNAMIC | UNIT_LOGS에서 추출 | OK |
| vendorItemIdList | DYNAMIC | UNIT_LOGS에서 추출 | OK |
| itemStartTime | DYNAMIC | 동적 계산 | OK |
| itemEndTime | DYNAMIC | 동적 계산 | OK |
| vendorItemCount | DYNAMIC | len(UNIT_LOGS) | OK |

#### [CRITICAL] Schema 18359_v1 (Bypass)
현재 구현에서 `logCategory`, `logType` 누락 가능성:
- 원본: `logCategory=impression`, `logType=impression`
- bypass로 전달 시 이 필드들이 포함되어 있는지 확인 필요

#### [OK] Schema 137_v12, 14057_v2, 15987_v1, 17062_v1
- 성능 측정 스키마 - 하드코딩 허용

---

## 4. 179_P_v2_bulksubmit_add_to_cart.py

### 발견된 스키마 (원본 캡처)
- 10_v77, 11599_v4, 14044_v1, 15989_v1

### 분석 결과

#### [CRITICAL] Schema 10_v77 (SdpAddToCart) - 핵심 스키마
| 필드 | 원본 | 현재 구현 | 상태 |
|------|------|----------|------|
| currentWidget | CONSTANT="handlebar" | 없음/다름 | **심각** |
| benefitType | DYNAMIC (WOT, OT, WID) | bypass | 확인필요 |
| brandId | DYNAMIC | bypass | OK |
| brandName | DYNAMIC | bypass | OK |
| couponDiscountApplied | DYNAMIC | bypass | 확인필요 |
| discountRate | DYNAMIC | bypass | 확인필요 |
| finalPrice | DYNAMIC | bypass | OK |
| finalUnitPrice | DYNAMIC | bypass | 확인필요 |
| hasInstantDiscount | DYNAMIC | bypass | 확인필요 |
| hasOptionTable | DYNAMIC | bypass | 확인필요 |
| itemProductId | CONSTANT=4 | bypass | 확인필요 |
| layoutStyle | DYNAMIC (NORMAL, FASHION, CE) | bypass | 확인필요 |
| limitedTimeUrgencyType | CONSTANT | bypass | 확인필요 |
| manageCode | DYNAMIC | bypass | 확인필요 |
| originalPrice | DYNAMIC | bypass | 확인필요 |
| ratingAverage | DYNAMIC | bypass | 확인필요 |
| ratingCount | DYNAMIC | bypass | 확인필요 |
| salesPrice | DYNAMIC | bypass | 확인필요 |
| salesUnitPrice | DYNAMIC | bypass | 확인필요 |
| subSourceType | CONSTANT="handyman_srp" | bypass | 확인필요 |

**심각 이슈**:
- `currentWidget`: 원본은 항상 "handlebar", 현재 구현에서 이 필드가 없거나 다른 값

**Extra 필드**:
| 필드 | 원본 | 현재 구현 | 상태 |
|------|------|----------|------|
| currentView | CONSTANT="/search_list" | 하드코딩 | OK |
| eventReferrer | CONSTANT="sdp_click_duration" | 하드코딩 | OK |

#### [개선필요] Schema 11599_v4 (QuantityPickerLogging)
| 필드 | 원본 | 현재 구현 | 상태 |
|------|------|----------|------|
| sdpHandlerClickType | CONSTANT="add_to_cart" | bypass | 확인필요 |
| ynCouponDiscount | DYNAMIC (yes/no) | bypass | 확인필요 |
| ynInstantDiscount | DYNAMIC (yes/no) | bypass | 확인필요 |
| originalPrice | DYNAMIC | bypass | 확인필요 |
| salesPrice | DYNAMIC | bypass | 확인필요 |

#### [OK] Schema 14044_v1 (ImplicitClick)
| 필드 | 원본 | 현재 구현 | 상태 |
|------|------|----------|------|
| traceId | CONSTANT | context.RESULT.PRODUCT.sdp_traceId | OK |
| serverTime | DYNAMIC | datetime.now() | OK |
| pvid | DYNAMIC | context.RESULT.SEARCH.srp_pvId | OK |

---

## 종합 개선 권장사항

### 즉시 수정 필요 (Critical)

1. **179_P - Schema 10_v77**
   - `currentWidget` 필드 추가: 값 = "handlebar"
   - 현재 bypass에서 이 필드가 누락되었는지 확인

2. **156_P - Schema 18359_v1**
   - bypass 데이터에 `logCategory`, `logType` 포함 여부 확인
   - 누락 시 서버에서 validation 실패 가능

3. **147_P - Schema 11942_v6**
   - bypass 데이터 검증 필요

### 개선 권장 (Medium Priority)

1. **133_P - Schema 11942_v8**
   - `abTestId`, `abGroup`: 128_G에서 동적 추출하도록 개선
   - 현재 하드코딩 (88343/B, 88344/A) → bypass.extra에서 추출

2. **147_P - Schema 7960_v1**
   - `sdp.previousViewType`: "LIST"로 수정 (원본 일치)
   - `KEY_THUMBNAIL_IMAGE`: None으로 설정 (원본 일치)

3. **133_P - Schema 116_v23**
   - `searchViewType`: 원본 분석 결과 항상 "LIST" → 확인 필요

### 확인 필요 (Low Priority)

1. **156_P - Schema 14741_v36**
   - UNIT_LOGS에서 extra 필드들이 올바르게 hydration되는지 검증
   - 특히: abGroups, abTestIds, catalogBrandName, finalTitle, priceInfo

2. **179_P - Schema 10_v77, 11599_v4**
   - sdp_atc_click_schemas에서 모든 필드가 올바르게 추출되는지 검증

---

## 부록: 스키마별 필드 매핑 상세

### 원본 캡처 통계
- 총 키워드: 25개
- 총 샘플: 133_P(200), 147_P(175), 156_P(459), 179_P(100)
- 분석 기간: 20260112

### 동적 필드 vs 상수 필드 분류

| 스키마 | 동적 필드 | 상수 필드 |
|--------|----------|----------|
| 116_v23 | 5 (q, searchId, searchCount, keywordType, ixid) | 30+ |
| 124_v53 | 25+ | 20+ |
| 14741_v36 | 10 (핵심만) | 100+ (대부분 빈값) |
| 10_v77 | 30+ | 10 |

---

*End of Report*
