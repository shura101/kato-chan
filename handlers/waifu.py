import requests
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

async def send_waifu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    res = requests.get("https://api.waifu.pics/sfw/waifu")
    image = res.json()['url']
    keyboard = [[InlineKeyboardButton("Acak Lagi", callback_data="waifu")],
                [InlineKeyboardButton("Kembali ke Menu", callback_data="menu")]]
    await update.callback_query.edit_message_photo(photo=image, reply_markup=InlineKeyboardMarkup(keyboard))