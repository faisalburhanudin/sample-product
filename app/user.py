from typing import Optional

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
