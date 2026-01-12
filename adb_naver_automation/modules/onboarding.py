import time
from ..core.engine import AutomationEngine

class OnboardingModule(AutomationEngine):
    def __init__(self, device_id):
        super().__init__(device_id)

    def analyze_state(self, content):
        """Analyzes the current UI state specific to Onboarding."""
        # State 1: Onboarding (Start Button)
        if 'text="네이버 시작하기"' in content or 'content-desc="네이버 시작하기"' in content:
            if 'text="시작하기 전에"' not in content and 'resource-id="com.nhn.android.search:id/startNaverBtnLayout"' not in content:
                return "STATE_ONBOARDING"
            
        # State 2: Login Prompt
        if 'text="나중에 할게요"' in content:
            return "STATE_LOGIN_PROMPT"

        # State 2.5: Before Starting
        if 'text="시작하기 전에"' in content:
            return "STATE_BEFORE_STARTING"
            
        # State 2.8: Tutorial Overlay
        if 'resource-id="com.nhn.android.search:id/startNaverBtnLayout"' in content:
            return "STATE_TUTORIAL"

        # State 3: Network Error (Retry Button)
        if 'text="재시도"' in content or 'text="네트워크에 연결할 수 없습니다."' in content:
            return "STATE_NETWORK_ERROR"

        # State 4: Main Screen
        if 'text="홈"' in content and 'resource-id="com.nhn.android.search:id/tabText"' in content:
             return "STATE_MAIN"
        if 'resource-id="com.nhn.android.search:id/search_edit_text"' in content:
             return "STATE_MAIN"
             
        return "UNKNOWN"

    def execute_step(self):
        """Execute single step of onboarding logic."""
        self.dump_ui()
        content = self.get_ui_content()
        state = self.analyze_state(content)
        
        print(f"[Onboarding] Current State: {state}")
        
        if state == "STATE_ONBOARDING":
            print("[Action] Click 'Start'")
            self.tap(540, 2093)
            return True
            
        elif state == "STATE_LOGIN_PROMPT":
            print("[Action] Click 'Later'")
            self.tap(540, 2098)
            return True
            
        elif state == "STATE_BEFORE_STARTING":
            print("[Action] Click 'Start (Before)'")
            self.tap(540, 2081)
            return True

        elif state == "STATE_TUTORIAL":
            print("[Action] Click 'Start (Tutorial)'")
            self.tap(540, 2093)
            return True
        
        elif state == "STATE_NETWORK_ERROR":
            print("[Action] Click 'Retry' (Network Error)")
            self.tap(540, 1500) # Guessing Center
            return True
            
        elif state == "STATE_MAIN":
            print("[Onboarding] Metadata: Main Screen Reached.")
            return False 
            
        return False

    def run(self, max_steps=5):
        """Runs the onboarding loop."""
        print("[Onboarding] Starting Auto-Skip Macro...")
        step = 0
        while step < max_steps:
            step += 1
            print(f"[Onboarding] Step {step}/{max_steps}")
            
            action_taken = self.execute_step()
            
            # Check if done
            content = self.get_ui_content() # Re-read if needed, or rely on execute_step return
            # Better to check state again to start loop fresh
            state = self.analyze_state(content)
            
            if state == "STATE_MAIN":
                 print("[Onboarding] Finished: Main Screen Reached.")
                 return True
                 
            if not action_taken:
                 print("[Onboarding] No action possible. Retrying...")
                 time.sleep(3) # Reduce spam
                 continue
                 
            time.sleep(3) # Wait for transition
            
        print("[Onboarding] Max steps reached.")
        return False
