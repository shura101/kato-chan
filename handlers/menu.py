from telegram import Update
from telegram.ext import ContextTypes

async def back_to_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Kembali ke menu utama:\n\n"
        "/anime - Fitur seputar anime\n"
        "/crypto - Harga & info crypto\n"
        "/coding - Bantu deteksi error coding"
    )
    await update.message.reply_text(text)