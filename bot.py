from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Anime", callback_data="menu_anime")],
        [InlineKeyboardButton("Crypto", callback_data="menu_crypto")],
        [InlineKeyboardButton("Coding", callback_data="menu_coding")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Halo, aku Kato Chan! Pilih menu di bawah ini:",
        reply_markup=reply_markup
    )

# Unknown message handler
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Maaf, aku tidak mengerti perintah itu. Ketik /start untuk melihat menu.")

# Main function
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.COMMAND, unknown))

    print("Kato Chan Bot is running...")
    app.run_polling()
