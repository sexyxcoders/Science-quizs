# bot/models/attempts_model.py
from ..utils.db import attempts_col

def add_attempt(user_id, question_id, correct):
    """
    Record an attempt for a user.
    """
    attempts_col.insert_one({
        "user_id": user_id,
        "question_id": question_id,
        "correct": correct
    })

def get_user_attempts(user_id):
    """
    Get all attempts made by a user.
    """
    return list(attempts_col.find({"user_id": user_id}))
