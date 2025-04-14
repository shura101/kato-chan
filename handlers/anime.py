from telegram import Update
from telegram.ext import ContextTypes
from utils.anilist import get_anime_info
from utils.waifu import get_waifu_image
from utils.anilist import get_anime_by_genre
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

async def anime_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🎬 Info Anime", callback_data="info_anime"),
            InlineKeyboardButton("🎭 Genre Anime", callback_data="anime_genre"),
        ],
        [
            InlineKeyboardButton("👩‍🦰 Waifu Random", callback_data="waifu"),
            InlineKeyboardButton("🎉 Anime Quote", callback_data="anime_quote"),
        ],
        [
            InlineKeyboardButton("🔙 Kembali ke Menu Utama", callback_data="main_menu")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Pilih fitur anime yang ingin kamu jelajahi:", reply_markup=reply_markup)

async def info_anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        title = " ".join(context.args)
        anime = get_anime_info(title)
        if anime:
            response = (
                f"**{anime['title']['romaji']}** ({anime['title']['english']})\n"
                f"Episodes: {anime['episodes']}\n"
                f"Status: {anime['status']}\n"
                f"Score: {anime['averageScore']}%\n"
                f"[Lihat di Anilist]({anime['siteUrl']})"
            )
            await update.message.reply_text(response, parse_mode="Markdown")
        else:
            await update.message.reply_text("Anime tidak ditemukan.")
    else:
        await update.message.reply_text("Contoh: /info_anime naruto")

async def waifu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_url = get_waifu_image(nsfw=False)
    if image_url:
        await update.message.reply_photo(photo=image_url, caption="Waifu hari ini (≧∇≦)/")
    else:
        await update.message.reply_text("Gagal mengambil gambar waifu.")

async def anime_genre(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Contoh penggunaan: `/genre action`", parse_mode='Markdown')
        return

    genre = " ".join(context.args)
    msg = await get_anime_by_genre(genre)
    await update.message.reply_text(msg, parse_mode='Markdown', disable_web_page_preview=True)