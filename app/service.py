from flask import Flask, request, jsonify
from pymongo import MongoClient
import bcrypt
from app import users_collection
from mongoDB_URL import mongoDB_URL

app = Flask(__name__)
client = MongoClient(mongoDB_URL())
db = client["mydatabase"]
users_collection = db["Test"]

@app.route('/')
def home():
    return "Welcome to the page"

@app.route('/register', methods=["POST", "GET"])
def register_user():
  if request.method == "POST":
    phone_number = request.form("phone_number")
    pin = request.form("pin")

    hashed = bcrypt.hashpw(pin.encode('utf-8'), bcrypt.gensalt())
    user_data = {"phone_nuber":phone_number, "pin":hashed}
    for user_info in users_collection:
      if user_data in user_info:
        return "User already exist"

      else:
        user = users_collection.insert_one(user_data)
        return jsonify(user)



@app.route('/validate/<int:phone_number>/<int:pin>', methods=['GET'])
def validate_old_pin(phone_number,pin):
  user = users_collection.find_one({"phone_number":phone_number})

  if user:
    if user["pin"] == pin:
      return True

    else:
      return False

  else:
    return False

@app.route('/register/<int:pin>', methods = ['GET'])
def lock_account(pin):
  if request.method == 'GET':
    for user in users_collection:
      if user["pin"] != pin:
    # Update the user document to set the "account_status" field to "locked"
        users_collection.update_one({"pin": pin}, {"$set": {"account_status": "locked"}})


client.close()   