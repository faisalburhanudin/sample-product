import os

from flask import Flask
from flask_migrate import Migrate

from app import route, model


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///:memory:")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def create_app():
    """Create flask instance"""
    app = Flask(__name__)

    app.config.from_object(Config)

    app.register_blueprint(route.bp)

    model.db.init_app(app)
    Migrate(app, model.db)
    return app
