
import hashlib
import sys

def generate_x_signature(timestamp: str, pcid: str) -> str:
    print(f"Input Timestamp: {timestamp}")
    print(f"Input PCID: {pcid}")
    
    if not pcid or not timestamp:
        print("Error: Missing inputs")
        return ""

    last_char = pcid[-1]
    print(f"Last Char: {last_char}")
    
    if not last_char.isdigit():
        print(f"Error: Last char not digit: {last_char}")
        return ""

    n = int(last_char)
    print(f"N: {n}")

    suffix = pcid[-n:] if n > 0 else ''
    print(f"Suffix: {suffix}")

    input_str = timestamp + suffix
    print(f"Hash Input: {input_str}")
    
    input_bytes = input_str.encode('utf-8')
    hash_result = hashlib.sha256(input_bytes).hexdigest()
    
    return hash_result

# Capture Data
timestamp = "1768198055114"
pcid = "17681980545865986756276"
expected_sig = "9a712d15bfd394b25c3de7b9900b598775512c65bfb0f573697d64b695a8fd57"

generated_sig = generate_x_signature(timestamp, pcid)

print(f"\nGenerated Signature: {generated_sig}")
print(f"Expected  Signature: {expected_sig}")

if generated_sig == expected_sig:
    print("\n[SUCCESS] Custom implementation MATCHES Native Signature!")
else:
    print("\n[FAILURE] Mismatch! Logic is incorrect or placeholder.")
