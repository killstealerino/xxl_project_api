from datetime import datetime

from model import event_model, event_create
from storage import load_events, save_events

def create_event(event_data: event_create):
    events = load_events()

    max_id = max(
        (event[id] for event in events),
        default=0
    )

    event = event_model(
        id = max_id+1,
        text= event_data.text,
        impact = event_data.impact,
        create_date = datetime.now()
    )

    event.append(event.model_dump(mode="json"))

    save_events(events)

    return event