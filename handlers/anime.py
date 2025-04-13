from telegram import Update
from telegram.ext import ContextTypes

async def anime_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.edit_message_text("Fitur anime belum tersedia. Nantikan update selanjutnya!")