import json

import peewee as pw

database = pw.MySQLDatabase("espro")


class JSONField(pw.TextField):
    """
    Simple and dummy way to support JSON.
    TODO: find more optimise way
    """

    def db_value(self, value):
        return json.dumps(value)

    def python_value(self, value):
        if value is not None:
            return json.loads(value)


class BaseModel(pw.Model):
    class Meta:
        database = database
