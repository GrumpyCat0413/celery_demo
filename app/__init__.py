import time

from flask import Flask


def create_app():
    app = Flask(__name__)
    from .hello import api as hello_blueprint
    app.register_blueprint(hello_blueprint, url_prefix='/api')
    return app
