import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def popular_anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    res = requests.get("https://api.jikan.moe/v4/top/anime")
    data = res.json()
    text = "Nih anime paling populer sekarang, Onii-chan~ \n\n"
    for i, anime in enumerate(data['data'][:5], start=1):
        text += f"{i}. {anime['title']} ⭐ (Score: {anime['score']})\n"
    text += "\nYang mana favoritmu~?"

    keyboard = [[InlineKeyboardButton("Kembali ke Menu", callback_data="menu")]]
    await update.callback_query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))