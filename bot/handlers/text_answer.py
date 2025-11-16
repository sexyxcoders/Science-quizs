# bot/handlers/text_answer.py
from pyrogram import Client, filters
from ..models.question_model import get_random_question
from ..models.user_model import update_score
from ..models.attempts_model import add_attempt

@Client.on_message(filters.text & ~filters.command)
async def text_answer(client, message):
    """
    Handles text answers sent by users.
    Compares with a random question (or last question if you implement session tracking).
    """
    user_id = message.from_user.id
    user_answer = message.text.strip()

    question = get_random_question()  # Replace with last active question per user for accuracy
    if not question:
        await message.reply_text("No active question found. Use /quiz to get a question.")
        return

    correct = question["answer"].lower() == user_answer.lower()
    if correct:
        update_score(user_id, 1)
        await message.reply_text("✅ Correct!")
    else:
        await message.reply_text(f"❌ Wrong! Correct answer: {question['answer']}")

    add_attempt(user_id, str(question["_id"]), correct)
