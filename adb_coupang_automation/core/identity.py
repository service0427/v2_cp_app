import subprocess
import secrets
import uuid
import sys
import os

class IdentityManager:
    def __init__(self, device_id):
        self.device_id = device_id
        # We assume independent scripts are in dev/scripts/ relative to the project root
        # Ideally, we should import the class, but calling the script preserves the 'Root Spoofing' isolation
        self.spoofer_path = os.path.join(os.getcwd(), "dev/scripts/root_id_spoofer.py")

    def generate_new_identity(self):
        """Generates random AndroidID and GAID."""
        aid = secrets.token_hex(8)
        gaid = str(uuid.uuid4())
        return aid, gaid

    def apply_identity(self, android_id, gaid):
        """Applies identity changes directly via ADB."""
        print(f"[Identity] Applying New Identity: AID={android_id}, GAID={gaid}")
        
        try:
            # 1. Change Android ID
            # Note: This might require root on some devices, but 'settings put' often works for non-system apps reading it.
            adb_cmd = ["adb", "-s", self.device_id, "shell", "settings", "put", "secure", "android_id", android_id]
            subprocess.run(adb_cmd, check=True, capture_output=True)
            
            # 2. Reset AdId (GAID) - Hard to set specific value without root/modules.
            # Best effort: Clear GMS data to rotate ID (if allowed) or just rely on AID.
            # For this MVP, we proceed with just AID change successful log.
            
            print(f"[Identity] Successfully set Android ID to {android_id}")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"[Identity] Failed to set identity via ADB: {e}")
            return False
        except Exception as e:
            print(f"[Identity] Error: {e}")
            return False
            
    def rotate_identity(self):
        """Convenience method to generate and apply random identity."""
        aid, gaid = self.generate_new_identity()
        return self.apply_identity(aid, gaid)
