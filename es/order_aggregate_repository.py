import uuid

from event_store.event_store import EventStore
from es.order_aggregate import OrderAggregate


class OrderAggregateRepository:
    def __init__(self, event_store: EventStore):
        self.event_store = event_store

    def get(self, aggregate_id: uuid.UUID):
        event_stream = self.event_store.load_stream(aggregate_id)
        return OrderAggregate(event_stream)

    def save(self, order: OrderAggregate):
        self.event_store.append_to_stream(order.id, order.version, order.changes)
