#!/usr/bin/env python3
"""
쿠팡 앱 순수 패킷 캡처 도구 (TCPDUMP 기반)

기능:
    1. 기존 프록시/Frida 프로세스 정리 및 설정 초기화
    2. 기기 내 tcpdump 실행 (전체 패킷 캡처)
    3. 쿠팡 앱 자동 실행
    4. 사용자 조작 대기
    5. 종료 시 PC로 pcap 파일 가져오기

사용법:
    python3 cp_packet_capture.py
"""

import os
import sys
import time
import signal
import subprocess
import argparse
from datetime import datetime
from pathlib import Path

# 설정
DEVICE_ID = "RF9XC00EXGM"
PACKAGE_NAME = "com.coupang.mobile"
PROJECT_ROOT = Path("/home/tech/v2_cp_app")
CAPTURE_DIR = PROJECT_ROOT / "captures" / "packet"
REMOTE_PCAP_PATH = "/sdcard/cp_capture_temp.pcap"

# 글로벌 상태
tcpdump_process = None

def run_adb(cmd_list, check=True):
    """ADB 명령어 실행 헬퍼"""
    full_cmd = ["adb", "-s", DEVICE_ID] + cmd_list
    try:
        result = subprocess.run(
            full_cmd,
            capture_output=True,
            text=True,
            check=check
        )
        return result
    except subprocess.CalledProcessError as e:
        print(f"[ADB 오류] 명령어: {' '.join(full_cmd)}")
        print(f"  Stderr: {e.stderr.strip()}")
        return None

def run_adb_shell(shell_cmd, check=True):
    """ADB Shell 명령어 실행 헬퍼"""
    return run_adb(["shell", shell_cmd], check=check)

def run_adb_root_shell(shell_cmd, background=False):
    """Root 권한으로 ADB Shell 실행"""
    # su -c 'cmd' 형태로 실행
    cmd = f"su -c '{shell_cmd}'"
    
    if background:
        # 백그라운드 실행을 위해 subprocess.Popen 사용
        full_cmd = ["adb", "-s", DEVICE_ID, "shell", cmd]
        return subprocess.Popen(
            full_cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    else:
        return run_adb(["shell", cmd])

def cleanup_environment():
    """환경 정리: 프록시 해제, 프로세스 종료"""
    print("\n[초기화] 환경 정리 중...")

    # 1. PC 프로세스 정리
    print("  - PC: mitmproxy, frida 프로세스 종료")
    subprocess.run(["pkill", "-f", "mitmdump"], capture_output=True)
    subprocess.run(["pkill", "-f", "frida"], capture_output=True)

    # 2. 기기 프록시 해제
    print("  - 기기: 프록시 설정 해제")
    run_adb_shell("settings put global http_proxy :0", check=False)

    # 3. 기기 기존 tcpdump 종료
    print("  - 기기: 기존 tcpdump 프로세스 정리")
    run_adb_root_shell("pkill -f tcpdump", background=False)
    
    # 4. 기기 임시 파일 삭제
    run_adb_shell(f"rm -f {REMOTE_PCAP_PATH}", check=False)

def start_tcpdump():
    """기기에서 tcpdump 시작"""
    print(f"\n[캡처] tcpdump 시작 중... (저장소: {REMOTE_PCAP_PATH})")
    
    # -i any: 모든 인터페이스
    # -s 0: 패킷 전체 저장 (스냅샷 길이 무제한)
    # -w: 파일로 저장
    cmd = f"tcpdump -i any -s 0 -w {REMOTE_PCAP_PATH}"
    
    # 백그라운드로 실행하지만, Python 객체로 관리하지 않음 (adb shell이 블로킹되므로)
    # 대신 nohup 등을 사용하거나, Popen으로 실행 후 관리
    
    process = run_adb_root_shell(cmd, background=True)
    
    # 실행 확인을 위해 잠시 대기
    time.sleep(2)
    
    # 프로세스가 살아있는지 확인 (ps)
    check = run_adb_shell("ps -A | grep tcpdump", check=False)
    if check and "tcpdump" in check.stdout:
        print("[캡처] tcpdump 실행 성공")
        return process
    else:
        print("[오류] tcpdump 실행 실패! (루팅 권한 확인 필요)")
        if check:
            print(f"  ps output: {check.stdout}")
        return None

def launch_app():
    """쿠팡 앱 재실행"""
    print(f"\n[앱] 쿠팡 앱({PACKAGE_NAME}) 재실행 중...")
    
    # 강제 종료
    run_adb_shell(f"am force-stop {PACKAGE_NAME}")
    time.sleep(1)
    
    # 실행 (Monkey 활용)
    run_adb_shell(f"monkey -p {PACKAGE_NAME} -c android.intent.category.LAUNCHER 1")
    print("[앱] 실행 명령 전송 완료")

def stop_capture_and_pull():
    """캡처 종료 및 파일 가져오기"""
    print("\n\n" + "="*50)
    print("[종료] 캡처 중단 및 파일 저장")
    
    # 1. tcpdump 종료
    print("  - 기기: tcpdump 종료 중...")
    run_adb_root_shell("pkill -f tcpdump")
    time.sleep(1) # 파일 플러시 대기
    
    # 2. 파일 가져오기
    CAPTURE_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    local_path = CAPTURE_DIR / f"packet_{timestamp}.pcap"
    
    print(f"  - 파일 전송: 기기 -> PC ({local_path})")
    result = run_adb(["pull", REMOTE_PCAP_PATH, str(local_path)])
    
    if result and result.returncode == 0:
        print(f"\n[성공] 캡처 파일 저장 완료!")
        print(f"  경로: {local_path}")
        try:
            size = local_path.stat().st_size / 1024 / 1024
            print(f"  크기: {size:.2f} MB")
        except:
            pass
            
        # tshark 안내
        print("\n[분석 팁]")
        print(f"  tshark -r {local_path.name} -Y \"ssl.handshake.type == 1\" -T fields -e ssl.handshake.extensions_server_name | sort | uniq -c | sort -nr")
    else:
        print("\n[실패] 파일 가져오기 실패")
        
    # 3. 기기 임시 파일 삭제
    run_adb_shell(f"rm -f {REMOTE_PCAP_PATH}", check=False)
    
    sys.exit(0)

def main():
    global tcpdump_process
    
    # 시그널 핸들러
    signal.signal(signal.SIGINT, lambda s, f: stop_capture_and_pull())
    signal.signal(signal.SIGTERM, lambda s, f: stop_capture_and_pull())

    print("=" * 60)
    print("  쿠팡 앱 순수 패킷 캡처 (No SSL Bypass)")
    print("  Target: RF9XC00EXGM (Rooted)")
    print("=" * 60)

    # 1. 환경 정리
    cleanup_environment()

    # 2. 캡처 시작
    tcpdump_process = start_tcpdump()
    if not tcpdump_process:
        sys.exit(1)

    # 3. 앱 실행
    launch_app()

    # 4. 대기
    print("\n" + "-" * 60)
    print("  [녹화 중] 앱을 조작하세요 (검색, 상품 클릭 등)")
    print("  완료되면 Ctrl+C를 눌러 저장하세요.")
    print("-" * 60)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        stop_capture_and_pull()

if __name__ == "__main__":
    main()
