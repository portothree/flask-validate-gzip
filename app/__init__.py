from flask import Flask

from .controllers.comm_actions import comm_actions_blueprint


def create_app():
    app = Flask(__name__)

    url_prefix = "/api"

    app.register_blueprint(comm_actions_blueprint, url_prefix=url_prefix)

    return app
