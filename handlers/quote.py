import requests
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

async def anime_quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    res = requests.get("https://animechan.xyz/api/random")
    data = res.json()
    quote = f'"{data["quote"]}"\n- {data["character"]} ({data["anime"]})'
    keyboard = [[InlineKeyboardButton("Lagi dong!", callback_data="quote")],
                [InlineKeyboardButton("Kembali ke Menu", callback_data="menu")]]
    await update.callback_query.edit_message_text(quote, reply_markup=InlineKeyboardMarkup(keyboard))