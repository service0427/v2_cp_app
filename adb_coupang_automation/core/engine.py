import subprocess
import os
import time
import random

class AutomationEngine:
    def __init__(self, device_id):
        self.device_id = device_id
        self.dump_path = "/sdcard/window_dump.xml"
        self.local_dump_path = "current_ui.xml"

    def swipe(self, x1, y1, x2, y2, duration=300):
        """Executes a swipe gesture."""
        cmd = ["shell", "input", "swipe", str(x1), str(y1), str(x2), str(y2), str(duration)]
        self.run_adb(cmd, check=False)

    def scroll_down(self, distance=400, duration=400):
        """Scrolls DOWN by swiping UP with randomized coordinates."""
        # Randomize Start X (Center +/- 100) -> 440~640
        start_x = random.randint(440, 640)
        # Randomize End X (Simulation of slight curve/diagonal) -> Start X +/- 20
        end_x = start_x + random.randint(-20, 20)
        
        # Randomize Start Y (Lower part +/- 50) -> 1550~1650
        start_y = random.randint(1550, 1650)
        end_y = start_y - distance
        
        # Ensure end_y is within bounds (e.g., > 0)
        if end_y < 0: end_y = 0
            
        self.swipe(start_x, start_y, end_x, end_y, duration)

    def scroll_up(self, distance=400, duration=400):
        """Scrolls UP by swiping DOWN with randomized coordinates."""
        # Randomize Start X (Center +/- 100) -> 440~640
        start_x = random.randint(440, 640)
        # Randomize End X (Simulation of slight curve/diagonal) -> Start X +/- 20
        end_x = start_x + random.randint(-20, 20)
        
        # Randomize Start Y (Upper part +/- 50) -> 350~450
        start_y = random.randint(350, 450)
        end_y = start_y + distance
        
        # Ensure end_y is within bounds (e.g., < 2300)
        if end_y > 2300: end_y = 2300

        self.swipe(start_x, start_y, end_x, end_y, duration)

    def perform_browsing_scroll(self, scroll_down_count=3, scroll_up_count=5):
        """
        Executes a browsing pattern: Scroll DOWN N times, then Scroll UP M times.
        Used to simulate reading content and then returning to the top.
        Includes randomization for human-like behavior.
        """
        print(f"[Engine] Starting Browsing Scroll Sequence (Down: {scroll_down_count}, Up: {scroll_up_count})...")

        # 1. Scroll Down Sequence
        for i in range(scroll_down_count):
            print(f"[Engine] Scroll DOWN {i+1}/{scroll_down_count}")
            # Randomize distance (approx one page: 1000~1500) and duration
            dist = random.randint(1000, 1500)
            dur = random.randint(400, 700)
            self.scroll_down(distance=dist, duration=dur)
            time.sleep(random.uniform(0.8, 1.5))

        time.sleep(random.uniform(1.0, 2.0))

        # 2. Scroll Up Sequence
        for i in range(scroll_up_count):
            print(f"[Engine] Scroll UP {i+1}/{scroll_up_count}")
            # Randomize distance (slightly larger to ensure return to top) and duration
            dist = random.randint(1200, 1600)
            dur = random.randint(400, 800)
            self.scroll_up(distance=dist, duration=dur)
            time.sleep(random.uniform(0.8, 1.5))


    def run_adb(self, args, check=True):
        cmd = ["adb", "-s", self.device_id] + args
        result = subprocess.run(cmd, capture_output=True, text=True)
        if check and result.returncode != 0:
            print(f"[Automator] ADB Error: {result.stderr.strip()}")
        return result

    def tap(self, x, y):
        print(f"[Automator] Tapping ({x}, {y})")
        self.run_adb(["shell", "input", "tap", str(x), str(y)], check=False)

    def dump_ui(self):
        """Dumps UI hierarchy to local file."""
        self.run_adb(["shell", "uiautomator", "dump", self.dump_path], check=False)
        self.run_adb(["pull", self.dump_path, self.local_dump_path], check=False)
        
    def get_ui_content(self):
        """Reads local dump file."""
        if not os.path.exists(self.local_dump_path):
            return ""
        try:
            with open(self.local_dump_path, "r", encoding="utf-8") as f:
                return f.read()
        except:
            return ""
            
    def tap_element(self, identifier, fallback_x=None, fallback_y=None):
        """Finds an element by identifier (text, resource-id) and taps its center."""
        
        self.dump_ui()
        content = self.get_ui_content()
        
        if identifier in content:
            try:
                # Find bounds="..." near the identifier
                # Simplistic parsing: split by identifier, look ahead for bounds
                import re
                
                # Regex to find bounds="[0,0][100,100]" assoc with the identifier line likely
                # Ideally we parse XML, but for quick fix: grep line containing identifier
                
                # Find the 'node' tag containing the identifier
                # <node ... text="identifier" ... bounds="[x1,y1][x2,y2]" ... />
                pattern = f'{identifier}.*?bounds="\\[(\\d+),(\\d+)\\]\\[(\\d+),(\\d+)\\]"'
                match = re.search(pattern, content)
                
                if not match:
                     # Try searching backwards if attributes are ordered differently
                     # e.g. bounds is before identifier? Less likely in standard output but possible.
                     # Or just find the bounds in the same chunk.
                     pass

                if match:
                    x1, y1, x2, y2 = map(int, match.groups())
                    center_x = (x1 + x2) // 2
                    center_y = (y1 + y2) // 2
                    print(f"[Automator] Found {identifier} at ({center_x}, {center_y}). Tapping...")
                    self.tap(center_x, center_y)
                    return True
                else:
                    # Fallback regex for "bounds" appearing ANYWHERE in the node string
                    # Split content by "node" tags? Too complex.
                    # Let's rely on fallback if regex fails for now or just generic tap
                    print(f"[Automator] Element {identifier} found but bounds could not be parsed.")
            except Exception as e:
                print(f"[Automator] Error parsing bounds for {identifier}: {e}")

        # Fallback
        if fallback_x and fallback_y:
            print(f"[Automator] Element {identifier} NOT found. Using fallback ({fallback_x}, {fallback_y}).")
            self.tap(fallback_x, fallback_y)
            return True
            
        return False
