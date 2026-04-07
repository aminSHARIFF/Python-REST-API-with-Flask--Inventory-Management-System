import pytest
from unittest.mock import patch
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test GET all inventory
def test_get_inventory(client):
    response = client.get('/inventory')
    assert response.status_code == 200

# Test GET single item that exists
def test_get_single_item(client):
    response = client.get('/inventory/1')
    assert response.status_code == 200

# Test GET single item that does not exist
def test_get_item_not_found(client):
    response = client.get('/inventory/999')
    assert response.status_code == 404

# Test POST add new item
def test_add_item(client):
    new_item = {
        "name": "Test Product",
        "brand": "Test Brand",
        "price": 9.99,
        "quantity": 10,
        "barcode": "111222333"
    }
    response = client.post('/inventory', json=new_item)
    assert response.status_code == 201

# Test PATCH update item
def test_update_item(client):
    update = {"price": 5.99, "quantity": 20}
    response = client.patch('/inventory/1', json=update)
    assert response.status_code == 200

# Test DELETE item
def test_delete_item(client):
    response = client.delete('/inventory/1')
    assert response.status_code == 200

# Test external API with mock
def test_lookup_product(client):
    mock_response = {
        "status": 1,
        "product": {
            "product_name": "Test Milk",
            "brands": "Test Brand"
        }
    }
    with patch('app.requests.get') as mock_get:
        mock_get.return_value.json.return_value = mock_response
        response = client.get('/lookup/123456')
        assert response.status_code == 200