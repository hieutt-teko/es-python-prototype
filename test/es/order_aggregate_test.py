from es.order_aggregate import OrderAggregate
from es.events import OrderAttributeChangeEvent


def test_create():
    order = OrderAggregate.create(1)

    assert order.version == 1
    assert len(order.changes) == 1


def test_change_status():
    order = OrderAggregate.create(1)
    event_1 = OrderAttributeChangeEvent(user_id=1, new_status="draft")
    order.apply(event_1)

    assert order.user_id == 1
    assert order.status == "draft"
    assert len(order.changes) == 2
