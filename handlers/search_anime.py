from telegram import Update
from telegram.ext import ContextTypes

async def search_anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Fitur cari anime sedang dikembangkan, ya~")