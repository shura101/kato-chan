from telegram import Update
from telegram.ext import ContextTypes

async def coding_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.edit_message_text("Fitur coding belum tersedia. Nantikan update selanjutnya!")