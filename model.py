from datetime import datetime
from pydantic import BaseModel

class event_model(BaseModel):
    id: int
    text: str
    impact: int
    created_at: datetime

class event_create(BaseModel):
    text: str
    impact: int