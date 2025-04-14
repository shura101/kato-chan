from telegram import Update
from telegram.ext import ContextTypes
from utils.waifu import get_waifu_image  # Untuk gambar waifu

async def anime_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menu utama /anime yang menampilkan pilihan untuk sub-perintah."""
    text = (
        "Menu Anime:\n"
        "/anime info_anime - Informasi tentang anime\n"
        "/anime waifu - Gambar waifu\n"
    )
    await update.message.reply_text(text)

async def info_anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menampilkan informasi tentang anime tertentu."""
    if context.args:
        anime_name = " ".join(context.args)
        # Dapatkan informasi anime dari API atau sumber lain
        info = f"Informasi tentang anime: {anime_name}"  # Ganti dengan logika yang sesuai
        await update.message.reply_text(info)
    else:
        await update.message.reply_text("Silakan sebutkan nama anime untuk mencari informasi!")

async def waifu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menampilkan gambar waifu berdasarkan mode (SFW atau NSFW)."""
    if len(context.args) > 0 and context.args[0].lower() == "nsfw":
        mode = "nsfw"
    else:
        mode = "sfw"
    
    # Ambil gambar waifu
    url = get_waifu_image(mode)
    if url:
        await update.message.reply_photo(photo=url, caption=f"Mode: {mode.upper()} | Waifu")
    else:
        await update.message.reply_text("Gagal mengambil gambar waifu.")