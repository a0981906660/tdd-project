import functools
import operator
from money import Money

class Portfolio:
    def __init__(self):
        self.moneys = []

    def add(self, *moneys):
        self.moneys.extend(moneys)    

    def evaluate(self, currency):
        total = functools.reduce(
            # the 0 here (the last argument of reduce) is the initial value of the accumulator
            operator.add, map(lambda m: m.amount, self.moneys), 0)
        return Money(total, currency)

