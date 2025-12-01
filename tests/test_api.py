import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import tempfile
import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client(monkeypatch, tmp_path):
    db_file = tmp_path / 'test.db'
    monkeypatch.setenv('DATABASE_URL', f'sqlite:///{db_file}')
    from app.db import Base, engine
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as c:
        yield c

def test_health(client):
    r = client.get('/health')
    assert r.status_code == 200
    assert r.json() == {'status': 'ok'}

def test_create_and_get_place(client):
    create = client.post('/places', json={'name': 'Cafe Quiet', 'address': 'Main St', 'rating': 5})
    assert create.status_code == 201
    data = create.json()
    assert data['name'] == 'Cafe Quiet'
    get = client.get(f"/places/{data['id']}")
    assert get.status_code == 200
    assert get.json()['name'] == 'Cafe Quiet'

def test_list_places(client):
    client.post('/places', json={'name': 'A', 'address': 'X'})
    client.post('/places', json={'name': 'B', 'address': 'Y'})
    r = client.get('/places')
    assert r.status_code == 200
    assert isinstance(r.json(), list)
    assert len(r.json()) >= 2
