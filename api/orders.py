from flask import Blueprint

bp = Blueprint("orders", __name__, url_prefix="/orders")


@bp.route("", methods=["POST"])
def create():
    return "OK"


@bp.route("", methods=["PUT"])
def change():
    return "OK"


@bp.route("/<id>")
def get(id):
    return "OK"


@bp.route("")
def list_():
    return "OK"
