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
