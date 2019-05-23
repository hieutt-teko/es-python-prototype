import uuid
import functools
from typing import List

from es.events import OrderCreatedEvent, OrderAttributeChangeEvent
from helpers import method_dispatch
from es.events import Event, EventStream


class OrderAggregate:
    id: uuid.UUID
    version: int
    changes: List[Event] = []

    user_id: int
    status: str

    def __init__(self, event_stream: EventStream):
        self.version = event_stream.version

        for event in event_stream.events:
            self.apply(event)

    @classmethod
    def create(cls, user_id):
        """
        Helper static method create new Order
        """
        init_event = OrderCreatedEvent(id=uuid.uuid4(), user_id=user_id)
        init_event_stream = EventStream(events=[init_event], version=1)
        instance = cls(init_event_stream)
        instance.changes.append(init_event)
        return instance

    @method_dispatch
    def apply(self, event):
        """
        Polymorphism way to run `apply` into an event.
        """
        raise ValueError("Unknown event!")

    @apply.register(OrderCreatedEvent)
    def _(self, event: OrderCreatedEvent):
        self.id = event.id
        self.user_id = event.user_id
        self.status = "new"

    @apply.register(OrderAttributeChangeEvent)
    def _(self, event: OrderAttributeChangeEvent):
        self.user_id = event.user_id
        self.status = event.new_status
