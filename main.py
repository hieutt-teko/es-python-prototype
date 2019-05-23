from flask import Flask

from api.orders import bp as bp_orders
from api.todo import bp as bp_todo
from models.base import database


def create_app():
    app = Flask(__name__)

    # Register blueprint
    app.register_blueprint(bp_orders)
    app.register_blueprint(bp_todo)

    # Database session the dummy way. lol
    @app.before_request
    def before_request():
        database.connect()

    @app.after_request
    def after_request(response):
        database.close()
        return response

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
