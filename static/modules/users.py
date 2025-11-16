# admin-panel/modules/users.py
from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "science_quiz_bot")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
users_col = db["users"]

def get_all_users():
    """
    Return a list of all users sorted by score descending.
    """
    return list(users_col.find().sort("score", -1))

def get_user(user_id):
    return users_col.find_one({"user_id": user_id})
