import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 154
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '12098',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/bulksubmit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '12098',
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/4.9.3'
    }
    
    body = [
        {
            'common': {
                'platform': 'android',
                'libraryVersion': '0.6.7',
                'pcid': '17679762746194168937968',
                'lang': 'ko-KR',
                'appCode': 'coupang',
                'market': 'KR',
                'resolution': '1080x2340',
                'eventTime': '2026-01-10T01:31:57.719+0900',
                'memberSrl': '',
                'app': {
                    'osVersion': '15',
                    'model': 'SM-A165N',
                    'appVersionName': '9.0.4',
                    'appVersionCode': 2409040,
                    'uuid': 'f0b740d2-3447-3b2b-b118-d66257275f8f'
                },
                'location': {
                    'region': 'KR',
                    'locale': 'ko-KR',
                    'mcc': '',
                    'timezone': 'Asia/Seoul'
                },
                'appId': 'com.coupang.mobile',
                'appSessionId': '56b36f12-6759-43bb-9077-f7cddcecc13c',
                'systemLanguage': 'ko'
            },
            'meta': {
                'schemaId': 14502,
                'schemaVersion': 3
            },
            'data': {
                'domain': 'SDP',
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'sdp',
                'eventName': 'sdp_atf_review_social_proof_nudge_impression',
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'productId': 9024146312,
                'itemId': 26462223018,
                'vendorItemId': 93437504336,
                'reviewRating': '4.0',
                'numberOfReviews': 1,
                'socialProofNumUsers': 1,
                'socialProofNumUsersList': ''
            },
            'extra': {}
        },
        {
            'common': {
                'platform': 'android',
                'libraryVersion': '0.6.7',
                'pcid': '17679762746194168937968',
                'lang': 'ko-KR',
                'appCode': 'coupang',
                'market': 'KR',
                'resolution': '1080x2340',
                'eventTime': '2026-01-10T01:31:57.751+0900',
                'memberSrl': '',
                'app': {
                    'osVersion': '15',
                    'model': 'SM-A165N',
                    'appVersionName': '9.0.4',
                    'appVersionCode': 2409040,
                    'uuid': 'f0b740d2-3447-3b2b-b118-d66257275f8f'
                },
                'location': {
                    'region': 'KR',
                    'locale': 'ko-KR',
                    'mcc': '',
                    'timezone': 'Asia/Seoul'
                },
                'appId': 'com.coupang.mobile',
                'appSessionId': '56b36f12-6759-43bb-9077-f7cddcecc13c',
                'systemLanguage': 'ko'
            },
            'meta': {
                'schemaId': 6739,
                'schemaVersion': 2
            },
            'data': {
                'logType': 'impression',
                'domain': 'sdp',
                'eventName': 'sdp_price_policy_info_button_impression',
                'logCategory': 'impression',
                'pageName': 'sdp',
                'productId': 9024146312,
                'itemId': 26462223018,
                'vendorItemId': 93437504336
            },
            'extra': {}
        },
        {
            'common': {
                'platform': 'android',
                'libraryVersion': '0.6.7',
                'pcid': '17679762746194168937968',
                'lang': 'ko-KR',
                'appCode': 'coupang',
                'market': 'KR',
                'resolution': '1080x2340',
                'eventTime': '2026-01-10T01:31:57.752+0900',
                'memberSrl': '',
                'app': {
                    'osVersion': '15',
                    'model': 'SM-A165N',
                    'appVersionName': '9.0.4',
                    'appVersionCode': 2409040,
                    'uuid': 'f0b740d2-3447-3b2b-b118-d66257275f8f'
                },
                'location': {
                    'region': 'KR',
                    'locale': 'ko-KR',
                    'mcc': '',
                    'timezone': 'Asia/Seoul'
                },
                'appId': 'com.coupang.mobile',
                'appSessionId': '56b36f12-6759-43bb-9077-f7cddcecc13c',
                'systemLanguage': 'ko'
            },
            'meta': {
                'schemaId': 15268,
                'schemaVersion': 2
            },
            'data': {
                'logType': 'impression',
                'domain': 'SDP',
                'eventName': 'sdp_saving_amount_impression',
                'logCategory': 'impression',
                'pageName': 'sdp',
                'productId': 9024146312,
                'itemId': 26462223018,
                'vendoritemId': 93437504336,
                'displayedDiscountAmount': 0
            },
            'extra': {}
        },
        {
            'common': {
                'platform': 'android',
                'libraryVersion': '0.6.7',
                'pcid': '17679762746194168937968',
                'lang': 'ko-KR',
                'appCode': 'coupang',
                'market': 'KR',
                'resolution': '1080x2340',
                'eventTime': '2026-01-10T01:31:57.774+0900',
                'memberSrl': '',
                'app': {
                    'osVersion': '15',
                    'model': 'SM-A165N',
                    'appVersionName': '9.0.4',
                    'appVersionCode': 2409040,
                    'uuid': 'f0b740d2-3447-3b2b-b118-d66257275f8f'
                },
                'location': {
                    'region': 'KR',
                    'locale': 'ko-KR',
                    'mcc': '',
                    'timezone': 'Asia/Seoul'
                },
                'appId': 'com.coupang.mobile',
                'appSessionId': '56b36f12-6759-43bb-9077-f7cddcecc13c',
                'systemLanguage': 'ko'
            },
            'meta': {
                'schemaId': 3432,
                'schemaVersion': 8
            },
            'data': {
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'sdp',
                'eventName': 'impression_pdd_widget',
                'domain': 'sdp',
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'productId': 9024146312,
                'itemId': 26462223018,
                'vendorItemId': 93437504336,
                'isWowMember': False,
                'pdd': '',
                'pddMessage': '',
                'cutoffTime': '',
                'isFreeShipping3pBadge': True,
                'isFreeReturn3pBadge': False,
                'isSameDayShipOut3pBadge': True,
                'isUrgent': False,
                'rocketType': 'NA'
            },
            'extra': {}
        },
        {
            'common': {
                'platform': 'android',
                'libraryVersion': '0.6.7',
                'pcid': '17679762746194168937968',
                'lang': 'ko-KR',
                'appCode': 'coupang',
                'market': 'KR',
                'resolution': '1080x2340',
                'eventTime': '2026-01-10T01:31:57.897+0900',
                'memberSrl': '',
                'app': {
                    'osVersion': '15',
                    'model': 'SM-A165N',
                    'appVersionName': '9.0.4',
                    'appVersionCode': 2409040,
                    'uuid': 'f0b740d2-3447-3b2b-b118-d66257275f8f'
                },
                'location': {
                    'region': 'KR',
                    'locale': 'ko-KR',
                    'mcc': '',
                    'timezone': 'Asia/Seoul'
                },
                'appId': 'com.coupang.mobile',
                'appSessionId': '56b36f12-6759-43bb-9077-f7cddcecc13c',
                'systemLanguage': 'ko'
            },
            'meta': {
                'schemaId': 10401,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'sdp',
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'sdp',
                'eventName': 'sdp_wow_cashback_nudge_impression',
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'productId': 9024146312,
                'itemId': 26462223018,
                'vendorItemId': 93437504336
            },
            'extra': {}
        },
        {
            'common': {
                'platform': 'android',
                'libraryVersion': '0.6.7',
                'pcid': '17679762746194168937968',
                'lang': 'ko-KR',
                'appCode': 'coupang',
                'market': 'KR',
                'resolution': '1080x2340',
                'eventTime': '2026-01-10T01:31:57.994+0900',
                'memberSrl': '',
                'app': {
                    'osVersion': '15',
                    'model': 'SM-A165N',
                    'appVersionName': '9.0.4',
                    'appVersionCode': 2409040,
                    'uuid': 'f0b740d2-3447-3b2b-b118-d66257275f8f'
                },
                'location': {
                    'region': 'KR',
                    'locale': 'ko-KR',
                    'mcc': '',
                    'timezone': 'Asia/Seoul'
                },
                'appId': 'com.coupang.mobile',
                'appSessionId': '56b36f12-6759-43bb-9077-f7cddcecc13c',
                'systemLanguage': 'ko'
            },
            'meta': {
                'schemaId': 17113,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'sdp',
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'sdp',
                'eventName': 'social_proof_area_view',
                'productId': 9024146312,
                'itemId': 26462223018,
                'vendorItemId': 93437504336,
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'isSocialProofEligibleList': '',
                'isSocialProofNudgeExist': False,
                'socialProofEligibleLocation': 'SDP_ATF'
            },
            'extra': {}
        },
        {
            'common': {
                'platform': 'android',
                'libraryVersion': '0.6.7',
                'pcid': '17679762746194168937968',
                'lang': 'ko-KR',
                'appCode': 'coupang',
                'market': 'KR',
                'resolution': '1080x2340',
                'eventTime': '2026-01-10T01:31:58.041+0900',
                'memberSrl': '',
                'app': {
                    'osVersion': '15',
                    'model': 'SM-A165N',
                    'appVersionName': '9.0.4',
                    'appVersionCode': 2409040,
                    'uuid': 'f0b740d2-3447-3b2b-b118-d66257275f8f'
                },
                'location': {
                    'region': 'KR',
                    'locale': 'ko-KR',
                    'mcc': '',
                    'timezone': 'Asia/Seoul'
                },
                'appId': 'com.coupang.mobile',
                'appSessionId': '56b36f12-6759-43bb-9077-f7cddcecc13c',
                'systemLanguage': 'ko'
            },
            'meta': {
                'schemaId': 248,
                'schemaVersion': 44
            },
            'data': {
                'domain': 'sdp',
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'sdp',
                'eventName': 'sdp_atf',
                'productId': 9024146312,
                'itemId': 26462223018,
                'vendorItemId': 93437504336,
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'q': '호박식혜 달빛',
                'searchId': '0797993d22350',
                'rank': 1,
                'sourceType': 'search',
                'invalid': False,
                'salePrice': 26990,
                'isOutOfStock': False,
                'isRetail': False,
                'categoryId': 0,
                'style': 'NORMAL',
                'firstPrice': '32000',
                'thirdPrice': '26990',
                'brandName': '',
                'isQuantityLimit': 'N',
                'layoutStyle': 'NORMAL',
                'offerCondition': 'NEW',
                'isLoyaltyMember': False,
                'hasPricePolicyInfo': True,
                'deliveryFee': 'free',
                'hasPrevPurchasedProduct': False,
                'reviewRating': '4.0',
                'isRlux': False,
                'isFarfetch': False,
                'brandId': -1,
                'canEGift': False,
                'vendorId': 'A01492649',
                'isBadReferencePrice': 'False',
                'originalPrice': '32000',
                'vendorName': '달빛기정떡',
                'ratingCount': 1,
                'isReviewScore': False,
                'discountRate': '15.0',
                'underThresholdCouponSavingAmount': 'null',
                'targetedCouponSavingAmount': 'null',
                'instantDiscountSavingAmount': 'null',
                'overThresholdCouponSavingAmount': 'null',
                'salesPrice': 26990,
                'isGiftable': False,
                'finalPrice': 26990,
                'abGroup': '',
                'wowUnderThresholdCouponThreshold': 'null',
                'ccidEligibleSavingAmount': 'null',
                'wowUnderThresholdCouponSavingAmount': 'null',
                'wowOverThresholdCouponSavingAmount': 'null',
                'abTestId': '',
                'unitPrice': '(100ml당 675원)',
                'isFreeDeliveryEligible': True,
                'underThresholdCouponThreshold': 'null',
                'isWeeklyPopularItem': False,
                'isBadDiscount': 'false',
                'anchorPrice': '32000',
                'isPremiumGrocery': False,
                'wowInstantDiscountSavingAmount': 'null',
                'hasCoupangRecoBadge': 'N',
                'wowCcidEligibleSavingAmount': 'null',
                'myCcidDiscountSavingAmount': 'null',
                'businessType': '3p',
                'remoteAreaShippingFeeBadge': 'False'
            },
            'extra': {
                'deliveryValueType': 'VENDOR_DELIVERY',
                'rocketWow': 'STANDARD',
                'memberStatus': 'NOT_MEMBER',
                'defaultAddressEligible': True,
                'layoutType': 'NORMAL',
                'hasReviewRating': 'true'
            }
        },
        {
            'common': {
                'platform': 'android',
                'libraryVersion': '0.6.7',
                'pcid': '17679762746194168937968',
                'lang': 'ko-KR',
                'appCode': 'coupang',
                'market': 'KR',
                'resolution': '1080x2340',
                'eventTime': '2026-01-10T01:31:58.042+0900',
                'memberSrl': '',
                'app': {
                    'osVersion': '15',
                    'model': 'SM-A165N',
                    'appVersionName': '9.0.4',
                    'appVersionCode': 2409040,
                    'uuid': 'f0b740d2-3447-3b2b-b118-d66257275f8f'
                },
                'location': {
                    'region': 'KR',
                    'locale': 'ko-KR',
                    'mcc': '',
                    'timezone': 'Asia/Seoul'
                },
                'appId': 'com.coupang.mobile',
                'appSessionId': '56b36f12-6759-43bb-9077-f7cddcecc13c',
                'systemLanguage': 'ko'
            },
            'meta': {
                'schemaId': 11942,
                'schemaVersion': 6
            },
            'data': {
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'sdp',
                'eventName': 'ab_test_exposure',
                'domain': 'sdp',
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'productId': 9024146312,
                'itemId': 26462223018,
                'vendorItemId': 93437504336,
                'abGroup': 'A',
                'abTestId': '91432'
            },
            'extra': {}
        },
        {
            'common': {
                'platform': 'android',
                'libraryVersion': '0.6.7',
                'pcid': '17679762746194168937968',
                'lang': 'ko-KR',
                'appCode': 'coupang',
                'market': 'KR',
                'resolution': '1080x2340',
                'eventTime': '2026-01-10T01:31:58.043+0900',
                'memberSrl': '',
                'app': {
                    'osVersion': '15',
                    'model': 'SM-A165N',
                    'appVersionName': '9.0.4',
                    'appVersionCode': 2409040,
                    'uuid': 'f0b740d2-3447-3b2b-b118-d66257275f8f'
                },
                'location': {
                    'region': 'KR',
                    'locale': 'ko-KR',
                    'mcc': '',
                    'timezone': 'Asia/Seoul'
                },
                'appId': 'com.coupang.mobile',
                'appSessionId': '56b36f12-6759-43bb-9077-f7cddcecc13c',
                'systemLanguage': 'ko'
            },
            'meta': {
                'schemaId': 7,
                'schemaVersion': 82
            },
            'data': {
                'domain': 'sdp',
                'logCategory': 'view',
                'logType': 'page',
                'pageName': 'sdp',
                'eventName': 'sdp_product_page_view',
                'productId': 9024146312,
                'itemId': 26462223018,
                'vendorItemId': 93437504336,
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh',
                'style': 'NORMAL',
                'isLoyaltyMember': False,
                'searchId': '0797993d22350',
                'filterKey': 'GENDER_TAB:0',
                'q': '호박식혜 달빛',
                'sourceType': 'search',
                'soldOut': 'false',
                'rank': 1,
                'brandId': -1,
                'isRlux': False,
                'isFarfetch': False,
                'vendorId': 'A01492649',
                'offerCondition': 'NEW',
                'brandName': '',
                'invalid': False,
                'isCoupick': False,
                'isPremium': False,
                'withBundleOption': 'NONE',
                'canEGift': False,
                'isCcidEligible': False,
                'displayCcidBadge': False,
                'normalInstantDiscountRate': 0,
                'wowOnlyInstantDiscountRate': 0,
                'layoutStyle': 'NORMAL',
                'is3p': True,
                'isRocketMart': False,
                'isQuickView': False,
                'unitPrice': '(100ml당 675원)',
                'hasInstantDiscount': False,
                'hasWowInstantDiscount': False,
                'hasOverThreshCoupon': False,
                'hasWowOverThreshCoupon': False,
                'isGiftWrappingAvailable': False,
                'isRetailReturnedItem': False,
                'isOrangeBadge': False,
                'isPreOrder': False,
                'isRocketInstall': False,
                'hasBrandShop': False,
                'rocketType': 'NA',
                'hasPrevPurchasedProduct': False,
                'reviewRating': '4.0',
                'hasRuleBasedTitle': 'false',
                'isRuleBasedTitleEligible': 'false',
                'hasTimedealDiscount': False,
                'hasGoldboxDiscount': False,
                'isAlmostOOS': False,
                'isBadDiscount': 'false',
                'finalPrice': 26990,
                'appliedInstantDiscount': False,
                'appliedWowInstantDiscount': False,
                'appliedOverThreshCoupon': False,
                'appliedWowOverThreshCoupon': False,
                'appliedCcidApplied': False,
                'appliedWCcidApplied': False,
                'appliedTargetedCoupon': False,
                'toggleViewType': 'srp_grid',
                'hasDisplayMyCcidPrice': False,
                'isSocialProofEligibleList': '',
                'isUnderThreshold': False,
                'isPremiumGrocery': False,
                'extraAttributes': 'freshReorderNudgeFlag:false',
                'hasUspGeneratedByAi': False,
                'numAtfImages': '9',
                'isLanding': True,
                'appliedFontScale': '1.0',
                'systemFontScale': '1.0'
            },
            'extra': {
                'pvId': '92910302',
                'layoutType': 'NORMAL',
                'abCriteria': False
            }
        },
        {
            'common': {
                'platform': 'android',
                'libraryVersion': '0.6.7',
                'pcid': '17679762746194168937968',
                'lang': 'ko-KR',
                'appCode': 'coupang',
                'market': 'KR',
                'resolution': '1080x2340',
                'eventTime': '2026-01-10T01:31:58.046+0900',
                'memberSrl': '',
                'app': {
                    'osVersion': '15',
                    'model': 'SM-A165N',
                    'appVersionName': '9.0.4',
                    'appVersionCode': 2409040,
                    'uuid': 'f0b740d2-3447-3b2b-b118-d66257275f8f'
                },
                'location': {
                    'region': 'KR',
                    'locale': 'ko-KR',
                    'mcc': '',
                    'timezone': 'Asia/Seoul'
                },
                'appId': 'com.coupang.mobile',
                'appSessionId': '56b36f12-6759-43bb-9077-f7cddcecc13c',
                'systemLanguage': 'ko'
            },
            'meta': {
                'schemaId': 13840,
                'schemaVersion': 1
            },
            'data': {
                'domain': 'sdp',
                'logCategory': 'impression',
                'logType': 'impression',
                'pageName': 'sdp',
                'eventName': 'sdp_section_impression',
                'sectionNum': '1',
                'actionType': 'in',
                'productId': 9024146312,
                'itemId': 26462223018,
                'vendorItemId': 93437504336,
                'sdpVisitKey': 'fyuk5pnr11rkb1z4qh'
            },
            'extra': {}
        }
    ]
    
    return run_request(session, method, url, headers, body)
