import logging
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ANILIST_API_URL = os.getenv("ANILIST_API_URL")
COINGECKO_API_URL = os.getenv("COINGECKO_API_URL")
WAIFU_API_URL = os.getenv("WAIFU_API_URL")

# Set up logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Anime", callback_data="anime")],
        [InlineKeyboardButton("Crypto", callback_data="crypto")],
        [InlineKeyboardButton("Coding Help", callback_data="coding")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to Kato Chan Bot! Choose a feature:", reply_markup=reply_markup)

async def anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Random Waifu", callback_data="waifu")],
        [InlineKeyboardButton("Back to Menu", callback_data="back_to_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.edit_text("Anime Feature:\nChoose an option:", reply_markup=reply_markup)

async def crypto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Bitcoin Price", callback_data="bitcoin_price")],
        [InlineKeyboardButton("Back to Menu", callback_data="back_to_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.edit_text("Crypto Feature:\nChoose an option:", reply_markup=reply_markup)

async def coding(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Send Code for Error Check", callback_data="send_code")],
        [InlineKeyboardButton("Back to Menu", callback_data="back_to_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.edit_text("Coding Help Feature:\nSend your code for error checking:", reply_markup=reply_markup)

async def waifu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get(WAIFU_API_URL)
    image_url = response.json().get('url')
    await update.callback_query.message.reply_photo(image_url)

async def bitcoin_price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get(f"{COINGECKO_API_URL}/simple/price?ids=bitcoin&vs_currencies=usd")
    price = response.json().get('bitcoin', {}).get('usd', 'N/A')
    await update.callback_query.message.reply_text(f"Current Bitcoin Price: ${price}")

async def back_to_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)

async def send_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.message.reply_text("Send your Python code, and I'll check for errors.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = update.message.text
    try:
        exec(code)
        await update.message.reply_text("Code executed successfully!")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(anime, pattern='^anime$'))
    application.add_handler(CallbackQueryHandler(crypto, pattern='^crypto$'))
    application.add_handler(CallbackQueryHandler(coding, pattern='^coding$'))
    application.add_handler(CallbackQueryHandler(waifu, pattern='^waifu$'))
    application.add_handler(CallbackQueryHandler(bitcoin_price, pattern='^bitcoin_price$'))
    application.add_handler(CallbackQueryHandler(back_to_menu, pattern='^back_to_menu$'))
    application.add_handler(CallbackQueryHandler(send_code, pattern='^send_code$'))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()
