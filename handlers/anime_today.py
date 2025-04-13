import datetime
import requests
from telegram import Update
from telegram.ext import ContextTypes

async def anime_today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    today = datetime.datetime.now().strftime("%A").lower()
    url = f"https://api.jikan.moe/v4/schedules/{today}"
    res = requests.get(url)
    data = res.json()
    text = f"Jadwal Anime Hari Ini ({today.title()}):\n\n"
    for anime in data['data'][:5]:
        text += f"• {anime['title']} - {anime['broadcast']['time'] or 'N/A'}\n"
    await update.callback_query.edit_message_text(text)