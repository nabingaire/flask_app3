import unittest
import os
from pymongo import MongoClient
from pymongo.errors import OperationFailure, ConnectionFailure
from dotenv import load_dotenv

class DBReadTest(unittest.TestCase):
    
    def setUp(self):
        load_dotenv()
        self.mongo_url = os.getenv('MONGODB_URL')
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
                self.mongo_url = os.getenv('MONGODB_URL2')
                self.client = MongoClient(self.mongo_url)
                self.client.admin.command('ping')
            
            finally:
                if self.client:
                    self.client.close()
       
        

if __name__=="__main__":
    unittest.main()
    
    