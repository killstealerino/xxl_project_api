from fastapi import FastAPI
from models import EventCreate
from services import create_event

app = FastAPI()

@app.post("/events")
def add_event(event_data: EventCreate):
    return create_event(event_data)