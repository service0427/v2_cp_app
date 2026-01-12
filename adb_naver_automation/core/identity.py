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
        """Calls the root_id_spoofer.py script to apply identity."""
        print(f"[Identity] Applying New Identity: AID={android_id}, GAID={gaid}")
        
        cmd = [
            "python3", self.spoofer_path,
            "--android-id", android_id,
            "--gaid", gaid,
            "--deep-clean" # Always deep clean for new identity
        ]
        
        try:
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode == 0:
                print("[Identity] Success.")
                return True
            else:
                print(f"[Identity] Failed (Exit {res.returncode}):\n{res.stderr}")
                return False
        except Exception as e:
            print(f"[Identity] Error: {e}")
            return False
            
    def rotate_identity(self):
        """Convenience method to generate and apply random identity."""
        aid, gaid = self.generate_new_identity()
        return self.apply_identity(aid, gaid)
