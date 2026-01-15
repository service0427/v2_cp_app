from typing import Dict, Any, List
from .base import BaseSchema

class GenericSchema(BaseSchema):
    """
    A generic schema implementation that builds its payload based on a JSON definition.
    Allows for dynamic schema creation without defining individual Python classes.
    """

    def __init__(self, context: Dict[str, Any], definition: Dict[str, Any]):
        super().__init__(context)
        self.definition = definition

    @property
    def schema_id(self) -> int:
        return self.definition.get('schemaId')

    @property
    def schema_version(self) -> int:
        return self.definition.get('schemaVersion')

    def _resolve_value(self, source_path: str, default_value: Any = None) -> Any:
        """
        Resolves a value from the context using dot notation (e.g., 'RESULT.SEARCH.rank').
        """
        if not source_path:
            return default_value

        current = self.context
        parts = source_path.split('.')
        
        for part in parts:
            if isinstance(current, dict):
                current = current.get(part)
            else:
                return default_value
                
            if current is None:
                return default_value
                
        return current

    def get_data(self) -> Dict[str, Any]:
        data = {}
        
        # 1. Apply static fields
        static_fields = self.definition.get('static', {}).get('data', {})
        data.update(static_fields)
        
        # 2. Apply dynamic mappings
        mappings = self.definition.get('mapping', {}).get('data', {})
        for field_name, rule in mappings.items():
            # rule can be a string (source path) or a dict (complex rule)
            if isinstance(rule, str):
                val = self._resolve_value(rule)
                if val is not None:
                    data[field_name] = val
            elif isinstance(rule, dict):
                source = rule.get('source')
                default = rule.get('default')
                val = self._resolve_value(source, default)
                if val is not None:
                    data[field_name] = val
                    
        return data

    def get_extra(self) -> Dict[str, Any]:
        extra = {}
        
        # 1. Apply static extra
        static_extra = self.definition.get('static', {}).get('extra', {})
        extra.update(static_extra)
        
        # 2. Apply dynamic mappings for extra
        mappings = self.definition.get('mapping', {}).get('extra', {})
        for field_name, rule in mappings.items():
            if isinstance(rule, str):
                val = self._resolve_value(rule)
                if val is not None:
                    extra[field_name] = val
            elif isinstance(rule, dict):
                source = rule.get('source')
                default = rule.get('default')
                val = self._resolve_value(source, default)
                if val is not None:
                    extra[field_name] = val
                    
        return extra
