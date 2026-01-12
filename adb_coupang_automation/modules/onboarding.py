import time
from ..core.engine import AutomationEngine

class OnboardingModule(AutomationEngine):
    def __init__(self, device_id):
        super().__init__(device_id)

    def check_focus(self):
        """Checks the current focused activity via ADB."""
        res = self.run_adb(["shell", "dumpsys", "window", "|", "grep", "-E", "'mCurrentFocus|mFocusedApp'"], check=False)
        output = res.stdout
        if "com.coupang.mobile" in output and "MainActivity" in output:
             return True
        return False

    def analyze_state(self, content):
        """Analyzes the current UI state specific to Coupang Onboarding."""
        # State Priority 0: Check System Focus (The Ultimate Truth)
        # If MainActivity is focused, we are done, regardless of what XML says (zombie overlays).
        if self.check_focus():
             print("[Onboarding] Focus Check: MainActivity is FOCUSED. Override to STATE_MAIN.")
             return "STATE_MAIN"

        # State 0: Chrome Overlay (Force Stop Priority)
        if 'package="com.android.chrome"' in content:
             return "STATE_LOGIN_WEBVIEW"
             
        # State 1: Permission Guide Overlay
        if 'resource-id="com.coupang.mobile:id/confirm_button"' in content:
            return "STATE_PERMISSION_GUIDE"
            
        if 'text="쿠팡 앱 이용을 위한 권한 안내"' in content:
            return "STATE_PERMISSION_GUIDE"

        # State 1.5: Login Prompt (Auto-Dismiss)
        if 'text="로그인"' in content and ('text="회원가입"' in content or 'text="아이디"' in content):
             return "STATE_LOGIN_PROMPT"

        # State 1.8: WebView Login (login.coupang.com)
        if 'text="login.coupang.com"' in content:
             return "STATE_LOGIN_WEBVIEW"
        if 'text="휴대폰번호 로그인"' in content:
             return "STATE_LOGIN_WEBVIEW"
        if 'resource-id="com.android.chrome:id/close_button"' in content:
             return "STATE_LOGIN_WEBVIEW"

        # State 2: Main Screen (Coupang Home)
        # Check for bottom tab bar items or search bar or logo
        if 'resource-id="com.coupang.mobile:id/coupang_logo"' in content:
             return "STATE_MAIN"
        if 'text="쿠팡에서 검색하세요!"' in content:
             return "STATE_MAIN"
        if 'resource-id="com.coupang.mobile:id/tab_menu"' in content:
             return "STATE_MAIN"
             
        if 'text="검색"' in content and 'resource-id="com.coupang.mobile:id/icon"' in content:
             return "STATE_MAIN"
        if 'text="쿠팡홈"' in content: # Default tab name often
             return "STATE_MAIN"
        if 'text="카테고리"' in content:
             return "STATE_MAIN"
        if 'text="마이쿠팡"' in content:
             return "STATE_MAIN"
        if 'resource-id="com.coupang.mobile:id/toolbar_search_text_view"' in content:
             return "STATE_MAIN"
             
        return "UNKNOWN"

    def execute_step(self):
        """Execute single step of onboarding logic."""
        self.dump_ui()
        content = self.get_ui_content()
        # [DEBUG] Print content to debug UNKNOWN state
        print(f"[DEBUG] UI Content (First 500): {content[:500]}")
        state = self.analyze_state(content)
        
        print(f"[Onboarding] Current State: {state}")
        
        if state == "STATE_PERMISSION_GUIDE":
            print("[Action] Click 'Confirm' (Permission Guide)")
            # Use confirmed Resource ID
            self.tap_element(identifier='resource-id="com.coupang.mobile:id/confirm_button"')
            return True
            
        elif state == "STATE_LOGIN_PROMPT":
            print("[Action] Dismissing Login Prompt")
            # Try specific close buttons
            if self.tap_element(identifier='resource-id="com.coupang.mobile:id/close"'): return "DISMISSED"
            if self.tap_element(identifier='resource-id="com.coupang.mobile:id/close_button"'): return "DISMISSED"
            if self.tap_element(identifier='text="닫기"'): return "DISMISSED"
            if self.tap_element(identifier='text="다음에 하기"'): return "DISMISSED"
            
            # Fallback: Tap top-right corner (common for X button)
            print("[Action] Fallback: Tapping Top-Right for Close")
            self.tap(980, 150)
            return "DISMISSED" # User Request: Assume done after one dismiss

        elif state == "STATE_LOGIN_WEBVIEW":
            print("[Action] WebView Login Detected.")
            # Priority 1: Tap Close Button (X)
            if self.tap_element(identifier='resource-id="com.android.chrome:id/close_button"'):
                 print("[Action] Tapped Chrome Close Button.")
                 # Check if it persists? We loop anyway.
            else:
                 print("[Action] Close Button not found. Trying Back.")
                 self.run_adb(["shell", "input", "keyevent", "4"], check=False)
                 
            # Priority 2: Force Stop Chrome (Aggressive) (To prevent loop)
            # We blindly force stop Chrome to kill the overlay
            print("[Action] Force Stopping Chrome to kill WebView overlay...")
            self.run_adb(["shell", "am", "force-stop", "com.android.chrome"], check=False)
            time.sleep(1)
            return "DISMISSED" # User Request: Assume done after one dismiss
            
        elif state == "STATE_MAIN":
            print("[Onboarding] Metadata: Main Screen Reached.")
            return False 
            
        return False

    def run(self, max_steps=15):
        """Runs the onboarding loop."""
        print("[Onboarding] Starting Auto-Skip Macro...")
        step = 0
        while step < max_steps:
             step += 1
             print(f"[Onboarding] Step {step}/{max_steps}")
            
             result = self.execute_step()
             
             # User Request: If Login/WebView was dismissed, Assume Success and Break Immediately
             if result == "DISMISSED":
                 print(f"[Onboarding] Login/WebView Dismissed. Immediate Exit to Search.")
                 return True

             # Check if done
             self.dump_ui() # CRITICAL: Refresh UI state, otherwise we read stale XML after force-stop
             content = self.get_ui_content() 
             # Better to check state again to start loop fresh
             state = self.analyze_state(content)
             
             if state == "STATE_MAIN":
                  print(f"[Onboarding] Finished: Reached {state}.")
                  return True
                  
             if not result:
                  print("[Onboarding] No action possible. Retrying...")
                  time.sleep(1) # Reduce spam, but keep responsive
                  continue
                  
             time.sleep(1) # Wait for transition (Reduced from 3s)
            
        print("[Onboarding] Max steps reached.")
        return False
