from adb_naver_automation.core.engine import AutomationEngine
import time
import re

class SearchInputModule(AutomationEngine):
    def inspect_state(self):
        """Dumps UI and returns content for analysis."""
        self.dump_ui()
        return self.get_ui_content()

    def is_search_page(self, content=None):
        """Checks if current screen is the Search Page."""
        if content is None:
            content = self.inspect_state()
            
        # Indicators:
        # 1. Resource ID: com.nhn.android.search.InAppBrowser:id/search_window_edit
        # 2. Text: "검색어 또는 URL 입력"
        if "com.nhn.android.search.InAppBrowser:id/search_window_edit" in content:
            return True
        if 'text="검색어 또는 URL 입력"' in content:
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
        # Pattern: resource-id="android:id/content" ... bounds="[0,96][1080,1332]"
        try:
            match = re.search(r'resource-id="android:id/content".*?bounds="\[(\d+),(\d+)\]\[(\d+),(\d+)\]"', content)
            if match:
                x1, y1, x2, y2 = map(int, match.groups())
                height = y2 - y1
                print(f"[Input] Content Height: {height} (Threshold: 1600)")
                
                if height < 1600: # Threshold for keyboard presence
                    return True
        except Exception as e:
            print(f"[Input] Error parsing bounds: {e}")
            
        return False

    def ensure_search_ready(self):
        """
        Follows User Protocol:
        1. Check State (Search Page?)
        2. Check Keypad (Open?)
        3. If no keypad, Tap Search Bar.
        4. Re-check Keypad.
        """
        print("[Input] Step 1: Verifying Search Page...")
        content = self.inspect_state()
        
        if not self.is_search_page(content):
            print("[Failure] Not on Search Page.")
            return False
        print("[Success] On Search Page.")

        print("[Input] Step 2: Checking Keyboard State...")
        if self.is_keyboard_open(content):
            print("[Success] Keyboard is ALREADY OPEN.")
            return True
        
        print("[Input] Keyboard CLOSED. Step 3: Tapping Search Bar...")
        # Tap the search edit text directly
        # ID: com.nhn.android.search.InAppBrowser:id/search_window_edit
        # We need its center. Reuse interaction logic or parse here.
        # Simple parse for now:
        match = re.search(r'resource-id="com.nhn.android.search.InAppBrowser:id/search_window_edit".*?bounds="\[(\d+),(\d+)\]\[(\d+),(\d+)\]"', content)
        if match:
            x1, y1, x2, y2 = map(int, match.groups())
            cx, cy = (x1+x2)//2, (y1+y2)//2
            print(f"[Input] Tapping Search Box at ({cx}, {cy})...")
            self.tap(cx, cy)
            time.sleep(2) # Wait for keyboard animation
        else:
            print("[Error] Could not find search bar element to tap.")
            return False

        print("[Input] Step 4: Re-checking Keyboard State...")
        # Refresh Content
        content = self.inspect_state()
    def clear_search_input(self):
        """Clears the search input field by tapping the 'X' button or Long Press Delete."""
        print("[Input] Clearing Search Input...")
        
        # Method 1: Tap 'X' Button via ID
        # ID: com.nhn.android.search.InAppBrowser:id/search_window_editor_empty_button
        # Bounds: [815,164][883,232] -> Center (849, 198)
        # We can implement a specialized tap_element here or just tap the coordinates.
        print("[Input] Tapping 'X' Reset Button (search_window_editor_empty_button)...")
        # Try to tap by ID bounds if available? 
        # For now, let's use the explicit coordinate which we confirmed matches the ID.
        self.tap(849, 198)
        time.sleep(1)
        
        return True

    def verify_input_content(self, expected_text):
        """Dumps UI and checks if input field contains expected text."""
        print(f"[Input] Verifying Content matches '{expected_text}'...")
        content = self.inspect_state()
        
        # Check text attribute of com.nhn.android.search.InAppBrowser:id/search_window_edit
        if f'text="{expected_text}"' in content:
            print("[Success] Input verified correctly.")
            return True
        else:
            print("[Failure] Input mismatch or not found.")
            return False

    def get_search_input_text(self):
        """Extracts the actual text currently in the search bar."""
        content = self.inspect_state()
        # Find text="..." inside com.nhn.android.search.InAppBrowser:id/search_window_edit
        # Regex: resource-id="...search_window_edit".*?text="([^"]*)"
        try:
            match = re.search(r'resource-id="com.nhn.android.search.InAppBrowser:id/search_window_edit".*?text="([^"]*)"', content)
            if match:
                text = match.group(1)
                print(f"[Input] Current Text: '{text}'")
                return text
        except Exception as e:
            print(f"[Input] Error extracting text: {e}")
            
        print("[Input] Could not extract text.")
        return ""
