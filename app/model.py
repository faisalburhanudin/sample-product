from enum import Enum
from typing import Optional

from flask_sqlalchemy import SQLAlchemy


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


class ClothesSize(Enum):
    XXXS = 1
    XXS = 2
    XS = 3
    S = 4
    M = 5
    L = 6
    XL = 7
    XXL = 8
    XXXL = 9
    XXXXL = 9


class WrongClothesSize(Exception):
    pass


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)

    username = db.Column(db.String(50), unique=True, nullable=False)

    email = db.Column(db.String(50), unique=True, nullable=False)

    photo_filename = db.Column(db.String(225), unique=True, nullable=False, default="")

    clothes_size_value = db.Column(db.Integer, nullable=False, default=0)

    def set_clothes_size(self, size: ClothesSize):
        """set user clothes size

        Args:
            size: instance of ClothesSize
        """
        if isinstance(size, ClothesSize):
            raise WrongClothesSize

        self.clothes_size_value = size.value

    @property
    def clothes_size(self) -> Optional[ClothesSize]:
        """get clothes size in enum format

        Returns:
            ClothesSize object
        """
        if self.clothes_size_value:
            return ClothesSize(self.clothes_size_value)
        return None

    @property
    def photo_url(self):
        """todo get photo url"""
        return ""
