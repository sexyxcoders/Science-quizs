# admin-panel/modules/categories.py
from pymongo import MongoClient
import os
from bson.objectid import ObjectId

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "science_quiz_bot")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
categories_col = db["categories"]

def get_categories():
    return list(categories_col.find())

def add_category(name):
    categories_col.insert_one({"name": name})

def edit_category(cid, name):
    categories_col.update_one({"_id": ObjectId(cid)}, {"$set": {"name": name}})

def delete_category(cid):
    categories_col.delete_one({"_id": ObjectId(cid)})
