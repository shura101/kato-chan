import logging
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from handlers.menu import start, handle_menu
from handlers.search_anime import search_anime
from handlers.nsfw import nsfw_command
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("anime", search_anime))
app.add_handler(CommandHandler("nsfw", nsfw_command))
app.add_handler(CallbackQueryHandler(handle_menu))

if __name__ == "__main__":
    print("Bot is running...")
    app.run_polling()