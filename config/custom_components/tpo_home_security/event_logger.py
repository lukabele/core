from datetime import datetime
from typing import List


class Event:
    def __init__(self, description: str, timestamp: datetime = None):
        self.description = description
        self.timestamp = timestamp or datetime.now()

    def __str__(self):
        return f"[{self.timestamp.isoformat()}] {self.description}"


class EventLog:
    def __init__(self):
        self.logs: List[Event] = []

    def add_event(self, event: Event):
        self.logs.append(event)

    def get_logs(self) -> List[Event]:
        return self.logs


class EventLogger:
    def __init__(self, event_log: EventLog):
        self.event_log = event_log

    def logEvent(self, event: str):
        new_event = Event(description=event)
        self.event_log.add_event(new_event)
        print(f"Event logged: {new_event}")
