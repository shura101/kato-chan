from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os

from handlers.anime_today import anime_today
from handlers.random_waifu import random_waifu
from handlers.anime_quote import anime_quote
from handlers.popular_anime import popular_anime
from handlers.search_anime import search_anime

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Anime Hari Ini", callback_data='anime_today')],
        [InlineKeyboardButton("Cari Anime", switch_inline_query_current_chat='')],
        [InlineKeyboardButton("Random Waifu", callback_data='random_waifu')],
        [InlineKeyboardButton("Quote Anime", callback_data='anime_quote')],
        [InlineKeyboardButton("Anime Populer", callback_data='popular_anime')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Selamat datang di Kato Chan Bot!", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == 'anime_today':
        await anime_today(update, context)
    elif data == 'random_waifu':
        await random_waifu(update, context)
    elif data == 'anime_quote':
        await anime_quote(update, context)
    elif data == 'popular_anime':
        await popular_anime(update, context)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("anime", search_anime))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()