import requests
from telegram import Update
from telegram.ext import ContextTypes

async def popular_anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    res = requests.get("https://api.jikan.moe/v4/top/anime")
    data = res.json()
    text = "Anime Populer Saat Ini:\n\n"
    for anime in data['data'][:5]:
        text += f"• {anime['title']} (Score: {anime['score']})\n"
    await update.callback_query.edit_message_text(text)