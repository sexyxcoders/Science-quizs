# bot/handlers/start.py
from pyrogram import Client, filters
from ..models.user_model import create_user

@Client.on_message(filters.command("start"))
async def start(client, message):
    """
    Handles the /start command.
    Registers the user in the database if not already registered.
    Sends a welcome message with instructions.
    """
    # Create user in DB if not exists
    create_user(user_id=message.from_user.id, username=message.from_user.username)

    # Welcome message
    welcome_text = (
        "👋 Welcome to the Science Quiz Bot!\n\n"
        "You can test your science knowledge with random quizzes.\n\n"
        "Use the following commands:\n"
        "/quiz - Start a new quiz question\n"
        "/stats - View your personal score\n"
        "/leaderboard - View the top players\n"
    )

    await message.reply_text(welcome_text)
