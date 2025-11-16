# bot/utils/db.py
from pymongo import MongoClient
import os

# MongoDB connection URI
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "science_quiz_bot")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Collections
users_col = db["users"]
questions_col = db["questions"]
attempts_col = db["attempts"]