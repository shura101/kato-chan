from telegram import Update
from telegram.ext import ContextTypes

async def crypto_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.edit_message_text("Fitur crypto belum tersedia. Nantikan update selanjutnya!")