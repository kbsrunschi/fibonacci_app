#!flask/bin/python
import unittest
from fibonacci import Fibonacci

class TestFibonacciViewer(unittest.TestCase):
    def test_invalid_number(self):
        with self.assertRaises(SomeException) as cm:
            Fibonacci().calc_fib(-1)

        self.assertEqual(cm.exception.error_code, 404)

    def test_valid_number(self):
        self.assertEqual(Fibonacci().calc_fib(4), 3)
        self.assertEqual(Fibonacci().calc_fib(10), 3)


if __name__ == '__main__':
    unittest.main()
