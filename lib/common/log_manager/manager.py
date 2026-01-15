from typing import List, Dict, Any
import datetime
from lib.common.utils import generate_common_payload
from lib.common.log_manager.schemas.base import BaseSchema

class LogManager:
    """
    Manages the collection, batching, and formatting of logs for bulksubmit.
    Mimics the APK's LogManager queuing system.
    """
    
    def __init__(self, context: Dict[str, Any]):
        self.context = context
        self.queue: List[BaseSchema] = []
        
    def add(self, schema: BaseSchema):
        """Add a schema instance to the queue."""
        if not isinstance(schema, BaseSchema):
            raise ValueError(f"Invalid schema type: {type(schema)}")
        self.queue.append(schema)
        
    def clear(self):
        """Clear the current queue."""
        self.queue = []
        
    def flush(self) -> List[Dict[str, Any]]:
        """
        Process all queued schemas and return the final payload list for bulksubmit.
        Automatically injects 'common' payload and handles timestamp sequencing.
        """
        if not self.queue:
            return []

        payload_list = []
        
        # Base time for this flush batch
        # All logs in a batch usually share a close timeframe
        base_time = datetime.datetime.now()
        
        for schema in self.queue:
            # 1. Convert Schema to partial dict (Meta, Data, Extra)
            # This also calculates the jittered event time
            partial_payload = schema.to_dict(base_time=base_time)
            
            # 2. Generate Common Payload
            # We use the event_time calculated by the schema to ensure
            # the common.eventTime matches the actual event occurrence
            event_time = partial_payload.get('_internal', {}).get('event_time')
            common_payload = generate_common_payload(self.context, event_time=event_time)
            
            # 3. Assemble Final Entry
            entry = {
                'common': common_payload,
                'meta': partial_payload['meta'],
                'data': partial_payload['data'],
                'extra': partial_payload['extra']
            }
            
            payload_list.append(entry)
            
        # Clear queue after flushing
        self.clear()
        
        return payload_list
