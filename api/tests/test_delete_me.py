import pytest
from starlette.testclient import TestClient

from api.app_factory import create_app


# TODO: move to tests/conftest.py
@pytest.fixture(scope='module')
def api_client():
    app = create_app()
    _api_client = TestClient(app)
    yield _api_client


# FIXME
def test_demo_route(api_client):
    response = api_client.get('/demo')
    assert response.status_code == 200
    assert response.json() == {'hello': 'world'}


# FIXME
def test_404(api_client):
    response = api_client.get('/none')
    assert response.status_code == 404
