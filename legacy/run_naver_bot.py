import argparse
import time
import random
import builtins
from datetime import datetime

# [Global Logging Override]
# User Request: Fixed 3-digit microsecond timestamp for ALL logs.
original_print = builtins.print

def timestamped_print(*args, **kwargs):
    now = datetime.now()
    # Format: [HH:MM:SS.mmm]
    # microseconds is 6 digits (e.g., 123456). We slice first 3.
    timestamp = f"[{now.strftime('%H:%M:%S')}.{str(now.microsecond // 1000).zfill(3)}]"
    original_print(timestamp, *args, **kwargs)

builtins.print = timestamped_print

from adb_naver_automation.core.lifecycle import AppLifecycle
from adb_naver_automation.core.identity import IdentityManager
from adb_naver_automation.modules.onboarding import OnboardingModule
from adb_naver_automation.modules.interaction import InteractionModule
from adb_naver_automation.modules.search_input import SearchInputModule
from adb_naver_automation.modules.keyboard import KeyboardModule
from adb_naver_automation.modules.search_results import SearchResultsModule

# Configuration
DEVICE_ID = "RF9XC00EXGM"

# 1. Search Keywords (Random Selection)
SEARCH_KEYWORDS = [
    "아이간식 달빛기정떡",
    "개별포장 달빛기정떡"
]

# 2. Target Product Keyword (Common Identification)
# Text observed: '달빛 국산쌀 기정 잔기지 술떡 개별포장 식사대용 아이간식'
TARGET_PRODUCT_KEYWORD = "달빛 국산쌀 기정 잔기지 술떡"

def main():
    parser = argparse.ArgumentParser(description="Naver App Automation Bot")
    parser.add_argument("--steps", "-l", type=int, default=1, help="Number of loops to run")
    parser.add_argument("--toggle-ip", "-t", action="store_true", help="Toggle IP before each run")
    args = parser.parse_args()

    print("==========================================")
    print(f"  Naver App Automation Bot")
    print(f"  Target: {DEVICE_ID}")
    print("==========================================")

    # Initialize Modules
    lifecycle = AppLifecycle(DEVICE_ID)
    identity = IdentityManager(DEVICE_ID)
    onboarding = OnboardingModule(DEVICE_ID)
    interaction = InteractionModule(DEVICE_ID)
    search_input = SearchInputModule(DEVICE_ID)
    keyboard = KeyboardModule(DEVICE_ID)
    search_results = SearchResultsModule(DEVICE_ID)

    # Initial Cleanup
    lifecycle.ensure_network_environment()

    for cycle in range(args.steps):
         print(f"--- Cycle {cycle+1}/{args.steps} ---")

         # [Phase Pre-0]: Force Stop App (Cleanup previous cycle)
         lifecycle.force_stop()

         # Phase 0: IP Toggle (Optional)
         if args.toggle_ip:
             print("\n[Phase 0] Network Toggle...")
             success = lifecycle.toggle_ip(subnet=20)
             if not success:
                 print("[Warning] IP Toggle failed. Using current IP.")
             
             # Proceed immediately without check
             print("[Info] IP Toggle Complete (or skipped). Proceeding...")

         # Phase 1: Identity Rotation
         print("\n[Phase 1] Identity Rotation...")
         identity.rotate_identity()

         # Phase 2: App Launch
         print("\n[Phase 2] App Launch...")
         
         # Ensure unlocked (Important after reboot)
         interaction.wake_and_unlock()
         
         lifecycle.perform_cold_start()

         # Phase 3: Onboarding
         print("\n[Phase 3] Onboarding Automation...")
         if not onboarding.run(): # run() returns True if Main Screen reached
             print("[Error] Failed to complete onboarding. Skipping cycle.")
             continue

         # Phase 4: Scroll & Click Search
         print("\n[Phase 4] Interaction (Scroll & Click)...")
         interaction.wake_and_unlock() # Ensure screen on
         
         # Scroll Loop
         interaction.run_scroll_and_click() # This handles verify internally? Yes interaction.py logic

         # Phase 5: Search Input
         print("\n[Phase 5] Search Input...")
         
         # 1. Verify Search Page
         if interaction.verify_search_page():
              print("[Search] Search Page Verified.")
              
              # 2. Reset (Tap X)
              interaction.tap_element("search_window_editor_empty_button", fallback_x=849, fallback_y=198)
              time.sleep(1) # Wait for clear
              
              # Check if "Input Field" is ready?
              # We just tap coordinates for keyboard
              
              # 3. Type (with High-Level Logic)
              typing_keyword = random.choice(SEARCH_KEYWORDS)
              finding_keyword = TARGET_PRODUCT_KEYWORD
              
              print(f"[Action] Selected Keyword: '{typing_keyword}' -> Target: '{finding_keyword}'")
              
              # Define Callbacks
              def verify_input(text):
                  return search_input.verify_input_content(text)
                  
              def clear_input():
                  search_input.clear_search_input()
                  # Ensure empty state via X button just in case
                  interaction.tap_element("search_window_editor_empty_button", fallback_x=849, fallback_y=198)
                  time.sleep(0.5)

              # Execute Typing
              entered_search = keyboard.perform_hangul_typing(
                  text=typing_keyword,
                  validator_func=verify_input,
                  clear_func=clear_input,
                  max_attempts=2
              )

              if entered_search:
                  print("[Action] Input Verified. Pressing Enter...")
                  keyboard.press_enter()
                  print("[Success] Search Executed!")
              
              if entered_search:
                  # Phase 6: Result Selection & Verification
                  time.sleep(5)
                  print("\n==================================")
                  print(" Phase 6: Result Selection")
                  print("==================================")
                  
                  # Verify SERP with Timeout (30s)
                  serp_verified = False
                  start_serp_check = time.time()
                  print("[Search] Verifying Results Page (Max 30s)...")
                  
                  while time.time() - start_serp_check < 30:
                      if search_results.is_results_page():
                          serp_verified = True
                          break
                      time.sleep(2)
                  
                  if serp_verified:
                      print('[Action] Randomized Browsing on SERP...')
                      search_results.perform_browsing_action()
                      
                      print(f'[Action] Finding Target Product: {finding_keyword}...')
                      # Uses scan_for_product for scroll-and-search
                      target_bounds = search_results.scan_for_product(finding_keyword, max_scrolls=10)
                      
                      if target_bounds:
                          click_x, click_y = search_results.get_random_click_point(target_bounds)
                          print(f'[Action] Clicking Target at ({click_x}, {click_y})...')
                          search_results.tap(click_x, click_y)
                          time.sleep(5) # Wait for PDP
                          
                          if search_results.is_product_page():
                              print('[Success] Successfully entered Product Page!')
                              search_results.scroll_product_page()
                              print('[Success] Product Interaction Complete.')
                          else:
                              print('[Failure] Did not detect Product Page.')
                      else:
                          print('[Failure] Target product not found on SERP.')
                  else:
                      print('[Failure] Not on Results Page after search.')
              else:
                   print("[Failure] Could not proceed to search.")

         else:
              print("[Failure] Search Page NOT Detected.")
         
         print(f"\n[Cycle {cycle+1}] Complete.")
         time.sleep(5)

    print("\n[Bot] Execution Complete.")

if __name__ == "__main__":
    main()
