import pytest
from app.app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_index(client):
    resp = client.get('/')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data['status'] == 'ok'
    assert 'CI Pipeline Sample App' in data['message']

def test_add_success(client):
    resp = client.get('/add?a=2&b=3')
    assert resp.status_code == 200
    assert resp.get_json()['result'] == 5.0

def test_subtract_success(client):
    resp = client.get('/subtract?a=10&b=4')
    assert resp.status_code == 200
    assert resp.get_json()['result'] == 6.0

def test_add_invalid_input(client):
    resp = client.get('/add?a=foo&b=2')
    assert resp.status_code == 400
    assert 'error' in resp.get_json()

def test_subtract_missing_params_default_zero(client):
    resp = client.get('/subtract')
    assert resp.status_code == 200
    assert resp.get_json()['result'] == 0.0
