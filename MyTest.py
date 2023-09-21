import json
import pytest
from flask import Flask
from your_module import app

# Créez un client de test Flask pour interagir avec l'application
@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

# Testez la route d'accueil
def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Bienvenue sur l'application de gestion" in response.data

# Testez la route de liste des machines (GET)
def test_liste_machine_get(client):
    response = client.get('/machines')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "machines" in data

# Testez la route de liste des machines (POST)
def test_liste_machine_post(client):
    data = {
        "name": "Machine1",
        "type": "Type1"
    }
    response = client.post('/machines', json=data)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "machine" in data

# Testez la route de détails d'une machine (GET)
def test_get_machine(client):
    response = client.get('/machines/Machine1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "machine" in data

# Testez la route de modification d'une machine (PUT)
def test_edit_machine(client):
    data = {
        "name": "Machine1",
        "type": "Type2"
    }
    response = client.put('/machines/Machine1', json=data)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "machine" in data

# Testez la route de suppression d'une machine (DELETE)
def test_delete_machine(client):
    response = client.delete('/machines/Machine1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "machine" in data
