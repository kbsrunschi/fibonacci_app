#!flask/bin/python
class Fibonacci(object):
    """ Simple class to calculate a Fibonnaci number """
    def __init__(self):
        self._cache = {}

    def calc_fib(self, position):
        """ Calculate the fibonnaci number for a given position in the sequence """
        if position in self._cache:
            return self._cache[position]
        elif position < 0:
            return 0
        elif position > 1:
            return self._cache.setdefault(position, self.calc_fib(position-1) + self.calc_fib(position-2))
        return position
