import os
import glob
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib.capture_parser import parse_capture_file

CAPTURE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'captures')

def batch_rename():
    # Get all capture files matching the pattern
    files = glob.glob(os.path.join(CAPTURE_DIR, 'capture_*.json'))
    
    # Sort by creation time to process in order (optional but nice)
    files.sort(key=os.path.getctime)
    
    renamed_count = 0
    
    print(f"Found {len(files)} capture files to process.")
    
    for filepath in files:
        filename = os.path.basename(filepath)
        
        # Skip if already renamed (though glob shouldn't pick them up if they don't match capture_*.json)
        if not filename.startswith('capture_'):
            continue
            
        print(f"Processing {filename}...")
        
        result = parse_capture_file(filepath)
        
        if result and result.get('q') and result.get('productId'):
            q = result['q'].replace(' ', '_') # Replace spaces with underscores
            pid = result['productId']
            rank = result.get('rank', '0')
            
            # Construct new filename: Keyword-ProductId-Rank.json
            new_filename = f"{q}-{pid}-{rank}.json"
            new_filepath = os.path.join(CAPTURE_DIR, new_filename)
            
            # Rename
            try:
                os.rename(filepath, new_filepath)
                print(f"  -> Renamed to: {new_filename}")
                renamed_count += 1
            except Exception as e:
                print(f"  -> Error renaming {filename}: {e}")
        else:
            print(f"  -> Skipped (Missing metadata): q={result.get('q')}, pid={result.get('productId')}")

    print(f"\nBatch rename complete. Renamed {renamed_count} files.")

if __name__ == "__main__":
    batch_rename()
