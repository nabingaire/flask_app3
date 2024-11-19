import unittest
from pymongo import MongoClient
import os
from dotenv import load_dotenv


class DBWriteTest(unittest.TestCase):
    
    def setUp(self):
        load_dotenv()
        self.mongo_url = "mongodb+srv://nabin:nabin@shop.sccvu.mongodb.net/?retryWrites=true&w=majority&appName=shop"
        self.client = MongoClient(self.mongo_url)
        self.db = self.client.get_database('shop_db')
        self.products_all = self.db.get_collection('products')
        
        
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