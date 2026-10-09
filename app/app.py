from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Ahoj z Dockeru! Verze 1.0</h1>"

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



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