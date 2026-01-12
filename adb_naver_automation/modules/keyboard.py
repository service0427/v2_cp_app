from adb_naver_automation.core.engine import AutomationEngine
from adb_naver_automation.utils.hangul import decompose_text, resolve_shift_key
from adb_naver_automation.modules.interaction import InteractionModule
import time
import random
import re
import subprocess

class KeyboardModule(AutomationEngine):
    def __init__(self, device_id):
        super().__init__(device_id)
        # Coordinate Map for Samsung Keyboard (1080x2340) - CALIBRATED V2
        # Assumed Keyboard Area: Y=1330 to Y=2250
        # Suggestion Bar: ~1350
        # Number Row: ~1450-1500
        # Row 1 (QWERTY/ㅂㅈㄷ): Y ~ 1650 (Safe from numbers)
        # Row 2 (ASDF/ㅁㄴㅇ): Y ~ 1800
        # Row 3 (ZXCV/ㅋㅌㅊ): Y ~ 1950
        # Row 4 (Space): Y ~ 2150
        
        # Key Spacing (Width 1080 / 10 keys = 108px per key)
        self.KEY_MAP = {
            # Row 1 (ㅂㅈㄷㄱㅅㅛㅕㅑㅐㅔ) - Y=1650
            'ㅂ': (59, 1650), 'ㅈ': (165, 1650), 'ㄷ': (273, 1650), 'ㄱ': (381, 1650), 'ㅅ': (489, 1650),
            'ㅛ': (597, 1650), 'ㅕ': (705, 1650), 'ㅑ': (813, 1650), 'ㅐ': (921, 1650), 'ㅔ': (1029, 1650),
            
            # Row 2 (ㅁㄴㅇㄹㅎㅗㅓㅏㅣ) - Y=1800
            'ㅁ': (113, 1800), 'ㄴ': (221, 1800), 'ㅇ': (329, 1800), 'ㄹ': (437, 1800), 'ㅎ': (545, 1800),
            'ㅗ': (653, 1800), 'ㅓ': (761, 1800), 'ㅏ': (869, 1800), 'ㅣ': (977, 1800),
            
            # Row 3 (Shift ㅋ ㅌ ㅊ ㅍ ㅠ ㅜ ㅡ Backspace) - Y=1950
            'SHIFT': (120, 1950), # Left Shift
            'ㅋ': (250, 1950), 'ㅌ': (358, 1950), 'ㅊ': (466, 1950), 'ㅍ': (574, 1950),
            'ㅠ': (682, 1950), 'ㅜ': (790, 1950), 'ㅡ': (898, 1950),
            'BACKSPACE': (1000, 1950),
            
            # Row 4 - Y=2150
            'SPACE': (540, 2150),
            'ENTER': (950, 2150),
            
            # English Map (partial/overlay)
            'q': (59, 1650), 'w': (165, 1650), 'e': (273, 1650), 'r': (381, 1650), 't': (489, 1650),
            'y': (597, 1650), 'u': (705, 1650), 'i': (813, 1650), 'o': (921, 1650), 'p': (1029, 1650)
        }
        # Hangul to English QWERTY Mapping (2-Set 2beolsik)
        self.HANGUL_TO_ENGLISH_MAP = {
            'ㅂ': 'q', 'ㅃ': 'Q', 'ㅈ': 'w', 'ㅉ': 'W', 'ㄷ': 'e', 'ㄸ': 'E', 'ㄱ': 'r', 'ㄲ': 'R', 'ㅅ': 't', 'ㅆ': 'T',
            'ㅛ': 'y', 'ㅕ': 'u', 'ㅑ': 'i', 'ㅐ': 'o', 'ㅒ': 'O', 'ㅔ': 'p', 'ㅖ': 'P',
            'ㅁ': 'a', 'ㄴ': 's', 'ㅇ': 'd', 'ㄹ': 'f', 'ㅎ': 'g', 'ㅗ': 'h', 'ㅓ': 'j', 'ㅏ': 'k', 'ㅣ': 'l',
            'ㅋ': 'z', 'ㅌ': 'x', 'ㅊ': 'c', 'ㅍ': 'v', 'ㅠ': 'b', 'ㅜ': 'n', 'ㅡ': 'm',
            ' ': ' ' # Space maps to space
        }

    def tap_key(self, key_char):
        if key_char in self.KEY_MAP:
            x, y = self.KEY_MAP[key_char]
            # Add slight randomization (Human error)
            x += random.randint(-5, 5) # V2 calibration is precise, don't deviate too much
            y += random.randint(-5, 5)
            
            print(f"[Keyboard] Tapping '{key_char}' at ({x}, {y})")
            self.tap(x, y)
            
            # Random typing delay (Human-like variance)
            # Fast typists: 50ms-150ms
            time.sleep(random.uniform(0.05, 0.15)) 
        else:
            print(f"[Keyboard] Error: Key '{key_char}' not found in map.")

    def tap_lang_switch(self):
        """Taps the Language Switch key (Hangul/English)."""
        # Coordinate from user feedback (x=230, Y=2150 is Row 4)
        print("[Keyboard] Tapping Language Switch Key...")
        self.tap(230, 2150)
        time.sleep(1)

    def type_hangul_text(self, text):
        print(f"[Keyboard] Typing Hangul: {text}")
        
        # 1. Decompose
        jamo_list = decompose_text(text)
        print(f"[Keyboard] Jamo Sequence: {jamo_list}")

        # 2. Type Loop
        for j in jamo_list:
            if j == ' ':
                self.tap_key('SPACE')
                continue
                
            # Shift Logic
            base_char, needs_shift = resolve_shift_key(j)
            
            if needs_shift:
                print(f"[Keyboard] Double Consonant '{j}' detected. Pressing Shift.")
                self.tap_key('SHIFT')
                time.sleep(0.1)
                self.tap_key(base_char)
            else:
                self.tap_key(base_char)

    def press_enter(self):
        self.tap_key('ENTER')

    def is_english_typo(self, target_hangul, actual_text):
        """
        Detects if the actual text is the English QWERTY equivalent of the target Hangul.
        Example: target='아이' -> mapped='dkdl'. If actual='dkdl...', returns True.
        """
        mapped_english = ""
        try:
            # We need simple decomposition.
            jamo_list = decompose_text(target_hangul)
            for char in jamo_list:
                if char in self.HANGUL_TO_ENGLISH_MAP:
                    mapped_english += self.HANGUL_TO_ENGLISH_MAP[char]
                else:
                    mapped_english += char 
        except Exception as e:
            print(f"[Keyboard] Error mapping hangul: {e}")
            return False
            
        print(f"[Keyboard] Checking English Typo: Target='{target_hangul}' -> Mapped='{mapped_english}' vs Actual='{actual_text}'")
        
        if not actual_text:
            return False
            
        # Check if actual text starts with the beginning of mapped English text
        # (Handling partial typing due to autocomplete or truncation)
        check_len = min(len(actual_text), len(mapped_english))
        if check_len < 2: return False # Too short to judge

        if actual_text[:check_len] == mapped_english[:check_len]:
            return True
            
        return False

    def get_current_language_mode(self):
        """
        Determines current keyboard language using Android Secure Settings.
        Returns: 'HANGUL', 'ENGLISH', or 'UNKNOWN'
        """
        try:
            cmd = "settings get secure selected_input_method_subtype"
            result = subprocess.run(
                ["adb", "-s", self.device_id, "shell", cmd],
                capture_output=True, text=True
            ).stdout.strip()
            
            print(f"[Keyboard] System Subtype Hash: {result}")
            
            if result == "4521984":
                return "HANGUL"
            elif result in ["65537", "65538", "65555"]: # en_US, en_GB, en_IN
                return "ENGLISH"
            return "UNKNOWN"
        except Exception as e:
            print(f"[Keyboard] Error checking system language: {e}")
            return "UNKNOWN"

    def ensure_hangul_mode(self):
        """Checks system language and switches to Hangul if currently English."""
        current_lang = self.get_current_language_mode()
        print(f"[Input] Current Keyboard Mode: {current_lang}")
        
        if current_lang == 'ENGLISH':
            print("[Input] English Mode Detected. Switching to Hangul...")
            self.tap_lang_switch()
            time.sleep(1)
            return True
        return False

    def perform_hangul_typing(self, text, validator_func=None, clear_func=None, max_attempts=2):
        """
        High-level method to type Hangul text with verification and retry logic.
        
        Args:
            text (str): The Hangul text to type.
            validator_func (callable): Function that returns True if input is correct.
            clear_func (callable): Function to clear the input field before retrying.
            max_attempts (int): Number of retry attempts.
            
        Returns:
            bool: True if typing and verification succeeded, False otherwise.
        """
        for attempt in range(max_attempts):
            print(f"[Keyboard] Typing Attempt {attempt+1}/{max_attempts}")
            
            # 1. Ensure Language
            self.ensure_hangul_mode()
            
            # 2. Clear Field (if provided)
            if clear_func:
                clear_func()
            
            # 3. Type Text
            self.type_hangul_text(text)
            
            # 4. Verify (if provided)
            if validator_func:
                if validator_func(text):
                    print("[Action] Input Verified.")
                    return True
                else:
                    print(f"[Input] Mismatch detected (Attempt {attempt+1}).")
            else:
                # No validation needed
                return True
                
        print("[Failure] Failed to type and verify text after retries.")
        return False
