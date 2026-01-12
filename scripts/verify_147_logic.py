import json
import os

def verify_logic():
    # Load context from the failed scenario
    context_path = '/home/tech/v2_cp_app/logs/session/20260112/210334_노트북_8099175514/context.log'
    with open(context_path, 'r') as f:
        context = json.load(f)

    print(f"Loaded Context. INPUT.q = {context['INPUT']['q']}")
    
    # Simulate 147_P logic
    bypass_124 = context.get('srp_click_log_bypass', {})
    fallback_124 = context.get('RESULT', {}).get('META', {}).get('SEARCH', {}).get('124_53', {})
    
    print(f"Bypass 124 Keys: {bypass_124.keys()}")
    if bypass_124:
         print(f"Bypass Mandatory Keys: {bypass_124.get('mandatory', {}).keys()}")
         
    print(f"Fallback 124 Keys: {fallback_124.keys()}")

    schema_124_data = (bypass_124.get('mandatory') or fallback_124.get('data') or {}).copy()
    
    print(f"Initial Schema 124 Data Keys: {schema_124_data.keys()}")
    
    # Inject Missing Keys (Copy-paste from 147_P)
    if not schema_124_data.get('q'):
        print("Injecting q...")
        schema_124_data['q'] = context.get('INPUT', {}).get('q')
        
    if not schema_124_data.get('internalCategoryId'):
        print("Injecting internalCategoryId...")
        schema_124_data['internalCategoryId'] = context.get('RESULT', {}).get('SEARCH', {}).get('internalCategoryId')
        
    if not schema_124_data.get('id'):
         print("Injecting id...")
         schema_124_data['id'] = context.get('RESULT', {}).get('ROOT', {}).get('productId')
         
    if not schema_124_data.get('itemProductId'):
         print("Injecting itemProductId...")
         schema_124_data['itemProductId'] = 4 

    if not schema_124_data.get('searchViewType'):
         print("Injecting searchViewType...")
         schema_124_data['searchViewType'] = context.get('RESULT', {}).get('SEARCH', {}).get('searchViewType', 'GRID_2')

    if not schema_124_data.get('rank'):
        print("Injecting rank...")
        schema_124_data['rank'] = context.get('RESULT', {}).get('SEARCH', {}).get('srp_rank')

    print(f"Final Schema 124 Data: {schema_124_data}")
    
    # Check if q is present
    if 'q' in schema_124_data:
        print(f"SUCCESS: q is present: {schema_124_data['q']}")
    else:
        print("FAILURE: q is MISSING")

if __name__ == "__main__":
    verify_logic()
