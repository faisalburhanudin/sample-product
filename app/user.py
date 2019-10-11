from enum import Enum

from app import db


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

    photo_filename = db.Column(db.String(225), unique=True, nullable=False)

    clothes_size_value = db.Column(db.Integer, nullable=False)

    def set_clothes_size(self, size: ClothesSize):
        """set user clothes size

        :param size: instance of ClothesSize
        """
        if isinstance(size, ClothesSize):
            raise WrongClothesSize

        self.clothes_size_value = size.value

    @property
    def clothes_size(self) -> ClothesSize:
        """get clothes size in enum format

        :return: ClothesSize object
        """
        return ClothesSize(self.clothes_size_value)
