import uuid
import abc
from typing import Optional, List

from events.event_stream import EventStream
from events.events import Event


class EventStore(abc.ABCMeta):
    @abc.abstractmethod
    def load_stream(self, aggregate_id: uuid.UUID) -> EventStream:
        """
        Load and event stream of an aggregate
        """
        pass

    @abc.abstractmethod
    def append_to_stream(
        self,
        aggregate_id: uuid.UUID,
        expect_version: Optional[int],
        events: List[Event],
    ) -> None:
        """
        Add new entity into an event stream
        """
        pass
