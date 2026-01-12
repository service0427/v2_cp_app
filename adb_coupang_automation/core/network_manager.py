import subprocess
import time
import os

class NetworkManager:
    def __init__(self, device_id):
        self.device_id = device_id
    
    def run_adb(self, args, check=True):
        cmd = ["adb", "-s", self.device_id] + args
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result

    def update_wireguard_config(self, subnet):
        print(f"[Network] Updating WireGuard Config for Subnet {subnet}...")
        
        # User Provided Keys (2026-01-10)
        private_key = "yCtkzpXoQssoN2oWxBVVW6p2tJc6yM1zW+9PbPSu9lg=" 
        public_key = "PXcOM8fwfOU1IyP0uXduprYunXTK5XzdmUceagJZLSc="
        
        # Calculate new config
        address = f"10.8.{subnet}.0/24" 
        # port = 10000 + int(subnet) # Incorrect assumption
        # Doc says 55555 is the Endpoint Port
        endpoint = f"112.161.54.7:55555"
        
        config_content = f"""[Interface]
PrivateKey = {private_key}
Address = {address}
DNS = 1.1.1.1

[Peer]
PublicKey = {public_key}
Endpoint = {endpoint}
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25
"""
        # Write local temp
        with open("wg_temp.conf", "w") as f:
            f.write(config_content)
            
        # Push to device
        self.run_adb(["push", "wg_temp.conf", "/data/local/tmp/wg.conf"], check=False)
        
        # Move via SU and Fix Permissions
        # WireGuard needs app ownership (u0_aXXX). We need to find the UID.
        # But 'cp' usually preserves destination if overwriting? 
        # Safer to chown after.
        # Let's find owner of existing file first? 
        # Actually, let's just copy over and `chmod 600`. The app might reset ownership if it runs as user.
        # We'll use specific path.
        
        target_path = "/data/data/com.wireguard.android/files/wg.conf"
        
        # Identified Owner: u0_a333
        self.run_adb(["shell", "su -c 'cp /data/local/tmp/wg.conf /data/data/com.wireguard.android/files/wg.conf'"], check=False)
        self.run_adb(["shell", "su -c 'chmod 600 /data/data/com.wireguard.android/files/wg.conf'"], check=False)
        self.run_adb(["shell", "su -c 'chown u0_a333:u0_a333 /data/data/com.wireguard.android/files/wg.conf'"], check=False)
        
        # Restart WireGuard to pick up changes
        self.run_adb(["shell", "am force-stop com.wireguard.android"], check=False)
        time.sleep(1)
        # It will be started by 'lifecycle.reset_network' (SET_TUNNEL_UP)
        
        os.remove("wg_temp.conf")
        print(f"[Network] Config updated to {endpoint} ({address})")
