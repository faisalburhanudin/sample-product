import os

from logging.config import dictConfig
from flask import Flask
from flask_migrate import Migrate

from app import route, model

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
)


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
