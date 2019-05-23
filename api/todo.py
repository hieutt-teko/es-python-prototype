"""
Example for testing peewee with flask
"""
import uuid

from flask import request, jsonify, Blueprint

from models.models import ToDo

bp = Blueprint("todo", __name__, url_prefix="/todo")


@bp.route("", methods=["POST"])
def create():
    data = request.get_json()
    todo = ToDo(uuid=uuid.uuid4(), name=data["name"], status=False)
    todo.save(force_insert=True)
    return jsonify(todo.to_json())

@bp.route("")
def list_():
    todos = ToDo.select()
    return jsonify([todo.to_json() for todo in todos])
