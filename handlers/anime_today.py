import datetime
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def anime_today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    today = datetime.datetime.now().strftime("%A").lower()
    url = f"https://api.jikan.moe/v4/schedules/{today}"
    res = requests.get(url)
    data = res.json()
    text = f"UwU~ Ini jadwal anime hari ini ({today.title()}), Onii-chan~\n\n"
    for anime in data['data'][:5]:
        text += f"• {anime['title']} - {anime['broadcast']['time'] or 'N/A'}\n"
    text += "\nJangan lupa nonton ya~!"

    keyboard = [[InlineKeyboardButton("Kembali ke Menu", callback_data="menu")]]
    await update.callback_query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))