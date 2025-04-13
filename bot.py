from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os

from handlers.anime_today import anime_today
from handlers.random_waifu import random_waifu
from handlers.anime_quote import anime_quote
from handlers.popular_anime import popular_anime
from handlers.search_anime import search_anime
from handlers.seasonal_anime import seasonal_anime
from handlers.genre_filter import genre_filter, genre_result

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Anime Hari Ini", callback_data='anime_today')],
        [InlineKeyboardButton("Cari Anime", switch_inline_query_current_chat='/anime')],
        [InlineKeyboardButton("Random Waifu", callback_data='random_waifu')],
        [InlineKeyboardButton("Quote Anime", callback_data='anime_quote')],
        [InlineKeyboardButton("Anime Populer", callback_data='popular_anime')],
        [InlineKeyboardButton("Anime Musiman", callback_data='seasonal')],
        [InlineKeyboardButton("Filter Genre", callback_data='genre_select')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Halo~ Aku Kato Chan, siap bantu cari anime untukmu, Onii-chan~ UwU", reply_markup=reply_markup)

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
    elif data == 'seasonal':
        await seasonal_anime(update, context)
    elif data == 'genre_select':
        await genre_filter(update, context)
    elif data.startswith('genre_'):
        await genre_result(update, context)
    elif data == 'start':
        await start(update, context)

async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ehhh? Kato gak ngerti maksud Onii-chan… Coba ketik /start ya~")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("anime", search_anime))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.COMMAND, unknown_command))
    app.run_polling()