from typing import Optional

from app.exception import UserNotFound
from app.model import db, User


def create(username: str, email: str) -> User:
    """Create new user

    Args:
        username: name user
        email: email user

    Returns:
        User object
    """
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user


def get_by_id(user_id: int) -> Optional[User]:
    """Get user by id
    if user not found None is return

    Args:
        user_id: id user

    Returns:
        User object or None
    """
    user = User.query.filter_by(id=user_id).first()
    return user


def delete(user_id: int):
    """Delete user by id

    Args:
        user_id: id user will be deleted
    """
    usr = get_by_id(user_id)
    if not usr:
        raise UserNotFound

    db.session.delete(usr)
    db.session.commit()


def update(user_id: int, username: str = None, email: str = None) -> User:
    """Update user information

    Args:
        user_id: id user will be update
        username: new username
        email: new email

    Returns:
        User object
    """
    usr = get_by_id(user_id)
    if not usr:
        raise UserNotFound

    if username is not None:
        usr.username = username

    if email is not None:
        usr.email = email

    db.session.add(usr)
    db.session.commit()
    return usr
