import functools
import operator
from money import Money

class Portfolio:
    def __init__(self):
        self.moneys = []
        self._eur_to_used = 1.2

    def add(self, *moneys):
        self.moneys.extend(moneys)    
    
    def __convert(self, aMoney, aCurrency):
        exchangeRates = {
            "EUR->USD": 1.2,
            "USD->KRW": 1100,
        }
        if aMoney.currency == aCurrency:
            return aMoney.amount
        else:
            key = aMoney.currency + "->" + aCurrency
            return aMoney.amount * exchangeRates[key]

    # method injection from Bank class
    def evaluate(self, bank, currency):
        total = Money(0, currency)
        failures = ""
        for m in self.moneys:
            c, k = bank.convert(m, currency)
            if k is None:
                total += c
            else:
                failures += k if not failures else "," + k
        # empty string is False
        if not failures:
            return total
        raise Exception("Missing exchange rate(s):[" + failures +"]")

