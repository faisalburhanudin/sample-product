import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import route


class Database(SQLAlchemy):

    def __init__(self):
        super().__init__()

    def create_all(self, bind='__all__', app=None):
        """Destructive method, override create all to make sure only create memory database"""
        self._memory_only(app=app)
        self._execute_for_all_tables(app, bind, 'create_all')

    def drop_all(self, bind='__all__', app=None):
        """Destructive method, override drop all to make sure only drop memory database"""
        self._memory_only(app=app)
        self._execute_for_all_tables(app, bind, 'drop_all')

    def _memory_only(self, app):
        """make sure to drop sqlite memory only"""
        database_uri = self.get_app(app).config['SQLALCHEMY_DATABASE_URI']
        if database_uri != "sqlite:///:memory:":
            raise Exception("Cannot drop_all except sqlite:///:memory:")


db = Database()


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///:memory:")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def create_app():
    """Create flask instance"""
    app = Flask(__name__)

    app.config.from_object(Config)

    app.register_blueprint(route.bp)

    db.init_app(app)
    return app
