from fastapi import FastAPI
from models import EventCreate, EventUpdate
import services

app = FastAPI()

@app.post("/events")
def add_event_endpoint(event_data: EventCreate):
    return services.create_event(event_data)

@app.get("/events")
def get_events_endpoint():
    return services.get_all_events()

@app.delete("/events/{event_id}")
def delete_event_endpoint(event_id: int):
    return services.delete_event_service(event_id)

@app.patch("/events/{event_id}")
def patch_event_endpoint(event_id: int, event_data: EventUpdate):
    return services.patch_event_service(event_id, event_data)

@app.get("/balance")
def sum_impact_endpoint():
    return services.sum_events_impact_service()