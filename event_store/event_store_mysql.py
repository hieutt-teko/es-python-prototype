import uuid
from typing import Optional, List

from events.event_stream import EventStream
import events.events as events
from events.events import Event

from event_store.event_store import EventStore
from models.models import EventModel, AggregateModel
from models.base import database


class MySQLEventStore(EventStore):
    def load_stream(self, aggregate_id: uuid.UUID) -> EventStream:
        # TODO: join into single query
        with database.atomic() as tx:
            aggregate = AggregateModel.get(AggregateModel.uuid == aggregate_id)
            event_models = EventModel.select().where(EventModel.uuid == aggregate_id)

        events = [MySQLEventStore._convert_to_event(event) for event in event_models]
        return EventStream(events, aggregate.uuid)

    def append_to_stream(
            self,
            aggregate_id: uuid.UUID,
            expect_version: Optional[int],
            events: List[Event],
    ) -> None:
        # Update aggregate
        if expect_version:  # update
            aggregate = AggregateModel.select().where(AggregateModel.uuid == aggregate_id, AggregateModel.version == expect_version)
            aggregate.version = expect_version + 1
            aggregate.save()
        else:  # insert new
            aggregate = AggregateModel(uuid=aggregate_id, version=1)
            aggregate.save(force_insert=True)

        # Update event store
        # TODO: insert many
        for event in events:
            # HACK: prototype only
            EventModel(aggregate_id=aggregate_id, name=event.__class__.__name__, data=event.__dict__).save(force_insert=True)


    @classmethod
    def _convert_to_event(cls, event_model_instance: EventModel) -> Event:
        event_type = event_model_instance.name
        event_data = event_model_instance.data

        event_cls= getattr(events, event_type)
        return event_cls(**event_data)
