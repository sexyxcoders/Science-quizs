# bot/models/question_model.py
from ..utils.db import questions_col
import json
import os

def add_question(question, options, answer, category="General"):
    """
    Add a question to MongoDB.
    """
    questions_col.insert_one({
        "question": question,
        "options": options,
        "answer": answer,
        "category": category
    })

def get_random_question():
    """
    Get a random question from MongoDB.
    """
    pipeline = [{"$sample": {"size": 1}}]
    result = list(questions_col.aggregate(pipeline))
    return result[0] if result else None

def get_all_questions():
    """
    Return all questions from DB.
    """
    return list(questions_col.find())

def load_questions_from_file(file_path=None):
    """
    Load questions from a JSON file into MongoDB.
    """
    file_path = file_path or os.path.join(os.path.dirname(__file__), "../data/_questions.json")
    with open(file_path, "r") as f:
        questions = json.load(f)
        for q in questions:
            add_question(q["question"], q["options"], q["answer"], q.get("category", "General"))
