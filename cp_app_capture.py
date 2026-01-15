#!/usr/bin/env python3
"""
쿠팡 앱 트래픽 캡처 도구 (Frida SSL Bypass 포함)

사용법:
    python3 cp_app_capture.py              # 캡처 시작 (Frida SSL bypass + mitmproxy)
    python3 cp_app_capture.py --no-frida   # Frida 없이 (인증서 설치 필요)
    python3 cp_app_capture.py --no-proxy   # 프록시 설정 없이 (수동 설정용)
    python3 cp_app_capture.py --clear-data # 쿠팡 앱 데이터 초기화 후 시작

캡처 중:
    Ctrl+C 누르면 프록시 해제 + 로그 저장 + 종료
"""

import os
import sys
import json
import time
import signal
import subprocess
import argparse
import threading
from datetime import datetime
from pathlib import Path

# 설정
DEVICE_ID = "RF9XC00EXGM"
PROXY_PORT = 8888
PROJECT_ROOT = Path("/home/tech/v2_cp_app")
CAPTURE_DIR = PROJECT_ROOT / "captures"
SSL_BYPASS_SCRIPT = PROJECT_ROOT / "dev" / "adb_control" / "ssl_bypass.js"
COUPANG_APP_PACKAGE = "com.coupang.mobile"
PC_IP = None  # 자동 감지

# 캡처할 도메인 (쿠팡 관련)
CAPTURE_DOMAINS = [
    "ljc.coupang.com",        # LJC 로깅 API
    "cmapi.coupang.com",      # 검색/상품 API
    "api.coupang.com",        # 기타 API
    "m.coupang.com",          # 모바일 웹
    "coupang.com",            # 메인 도메인
]

# 글로벌 상태
captured_requests = []
capture_file = None
mitm_process = None
frida_process = None
use_frida = True


def get_pc_ip():
    """PC의 IP 주소 가져오기 (adb 연결용)"""
    global PC_IP
    if PC_IP:
        return PC_IP

    try:
        # ip addr로 로컬 IP 찾기
        result = subprocess.run(
            ["ip", "addr", "show"],
            capture_output=True, text=True
        )
        for line in result.stdout.split("\n"):
            if "inet " in line and "127.0.0.1" not in line:
                # "inet 192.168.0.100/24 ..."
                parts = line.strip().split()
                for i, p in enumerate(parts):
                    if p == "inet" and i + 1 < len(parts):
                        PC_IP = parts[i + 1].split("/")[0]
                        return PC_IP
    except:
        pass

    # 기본값
    PC_IP = "221.154.248.236"
    return PC_IP


def set_proxy():
    """Android 기기에 프록시 설정"""
    pc_ip = get_pc_ip()
    print(f"[프록시] 설정 중... {pc_ip}:{PROXY_PORT}")

    try:
        # WiFi 프록시 설정
        subprocess.run([
            "adb", "-s", DEVICE_ID, "shell",
            f"settings put global http_proxy {pc_ip}:{PROXY_PORT}"
        ], check=True, capture_output=True)
        print(f"[프록시] 설정 완료: {pc_ip}:{PROXY_PORT}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[프록시] 설정 실패: {e}")
        return False


def clear_proxy():
    """Android 기기 프록시 해제"""
    print("[프록시] 해제 중...")

    try:
        subprocess.run([
            "adb", "-s", DEVICE_ID, "shell",
            "settings put global http_proxy :0"
        ], check=True, capture_output=True)
        print("[프록시] 해제 완료")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[프록시] 해제 실패: {e}")
        return False


def save_capture():
    """캡처된 데이터 저장"""
    global captured_requests, capture_file

    if not captured_requests:
        print("[저장] 캡처된 요청 없음")
        return None

    CAPTURE_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    capture_file = CAPTURE_DIR / f"capture_{timestamp}.json"

    # 요약 정보 추가
    summary = {
        "capture_time": timestamp,
        "total_requests": len(captured_requests),
        "domains": list(set(r.get("host", "") for r in captured_requests)),
        "requests": captured_requests
    }

    with open(capture_file, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*60}")
    print(f"[저장 완료]")
    print(f"  파일: {capture_file}")
    print(f"  요청 수: {len(captured_requests)}")
    print(f"  도메인: {', '.join(summary['domains'][:5])}")
    print(f"{'='*60}")

    return capture_file


def cleanup(signum=None, frame=None):
    """정리: 프록시 해제 + 저장 + mitmproxy/frida 종료"""
    global mitm_process, frida_process

    print("\n\n[종료] 정리 중...")

    # 프록시 해제
    clear_proxy()

    # Frida 종료
    if frida_process:
        print("[Frida] 종료 중...")
        frida_process.terminate()
        try:
            frida_process.wait(timeout=3)
        except:
            frida_process.kill()
        frida_process = None

    # mitmproxy 종료
    if mitm_process:
        print("[mitmproxy] 종료 중...")
        mitm_process.terminate()
        try:
            mitm_process.wait(timeout=3)
        except:
            mitm_process.kill()
        mitm_process = None

    # 잠시 대기 후 캡처 데이터 로드 및 저장
    time.sleep(0.5)
    load_captured_requests()
    save_capture()

    print("[종료] 완료")
    sys.exit(0)


# mitmproxy 애드온 스크립트 생성
MITM_ADDON_SCRIPT = '''
import json
import sys
from mitmproxy import http

CAPTURE_DOMAINS = {domains}

captured = []

def request(flow: http.HTTPFlow):
    host = flow.request.host

    # [Mod] No Domain Filtering - Capture Everything
    # if not any(d in host for d in CAPTURE_DOMAINS):
    #    return

    req_data = {{
        "ts": flow.request.timestamp_start,
        "method": flow.request.method,
        "host": host,
        "path": flow.request.path,
        "url": flow.request.pretty_url,
        "headers": dict(flow.request.headers),
        "cookies": dict(flow.request.cookies),
    }}

    # POST body
    if flow.request.method == "POST" and flow.request.content:
        try:
            # deflate/gzip 압축 해제 시도
            import zlib
            try:
                body = zlib.decompress(flow.request.content)
            except:
                body = flow.request.content

            try:
                req_data["body"] = json.loads(body)
            except:
                # [Mod] Increased limit to 500KB
                req_data["body_raw"] = body.decode("utf-8", errors="ignore")[:500000]
        except Exception as e:
            req_data["body_error"] = str(e)

    # 파일에 즉시 저장 (append)
    with open("/tmp/mitm_capture.jsonl", "a") as f:
        f.write(json.dumps(req_data, ensure_ascii=False) + "\\n")

    # 콘솔 출력 (Highlight couplang logs)
    prefix = "*" if "coupang" in host else " "
    print(f"[{{flow.request.method}}] {{prefix}}{{host}}{{flow.request.path[:100]}}")

def response(flow: http.HTTPFlow):
    host = flow.request.host

    # [Mod] No Domain Filtering
    # if not any(d in host for d in CAPTURE_DOMAINS):
    #    return

    # Response body도 저장 (LJC 응답 확인용)
    if flow.response and flow.response.content:
        resp_data = {{
            "ts": flow.response.timestamp_end,
            "type": "response",
            "host": host,
            "path": flow.request.path,
            "status": flow.response.status_code,
        }}

        try:
            resp_data["body"] = json.loads(flow.response.content)
        except:
            # [Mod] Increased limit to 500KB
            if len(flow.response.content) < 500000:
                resp_data["body_raw"] = flow.response.content.decode("utf-8", errors="ignore")

        with open("/tmp/mitm_capture.jsonl", "a") as f:
            f.write(json.dumps(resp_data, ensure_ascii=False) + "\\n")
'''


def create_mitm_addon():
    """mitmproxy 애드온 스크립트 생성"""
    addon_path = Path("/tmp/mitm_addon.py")

    script = MITM_ADDON_SCRIPT.format(
        domains=json.dumps(CAPTURE_DOMAINS)
    )

    addon_path.write_text(script)
    return addon_path


def kill_existing_processes():
    """기존 mitmproxy/frida 프로세스 종료"""
    try:
        subprocess.run(["pkill", "-f", "mitmdump"], capture_output=True)
        subprocess.run(["pkill", "-f", "frida"], capture_output=True)
        time.sleep(1)
    except:
        pass


def check_frida_server():
    """frida-server 실행 확인 및 자동 시작"""
    try:
        # 1. 실행 중인지 확인
        result = subprocess.run(
            ["adb", "-s", DEVICE_ID, "shell", "ps -A | grep frida"],
            capture_output=True, text=True, timeout=3
        )
        if "frida-server" in result.stdout:
            print("[Frida] frida-server 실행 중")
            return True
            
        print("[Frida] frida-server가 실행 중이지 않습니다. 자동 시작 시도...")
        
        # 2. 실행 시도 (완전 비동기 - Popen 사용하거나 nohup)
        # 중요: su -c 내부에서 nohup 사용 및 stderr 리다이렉션 필수
        cmd = f"adb -s {DEVICE_ID} shell \"su -c 'nohup /data/local/tmp/frida-server >/dev/null 2>&1 &'\""
        subprocess.Popen(cmd, shell=True)
        
        time.sleep(3) # 시작 대기
        
        # 3. 재확인
        result = subprocess.run(
            ["adb", "-s", DEVICE_ID, "shell", "ps -A | grep frida"],
            capture_output=True, text=True, timeout=3
        )
        if "frida-server" in result.stdout:
            print("[Frida] frida-server 시작 성공")
            return True
            
        print("[Frida] frida-server 자동 시작 실패.")
        return False
        
    except Exception as e:
        print(f"[Frida] 확인 오류: {e}")
        return False
        
def launch_app_fallback():
    """ADB로 앱 강제 실행 (Frida 실패 시)"""
    print("[Fallback] ADB로 쿠팡 앱 실행 중...")
    try:
        # monkey 명령어로 패키지 실행 (Activity 이름 몰라도 됨)
        subprocess.run(
            ["adb", "-s", DEVICE_ID, "shell", f"monkey -p {COUPANG_APP_PACKAGE} -c android.intent.category.LAUNCHER 1"],
            capture_output=True, timeout=5
        )
    except Exception as e:
        print(f"[Fallback] 앱 실행 실패: {e}")


def clear_app_data():
    """쿠팡 앱 데이터 초기화"""
    print(f"[초기화] 쿠팡 앱 데이터 삭제 중...")

    try:
        # 앱 강제 종료
        subprocess.run(
            ["adb", "-s", DEVICE_ID, "shell", f"am force-stop {COUPANG_APP_PACKAGE}"],
            capture_output=True
        )
        time.sleep(1)

        # 앱 데이터 삭제
        result = subprocess.run(
            ["adb", "-s", DEVICE_ID, "shell", f"pm clear {COUPANG_APP_PACKAGE}"],
            capture_output=True, text=True
        )

        if "Success" in result.stdout:
            print("[초기화] 완료 - 앱이 초기 상태로 리셋됨")
            print("  (로그인, 설정, 캐시 모두 삭제)")
            return True
        else:
            print(f"[초기화] 실패: {result.stdout} {result.stderr}")
            return False

    except Exception as e:
        print(f"[초기화] 오류: {e}")
        return False


def start_frida():
    """Frida로 쿠팡 앱 실행 (SSL bypass)"""
    global frida_process

    if not SSL_BYPASS_SCRIPT.exists():
        print(f"[Frida] SSL bypass 스크립트 없음: {SSL_BYPASS_SCRIPT}")
        print("  스크립트 생성 중...")
        create_ssl_bypass_script()

    if not check_frida_server():
        return False

    # 앱 강제 종료
    print(f"[Frida] 쿠팡 앱 종료 중...")
    subprocess.run(
        ["adb", "-s", DEVICE_ID, "shell", f"am force-stop {COUPANG_APP_PACKAGE}"],
        capture_output=True
    )
    time.sleep(1)

    print(f"[Frida] SSL bypass 적용 중...")

    # Frida 실행 (Spawn)
    frida_path = "/home/tech/.local/bin/frida"
    frida_process = subprocess.Popen(
        [frida_path, "-D", DEVICE_ID, "-f", COUPANG_APP_PACKAGE, "-l", str(SSL_BYPASS_SCRIPT)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        cwd=str(SSL_BYPASS_SCRIPT.parent)
    )

    time.sleep(3)  # 앱 시작 대기

    if frida_process.poll() is not None:
        print("[Frida] 시작 실패!")
        return False

    print("[Frida] 쿠팡 앱 실행 완료 (SSL bypass 적용)")
    return True


def create_ssl_bypass_script():
    """SSL Pinning Bypass 스크립트 생성"""
    SSL_BYPASS_SCRIPT.parent.mkdir(parents=True, exist_ok=True)

    script = '''
// SSL Pinning Bypass for Android (OkHttp, Conscrypt, etc.)
Java.perform(function() {
    console.log("[*] SSL Pinning Bypass loaded");

    // OkHttp3 CertificatePinner
    try {
        var CertificatePinner = Java.use("okhttp3.CertificatePinner");
        CertificatePinner.check.overload("java.lang.String", "java.util.List").implementation = function(hostname, peerCertificates) {
            console.log("[+] OkHttp3 CertificatePinner bypassed for: " + hostname);
            return;
        };
        CertificatePinner.check.overload("java.lang.String", "[Ljava.security.cert.Certificate;").implementation = function(hostname, peerCertificates) {
            console.log("[+] OkHttp3 CertificatePinner bypassed for: " + hostname);
            return;
        };
    } catch(e) {
        console.log("[-] OkHttp3 CertificatePinner not found");
    }

    // TrustManagerImpl
    try {
        var TrustManagerImpl = Java.use("com.android.org.conscrypt.TrustManagerImpl");
        TrustManagerImpl.verifyChain.implementation = function(untrustedChain, trustAnchorChain, host, clientAuth, ocspData, tlsSctData) {
            console.log("[+] TrustManagerImpl bypassed for: " + host);
            return untrustedChain;
        };
    } catch(e) {
        console.log("[-] TrustManagerImpl not found");
    }

    // SSLContext
    try {
        var SSLContext = Java.use("javax.net.ssl.SSLContext");
        SSLContext.init.overload("[Ljavax.net.ssl.KeyManager;", "[Ljavax.net.ssl.TrustManager;", "java.security.SecureRandom").implementation = function(km, tm, sr) {
            console.log("[+] SSLContext.init bypassed");
            var TrustManager = Java.use("javax.net.ssl.X509TrustManager");
            var TrustAllCerts = Java.registerClass({
                name: "com.frida.TrustAllCerts",
                implements: [TrustManager],
                methods: {
                    checkClientTrusted: function(chain, authType) {},
                    checkServerTrusted: function(chain, authType) {},
                    getAcceptedIssuers: function() { return []; }
                }
            });
            var trustAllCerts = [TrustAllCerts.$new()];
            this.init(km, trustAllCerts, sr);
        };
    } catch(e) {
        console.log("[-] SSLContext bypass failed: " + e);
    }

    console.log("[*] SSL Bypass hooks installed");
});
'''

    SSL_BYPASS_SCRIPT.write_text(script)
    print(f"[Frida] SSL bypass 스크립트 생성됨: {SSL_BYPASS_SCRIPT}")


def start_mitmproxy():
    """mitmproxy 시작"""
    global mitm_process

    # 기존 프로세스 종료
    kill_existing_processes()

    # 임시 캡처 파일 초기화
    Path("/tmp/mitm_capture.jsonl").write_text("")

    addon_path = create_mitm_addon()

    print(f"[mitmproxy] 시작 중 (포트 {PROXY_PORT})...")

    mitm_process = subprocess.Popen(
        [
            "mitmdump",
            "-p", str(PROXY_PORT),
            "-s", str(addon_path),
            "--set", "block_global=false",
            "--set", "flow_detail=0",  # 기본 출력 최소화
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,  # stderr도 stdout으로
        bufsize=1,  # line buffered
        universal_newlines=True  # text mode
    )

    time.sleep(2)  # 시작 대기

    if mitm_process.poll() is not None:
        # 에러 메시지 출력
        output = mitm_process.stdout.read() if mitm_process.stdout else ""
        print(f"[mitmproxy] 시작 실패!")
        if output:
            print(f"  에러: {output[:200]}")
        return False

    print("[mitmproxy] 시작 완료")
    return True


def load_captured_requests():
    """임시 파일에서 캡처 데이터 로드"""
    global captured_requests

    capture_file = Path("/tmp/mitm_capture.jsonl")
    if not capture_file.exists():
        return

    captured_requests = []
    for line in capture_file.read_text().strip().split("\n"):
        if line:
            try:
                captured_requests.append(json.loads(line))
            except:
                pass


def monitor_output():
    """mitmproxy/frida 출력 모니터링 (별도 스레드)"""
    global mitm_process, frida_process

    while True:
        try:
            # mitmproxy 출력 (text mode)
            if mitm_process and mitm_process.poll() is None:
                line = mitm_process.stdout.readline()
                if line:
                    line = line.strip()
                    # mitmproxy 기본 로그 필터링 (우리 addon 출력만)
                    if line.startswith("[") and not line.startswith("[::"):
                        print(line)

            # frida 출력 (binary mode)
            if frida_process and frida_process.poll() is None:
                line = frida_process.stdout.readline()
                if line:
                    text = line.decode().strip()
                    # Frida 로그 중 중요한 것만 출력
                    if any(x in text for x in ["[+]", "[-]", "[*]", "Bypass"]):
                        print(f"[Frida] {text}")
        except Exception:
            pass

        time.sleep(0.05)


def main():
    global use_frida

    parser = argparse.ArgumentParser(description="쿠팡 앱 트래픽 캡처")
    parser.add_argument("--no-proxy", action="store_true", help="프록시 자동 설정 안함")
    parser.add_argument("--no-frida", action="store_true", help="Frida SSL bypass 없이 (인증서 설치 필요)")
    parser.add_argument("--clear-data", action="store_true", help="쿠팡 앱 데이터 초기화 후 시작")
    args = parser.parse_args()

    use_frida = not args.no_frida

    # Ctrl+C 핸들러
    signal.signal(signal.SIGINT, cleanup)
    signal.signal(signal.SIGTERM, cleanup)

    print("=" * 60)
    print("  쿠팡 앱 트래픽 캡처 도구")
    if use_frida:
        print("  (Frida SSL Bypass 모드)")
    print("=" * 60)
    print()

    # ADB 연결 확인
    result = subprocess.run(
        ["adb", "-s", DEVICE_ID, "get-state"],
        capture_output=True, text=True
    )
    if "device" not in result.stdout:
        print(f"[오류] 기기 연결 안됨: {DEVICE_ID}")
        sys.exit(1)
    print(f"[기기] 연결됨: {DEVICE_ID}")

    # 앱 데이터 초기화 (옵션)
    if args.clear_data:
        if not clear_app_data():
            print("[경고] 데이터 초기화 실패 - 계속 진행")

    # mitmproxy 시작
    if not start_mitmproxy():
        sys.exit(1)

    # 프록시 설정
    if not args.no_proxy:
        if not set_proxy():
            cleanup()
            sys.exit(1)
    else:
        print("[프록시] 수동 설정 모드 (--no-proxy)")

    # Frida로 앱 실행 (SSL bypass)
    if use_frida:
        if not start_frida():
            print("[경고] Frida 실패 - Fallback: ADB로 앱 실행 시도")
            launch_app_fallback()
            # print("  (인증서 오류 발생 가능)")

    print()
    print("-" * 60)
    print("  캡처 중... 앱에서 검색 → 상품 클릭 플로우 수행하세요")
    print("  종료하려면 Ctrl+C")
    print("-" * 60)
    print()

    # 출력 모니터링 스레드 시작
    monitor_thread = threading.Thread(target=monitor_output, daemon=True)
    monitor_thread.start()

    # 메인 루프
    try:
        while True:
            # 프로세스 상태 확인
            if mitm_process and mitm_process.poll() is not None:
                print("[mitmproxy] 프로세스 종료됨")
                break

            if use_frida and frida_process and frida_process.poll() is not None:
                print("[Frida] 프로세스 종료됨 - 앱이 종료되었거나 크래시 발생")
                break

            time.sleep(0.5)
    except KeyboardInterrupt:
        pass

    # 정리 (cleanup에서 load + save 처리)
    cleanup()


if __name__ == "__main__":
    main()
