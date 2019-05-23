import uuid
from typing import List
from dataclasses import dataclass


class Event:
    pass


@dataclass
class EventStream:
    events: List[Event]
    version: int


@dataclass
class OrderCreatedEvent(Event):
    id: uuid.UUID
    user_id: int


@dataclass
class OrderAttributeChangeEvent(Event):
    user_id: int
    new_status: str
