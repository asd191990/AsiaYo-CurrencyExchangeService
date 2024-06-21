from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

#測試基本轉換是否正常
def test_valid_conversion():
    response = client.get("/convert?source=USD&target=JPY&amount=1,525")
    assert response.status_code == 200
    assert response.json() == {"msg": "success", "amount": "170,496.53"}

#測試貨幣無效情況
def test_invalid_currency():
    response = client.get("/convert?source=XXX&target=JPY&amount=100")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid source or target currency"}

#測試amount格式不合格
def test_invalid_amount_format():
    response = client.get("/convert?source=USD&target=JPY&amount=abc")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid amount format"}

#測試負數金額
def test_negative_amount():
    response = client.get("/convert?source=USD&target=JPY&amount=-100")
    assert response.status_code == 400
    assert response.json() == {"detail": "Amount must be positive"}

#確認四捨五入
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

