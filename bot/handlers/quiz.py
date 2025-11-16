# bot/handlers/quiz.py
from pyrogram import Client, filters
from ..models.user_model import get_user
from ..models.question_model import get_random_question
from ..utils.helpers import format_question, shuffle_options
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.command("quiz"))
async def quiz(client, message):
    """
    Handles the /quiz command.
    Sends a random science question with inline buttons for options.
    """
    user = get_user(message.from_user.id)
    if not user:
        await message.reply_text("Please use /start first to register.")
        return

    # Get a random question from DB
    question = get_random_question()
    if not question:
        await message.reply_text("No questions available at the moment.")
        return

    # Shuffle options
    options = shuffle_options(question["options"])

    # Build inline keyboard for options
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(opt, callback_data=f"{str(question['_id'])}|{opt}")]
            for opt in options
        ]
    )

    # Send question text with buttons
    await message.reply_text(
        format_question({"question": question["question"], "options": options}),
        reply_markup=keyboard
    )
