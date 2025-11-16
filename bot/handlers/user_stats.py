# bot/handlers/user_stats.py
from pyrogram import Client, filters
from ..models.user_model import get_user, get_leaderboard

@Client.on_message(filters.command("stats"))
async def stats(client, message):
    """
    Shows the user's own score and attempts.
    """
    user = get_user(message.from_user.id)
    if not user:
        await message.reply_text("Please use /start first to register.")
        return

    text = (
        f"📊 Your Stats:\n"
        f"Score: {user.get('score', 0)}\n"
        f"Attempts: {user.get('attempts', 0)}"
    )
    await message.reply_text(text)

@Client.on_message(filters.command("leaderboard"))
async def leaderboard(client, message):
    """
    Shows top 10 users by score.
    """
    leaderboard_data = get_leaderboard()
    if not leaderboard_data:
        await message.reply_text("No leaderboard data yet.")
        return

    text = "🏆 Leaderboard:\n"
    for idx, u in enumerate(leaderboard_data, start=1):
        text += f"{idx}. {u.get('username', 'Unknown')} - {u.get('score', 0)} pts\n"

    await message.reply_text(text)