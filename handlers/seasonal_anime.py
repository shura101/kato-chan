import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import datetime

async def seasonal_anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    season = "winter" if month <= 3 else "spring" if month <= 6 else "summer" if month <= 9 else "fall"
    res = requests.get(f"https://api.jikan.moe/v4/seasons/{year}/{season}")
    data = res.json()
    text = f"Nih anime musiman {season.title()} {year}, Onii-chan~\n\n"
    for anime in data['data'][:5]:
        text += f"• {anime['title']} ({anime['type']})\n"
    text += "\nJangan sampai ketinggalan yaa~"

    keyboard = [[InlineKeyboardButton("Kembali ke Menu", callback_data="start")]]
    await update.callback_query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))