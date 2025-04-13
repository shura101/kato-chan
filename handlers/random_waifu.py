import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def random_waifu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    res = requests.get("https://api.waifu.pics/sfw/waifu")
    image_url = res.json()['url']
    keyboard = [
        [InlineKeyboardButton("Acak Lagi!", callback_data="random_waifu")],
        [InlineKeyboardButton("Kembali ke Menu", callback_data="menu")]
    ]
    await update.callback_query.edit_message_photo(photo=image_url, caption="Onii-chan~ ini waifumu hari ini~ UwU", reply_markup=InlineKeyboardMarkup(keyboard))