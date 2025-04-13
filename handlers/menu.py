from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Anime Hari Ini", callback_data="today_anime")],
        [InlineKeyboardButton("Anime Populer", callback_data="popular_anime")],
        [InlineKeyboardButton("Cari Anime", callback_data="search")],
        [InlineKeyboardButton("Waifu", callback_data="waifu")],
        [InlineKeyboardButton("Quote", callback_data="quote")],
        [InlineKeyboardButton("Genre", callback_data="genre")],
        [InlineKeyboardButton("Kembali ke Menu", callback_data="menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Hai, aku Kato Chan~ Mau cari apa hari ini?", reply_markup=reply_markup)

async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    if data == "menu":
        await start(update, context)
    elif data == "today_anime":
        from .today_anime import today_anime
        await today_anime(update, context)
    elif data == "popular_anime":
        from .popular_anime import popular_anime
        await popular_anime(update, context)
    elif data == "waifu":
        from .waifu import send_waifu
        await send_waifu(update, context)
    elif data == "quote":
        from .quote import anime_quote
        await anime_quote(update, context)
    elif data == "genre":
        from .genre import genre_menu
        await genre_menu(update, context)
    elif data.startswith("genre_"):
        from .genre import genre_result
        await genre_result(update, context)