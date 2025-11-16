# bot/handlers/callback.py
from pyrogram import Client
from pyrogram.types import CallbackQuery
from ..models.user_model import update_score
from ..models/attempts_model import add_attempt
from ..utils.db import questions_col

@Client.on_callback_query()
async def handle_callback(client: Client, callback_query: CallbackQuery):
    """
    Handles button clicks from quiz questions.
    Expects callback_data in format: "question_id|selected_option"
    """
    user_id = callback_query.from_user.id
    data = callback_query.data

    try:
        question_id, selected_option = data.split("|")
    except ValueError:
        await callback_query.answer("Invalid callback data.", show_alert=True)
        return

    # Fetch the question from DB
    question = questions_col.find_one({"_id": question_id})
    if not question:
        await callback_query.answer("❌ Question not found.", show_alert=True)
        return

    correct = question["answer"] == selected_option

    # Update score if correct
    if correct:
        update_score(user_id, 1)
        await callback_query.answer("✅ Correct!", show_alert=True)
    else:
        await callback_query.answer(f"❌ Wrong! Correct answer: {question['answer']}", show_alert=True)

    # Record the attempt
    add_attempt(user_id, question_id, correct)

    # Optionally, you can send the next question automatically
    # next_question = get_random_question()
    # if next_question:
    #     await callback_query.message.reply_text(format_question(next_question))
