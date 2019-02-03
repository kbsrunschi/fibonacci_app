#!flask/bin/python
from flask import abort

class Fibonacci:
    def __init__(self):
        self._cache = {}

    def calc_fib(self, n):
        if n in self._cache:
            return self._cache[n]
        elif n < 0:
            return 0
        elif n > 1:
            return self._cache.setdefault(n, self.calc_fib(n-1) + self.calc_fib(n-2))
        return n
