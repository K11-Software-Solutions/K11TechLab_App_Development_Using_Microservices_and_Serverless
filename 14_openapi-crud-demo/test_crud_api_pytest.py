import pytest

from crud_api import app

# --- Fixtures ---
@pytest.fixture(scope="module")
def client():
    with app.test_client() as client:
        yield client

# --- Parameterized Tests ---
@pytest.mark.parametrize("product", [
    {"name": "Camera", "price": 250},
    {"name": "Headphones", "price": 120},
    {"name": "Microphone", "price": 80}
])
def test_add_product_param(client, product):
    response = client.post('/product', json=product)
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == product["name"]
    assert data["price"] == product["price"]

def test_get_products(client):
    response = client.get('/products')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) >= 8

def test_add_product(client):
    new_product = {"name": "Speaker", "price": 99}
    response = client.post('/product', json=new_product)
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Speaker"
    assert data["price"] == 99

def test_get_product(client):
    response = client.get('/product/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data["id"] == 1

def test_delete_product(client):
    response = client.delete('/product/8')
    assert response.status_code == 200
    data = response.get_json()
    assert "result" in data

def test_get_nonexistent_product(client):
    response = client.get('/product/999')
    assert response.status_code == 404
    data = response.get_json()
    assert "error" in data

# --- CI Integration & Reporting ---
# To run with coverage and HTML report:
# pytest --cov=crud_api --cov-report=html --html=pytest_report.html --self-contained-html
# For GitHub Actions, see doc/pytest_automation.md
