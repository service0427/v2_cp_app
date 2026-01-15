import os
import json
from typing import Dict, Any, Optional
from .schemas.generic import GenericSchema
from .schemas.base import BaseSchema

class SchemaFactory:
    """
    Factory to create Schema instances based on JSON definitions.
    """
    
    _definitions: Dict[int, Dict[str, Any]] = {}
    _def_path = os.path.join(os.path.dirname(__file__), 'definitions')

    @classmethod
    def _load_definition(cls, schema_id: int) -> Optional[Dict[str, Any]]:
        if schema_id in cls._definitions:
            return cls._definitions[schema_id]
            
        file_path = os.path.join(cls._def_path, f"{schema_id}.json")
        if not os.path.exists(file_path):
            return None
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                definition = json.load(f)
                cls._definitions[schema_id] = definition
                return definition
        except Exception as e:
            print(f"[SchemaFactory] Error loading definition {schema_id}: {e}")
            return None

    @classmethod
    def create(cls, schema_id: int, context: Dict[str, Any]) -> BaseSchema:
        """
        Creates a schema instance for the given ID.
        Uses GenericSchema with a loaded definition.
        """
        definition = cls._load_definition(schema_id)
        
        if not definition:
            raise ValueError(f"Schema definition not found for ID: {schema_id}")
            
        return GenericSchema(context, definition)
