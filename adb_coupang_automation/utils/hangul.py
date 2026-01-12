
# Hangul Jamo Decomposition Utility

# Unicode Base Constants
HANGUL_BASE = 0xAC00
HANGUL_END = 0xD7A3

CHO_BASE = 0x1100
JUNG_BASE = 0x1161
JONG_BASE = 0x11A7

# Jamo Lists
CHOSUNG_LIST = [
    'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 
    'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]

JUNGSUNG_LIST = [
    'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 
    'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ'
]

JONGSUNG_LIST = [
    '', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 
    'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 
    'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]

# Computed Constants
NUM_CHOSUNG = 19
NUM_JUNGSUNG = 21
NUM_JONGSUNG = 28

def decompose_char(char):
    """Decomposes a single Hangul character into Jamos."""
    code = ord(char)
    
    if HANGUL_BASE <= code <= HANGUL_END:
        offset = code - HANGUL_BASE
        cho_idx = offset // (NUM_JUNGSUNG * NUM_JONGSUNG)
        jung_idx = (offset // NUM_JONGSUNG) % NUM_JUNGSUNG
        jong_idx = offset % NUM_JONGSUNG
        
        cho = CHOSUNG_LIST[cho_idx]
        jung = JUNGSUNG_LIST[jung_idx]
        jong = JONGSUNG_LIST[jong_idx]
        
        return [j for j in [cho, jung, jong] if j]
    
    return [char]

def decompose_text(text):
    """Decomposes a full string into a flat list of Jamos."""
    result = []
    for char in text:
        result.extend(decompose_char(char))
    return result

def is_double_consonant(jamo):
    """Checks if jamo requires SHIFT (Double Consonant)."""
    return jamo in ['ㅃ', 'ㅉ', 'ㄸ', 'ㄲ', 'ㅆ', 'ㅒ', 'ㅖ']

def resolve_shift_key(jamo):
    """Returns (BaseKey, NeedsShift) tuple for a Jamo."""
    shift_map = {
        'ㅃ': 'ㅂ', 'ㅉ': 'ㅈ', 'ㄸ': 'ㄷ', 'ㄲ': 'ㄱ', 'ㅆ': 'ㅅ',
        'ㅒ': 'ㅐ', 'ㅖ': '게' # Wait, 'ㅒ' is Shift+'ㅐ'? usually yes.
    }
    if jamo in shift_map:
        return shift_map[jamo], True
    return jamo, False
