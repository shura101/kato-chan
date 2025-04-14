from telegram import Update
from telegram.ext import ContextTypes

async def coding_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Fitur coding belum tersedia. Nantikan update selanjutnya!")