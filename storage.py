import json

EVENTS_PATH = "data/events.json"

def load_events():
    with open(EVENTS_PATH, "r", encoding="utf-8") as reading_file:
        return json.load(reading_file)

def save_events(events):
    with open(EVENTS_PATH, "w", encoding="utf-8") as reading_file:
        json.dump(events, reading_file, indent=4, ensure_ascii=False)