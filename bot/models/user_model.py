# bot/models/user_model.py
from ..utils.db import users_col

def create_user(user_id, username):
    """
    Create a new user if not exists.
    """
    if not users_col.find_one({"user_id": user_id}):
        users_col.insert_one({
            "user_id": user_id,
            "username": username,
            "score": 0,
            "attempts": 0
        })

def update_score(user_id, points):
    """
    Increment user score and attempts.
    """
    users_col.update_one(
        {"user_id": user_id},
        {"$inc": {"score": points, "attempts": 1}}
    )

def get_user(user_id):
    """
    Retrieve user document from DB.
    """
    return users_col.find_one({"user_id": user_id})

def get_leaderboard(limit=10):
    """
    Return top users sorted by score descending.
    """
    return list(users_col.find().sort("score", -1).limit(limit))
