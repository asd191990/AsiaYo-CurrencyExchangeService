from fastapi import FastAPI, HTTPException, Query, Depends
from currencyExchangeService import CurrencyExchangeService, get_currency_exchange_service

app = FastAPI()

# 路由設定
@app.get("/convert")
def convert_currency(
    source: str = Query(...),
    target: str = Query(...),
    amount: str = Query(...),
    service: CurrencyExchangeService = Depends(get_currency_exchange_service)
):

    converted_amount, error = service.convert(source, target, amount)
    if error:
        raise HTTPException(status_code=400, detail=error)
    
    formatted_amount = f"{converted_amount:,.2f}"
    return {"msg": "success", "amount": formatted_amount}

@app.get("/currencies")
def get_currencies(service: CurrencyExchangeService = Depends(get_currency_exchange_service)):
    return {"currencies": service.rates}

@app.get("/")
async def root():
    return {"test": "Hello World~"}