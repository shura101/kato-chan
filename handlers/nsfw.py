from telegram import Update
from telegram.ext import ContextTypes
import requests

ALLOWED_USERS = ["your_telegram_id"]

async def nsfw_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    if user_id not in ALLOWED_USERS:
        await update.message.reply_text("Fitur ini rahasia dan hanya untuk pemilik bot~")
        return
    res = requests.get("https://api.waifu.pics/nsfw/waifu")
    await update.message.reply_photo(res.json()["url"], caption="Hush~ ini rahasia ya...")