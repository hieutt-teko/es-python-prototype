import uuid

import peewee as pw

from models.base import BaseModel, JSONField


class EventModel(BaseModel):
    uuid = pw.UUIDField(primary_key=True, default=uuid.uuid4)
    aggregate_uuid = pw.UUIDField()
    name = pw.TextField()
    data = JSONField()


class AggregateModel(BaseModel):
    uuid = pw.UUIDField(primary_key=True, default=uuid.uuid4)
    version = pw.IntegerField()


class Order(BaseModel):
    uuid = pw.UUIDField(primary_key=True, default=uuid.uuid4)
    user_id = pw.IntegerField()
    status = pw.TextField()


class ToDo(BaseModel):
    uuid = pw.UUIDField(primary_key=True, default=uuid.uuid4)
    name = pw.TextField()
    status = pw.BooleanField()

    def to_json(self):
        return {"uuid": self.uuid, "name": self.name, "status": self.status}
