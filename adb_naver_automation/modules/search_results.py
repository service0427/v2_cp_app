from adb_naver_automation.core.engine import AutomationEngine
import time
import random
import re

class SearchResultsModule(AutomationEngine):
    def __init__(self, device_id):
        super().__init__(device_id)

    def is_results_page(self, content=None):
        """Checks if the current screen is the Search Results Page (SERP)."""
        if content is None:
            content = self.dump_ui_xml() # Helper to get content
            
        # Indicators: "빠른배송", "랭킹순", "가격비교" buttons
        # ID: filter_fast_delivery, filter_n_delivery
        is_page = 'resource-id="filter_fast_delivery"' in content or \
                  'text="빠른배송"' in content or \
                  'text="랭킹순"' in content
                  
        if is_page:
            print("[Search] Verified: On Search Results Page.")
        else:
            print("[Search] Warning: Not clearly on Results Page.")
        return is_page

    # swipe is now in AutomationEngine (inherited)

    def find_target_product(self, keyword="식사대용 아이간식"):
        """Finds the product containing the keyword and returns its bounds."""
        print(f"[Search] Searching for product with keyword: '{keyword}'...")
        content = self.dump_ui_xml()
        
        # Regex to find all node opening tags
        node_pattern = re.compile(r'<node [^>]*>')
        
        matches = []
        for match in node_pattern.finditer(content):
            node_tag = match.group()
            
            # Extract Text
            text_match = re.search(r'text="([^"]*)"', node_tag)
            text_val = text_match.group(1) if text_match else ""
            
            if not text_val:
                continue

            # CLEANING: Undo XML escaping and remove HTML tags
            # 1. Unescape: &lt;mark&gt; -> <mark>
            # 2. Remove tags: <mark>, </mark>
            # Simple approach: Replace common tags or just remove all <...>
            
            # Unescape simple entities manually or via logic if needed, 
            # but usually text in XML attr is just standard XML escaped.
            # &lt; -> <, &gt; -> >, &amp; -> &
            
            clean_text = text_val.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
            clean_text = re.sub(r'<[^>]+>', '', clean_text) # Remove HTML tags
            
            # Normalize whitespace
            clean_text = " ".join(clean_text.split())

            # Debug: Print candidates that partially match
            # if "달빛" in clean_text:
            #    print(f"[DEBUG] Candidate: '{clean_text}'")

            # EXACT SUBSTRING MATCH (Ctrl+F behavior)
            if keyword in clean_text:
                # Extract Bounds
                bounds_match = re.search(r'bounds="\[(\d+),(\d+)\]\[(\d+),(\d+)\]"', node_tag)
                if not bounds_match:
                    continue
                    
                x1, y1, x2, y2 = map(int, bounds_match.groups())
                
                # Validation
                if (y2 - y1) <= 0 or (x2 - x1) <= 0:
                    continue
                if y1 > 2000: 
                    continue
                    
                matches.append((x1, y1, x2, y2))
            
        if matches:
            # Sort by Y (Topmost visible first)
            matches.sort(key=lambda b: b[1])
            best_bounds = matches[0]
            print(f"[Search] Found matches: {len(matches)}. Best: {best_bounds}")
            return best_bounds
            
        print(f"[Search] Target '{keyword}' NOT found (Checked {len(content)} chars).")
        return None

    def is_product_page(self, content=None):
        """Checks if the current screen is a Product Detail Page (PDP)."""
        if content is None:
            content = self.dump_ui_xml()
            
        # Indicators: "구매하기", "장바구니", "선물하기"
        is_page = 'text="구매하기"' in content or \
                  'text="장바구니"' in content or \
                  'text="선물하기"' in content or \
                  'text="톡톡"' in content
                  
        if is_page:
            print("[Product] Verified: On Product Detail Page.")
        else:
            print("[Product] Warning: Not clearly on Product Page.")
        return is_page

    def perform_browsing_action(self):
        """Simulates human-like browsing on SERP (Scroll down, then back up)."""
        print("[Search] Simulating User Browsing (Shared Logic)...")
        # Reuse common logic: 3 Down, 4 Up (Search Context)
        self.perform_browsing_scroll(scroll_down_count=3, scroll_up_count=4)

    def reset_view_to_top(self, swipes=4):
        """Scrolls up aggressively to ensure we start from the top."""
        print("[Search] Resetting view to TOP before scanning...")
        for _ in range(swipes):
            self.scroll_up(distance=1500, duration=300) # Fast, long upward swipes
            time.sleep(0.5)
        time.sleep(1.0) # Settle

    def scan_for_product(self, keyword_group, max_scrolls=10):
        """
        Scrolls down from the top until the product matching keyword_group is found.
        Strategy:
        1. Check current view (lucky hit?).
        2. If not found, RESET to TOP.
        3. Scroll down with VARIABLE page units (avoid constant intervals).
        """
        
        # 1. Initial Check: Is it already on screen?
        print(f"[Search] Checking initial visibility for '{keyword_group}'...")
        bounds = self.find_target_product(keyword_group)
        
        if bounds:
            # [Precision Alignment]
            x1, y1, x2, y2 = bounds
            center_y = (y1 + y2) // 2
            screen_center_y = 1100 
            
            diff = center_y - screen_center_y
            print(f"[Search] Found at Y={center_y}. Distance from center: {diff}")
            
            if abs(diff) > 200:
                if diff > 0:
                    print(f"[Search] Target is low. precise SCROLL DOWN by {diff}px.")
                    self.scroll_down(distance=diff, duration=800)
                else:
                    print(f"[Search] Target is high. precise SCROLL UP by {abs(diff)}px.")
                    self.scroll_up(distance=abs(diff), duration=800)
                
                time.sleep(1.5)
                bounds = self.find_target_product(keyword_group)
                if bounds:
                    print(f"[Search] Alignment Complete. New Bounds: {bounds}")
                    return bounds
                else:
                    print("[Search] Warning: Target lost after alignment. Falling back to full scan.")
            else:
                print("[Search] Target already centered. Clicking.")
                return bounds

        # 2. If NOT found (or lost), Start Full Scan
        # [User Request] Removed mandatory Reset-to-Top since browsing action usually handles it.
        # print("[Search] Target NOT visible. Resetting to TOP and starting Full Scan...")
        # self.reset_view_to_top()
        
        print(f"[Search] Product not currently visible. Starting Scan Downwards (Max scrolls: {max_scrolls})...")
        for i in range(max_scrolls):
            # A. Check current view
            bounds = self.find_target_product(keyword_group)
            if bounds:
                 x1, y1, x2, y2 = bounds
                 center_y = (y1 + y2) // 2
                 diff = center_y - 1100
                 
                 if abs(diff) > 300: 
                     if diff > 0: self.scroll_down(distance=diff, duration=600)
                     else: self.scroll_up(distance=abs(diff), duration=600)
                     time.sleep(1.0)
                     bounds = self.find_target_product(keyword_group) 
                 
                 return bounds

            # B. Scroll Down (Variable/Human-like)
            print(f"[Search] Not in view. Scrolling down ({i+1}/{max_scrolls})...")
            
            view_height = 2200
            body_match = re.search(r'resource-id="com\.nhn\.android\.search:id/bodyView"[^>]*bounds="\[\d+,\d+\]\[\d+,(\d+)\]"', self.dump_ui_xml())
            if body_match: view_height = int(body_match.group(1))
            else:
                content_match = re.search(r'resource-id="android:id/content"[^>]*bounds="\[\d+,\d+\]\[\d+,(\d+)\]"', self.dump_ui_xml())
                if content_match: view_height = int(content_match.group(1))
            
            # [User Request] Variable Intervals (0.6 ~ 0.85)
            # Avoid constant 70% or full 100% scrolls. Mix it up.
            scroll_factor = random.uniform(0.60, 0.85)
            scroll_dist = int(view_height * scroll_factor)
            
            print(f"[Search] Variable Scroll: {scroll_dist}px (Factor: {scroll_factor:.2f})")
            self.scroll_down(distance=scroll_dist, duration=random.randint(600, 900))
            time.sleep(random.uniform(1.2, 2.0)) # Variable pause
            
        print("[Search] Product NOT found after max scrolls.")
        return None

    def scroll_product_page(self):
        """Simulates reading the product page."""
        print("[Product] Simulating Reading (Shared Logic)...")
        # Reuse common logic: 5 Down, 1 Up (Product Context)
        self.perform_browsing_scroll(scroll_down_count=5, scroll_up_count=1)
        print("[Product] Reading complete.")

    def get_random_click_point(self, bounds):
        """Calculates a random click point within bounds with padding."""
        x1, y1, x2, y2 = bounds
        width = x2 - x1
        height = y2 - y1
        
        # Padding: 20% of dimension
        pad_x = int(width * 0.2)
        pad_y = int(height * 0.2)
        
        click_x = random.randint(x1 + pad_x, x2 - pad_x)
        click_y = random.randint(y1 + pad_y, y2 - pad_y)
        
        return (click_x, click_y)

    def dump_ui_xml(self):
        """Helper to dump and read UI."""
        # Using AutomationEngine's subprocess or logic
        # Assuming run_adb is available
        self.run_adb(["shell", "uiautomator", "dump", "/sdcard/window_dump.xml"])
        self.run_adb(["pull", "/sdcard/window_dump.xml", "window_dump.xml"], check=False)
        try:
            with open("window_dump.xml", "r", encoding="utf-8") as f:
                content = f.read()
            
            # [User Request] Save raw XML for analysis
            with open("last_ui_dump.xml", "w", encoding="utf-8") as debug_f:
                debug_f.write(content)
                
            return content
        except:
            return ""
