from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EventCreate(BaseModel):
    event_type: str
    event_metadata: Optional[dict] = None
    timestamp: Optional[datetime] = None
