# bot/main.py
import os
from pyrogram import Client
from pyrogram.types import Message
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_ID = int(os.getenv("API_ID", "123456"))
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")

# Create Pyrogram Client
app = Client(
    "science_quiz_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Import handlers
from bot.handlers import start, quiz, callback, text_answer, user_stats
from bot.models.question_model import load_questions_from_file

# Load questions from JSON into MongoDB (run only once or if DB empty)
load_questions_from_file()

# Register handlers
app.add_handler(start)
app.add_handler(quiz)
app.add_handler(callback)
app.add_handler(text_answer)
app.add_handler(user_stats)

print("✅ Science Quiz Bot is starting...")

# Run the bot
app.run()
