from telegram import Update
from telegram.ext import ContextTypes

async def crypto_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Fitur crypto belum tersedia. Nantikan update selanjutnya!")