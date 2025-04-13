import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def genre_filter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Action", callback_data="genre_1"), InlineKeyboardButton("Romance", callback_data="genre_22")],
        [InlineKeyboardButton("Horror", callback_data="genre_14"), InlineKeyboardButton("Comedy", callback_data="genre_4")],
        [InlineKeyboardButton("Kembali ke Menu", callback_data="menu")]
    ]
    await update.callback_query.edit_message_text("Pilih genre yang kamu suka, Onii-chan~", reply_markup=InlineKeyboardMarkup(keyboard))

async def genre_result(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    genre_id = query.data.split("_")[1]
    res = requests.get(f"https://api.jikan.moe/v4/anime?genres={genre_id}&limit=5")
    data = res.json()
    text = "Nih anime-anime dari genre yang kamu pilih~\n\n"
    for anime in data['data']:
        text += f"• {anime['title']} ({anime['type']})\n"
    keyboard = [[InlineKeyboardButton("Kembali ke Genre", callback_data="genre_select")],
                [InlineKeyboardButton("Kembali ke Menu", callback_data="menu")]]
    await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))