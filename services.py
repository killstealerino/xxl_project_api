from datetime import datetime

from models import EventModel, EventCreate
from storage import load_events, save_events

def create_event(event_data: EventCreate):
    events = load_events()

    max_id = max(
        (event["id"] for event in events),
        default=0
    )

    event = EventModel(
        id = max_id+1,
        text= event_data.text,
        impact = event_data.impact,
        created_at = datetime.now()
    )

    events.append(event.model_dump(mode="json"))

    save_events(events)

    return event

def get_all_events():
    return load_events()

def delete_event_service(event_id: int):
    events = load_events()

    new_events = []

    for event in events:
        if event["id"] != event_id:
            new_events.append(event)

    if len(new_events) == len(events):
        return False

    save_events(new_events)

    return True
