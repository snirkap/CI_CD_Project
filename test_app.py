import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello(client):
    rv = client.get('/')
    if rv.data != b'Hello, World!':
        raise AssertionError(f"Expected b'Hello, World!', but got {rv.data}")
