from fastapi import FastAPI, HTTPException 
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
    deleted = services.delete_event(event_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )
    
    return {"massage": "Event deleted successfully"}

@app.patch("/events/{event_id}")
def patch_event_endpoint(event_id: int, event_data: EventUpdate):
    pathced = services.patch_event(event_id, event_data)

    if not pathced:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )
    
    return {"massage": "Event patched successfully"}

@app.get("/balance")
def sum_impact_endpoint():
    return services.sum_events_impact()