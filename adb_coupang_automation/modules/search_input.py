from adb_coupang_automation.core.engine import AutomationEngine
import time
import re

class SearchInputModule(AutomationEngine):
    def inspect_state(self):
        """Dumps UI and returns content for analysis."""
        self.dump_ui()
        return self.get_ui_content()

    def is_search_page(self, content=None):
        """Checks if we are in Search Mode (Input field active)."""
        if content is None:
            content = self.inspect_state()
            
        # Indicators:
        # 1. Resource ID: com.coupang.mobile:id/edit_text (The search input)
        # 2. Text: "쿠팡에서 검색하세요!" or current search query
        # 3. Presence of Search History or Auto-complete list
        if "com.coupang.mobile:id/edit_text" in content:
            return True
        if "com.coupang.mobile:id/search_bar_container" in content:
            return True
        return False

    def is_keyboard_open(self, content=None):
        """
        Checks if Soft Keyboard is open by analyzing layout height.
        Heuristic: content container is significantly shorter than screen height (~2200).
        """
        if content is None:
            content = self.inspect_state()

        # Find android:id/content bounds
        try:
            match = re.search(r'resource-id="android:id/content".*?bounds="\[(\d+),(\d+)\]\[(\d+),(\d+)\]"', content)
            if match:
                x1, y1, x2, y2 = map(int, match.groups())
                height = y2 - y1
                # print(f"[Input] Content Height: {height} (Threshold: 1600)")
                
                if height < 1600: # Threshold for keyboard presence
                    return True
        except Exception as e:
            pass # Silent fail
            
        return False

    def ensure_search_ready(self):
        """
        Follows User Protocol:
        1. Check State (Search Mode?)
        2. Check Keypad (Open?)
        3. If no keypad, Tap Search Bar.
        4. Re-check Keypad.
        """
        print("[Input] Step 1: Verifying Search Mode...")
        content = self.inspect_state()
        
        if not self.is_search_page(content):
            print("[Failure] Not in Search Mode.")
            return False
        # print("[Success] In Search Mode.")

        print("[Input] Step 2: Checking Keyboard State...")
        if self.is_keyboard_open(content):
            print("[Success] Keyboard is ALREADY OPEN.")
            return True
        
        print("[Input] Keyboard CLOSED. Step 3: Tapping Input Field...")
        # Tap the search edit text
        if not self.tap_element(identifier='resource-id="com.coupang.mobile:id/edit_text"'):
             # Fallback
             self.tap(500, 250)
        
        time.sleep(2) # Wait for keyboard animation
        
        print("[Input] Step 4: Re-checking Keyboard State...")
        if self.is_keyboard_open():
             print("[Success] Keyboard Open confirmed.")
             return True
        else:
             print("[Warning] Keyboard state unclear. Proceeding anyway.")
             return True

    def clear_search_input(self):
        """test_clear_search_input - Disabled by user request."""
        print("[Input] Clearing Search Input SKIPPED (User Request to avoid Camera click).")
        return True
        
        # Original Logic (Disabled):
        # print("[Input] Clearing Search Input...")
        # if self.tap_element(identifier='resource-id="com.coupang.mobile:id/cancel_button"'): ...
        # self.tap(880, 186)

    def verify_input_content(self, expected_text):
        """Dumps UI and checks if input field contains expected text."""
        # print(f"[Input] Verifying Content matches '{expected_text}'...")
        content = self.inspect_state()
        
        # Check text attribute of com.coupang.mobile:id/edit_text
        if f'text="{expected_text}"' in content:
            # print("[Success] Input verified correctly.")
            return True
        else:
            # print("[Failure] Input mismatch or not found.")
            return False

    def get_search_input_text(self):
        """Extracts the actual text currently in the search bar."""
        content = self.inspect_state()
        # Find text="..." inside com.coupang.mobile:id/edit_text
        try:
            match = re.search(r'resource-id="com.coupang.mobile:id/edit_text".*?text="([^"]*)"', content)
            if match:
                text = match.group(1)
                # print(f"[Input] Current Text: '{text}'")
                return text
        except Exception as e:
            pass
            
        return ""
