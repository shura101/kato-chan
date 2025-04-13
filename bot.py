import logging
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
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

def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Anime", callback_data="anime")],
        [InlineKeyboardButton("Crypto", callback_data="crypto")],
        [InlineKeyboardButton("Coding Help", callback_data="coding")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Welcome to Kato Chan Bot! Choose a feature:", reply_markup=reply_markup)

def anime(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Random Waifu", callback_data="waifu")],
        [InlineKeyboardButton("Back to Menu", callback_data="back_to_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.callback_query.message.edit_text("Anime Feature:\nChoose an option:", reply_markup=reply_markup)

def crypto(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Bitcoin Price", callback_data="bitcoin_price")],
        [InlineKeyboardButton("Back to Menu", callback_data="back_to_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.callback_query.message.edit_text("Crypto Feature:\nChoose an option:", reply_markup=reply_markup)

def coding(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Send Code for Error Check", callback_data="send_code")],
        [InlineKeyboardButton("Back to Menu", callback_data="back_to_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.callback_query.message.edit_text("Coding Help Feature:\nSend your code for error checking:", reply_markup=reply_markup)

def waifu(update: Update, context):
    response = requests.get(WAIFU_API_URL)
    image_url = response.json().get('url')
    update.callback_query.message.reply_photo(image_url)

def bitcoin_price(update: Update, context):
    response = requests.get(f"{COINGECKO_API_URL}/simple/price?ids=bitcoin&vs_currencies=usd")
    price = response.json().get('bitcoin', {}).get('usd', 'N/A')
    update.callback_query.message.reply_text(f"Current Bitcoin Price: ${price}")

def back_to_menu(update: Update, context):
    start(update, context)

def send_code(update: Update, context):
    update.callback_query.message.reply_text("Send your Python code, and I'll check for errors.")

def handle_message(update: Update, context):
    code = update.message.text
    try:
        exec(code)
        update.message.reply_text("Code executed successfully!")
    except Exception as e:
        update.message.reply_text(f"Error: {e}")

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(anime, pattern='^anime$'))
    dispatcher.add_handler(CallbackQueryHandler(crypto, pattern='^crypto$'))
    dispatcher.add_handler(CallbackQueryHandler(coding, pattern='^coding$'))
    dispatcher.add_handler(CallbackQueryHandler(waifu, pattern='^waifu$'))
    dispatcher.add_handler(CallbackQueryHandler(bitcoin_price, pattern='^bitcoin_price$'))
    dispatcher.add_handler(CallbackQueryHandler(back_to_menu, pattern='^back_to_menu$'))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
