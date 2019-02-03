#!flask/bin/python
import unittest
from fibonacci import Fibonacci

class TestFibonacciViewer(unittest.TestCase):
    def test_valid_number(self):
        self.assertEqual(Fibonacci().calc_fib(4), 3)
        self.assertEqual(Fibonacci().calc_fib(10), 55)


if __name__ == '__main__':
    unittest.main()
