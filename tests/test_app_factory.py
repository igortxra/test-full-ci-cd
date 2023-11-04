import pytest
from flask import Flask
from flask.testing import FlaskClient

from app import create_app


@pytest.fixture(name="client")
def create_test_client():
    """Returns FlaskClient instance for test purposes."""
    app = create_app()
    app.testing = True
    return app.test_client()


def test_app_factory_returns_app():
    """App factory must return an Flask instance."""
    app = create_app()
    assert isinstance(app, Flask)


def test_app_index_route_return(client: FlaskClient):
    """App index route must return status 200"""
    response = client.get("/")
    assert response.status_code == 200


def test_app_index_body_return(client: FlaskClient):
    """App index route must return empty json"""
    response = client.get("/")
    assert response.get_json() == {}
