from telegram import Update
from telegram.ext import ContextTypes

async def anime_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Fitur anime belum tersedia. Nantikan update selanjutnya!")