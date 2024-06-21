import decimal
import re
from decimal import Decimal, ROUND_HALF_UP

# Static exchange rate data
exchange_rates = {
    "TWD": {"TWD": Decimal('1'), "JPY": Decimal('3.669'), "USD": Decimal('0.03281')},
    "JPY": {"TWD": Decimal('0.26956'), "JPY": Decimal('1'), "USD": Decimal('0.00885')},
    "USD": {"TWD": Decimal('30.444'), "JPY": Decimal('111.801'), "USD": Decimal('1')}   
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
            amount = Decimal(re.sub(r'[,\s]', '', amount))
        except decimal.InvalidOperation:
            return None, "Invalid amount format"
        
        if amount < Decimal('0'):
            return None, "Amount must be positive"
        
        converted_amount = amount * self.rates[source][target]
        # Round to 2 decimal places using ROUND_HALF_UP rounding strategy
        converted_amount = converted_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        return converted_amount, None

def get_currency_exchange_service():
    return CurrencyExchangeService(exchange_rates)
