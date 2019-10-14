import pytest
import app
from app.model import db


@pytest.fixture()
def client():
    """Create flask test client"""
    instance = app.create_app()
    instance.app_context().push()

    with instance.app_context():
        db.create_all()

    yield instance.test_client()

    with instance.app_context():
        db.drop_all()
