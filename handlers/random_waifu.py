import requests
from telegram import Update
from telegram.ext import ContextTypes

async def random_waifu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    res = requests.get("https://api.waifu.pics/sfw/waifu")
    image_url = res.json()['url']
    await update.callback_query.edit_message_photo(photo=image_url, caption="Waifu acak untukmu.")