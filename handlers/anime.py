from telegram import Update
from telegram.ext import ContextTypes
from utils.anilist import get_anime_info
from utils.waifu import get_waifu_image

async def anime_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Menu Anime:\n"
        "/info_anime <judul> - Info anime berdasarkan judul\n"
        "/waifu - Gambar waifu acak\n" 
        "/menu - Kembali ke menu awal"
    )
    await update.message.reply_text(text)

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