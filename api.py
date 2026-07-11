from fastapi import FastAPI
from models import EventCreate, EventUpdate
from services import create_event, get_all_events, delete_event_service, patch_event_service

app = FastAPI()

@app.post("/events")
def add_event(event_data: EventCreate):
    return create_event(event_data)

@app.get("/events")
def get_events():
    return get_all_events()

@app.delete("/events/{event_id}")
def delete_event(event_id: int):
    return delete_event_service(event_id)

@app.patch("/events/{event_id}")
def patch_event_endpoint(event_id: int, event_data: EventUpdate):
    return patch_event_service(event_id, event_data)