import pytest
from app import app

def test_hello_endpoint():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Ahoj z Dockeru" in response.data

def test_health_endpoint():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    assert response.data == b"OK"