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
            
        # Indicators: "필터" button, "쿠팡 랭킹순", or Result Recycler View
        is_page = 'text="필터"' in content or \
                  'text="쿠팡 랭킹순"' in content or \
                  'resource-id="com.coupang.mobile:id/result_recycler_view"' in content or \
                  'resource-id="com.coupang.mobile:id/filter_bar_layout"' in content
                  
        if is_page:
            print("[Search] Verified: On Search Results Page.")
        else:
            print("[Search] Warning: Not clearly on Results Page.")
        return is_page

    # swipe is now in AutomationEngine (inherited)

    def find_target_product(self, keyword="식사대용 아이간식", price=None):
        """Finds the product containing the keyword AND price (if provided) and returns its bounds."""
        print(f"[Search] Searching for product: Keyword='{keyword}', Price='{price}'...")
        content = self.dump_ui_xml()
        
        # Regex to find all node opening tags
        # We need to parse more robustly for Price association.
        # Simple heuristic: Find Title Node, then check if Price Node is nearby.
        
        # 1. Parse all text nodes with bounds
        text_nodes = []
        node_pattern = re.compile(r'<node [^>]*text="([^"]*)"[^>]*bounds="\[(\d+),(\d+)\]\[(\d+),(\d+)\]"[^>]*>')
        
        for match in node_pattern.finditer(content):
            text_val, x1, y1, x2, y2 = match.groups()
            text_val = text_val.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            
            # Filter non-visible
            if x2-x1 <= 0 or y2-y1 <= 0: continue
            
            text_nodes.append({
                'text': text_val,
                'bounds': (x1, y1, x2, y2),
                'center_y': (y1 + y2) // 2
            })
            
        # 2. Find Candidates matches matching Keyword
        candidates = [n for n in text_nodes if keyword in n['text']]
        
        if not candidates:
            print(f"[Search] No visible titles match '{keyword}'.")
            return None
            
        # 3. If Price is required, filter/verify
        if price:
            print(f"[Search] Verifying Price '{price}' for {len(candidates)} candidates...")
            verified_candidates = []
            
            for cand in candidates:
                # Look for price text in nodes that are "close" to this title
                # Usually Price is BELOW the Title.
                # Threshold: Y distance 0 to +400px.
                c_y = cand['center_y']
                
                # Check all other nodes
                price_match = False
                for node in text_nodes:
                    # Check text match
                    if price not in node['text']: continue
                    
                    # Check spatial relation
                    n_y = node['center_y']
                    y_diff = n_y - c_y
                    
                    # Price should be below title (0 < diff < 500)
                    # And horizontally aligned? (roughly)
                    if 0 <= y_diff <= 500:
                        print(f"[Search] Found Price Match '{node['text']}' near Title.")
                        price_match = True
                        break
                
                if price_match:
                    verified_candidates.append(cand)
                    
            if not verified_candidates:
                print(f"[Search] found titles but NONE matched Price '{price}'.")
                return None
                
            candidates = verified_candidates
            
        # 4. Return top-most candidate
        candidates.sort(key=lambda n: n['bounds'][1])
        best = candidates[0]['bounds']
        print(f"[Search] Match Found! Bounds: {best}")
        return best

    def is_product_page(self, content=None):
        """Checks if the current screen is a Product Detail Page (PDP) OR Login Page (Success)."""
        if content is None:
            content = self.dump_ui_xml()
            
        # Indicators for PDP: "구매하기", "장바구니", "선물하기", "톡톡"
        is_pdp = 'text="구매하기"' in content or \
                 'text="장바구니"' in content or \
                 'text="선물하기"' in content or \
                 'text="톡톡"' in content
                 
        if is_pdp:
            print("[Product] Verified: On Product Detail Page.")
            return True

        # [User Request] Login Page is also valid end state
        # Indicators: "로그인", "login.coupang.com"
        is_login = 'text="로그인"' in content or \
                   'text="이메일 로그인"' in content or \
                   'login.coupang.com' in content
                   
        if is_login:
            print("[Product] Verified: On Login Page (Target Reached).")
            return True
            
        print("[Product] Warning: Not clearly on Product or Login Page.")
        return False

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

    def scan_for_product(self, keyword_group, price=None, max_scrolls=10):
        """
        Scrolls down from the top until the product matching keyword_group AND price is found.
        """
        
        # 1. Initial Check: Is it already on screen?
        print(f"[Search] Checking initial visibility for '{keyword_group}' (Price: {price})...")
        bounds = self.find_target_product(keyword_group, price)
        
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
                bounds = self.find_target_product(keyword_group, price)
                if bounds:
                    print(f"[Search] Alignment Complete. New Bounds: {bounds}")
                    return bounds
                else:
                    print("[Search] Warning: Target lost after alignment. Falling back to full scan.")
            else:
                print("[Search] Target already centered. Clicking.")
                return bounds

        # 2. If NOT found (or lost), Start Full Scan
        print(f"[Search] Product not currently visible. Starting Scan Downwards (Max scrolls: {max_scrolls})...")
        for i in range(max_scrolls):
            # A. Check current view
            bounds = self.find_target_product(keyword_group, price)
            if bounds:
                 x1, y1, x2, y2 = bounds
                 center_y = (y1 + y2) // 2
                 diff = center_y - 1100
                 
                 if abs(diff) > 300: 
                     if diff > 0: self.scroll_down(distance=diff, duration=600)
                     else: self.scroll_up(distance=abs(diff), duration=600)
                     time.sleep(1.0)
                     bounds = self.find_target_product(keyword_group, price) 
                 
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
