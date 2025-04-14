from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from utils.anilist import get_anime_info, get_anime_by_genre
from utils.waifu import fetch_random_waifu
from utils.quotes import fetch_random_quote


# Untuk tombol "🎬 Info Anime"
async def info_anime_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Ketik judul anime yang ingin kamu cari, misalnya: `Naruto`", parse_mode="Markdown")


# Untuk tombol "🎭 Genre Anime"
async def anime_genre_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Ketik nama genre, misalnya: `action`, `comedy`, atau `romance`.")


# Untuk tombol "👩‍🦰 Waifu Random"
async def waifu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    image_url = await fetch_random_waifu()
    await query.edit_message_media(
        media=InputMediaPhoto(media=image_url, caption="Waifumu telah dipanggil 💖")
    )


# Untuk tombol "🎉 Anime Quote"
async def anime_quote_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    quote_data = await fetch_random_quote()
    quote = f"_{quote_data['quote']}_\n\n~ *{quote_data['character']}* from *{quote_data['anime']}*"
    await query.edit_message_text(quote, parse_mode="Markdown")


# Untuk tombol "🔙 Kembali ke Menu Utama"
async def main_menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await anime_menu(update, context)
