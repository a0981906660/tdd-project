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

    def evaluate(self, currency):
        total = functools.reduce(
            # the 0 here (the last argument of reduce) is the initial value of the accumulator
            operator.add, map(lambda m: self.__convert(m, currency), self.moneys), 0
            )
        return Money(total, currency)

