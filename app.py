from flask import Flask,render_template
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

MONGODB_URL = os.getenv('MONGODB_URL2')

client = MongoClient(MONGODB_URL,server_api=ServerApi('1'))

MONGODB_DBNAME = os.getenv('MONGODB_DBNAME')
MONGODB_COLLECTION = os.getenv('MONGODB_COLLECTIONNAME')
db = client.get_database(MONGODB_DBNAME)
products_all = db.get_collection(MONGODB_COLLECTION)

@app.route('/')
def home():  # put application's code
    return render_template('home.html')

@app.route('/products')
def products():
        products = list(products_all.find())  # put application's code here
        return render_template('products.html', products=products)


if __name__ == '__main__':

    app.run()
