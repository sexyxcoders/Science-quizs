# admin-panel/modules/broadcast.py
from pymongo import MongoClient
import os
from pyrogram import Client
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "science_quiz_bot")
BOT_TOKEN = os.getenv("BOT_TOKEN")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
users_col = db["users"]

# Pyrogram client for sending messages
bot = Client("broadcast_bot", bot_token=BOT_TOKEN)

def send_broadcast(message):
    """
    Send a message to all users in the database.
    """
    bot.start()
    users = list(users_col.find())
    for user in users:
        try:
            bot.send_message(user["user_id"], message)
        except:
            continue
    bot.stop()
