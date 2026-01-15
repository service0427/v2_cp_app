from abc import ABC, abstractmethod
import datetime
import random
from typing import Dict, Any, Optional

class BaseSchema(ABC):
    """
    Abstract base class for all Coupang Log Schemas.
    Represents a single log entry (Schema) within a bulksubmit payload.
    """
    
    def __init__(self, context: Dict[str, Any]):
        self.context = context
        # Default jitter: 1-5ms to simulate realistic event timing
        self.time_offset_ms = random.randint(1, 5)

    @property
    @abstractmethod
    def schema_id(self) -> int:
        """Return the Schema ID (e.g., 124, 152)"""
        pass

    @property
    @abstractmethod
    def schema_version(self) -> int:
        """Return the Schema Version (e.g., 53, 4)"""
        pass

    @abstractmethod
    def get_data(self) -> Dict[str, Any]:
        """Return the 'data' part of the payload"""
        pass

    @abstractmethod
    def get_extra(self) -> Dict[str, Any]:
        """Return the 'extra' part of the payload"""
        pass
        
    def to_dict(self, base_time: datetime.datetime = None) -> Dict[str, Any]:
        """
        Convert the schema instance to the dictionary format expected by bulksubmit.
        
        Args:
            base_time: The base timestamp for the batch. If provided, jitter is added.
                      If None, current time is used.
        """
        # Calculate event time
        if base_time:
            event_time_dt = base_time + datetime.timedelta(milliseconds=self.time_offset_ms)
            event_time_str = event_time_dt.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "+0900"
        else:
            # Fallback to current time if no batch time provided
            now = datetime.datetime.now()
            event_time_str = now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "+0900"

        # Note: 'common' is NOT generated here. 
        # It is injected by the LogManager to ensure consistency across the batch.
        return {
            'meta': {
                'schemaId': self.schema_id,
                'schemaVersion': self.schema_version
            },
            'data': self.get_data(),
            'extra': self.get_extra(),
            '_internal': {
                'time_offset_ms': self.time_offset_ms,
                'event_time': event_time_str
            }
        }
