from flask import Flask


def create_app() -> Flask:
    """ Flask app factory. """
    app = Flask(__name__)

    @app.route("/")
    def index():
        return {}, 200

    return app
