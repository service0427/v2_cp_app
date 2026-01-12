import sys
import os
import json
from curl_cffi import requests

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.common.executor import run_request
from lib.device_profile import DEFAULT_PROFILE

# Reference Data Index: 195
# Method: GET
#
# Original Headers (Comparison):
# ------------------------------
# {
#     'sec-ch-ua-platform': '"Android"',
#     'user-agent': 'Mozilla/5.0 (Linux; Android 15; SM-A165N Build/AP3A.240905.015.A2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/131.0.6778.260 Mobile Safari/537.36',
#     'sec-ch-ua': '"Android WebView";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
#     'sec-ch-ua-mobile': '?1',
#     'accept': '*/*',
#     'origin': 'https://m.coupang.com',
#     'x-requested-with': 'com.coupang.mobile',
#     'sec-fetch-site': 'same-site',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-dest': 'empty',
#     'referer': 'https://m.coupang.com/',
#     'accept-encoding': 'gzip, deflate, br, zstd',
#     'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
#     'priority': 'u=1, i',
#     'cookie': 'PCID=17857832397245944678246; MARKETID=17857832397245944678246; x-coupang-accept-language=ko-KR; x-coupang-target-market=KR; coupang-app=COUPANG%7CAndroid%7C15%7C9.0.4%7C%7Cnull%7Cf0b740d2-3447-3b2b-b118-d66257275f8f%7CY%7CSM-A165N%7Cf0b740d234472b2bb118d66257275f8f%7C25ede38a-c6e9-41b2-818a-aef7b5c17d0a%7CXXHDPI%7C17679762746194168937968%7C%7C0%7C%7Cwifi%7C-1%7C%7C%7CAsia%2FSeoul%7Cc658d419f4d046cfb15f281769b15de7fbc66b30%7C%7C1080%7C450%7C-1%7C1.0%7Ctrue; run-mode=production; helloCoupang=Y; ISAPP=Y; sid=c658d419f4d046cfb15f281769b15de7fbc66b30; timeZoneCode=Asia%2FSeoul; UUID=f0b740d2-3447-3b2b-b118-d66257275f8f; _abck=7DF9E938533E260EB5EC8122F70296E0~-1~YAAQxuQ1F4lcNDCbAQAAasSZow9UiLlwLftmvmG84OI6Z7jaByl9/6FGRuuEy75mIgzyu0hQareumpZFak+uU4N5zPsOeDNY5fetWth7vMUJGrHf0Z+G+kzY2sMhyPvHrDnT1toqzLuTJShUeh2EayCbz+VM41OHpNehjgiDPHR8Ljstf9ZMdhAGOPkWVNpyuBquD4qWZaZtyeNHoxockW5888/IDZAwYpy16EI3F9DvFwgqlIwUZI5Hkbrth6prrMGzIUGH8q0MAtj3rz1ZdwhUhG81noCKL6zC3tSnXpBianGAONg2gI/UVBrnQ0QKKVLZQWIGiH5jbQ/6VywI5HyBvniPRN8k9SsBJ1CPPF5SD7WifLgMYRK3d9GO8baGQaJRKptjwrNCr4P1HkfN2XxuDSZqzia+f3CqOddy94wsiDEeRzv7E9SkIx+cQ8PYXyTK+aNLfh2pCw==~-1~-1~-1~-1~-1; ak_bmsc=E210E7525785AD1289511BB99C366A11~000000000000000000000000000000~YAAQxuQ1F4pcNDCbAQAAasSZox5pRZcVkU4c7Gv2CSGwDCuwpB7mIj/YLqw1Ol3uluB1jBqY/7cfEGycTyBoNAiUG11vFJ1mOl1b9XYdeHZpngJ1LN+QMhLEWiXlXIQpCAI/h4d0pbWAgCS4htP4Xo2u1kZ7C7hUZcpYwsVBT9WQTADs0Lfv/H0MTlzN+u03DmbWkXPdenaZoX7+BXKCwgv/lgJOlrd0Y6MrqCLEaTviCAehZjxN+sxovLpWmF2dIwcP3xnNXLAwaal7Bd4xI41ZUClpm/kzBEGMuoDDVGiVRAE3Aydpi+KPmZcceWoV3lXXk0e+sG7FCcLHaI+j1rYLGSoehEp/tz82IFXSX6i6f/BtetTKaq9EUXDdio0EKSPkoGUDEfdrNHShQ/hs; bm_sz=4EBE15967595348588360A8DC3737A6F~YAAQxuQ1F4tcNDCbAQAAasSZox7jP/cJdM3eenGaejTh4yYLEa+jdJmN43T78bgAPHVFodrJ2yD4z0PbcQ7cvmi/ATfJFnPH1YPhYal0ovfPIDuH6EINepowvAUdRNMutCRB1MQAl3Y3RHtZr3yr/bxD4BhQh0Uq5d0r5GMZ+vIBBu6w5wca2/QtRqHtjTJTI/LQiCll5FWRO/LUWGivFu3ttzqd00oAAK1jqeKHjT8wOetY1bISuF+zSxB22wM7ReBkmQTlj+FD/NHG/if8zMIDykN8MMakBybM4zZRPqs59v5IaDSGVPaekrEn5XTkGa/iZ29Wh58ypaXWQhQEbCKKYQVKK/IHyUUKftwnxtvoF2MBcza+cD9H~3753012~3753013; bm_ss=ab8e18ef4e; bm_so=F1C71FC8C852B24A147D96CEE03D5A6C329EB6ED5ED835227DBB3C6597D33215~YAAQ1uQ1FyDRvDKbAQAAKdSZowblNBIvhR5paPu3eEKX+Er4iVJ2bdOiSp/jzayU123mylOouT+FTBz3Z/4zOKV7eADtasmSe7vgcZ9ZDdEpds30DaFh2Z4DY+HkTN/bPsIa1Yzltw47zT7xp8EAAqENZwvJeEwV6Tj1vkn7iN9sHAC61CFec5HS9sre7AY8AiUznUCI7FDQQXdSHX9ZuFfu74zoPOlaACAr5omU1KwlNSAPp9lFniilaxqIpBfZk0QW0HsPBTTSSs/jYM1NNzmuMCa3JnOfFIFX+EY+sBfaJeUkJdzuPrseehbMcJpT97m1Mm4PQFHFtgKVm4RTJpQty+uOlmreseuXjw+OBFqOsEh0UMahopFMHMhCdxv0KIeQjQDhMDaZAVrXcFgav4TrQNa5Ks3opnz1RY7g2DsA96Sj9h2lLPFQE9Guzi9IleXdXrXBMKxq7vw6aDY9kEE=; bm_s=YAAQ1uQ1FybRvDKbAQAAr9aZowToyIpXNtMrFgeRFx+3R8Idon+WZufGaiijC+ez8L8bUXH5OUYgmIngUNfLNGXCohtPCGAKyjZR6CKj1p+azIrxPB74Euf1UToVbAWt7ZADtcuweOSr/OnFAp4gc6YpdSFPv7WIFfKqlFrMP/GZ453qRhaHdJfCW53Lr3gJ/GFqFUWYCt1LykW2TEAx/4dAmToTKKJ+WQCkeOuGiHnR0X0JVU08tgBa0wk7n5WRY+29HLSlgiGKSezUw3VwEZu4a6NJN0Kn9XkqamRLFbPY8x52HwEVxqbRXTAu5PKA8CMUSdWBd6r5eeShcKi4sUc1WpKg7fP8c7CD3G6lmG9GCowTYCFdhFrRheBZCQAWTWrmztrMsVn8IbDHmPtECyWeRhg06LFawVmKVVSTsfnohLKRTK7Jh3GB1e2OuIvsR/7BbxJLhagD5oE3sxShisU0J1f9U4hTerXVy5h+X/maZYZkKl67Ov5qyZEyeO4gv5mSiXmJQBsgWtsdTSXqEtk1nNGhfwU33J22TwRIfYDo4103+Z77/IUqBO7kQgHMxVIOXAu83w==; bm_sv=F69AF6A4ED78E636ED4F63006D3E24F8~YAAQbOQ1F+oNizSbAQAAxt6Zox4CI64gaKTr2+Du36p5VFILmcfQ+qPP3gFfoeKU2S+ANF/iMGFLMfXKcNamIWXs0J4dNGjgyyw0X2HlrCdgcVLigPmGvpeMpzXG3nsa8DH2LakP0ej0RqcfvrA5qlGa2naEVZU+OGeYIBeb8eQu/4HwpzL4nJSM2YaIPAa2iArevSIOIDyKfQ8ilqa9WncwOOjQQSLXA6M/tx0NOFJLRzFd0rqpiXlB/ZozKTumIQ==~1'
# }
# ------------------------------

def run(session: requests.Session):
    url = "https://bpa-sdk.coupang.com/api/banner/ssva/sdpbottom?kanCategoryId=1474&productId=9024146312&itemId=26462223018&vendorItemId=93437504336"
    method = "GET"
    
    headers = {
        'sec-ch-ua-platform': '"Android"',
        'user-agent': 'Mozilla/5.0 (Linux; Android 15; SM-A165N Build/AP3A.240905.015.A2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/131.0.6778.260 Mobile Safari/537.36',
        'sec-ch-ua': '"Android WebView";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'accept': '*/*',
        'origin': 'https://m.coupang.com',
        'x-requested-with': 'com.coupang.mobile',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://m.coupang.com/',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'priority': 'u=1, i',
        'cookie': 'PCID=17857832397245944678246; MARKETID=17857832397245944678246; x-coupang-accept-language=ko-KR; x-coupang-target-market=KR; coupang-app=COUPANG%7CAndroid%7C15%7C9.0.4%7C%7Cnull%7Cf0b740d2-3447-3b2b-b118-d66257275f8f%7CY%7CSM-A165N%7Cf0b740d234472b2bb118d66257275f8f%7C25ede38a-c6e9-41b2-818a-aef7b5c17d0a%7CXXHDPI%7C17679762746194168937968%7C%7C0%7C%7Cwifi%7C-1%7C%7C%7CAsia%2FSeoul%7Cc658d419f4d046cfb15f281769b15de7fbc66b30%7C%7C1080%7C450%7C-1%7C1.0%7Ctrue; run-mode=production; helloCoupang=Y; ISAPP=Y; sid=c658d419f4d046cfb15f281769b15de7fbc66b30; timeZoneCode=Asia%2FSeoul; UUID=f0b740d2-3447-3b2b-b118-d66257275f8f; _abck=7DF9E938533E260EB5EC8122F70296E0~-1~YAAQxuQ1F4lcNDCbAQAAasSZow9UiLlwLftmvmG84OI6Z7jaByl9/6FGRuuEy75mIgzyu0hQareumpZFak+uU4N5zPsOeDNY5fetWth7vMUJGrHf0Z+G+kzY2sMhyPvHrDnT1toqzLuTJShUeh2EayCbz+VM41OHpNehjgiDPHR8Ljstf9ZMdhAGOPkWVNpyuBquD4qWZaZtyeNHoxockW5888/IDZAwYpy16EI3F9DvFwgqlIwUZI5Hkbrth6prrMGzIUGH8q0MAtj3rz1ZdwhUhG81noCKL6zC3tSnXpBianGAONg2gI/UVBrnQ0QKKVLZQWIGiH5jbQ/6VywI5HyBvniPRN8k9SsBJ1CPPF5SD7WifLgMYRK3d9GO8baGQaJRKptjwrNCr4P1HkfN2XxuDSZqzia+f3CqOddy94wsiDEeRzv7E9SkIx+cQ8PYXyTK+aNLfh2pCw==~-1~-1~-1~-1~-1; ak_bmsc=E210E7525785AD1289511BB99C366A11~000000000000000000000000000000~YAAQxuQ1F4pcNDCbAQAAasSZox5pRZcVkU4c7Gv2CSGwDCuwpB7mIj/YLqw1Ol3uluB1jBqY/7cfEGycTyBoNAiUG11vFJ1mOl1b9XYdeHZpngJ1LN+QMhLEWiXlXIQpCAI/h4d0pbWAgCS4htP4Xo2u1kZ7C7hUZcpYwsVBT9WQTADs0Lfv/H0MTlzN+u03DmbWkXPdenaZoX7+BXKCwgv/lgJOlrd0Y6MrqCLEaTviCAehZjxN+sxovLpWmF2dIwcP3xnNXLAwaal7Bd4xI41ZUClpm/kzBEGMuoDDVGiVRAE3Aydpi+KPmZcceWoV3lXXk0e+sG7FCcLHaI+j1rYLGSoehEp/tz82IFXSX6i6f/BtetTKaq9EUXDdio0EKSPkoGUDEfdrNHShQ/hs; bm_sz=4EBE15967595348588360A8DC3737A6F~YAAQxuQ1F4tcNDCbAQAAasSZox7jP/cJdM3eenGaejTh4yYLEa+jdJmN43T78bgAPHVFodrJ2yD4z0PbcQ7cvmi/ATfJFnPH1YPhYal0ovfPIDuH6EINepowvAUdRNMutCRB1MQAl3Y3RHtZr3yr/bxD4BhQh0Uq5d0r5GMZ+vIBBu6w5wca2/QtRqHtjTJTI/LQiCll5FWRO/LUWGivFu3ttzqd00oAAK1jqeKHjT8wOetY1bISuF+zSxB22wM7ReBkmQTlj+FD/NHG/if8zMIDykN8MMakBybM4zZRPqs59v5IaDSGVPaekrEn5XTkGa/iZ29Wh58ypaXWQhQEbCKKYQVKK/IHyUUKftwnxtvoF2MBcza+cD9H~3753012~3753013; bm_ss=ab8e18ef4e; bm_so=F1C71FC8C852B24A147D96CEE03D5A6C329EB6ED5ED835227DBB3C6597D33215~YAAQ1uQ1FyDRvDKbAQAAKdSZowblNBIvhR5paPu3eEKX+Er4iVJ2bdOiSp/jzayU123mylOouT+FTBz3Z/4zOKV7eADtasmSe7vgcZ9ZDdEpds30DaFh2Z4DY+HkTN/bPsIa1Yzltw47zT7xp8EAAqENZwvJeEwV6Tj1vkn7iN9sHAC61CFec5HS9sre7AY8AiUznUCI7FDQQXdSHX9ZuFfu74zoPOlaACAr5omU1KwlNSAPp9lFniilaxqIpBfZk0QW0HsPBTTSSs/jYM1NNzmuMCa3JnOfFIFX+EY+sBfaJeUkJdzuPrseehbMcJpT97m1Mm4PQFHFtgKVm4RTJpQty+uOlmreseuXjw+OBFqOsEh0UMahopFMHMhCdxv0KIeQjQDhMDaZAVrXcFgav4TrQNa5Ks3opnz1RY7g2DsA96Sj9h2lLPFQE9Guzi9IleXdXrXBMKxq7vw6aDY9kEE=; bm_s=YAAQ1uQ1FybRvDKbAQAAr9aZowToyIpXNtMrFgeRFx+3R8Idon+WZufGaiijC+ez8L8bUXH5OUYgmIngUNfLNGXCohtPCGAKyjZR6CKj1p+azIrxPB74Euf1UToVbAWt7ZADtcuweOSr/OnFAp4gc6YpdSFPv7WIFfKqlFrMP/GZ453qRhaHdJfCW53Lr3gJ/GFqFUWYCt1LykW2TEAx/4dAmToTKKJ+WQCkeOuGiHnR0X0JVU08tgBa0wk7n5WRY+29HLSlgiGKSezUw3VwEZu4a6NJN0Kn9XkqamRLFbPY8x52HwEVxqbRXTAu5PKA8CMUSdWBd6r5eeShcKi4sUc1WpKg7fP8c7CD3G6lmG9GCowTYCFdhFrRheBZCQAWTWrmztrMsVn8IbDHmPtECyWeRhg06LFawVmKVVSTsfnohLKRTK7Jh3GB1e2OuIvsR/7BbxJLhagD5oE3sxShisU0J1f9U4hTerXVy5h+X/maZYZkKl67Ov5qyZEyeO4gv5mSiXmJQBsgWtsdTSXqEtk1nNGhfwU33J22TwRIfYDo4103+Z77/IUqBO7kQgHMxVIOXAu83w==; bm_sv=F69AF6A4ED78E636ED4F63006D3E24F8~YAAQbOQ1F+oNizSbAQAAxt6Zox4CI64gaKTr2+Du36p5VFILmcfQ+qPP3gFfoeKU2S+ANF/iMGFLMfXKcNamIWXs0J4dNGjgyyw0X2HlrCdgcVLigPmGvpeMpzXG3nsa8DH2LakP0ej0RqcfvrA5qlGa2naEVZU+OGeYIBeb8eQu/4HwpzL4nJSM2YaIPAa2iArevSIOIDyKfQ8ilqa9WncwOOjQQSLXA6M/tx0NOFJLRzFd0rqpiXlB/ZozKTumIQ==~1'
    }
    
    body = None
    
    return run_request(session, method, url, headers, body)
