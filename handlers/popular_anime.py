from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

async def popular_anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "Fitur Anime Populer sedang disiapkan~"
    keyboard = [[InlineKeyboardButton("Kembali ke Menu", callback_data="menu")]]
    await update.callback_query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))