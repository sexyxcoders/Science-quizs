# admin-panel/modules/questions.py
from pymongo import MongoClient
import os
from bson.objectid import ObjectId

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "science_quiz_bot")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
questions_col = db["questions"]

def get_questions(qid=None):
    if qid:
        return questions_col.find_one({"_id": ObjectId(qid)})
    return list(questions_col.find())

def add_question(question, options, answer, category="General"):
    questions_col.insert_one({
        "question": question,
        "options": options,
        "answer": answer,
        "category": category
    })

def edit_question(qid, question, options, answer, category="General"):
    questions_col.update_one(
        {"_id": ObjectId(qid)},
        {"$set": {"question": question, "options": options, "answer": answer, "category": category}}
    )

def delete_question(qid):
    questions_col.delete_one({"_id": ObjectId(qid)})
