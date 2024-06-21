# AsiaYo-CurrencyExchangeService

此專案為匯率轉換API，採用Python的FastAPI套件，使用get方式傳遞資料。


## 提供功能

- **轉換貨幣**: 使用已經定義的匯率將輸入進來的金額進行對應的貨幣轉換。
- **列出支援的貨幣**: 檢索服務支援的貨幣列表及其匯率。
- **錯誤處理**: 正確處理無效的貨幣代碼、錯誤的金額格式、負數金額和缺少查詢參數。

## 程式介紹

專案分成三個檔案，分別承擔各自責任。
- currencyExchangeService.py 專門處理貨幣相關的事情
- main.py 專門處理網站運行
- test_main.py 專門測試網站的項目是否符合預期。

## 本地安裝

    pip install -r requirements.txt

### 運行 FastAPI

    uvicorn main:app --reload --port 8080

### API 端點

#### 轉換貨幣

將金額從一種貨幣轉換為另一種。

- **URL**: `/convert`
- **方法**: `GET`
- **參數**:
  - `source`: 貨幣（限 `USD`、`JPY`、`TWD`）。
  - `target`: 目標貨幣（限 `USD`、`JPY`、`TWD`）。
  - `amount`: 要轉換的金額（例如 `100`、`1,234.56`）。
- **回應**:
  - 成功（200 OK）:
    ```json
    {
      "msg": "success",
      "amount": "<formatted_amount>"
    }
    ```
    - `formatted_amount` 為四捨五入至小數點後兩位的轉換後金額。
  - 錯誤（400 Bad Request）:
    ```json
    {
      "detail": "<error_message>"
    }
    ```

#### 內建測試


FastAPI 提供 內建的swagger 可供測試。

- **URL**: `/docs`

## 單元測試

    pytest test_main.py

## docker hub 

快速下載
    https://hub.docker.com/r/asd191990/currencyexchange

啟動
    docker run -d -p 80:80 asiayo-currencyexchangeimage

### 網站連結

- http://0.0.0.0:80
- http://0.0.0.0:80/docs
