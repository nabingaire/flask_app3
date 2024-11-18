import unittest
from pymongo import MongoClient
import os
from dotenv import load_dotenv


class DBWriteTest(unittest.TestCase):
    
    def setUp(self):
        load_dotenv()
        self.mongo_url = os.getenv('MONGODB_URL')
        self.client = MongoClient(self.mongo_url)
        self.db = self.client.get_database(os.getenv('MONGODB_DBNAME'))
        self.products_all = self.db.get_collection(os.getenv('MONGODB_COLLECTIONNAME'))
        
        
    def testInsertDocument(self):
        try:
            print("\nTesting DB write operation")
            testProduct = {
                "name": "samsung s26",
                "tag": "Electronics",
                "price": 1899.99,
                "image_path": "images/product1.jpg"
            }
            
            count = self.products_all.count_documents({})
            insertResult = self.products_all.insert_one(testProduct)
            finalCount = self.products_all.count_documents({})
            
            self.assertIsNotNone(insertResult, "Document insert failed!")
            self.assertEqual(finalCount, count+1, "Document insert failed!")
            self.products_all.delete_one({"_id":insertResult.inserted_id})
            
        finally:
            self.client.close()
            

if __name__=="__main__":
    unittest.main()