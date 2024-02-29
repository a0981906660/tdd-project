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
        if aMoney.currency == aCurrency:
            return aMoney.amount
        else:
            return aMoney.amount * self._eur_to_used

    def evaluate(self, currency):
        total = functools.reduce(
            # the 0 here (the last argument of reduce) is the initial value of the accumulator
            operator.add, map(lambda m: self.__convert(m, currency), self.moneys), 0
            )
        return Money(total, currency)

