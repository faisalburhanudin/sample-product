import pytest
import app
from app.model import db


@pytest.fixture()
def client():
    """Create flask test client"""
    instance = app.create_app()
    instance.app_context().push()

    db.create_all()

    yield instance.test_client()

    db.drop_all()
