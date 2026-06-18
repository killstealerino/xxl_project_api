from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def add_event(event_data: EventCreate):
    return create_event(event_data)