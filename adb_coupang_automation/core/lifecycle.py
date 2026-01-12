import subprocess
import time

class AppLifecycle:
    def __init__(self, device_id, pkg_name="com.coupang.mobile"):
        self.device_id = device_id
        self.pkg_name = pkg_name

    def run_adb(self, args, check=True):
        cmd = ["adb", "-s", self.device_id] + args
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result

    def force_stop(self):
        print(f"[Lifecycle] Force stopping {self.pkg_name}...")
        
        # Method 1: Standard AM Force Stop
        self.run_adb(["shell", f"am force-stop {self.pkg_name}"], check=False)
        
        # Method 2: Native Kill (Fail-safe for AMS crash)
        # Find PID
        res = self.run_adb(["shell", f"pidof {self.pkg_name}"], check=False)
        if res.returncode == 0 and res.stdout.strip():
            pid = res.stdout.strip()
            print(f"[Lifecycle] Process {pid} found. Executing Native Kill...")
            self.run_adb(["shell", "su", "-c", f"kill -9 {pid}"], check=False)

    def clear_data(self):
        print(f"[Lifecycle] Clearing data for {self.pkg_name}...")
        self.run_adb(["shell", f"pm clear {self.pkg_name}"], check=False)

    def grant_permission(self, permission):
        print(f"[Lifecycle] Granting permission: {permission}...")
        self.run_adb(["shell", f"pm grant {self.pkg_name} {permission}"], check=False)

    def launch(self):
        print(f"[Lifecycle] Launching {self.pkg_name}...")
        # Use monkey for reliable launch
        self.run_adb(["shell", f"monkey -p {self.pkg_name} -c android.intent.category.LAUNCHER 1"], check=False)
        # Check if launched?
        time.sleep(1)

    def restart(self):
        self.force_stop()
        time.sleep(1)
        self.launch()

    def clear_proxy(self):
        print(f"[Lifecycle] Clearing Global Proxy...")
        self.run_adb(["shell", "settings delete global http_proxy"], check=False)
        self.run_adb(["shell", "settings delete global global_http_proxy_host"], check=False)
        self.run_adb(["shell", "settings delete global global_http_proxy_port"], check=False)

    def set_wireguard_state(self, up=True):
        state = "UP" if up else "DOWN"
        print(f"[Lifecycle] Setting WireGuard Tunnel to {state}...")
        self.run_adb(["shell", f"am broadcast -a com.wireguard.android.action.SET_TUNNEL_{state} -e tunnel 'wg' -n com.wireguard.android/.model.TunnelManager\\$IntentReceiver"], check=False)
        time.sleep(2)

    def reset_network(self):
        self.clear_proxy()
        print("[Lifecycle] Network Reset (Proxies cleared).")
        return True

    def check_connection(self):
        # Check IP
        res_ip = self.run_adb(["shell", "ping -c 1 -W 2 8.8.8.8"], check=False)
        # Check DNS (Naver)
        res_dns = self.run_adb(["shell", "ping -c 1 -W 3 m.naver.com"], check=False)
        
        if res_ip.returncode == 0:
            if res_dns.returncode == 0:
                print("[Lifecycle] Network Online (DNS OK).")
                return True
            else:
                print("[Lifecycle] Internet OK but DNS FAILED (m.naver.com).")
                return False # Strict Fail
        else:
            print("[Lifecycle] Network Offline/Unreachable (IP Fail).")
            return False


    def kill_processes(self):
        print("[Lifecycle] Killing background processes (mitmdump, frida)...")
        subprocess.run(["pkill", "-9", "-f", "mitmdump"], capture_output=True)
        subprocess.run(["pkill", "-9", "-f", "frida"], capture_output=True)
        try:
             subprocess.run("fuser -k 8888/tcp", shell=True, stderr=subprocess.DEVNULL)
        except: pass
        time.sleep(1)

    def toggle_ip(self, subnet=20):
        print(f"[Lifecycle] Toggling IP (Subnet {subnet})...")
        max_retries = 3
        for attempt in range(max_retries):
            try:
                cmd = ["curl", "-s", f"http://112.161.54.7/toggle/{subnet}"]
                # Increased timeout to 30s
                res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                if res.returncode == 0:
                    print(f"[Lifecycle] Response: {res.stdout.strip()}")
                    return True
                else:
                    print(f"[Lifecycle] Toggle Failed: {res.stderr}")
            except subprocess.TimeoutExpired:
                print(f"[Lifecycle] Toggle Timeout (Attempt {attempt+1}/{max_retries})")
            except Exception as e:
                print(f"[Lifecycle] Toggle Error: {e}")
            
            # Wait before retry
            if attempt < max_retries - 1:
                time.sleep(5)
        
        print("[Lifecycle] Toggle Failed after retries.")
        return False

    def ensure_network_environment(self):
        """Prepares network, kills proxies, enforces VPN."""
        self.kill_processes()
        self.reset_network()

    def perform_cold_start(self):
        """Restarts the app cleanly."""
        # reset_network is handled globally in Phase 0.
        self.restart()
