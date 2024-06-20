import re

# 靜態資料
exchange_rates = {
    "TWD": {"TWD": 1, "JPY": 3.669, "USD": 0.03281},
    "JPY": {"TWD": 0.26956, "JPY": 1, "USD": 0.00885},
    "USD": {"TWD": 30.444, "JPY": 111.801, "USD": 1}
}


class CurrencyExchangeService:
    def __init__(self, rates):
        self.rates = rates

    def validate_currency(self, currency):
        if currency not in self.rates:
            return False
        return True

    def convert(self, source, target, amount):
        if not self.validate_currency(source) or not self.validate_currency(target):
            return None, "Invalid source or target currency"
        
        try:
            amount = float(re.sub(r'[,\s]', '', amount))
        except ValueError:
            return None, "Invalid amount format"
        
        if amount < 0:
            return None, "Amount must be positive"
        
        converted_amount = amount * self.rates[source][target]
        return round(converted_amount, 2), None

def get_currency_exchange_service():
    return CurrencyExchangeService(exchange_rates)
