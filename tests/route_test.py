import unittest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import app
from app import app  

class RouteTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_invalid_method(self):
        print("\nTesting invalid POST route; should return 405 HTTP code")
        response = self.client.post('/products')  
        self.assertEqual(response.status_code, 405)
   
    def test_valid_method(self):
        print("\nTesting valid GET route; should return 200 HTTP code")
        response = self.client.get('/products')  
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()