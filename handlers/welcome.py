from telegram import Update
from telegram.ext import ContextTypes

async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.chat_member.new_chat_members:
        await update.effective_chat.send_message(f"Selamat datang, {member.full_name}!")