import os
import json
from typing import List, Dict, Any
from .manager import LogManager
from .factory import SchemaFactory

class ScenarioManager:
    """
    Orchestrates the generation of schema bundles implementation of high-level scenarios.
    Loads scenario definitions from 'definitions/scenarios.json'.
    """

    _scenarios: Dict[str, List[int]] = {}
    _loaded = False

    def __init__(self, context: Dict[str, Any]):
        self.context = context
        self.log_manager = LogManager(context)
        self._load_scenarios()

    @classmethod
    def _load_scenarios(cls):
        if cls._loaded: return
        
        path = os.path.join(os.path.dirname(__file__), 'definitions', 'scenarios.json')
        if os.path.exists(path):
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    cls._scenarios = json.load(f)
                cls._loaded = True
            except Exception as e:
                print(f"[ScenarioManager] Failed to load scenarios.json: {e}")

    def execute_scenario(self, scenario_name: str) -> List[Dict[str, Any]]:
        """
        Executes a predefined scenario, generating and adding relevant schemas to the LogManager.
        Returns the flushed bulksubmit payload.
        """
        
        schema_ids = self._scenarios.get(scenario_name)
        
        if not schema_ids:
            print(f"[ScenarioManager] Warning: Scenario '{scenario_name}' not found or empty.")
            return []
            
        print(f"[ScenarioManager] Executing '{scenario_name}' with schemas: {schema_ids}")

        for s_id in schema_ids:
            try:
                # Factory creates the schema instance based on JSON definition
                # and populates it from self.context
                schema_instance = SchemaFactory.create(s_id, self.context)
                self.log_manager.add(schema_instance)
            except Exception as e:
                print(f"[ScenarioManager] Error creating schema {s_id}: {e}")
                # We typically continue to try other schemas in the batch
                continue
            
        return self.log_manager.flush()
