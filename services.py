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