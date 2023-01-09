import os
from flask import Flask, jsonify, request
from pymongo import MongoClient



# from flask_pymongo import PyMongo

# Initialize application
app = Flask(__name__)



#Initialize db
client = MongoClient("mongodb+srv://Nnadi-Samson:modonyebuchi@cluster0.5qs5vm3.mongodb.net/?retryWrites=true&w=majority")
db = client["mydatabase"]
users_collection = db["Test"]


# Import the application webservice
from app import service, error