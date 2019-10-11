from flask import Flask
from app import route


def create_app():
    app = Flask(__name__)
    app.register_blueprint(route.bp)
    return app
