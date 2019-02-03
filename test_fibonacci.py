#!flask/bin/python
import unittest
from fibonacci import Fibonacci

class TestFibonacciViewer(unittest.TestCase):
    def test_valid_number(self):
        self.assertEqual(Fibonacci().calc_fib(4), 3)
        self.assertEqual(Fibonacci().calc_fib(10), 55)

    def test_base_case(self):
        self.assertEqual(Fibonacci().calc_fib(0), 0)
        self.assertEqual(Fibonacci().calc_fib(1), 1)

    def test_negative_number(self):
        self.assertEqual(Fibonacci().calc_fib(-1), 0)

if __name__ == '__main__':
    unittest.main()
