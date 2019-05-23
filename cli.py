import click

from models.base import database
from models.models import EventModel, AggregateModel, Order, ToDo

@click.command()
def create_database():
    """
    Hacky way to init a table
    """
    database.create_tables([EventModel, AggregateModel, Order, ToDo])
    click.echo("Done create tables")

if __name__ == "__main__":
    create_database()
