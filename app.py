from flask import Flask, request, render_template
from datetime import date
# load mongodb pachage
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
import pymongo

#load env file
from dotenv import load_dotenv
load_dotenv() #load the env file

MONGO_URL = os.getenv('MONGO_URL') # assign the URL to a variable
client = pymongo.MongoClient(MONGO_URL)  # create a MongoClient object using the URL



db = client.test_database # create or access a database named 'test_database'
collection = db['chetana_collection'] # create or access a collection named 'chetana_collection' within the 'test_database'

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods = ['POST'])
def login_page():
    login_data = dict(request.form)
    collection.insert_one(login_data) # insert the login data into the MongoDB collection
    return 'data posted successfully'

@app.route('/view')
def view_data():
    data = collection.find() # retrieve all documents from the MongoDB collection
    data = list(data) # convert the cursor object to a list of documents
    for item in data:
        print(item) 
        del item['_id'] # remove the '_id' field from each document
    data = {
        'data' : data
    }
    return data
if __name__ == '__main__':
    app.run(port = 8080, debug=True)