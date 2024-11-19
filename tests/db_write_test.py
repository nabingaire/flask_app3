import unittest
from pymongo import MongoClient

'''
DBWriteTest is a unit test to verify that the app can successfully connect to MongoDb and do a write operation.
There are 2 main functions inside the test class:-
    1) setUp - This function sets the mongodb url, client, db object and collection object.
    2) testInsertDocument - This function tests the insertion of new document. First a test document is created.
        Before inserting total dccuments are counted. After inserting total document is counted.
        It is then asserted that before count +1 equals after count.
        Likewise, the databse is again queried to find the newly inserted document and asserted if the result is None.
        After assertions , the newly inserted document is deleted since it is for testing purpose only.

This test runs when following command is run during the github action.

- name: run tests
  run: |
    python -m unittest discover -s tests -p "*.py"
'''

class DBWriteTest(unittest.TestCase):
    
    def setUp(self):
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
            
            insertedData = self.products_all.find_one(testProduct)
            self.assertIsNotNone(insertedData,"Inserted document not found")
            self.assertEqual(insertedData["name"],testProduct["name"],"Inserted document name doesnot match")
            
            self.products_all.delete_one({"_id":insertResult.inserted_id})
            
        finally:
            self.client.close()
            

if __name__=="__main__":
    unittest.main()