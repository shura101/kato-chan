from telegram import Update
from telegram.ext import ContextTypes

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Maaf, aku tidak mengerti perintah itu. Ketik /start untuk melihat menu.")