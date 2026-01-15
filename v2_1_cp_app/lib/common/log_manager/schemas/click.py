from typing import Dict, Any, Optional
from .base import BaseSchema

class SrpProductClick(BaseSchema):
    """
    Schema 124: SrpProductClick
    Logged when a user clicks a product in the Search Results Page (SRP).
    """

    def __init__(self, context: Dict[str, Any]):
        super().__init__(context)
        self.search_result = context.get('RESULT', {}).get('SEARCH', {})
        self.root_result = context.get('RESULT', {}).get('ROOT', {})
        self.input_data = context.get('INPUT', {})
        
        # Bypass logic (from 147_P)
        self.bypass_mandatory = context.get('srp_bypass_mandatory', {})
        self.fallback_124_data = context.get('RESULT', {}).get('META', {}).get('SEARCH', {}).get('124_53', {}).get('data', {})

    @property
    def schema_id(self) -> int:
        return 124

    @property
    def schema_version(self) -> int:
        return 53

    def get_data(self) -> Dict[str, Any]:
        data = self.fallback_124_data.copy()
        
        # Priority: Bypass Mandatory > Input/Context > Fallback
        
        # 1. Query (q)
        if not data.get('q'):
            data['q'] = self.bypass_mandatory.get('q') or self.input_data.get('q')

        # 2. Internal Category ID
        if not data.get('internalCategoryId') or data.get('internalCategoryId') == '':
            data['internalCategoryId'] = self.bypass_mandatory.get('internalCategoryId') or \
                                         self.search_result.get('internalCategoryId', '')

        # 3. Product ID (id)
        if not data.get('id'):
            data['id'] = self.bypass_mandatory.get('id') or self.root_result.get('productId')

        # 4. Item Product ID
        if not data.get('itemProductId'):
            data['itemProductId'] = self.bypass_mandatory.get('itemProductId') or \
                                    self.root_result.get('itemProductId', '4')

        # 5. Search View Type
        if not data.get('searchViewType'):
            data['searchViewType'] = self.search_result.get('searchViewType', 'GRID_2')

        # 6. Rank
        if not data.get('rank'):
            data['rank'] = self.bypass_mandatory.get('searchRank') or self.search_result.get('srp_rank')
            
        return data

    def get_extra(self) -> Dict[str, Any]:
        # Merge extra from bypass and meta
        bypass_extra = self.context.get('srp_click_log_bypass', {}).get('extra', {})
        meta_extra = self.context.get('RESULT', {}).get('META', {}).get('SEARCH', {}).get('124_53', {}).get('extra', {})
        
        extra = {**meta_extra, **bypass_extra}
        
        # Mandatory overrides
        extra['currentView'] = '/search_list'
        extra['eventReferrer'] = 'click_search_list'
        
        return extra
