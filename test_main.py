from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_valid_conversion():
    response = client.get("/convert?source=USD&target=JPY&amount=1,525")
    assert response.status_code == 200
    assert response.json() == {"msg": "success", "amount": "170,496.53"}

def test_invalid_currency():
    response = client.get("/convert?source=XXX&target=JPY&amount=100")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid source or target currency"}

def test_invalid_amount_format():
    response = client.get("/convert?source=USD&target=JPY&amount=abc")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid amount format"}

def test_negative_amount():
    response = client.get("/convert?source=USD&target=JPY&amount=-100")
    assert response.status_code == 400
    assert response.json() == {"detail": "Amount must be positive"}

def test_rounding():
    response = client.get("/convert?source=USD&target=JPY&amount=1,234.567")
    assert response.status_code == 200
    assert response.json() == {"msg": "success", "amount": "138,025.83"}

# 沒帶資料 會被Query攔下 回傳422
def test_missing_source():
    response = client.get("/convert?target=JPY&amount=100")
    assert response.status_code == 422

def test_missing_target():
    response = client.get("/convert?source=USD&amount=100")
    assert response.status_code == 422

def test_missing_amount():
    response = client.get("/convert?source=USD&target=JPY")
    assert response.status_code == 422

