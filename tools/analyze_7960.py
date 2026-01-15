import json
import glob
import os

base_dir = "logs/split_test"
log_pattern = os.path.join(base_dir, "**", "147_P_v2_bulksubmit_click_search_product.log")

files = glob.glob(log_pattern, recursive=True)
print(f"Found {len(files)} log files.")

schema_7960_collection = []

for filepath in files:
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            # Handle the log format which might include headers/body text, but usually the split logs are pure JSON or captured request/response text.
            # Based on previous views, split logs seem to be full dumps. I need to find the JSON body.
            
            # Robust JSON extraction: Find the first outer list [...]
            start = content.find('[')
            if start != -1:
                # Naive bracket counting
                depth = 0
                end = -1
                for i in range(start, len(content)):
                    if content[i] == '[':
                        depth += 1
                    elif content[i] == ']':
                        depth -= 1
                        if depth == 0:
                            end = i
                            break
                            
                if end != -1:
                    json_str = content[start:end+1]
                    try:
                        data = json.loads(json_str)
                        for entry in data:
                            if entry.get('meta', {}).get('schemaId') == 7960:
                                product_name = filepath.split('/')[-4] # logs/split_test/<product>/session/...
                                
                                item = {
                                    "product": product_name,
                                    "data": entry.get('data'),
                                    "extra": entry.get('extra')
                                }
                                schema_7960_collection.append(item)
                    except json.JSONDecodeError:
                        print(f"JSON decode error in {filepath}")
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")

# Aggregate keys to see typical structure
all_extra_keys = set()
for item in schema_7960_collection:
    if item['extra']:
        all_extra_keys.update(item['extra'].keys())

print(f"Total 7960 schemas found: {len(schema_7960_collection)}")
print(f"All Extra Keys: {sorted(list(all_extra_keys))}")

# Print detail for analysis
for item in schema_7960_collection:
    print(f"\n--- {item['product']} ---")
    # specific fields of interest
    extra = item['extra']
    print(f"Thumbnail: {extra.get('KEY_THUMBNAIL_IMAGE')}")
    print(f"Price: {extra.get('KEY_SALE_PRICE')}")
    print(f"Rating: {extra.get('KEY_RATING_COUNT')} / {extra.get('KEY_RATING_AVERAGE')}")
    print(f"MVP: {extra.get('sdp.mvp')}")
    print(f"Scale: {extra.get('sdp.productImageScaleType')}")
    print(f"Raw Extra: {json.dumps(extra, ensure_ascii=False)}")
