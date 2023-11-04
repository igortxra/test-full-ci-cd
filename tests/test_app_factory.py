import pytest
from flask import Flask
from flask.testing import FlaskClient

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()


def test_app_factory_returns_app():
    description = "app factory must return an Flask instance"
    app = create_app()
    assert isinstance(app, Flask), description


def test_app_index_route_return(client: FlaskClient):
    description = "app index route must return status 200"
    response = client.get("/")
    assert response.status_code == 200, description


def test_app_index_body_return(client: FlaskClient):
    description = "app index route must return empty json"
    response = client.get("/")
    assert response.get_json() == {}, description
