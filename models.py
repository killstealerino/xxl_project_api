from datetime import datetime
from pydantic import BaseModel

class EventModel(BaseModel):
    id: int
    text: str
    impact: int
    created_at: datetime

class EventCreate(BaseModel):
    text: str
    impact: int

class EventUpdate(BaseModel):
    text: str
    impact: int
    updated_at: datetime