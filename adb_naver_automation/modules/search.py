from adb_naver_automation.core.engine import AutomationEngine
import time

class SearchModule(AutomationEngine):
    def run(self, keyword):
        print(f"[Search] Starting Search for keyword: '{keyword}'")
        
        # 1. Tap Search Bar (Heuristic: Top Center)
        # Naver App Main Screen Search Bar is typically at (540, 260) roughly on 1080x2340
        # Let's try 540, 300 to be safe (or inspect dump later)
        print("[Search] Tapping Search Bar Area...")
        self.tap(540, 300) 
        time.sleep(1.5)
        
        # 2. Input Text
        print(f"[Search] Typing '{keyword}'...")
        # Handle Korean input if necessary (ADB `input text` needs ASCII or encoded)
        # For now, assume ADB can handle or we use clipboard.
        # ADB Shell `input text` requires escaping.
        self.run_adb(["shell", f"input text {keyword}"], check=False)
        time.sleep(1)
        
        # 3. Press Enter / Search
        print("[Search] Pressing Enter...")
        self.run_adb(["shell", "input keyevent 66"], check=False) # KEYCODE_ENTER
        time.sleep(3)
        
        print("[Search] Search Action Completed (Blind).")
        return True
