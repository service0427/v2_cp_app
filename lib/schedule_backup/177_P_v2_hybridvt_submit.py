import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 176
# Method: POST
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'content-type': 'application/json; charset=utf-8',
#     'content-length': '5518',
#     'accept-encoding': 'gzip',
#     'user-agent': 'okhttp/4.9.3'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://ljc.coupang.com/api/v2/submit?appCode=coupang&market=KR"
    method = "POST"
    
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'content-length': '5518',
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/4.9.3'
    }
    
    body = {
        'common': {
            'platform': 'android',
            'libraryVersion': '0.6.7',
            'pcid': '17679762746194168937968',
            'lang': 'ko-KR',
            'appCode': 'coupang',
            'market': 'KR',
            'resolution': '1080x2340',
            'eventTime': '2026-01-10T01:32:03.873+0900',
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
            'schemaId': 17261,
            'schemaVersion': 1
        },
        'data': {
            'logType': 'impression',
            'feedsId': 'feed-a64e2632136d4204be0c58dee1e586a1',
            'feedRank': '1',
            'pageName': 'recommendation',
            'feedItems': '[{"itemId":"24409829458","productId":"8439185584","vendorItemId":"91424479771","provider":"matrix-/substitute","rank":"1"},{"itemId":"21750796778","productId":"7919053402","vendorItemId":"88799830943","provider":"unifiedads-/sdp_hybrid_ads","rank":"2"},{"itemId":"25935242390","productId":"8884949333","vendorItemId":"92918611260","provider":"matrix-/substitute","rank":"3"},{"itemId":"24428807313","productId":"8444685695","vendorItemId":"91436171399","provider":"unifiedads-/sdp_hybrid_ads","rank":"4"},{"itemId":"8438609270","productId":"7628759993","vendorItemId":"75726214866","provider":"matrix-/substitute","rank":"5"},{"itemId":"24428814718","productId":"8444687533","vendorItemId":"91436309864","provider":"unifiedads-/sdp_hybrid_ads","rank":"6"},{"itemId":"20143517661","productId":"5757041374","vendorItemId":"87236848982","provider":"matrix-/substitute","rank":"7"},{"itemId":"24922351975","productId":"9061173786","vendorItemId":"86092898689","provider":"unifiedads-/sdp_hybrid_ads","rank":"8"},{"itemId":"26420312729","productId":"8709935753","vendorItemId":"93396231413","provider":"matrix-/substitute","rank":"9"},{"itemId":"24428810886","productId":"8444686525","vendorItemId":"91436320667","provider":"unifiedads-/sdp_hybrid_ads","rank":"10"},{"itemId":"26832005654","productId":"8243592423","vendorItemId":"86092864793","provider":"matrix-/substitute","rank":"11"},{"itemId":"24421841082","productId":"8442763813","vendorItemId":"91436221149","provider":"unifiedads-/sdp_hybrid_ads","rank":"12"},{"itemId":"27087300150","productId":"9183773210","vendorItemId":"94055536143","provider":"matrix-/substitute","rank":"13"},{"itemId":"23303276151","productId":"8288420616","vendorItemId":"89851702773","provider":"unifiedads-/sdp_hybrid_ads","rank":"14"},{"itemId":"19296108464","productId":"159350344","vendorItemId":"86341396382","provider":"matrix-/substitute","rank":"15"},{"itemId":"25638393129","productId":"8803844900","vendorItemId":"84647710212","provider":"matrix-/substitute","rank":"16"},{"itemId":"21322374997","productId":"7090545477","vendorItemId":"88564058207","provider":"matrix-/substitute","rank":"17"},{"itemId":"19233294235","productId":"2372056363","vendorItemId":"86349759998","provider":"matrix-/substitute","rank":"18"},{"itemId":"6377099894","productId":"4892312604","vendorItemId":"73672215064","provider":"matrix-/substitute","rank":"19"},{"itemId":"20586525320","productId":"7055759161","vendorItemId":"87661459847","provider":"matrix-/substitute","rank":"20"},{"itemId":"23287599545","productId":"8164038141","vendorItemId":"90319849721","provider":"matrix-/substitute","rank":"21"},{"itemId":"22815412699","productId":"70722118","vendorItemId":"89850248971","provider":"matrix-/substitute","rank":"22"},{"itemId":"19296648780","productId":"6177364303","vendorItemId":"86411266139","provider":"matrix-/substitute","rank":"23"},{"itemId":"23610447620","productId":"9257664763","vendorItemId":"90636105117","provider":"matrix-/substitute","rank":"24"},{"itemId":"26452012142","productId":"9021512661","vendorItemId":"93427451464","provider":"matrix-/substitute","rank":"25"},{"itemId":"20154266506","productId":"7319899585","vendorItemId":"80653279724","provider":"matrix-/substitute","rank":"26"},{"itemId":"25425082352","productId":"8035182632","vendorItemId":"92418182751","provider":"matrix-/substitute","rank":"27"},{"itemId":"5825713725","productId":"4664196008","vendorItemId":"73124080087","provider":"unifiedads-/sdp_hybrid_ads","rank":"28"},{"itemId":"2817652108","productId":"1653813380","vendorItemId":"85401959202","provider":"unifiedads-/sdp_hybrid_ads","rank":"29"},{"itemId":"24428804955","productId":"8444685081","vendorItemId":"91436098318","provider":"unifiedads-/sdp_hybrid_ads","rank":"30"}]',
            'feedSourceInfo': '{"type":"ITEM","productId":"9024146312","itemId":"26462223018"}',
            'sourceType': 'hybrid_vt',
            'feedId': 'feed-a64e2632136d4204be0c58dee1e586a1-1.43.312:hybrid_vt-P9024146312_I26462223018',
            'feedType': 'hybrid_vt',
            'domain': 'sdp',
            'eventName': 'hybrid_vt',
            'feedTargetArea': 'SDP',
            'logCategory': 'impression',
            'feedPlacementKey': '1.43.312'
        },
        'extra': {
            'sentTime': '2026-01-09T16:32:03.862Z'
        }
    }
    
    return run_request(session, method, url, headers, body)
