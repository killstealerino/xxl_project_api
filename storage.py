import json

events_path = "data\events.json"

def load_events():
    with open(events_path, "r", encoding="utf-8") as reading_file:
        return json.load(reading_file)

def save_events(events):
    with open(events_path, "w", encoding="utf-8") as reading_file:
        json.dump(events, reading_file, indent=4, ensure_ascii=False)