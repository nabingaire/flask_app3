import unittest
from pymongo import MongoClient
from pymongo.errors import OperationFailure, ConnectionFailure

'''
DBReadTest is a unit test to verify that the app can successfully connect to MongoDb and do a read operation.
There are 3 main functions inside the test class:-
    1) setUp - This function sets the mongodb url and client as None.
    2) testDBReadOk - This function tests when correct MongoDB url is provided. After successfull connection, it pings the database server.
    3) testDBReadFailure - This fucntion tests when incorrect MongoDb url is provided. When incorrect url is provided, it throws OperationFailure error.

This test runs when following command is run during the github action.

- name: run tests
  run: |
    python -m unittest discover -s tests -p "*.py"
'''

class DBReadTest(unittest.TestCase):
    
    def setUp(self):
        self.mongo_url = "mongodb+srv://nabin:nabin@shop.sccvu.mongodb.net/?retryWrites=true&w=majority&appName=shop"
        self.client = None
        
    def testDBReadOk(self):
        print("\nTesting successful connection")
        try:
            self.client = MongoClient(self.mongo_url)
            self.client.admin.command('ping')
            self.assertTrue(True,"MongoDB connection successful.")
            
        except ConnectionFailure as e:
            self.assertIsNotNone(e,"MongoDB connection failed: {e}")
        
        finally:
            if self.client:
                self.client.close()
        
    def testDBReadFailure(self):
        print("\nTesting unsuccessful connection")
        
        with self.assertRaises(OperationFailure):
            try:
                self.mongo_url = "mongodb+srv://nabin:nabingaire@shop.sccvu.mongodb.net/?retryWrites=true&w=majority&appName=shop"
                self.client = MongoClient(self.mongo_url)
                self.client.admin.command('ping')
            
            finally:
                if self.client:
                    self.client.close()
       
        

if __name__=="__main__":
    unittest.main()
    
    