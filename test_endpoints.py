#!flask/bin/python
import unittest
from fibonacci_app.app import app

class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_landing_page(self):
        """ Assert that users successfully lands on homepage """
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_help_page(self):
        """ Assert that users successfully lands on help page """
        response = self.app.get('/fib/help', follow_redirects=True)
        self.assertEqual(response.status_code, 202)
        self.assertIn('Will return all previously viewed', response.data)

    def test_get(self):
        """ Assert that users successfully grabs all previously computed values """
        response = self.app.get('/fib', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Previously calculated fibonaccis', response.data)

    def test_post(self):
        """ Assert that users can successfully calculate a new Fibonacci number """
        response = self.app.post('/fib', json=dict(position=4), follow_redirects=True)
        self.assertEqual(response.status_code, 201)

    def test_delete_found_value(self):
        """ Assert that users can successfully delete a Fibonacci number """
        self.app.post('/fib', json=dict(position=4), follow_redirects=True)
        self.app.post('/fib', json=dict(position=5), follow_redirects=True)
        response = self.app.delete('/fib/4')
        self.assertIn('Position 4 has been removed', response.data)
        self.assertEqual(response.status_code, 201)

    def test_delete_not_found_value(self):
        """ Assert that users can successfully delete a Fibonacci number """
        response = self.app.delete('/fib/4')
        self.assertIn('Sorry!', response.data)
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
