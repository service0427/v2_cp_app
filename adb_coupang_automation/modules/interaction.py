from adb_coupang_automation.core.engine import AutomationEngine
import time
import random

class InteractionModule(AutomationEngine):
    def inspect_current_state(self):
        """Analyzes UI Dump and returns a state string."""
        print("[Interaction] Inspecting State...")
        self.dump_ui()
        content = self.get_ui_content()
        
        if 'package="com.sec.android.app.launcher"' in content: return "STATE_LAUNCHER"
        if 'com.nhn.android.search.InAppBrowser:id/inapp_greendot_owner' in content: return "STATE_MAIN"
        if 'text="검색어 또는 URL 입력"' in content: return "STATE_SEARCH_PAGE"
        return "STATE_UNKNOWN"

    def wake_and_unlock(self):
        """Checks for Screen Off/Lock state and wakes device."""
        self.dump_ui()
        content = self.get_ui_content()
        
        # Check for Keyguard / AOD / Charging Info
        if 'com.android.systemui:id/keyguard_root_view' in content or \
           'com.samsung.android.app.clockpack:id/aod_charging_info_layout' in content:
             print("[State] Detected Screen Off / Lock Screen. Waking up...")
             self.run_adb(["shell", "input keyevent 224"], check=False) # WAKEUP
             self.run_adb(["shell", "input keyevent 224"], check=False)
             time.sleep(1)
             print("[State] Swiping to Unlock...")
             self.run_adb(["shell", "input swipe 540 1800 540 500 300"], check=False)
             time.sleep(2)
             return True
        return False

    def ensure_main_screen(self):
        print("[Interaction] Checking current state (Green Dot Check)...")
        
        # 0. Handle Screen Off / Lock
        self.wake_and_unlock()

        max_reset_attempts = 5
        for i in range(max_reset_attempts):
            self.dump_ui()
            content = self.get_ui_content()
            
            # 1. Launcher Check
            if 'package="com.sec.android.app.launcher"' in content:
                 print("[State] Detected Launcher. Relaunching App...")
                 self.run_adb(["shell", "monkey -p com.nhn.android.search -c android.intent.category.LAUNCHER 1"], check=False)
                 time.sleep(5)
                 continue

            # 2. Main Screen Check (Green Dot OR Search Bar)
            # Use specific ID for Green Dot: com.nhn.android.search:id/searchBarGreenDotImageView
            if 'com.nhn.android.search:id/searchBarGreenDotImageView' in content or \
               'com.nhn.android.search.InAppBrowser:id/inapp_greendot_owner' in content:
                print(f"[State] Green Dot Detected. Confirmed Main Screen.")
                return True
                
            # 3. If green dot missing, Press BACK
            print(f"[State] Green Dot NOT found (Attempt {i+1}). Pressing BACK to reset...")
            self.run_adb(["shell", "input keyevent 4"], check=False)
            time.sleep(2)
            
        print("[Failure] Could not return to Main Screen after multiple BACKs.")
        return False

    def verify_search_page(self, max_retries=10):
        """Checks if Search Page is active (Retries included)."""
        print("[Interaction] Verifying Search Page (Max 20s wait)...")
        for i in range(max_retries):
            self.dump_ui()
            content = self.get_ui_content()
            
            # Checks for Search Bar or 'search_edit_text' or '검색어 또는 URL 입력'
            is_search = 'text="검색어 또는 URL 입력"' in content or \
                        'resource-id="com.nhn.android.search:id/search_edit_text"' in content or \
                        'resource-id="com.nhn.android.search:id/searchBarView"' in content
            
            if is_search:
                print(f"[Success] Search Page Detected! (Attempt {i+1})")
                return True
            
            time.sleep(2)
        
        print("[Failure] Search Page NOT Detected after retries.")
        return False

    # [Inherited] tap_element logic from AutomationEngine is used now.
    # It supports 'identifier' keyword and basic regex parsing.
    
    # def get_element_center(self, content, resource_id): ... (Removed)
    # def tap_element(self, resource_id, fallback_x=None, fallback_y=None): ... (Removed)

    def run_scroll_and_click(self):
        print("[Interaction] Starting Scroll Sequence...")
            
        # 1. Scroll Sequence (Shared Logic)
        # 1. Scroll Sequence (Shared Logic)
        self.perform_browsing_scroll(scroll_down_count=5, scroll_up_count=1)

        # 2. Click Sticky Search Bar (Intelligent ID Finding)
        # ID from inspector: com.nhn.android.search:id/searchBarView
        # Fallback: 540, 200 (Old heuristic)
        print("[Interaction] Clicking Sticky Search Bar...")
        self.tap_element("com.nhn.android.search:id/searchBarView", fallback_x=540, fallback_y=200)

        # 3. Verify Search Page Entry (Robust Wait)
        print("[Interaction] Verifying Search Page (Max 20s wait)...")
        
        max_checks = 10
        found = False
        
        for check in range(max_checks):
            self.dump_ui()
            content = self.get_ui_content()
            
            # Indicators:
            # 1. "검색어 또는 URL 입력" (Placeholder)
            # 2. "최근 검색어"
            # 3. Edit Text resource ID
            if 'text="검색어 또는 URL 입력"' in content or \
               'text="최근 검색어 내역이 없습니다."' in content or \
               'resource-id="com.nhn.android.search:id/search_edit_text"' in content:
                 print(f"[Success] Search Page Detected! (Attempt {check+1})")
                 found = True
                 break
            
            print(f"[Interaction] Clean Search Page not found yet (Attempt {check+1})...")
            time.sleep(2)

        if found:
             return True
        else:
             print("[Failure] Search Page NOT Detected after timeout.")
             return False
