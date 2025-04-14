from telegram import Update
from telegram.ext import ContextTypes
from utils.waifu import get_waifu_image  # Untuk gambar waifu

# Menu utama /anime yang menampilkan pilihan untuk sub-perintah
async def anime_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Menu Anime:\n"
        "/anime info_anime - Informasi tentang anime\n"
        "/anime waifu - Gambar waifu\n"
    )
    await update.message.reply_text(text)

async def handle_anime_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menangani sub-perintah yang ada di bawah /anime."""
    if context.args:
        command = context.args[0].lower()

        if command == "info_anime":
            await info_anime(update, context)
        elif command == "waifu":
            await waifu_command(update, context)
        else:
            await update.message.reply_text("Perintah tidak dikenal. Gunakan `/anime info_anime` atau `/anime waifu`.")
    else:
        # Jika tidak ada argumen, tampilkan menu utama
        await anime_menu(update, context)

async def info_anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menampilkan informasi tentang anime tertentu."""
    if context.args[1:]:
        anime_name = " ".join(context.args[1:])
        info = f"Informasi tentang anime: {anime_name}"  # Ganti dengan logika yang sesuai
        await update.message.reply_text(info)
    else:
        await update.message.reply_text("Silakan sebutkan nama anime untuk mencari informasi!")

async def waifu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menampilkan gambar waifu berdasarkan mode (SFW atau NSFW)."""
    if len(context.args) > 1 and context.args[1].lower() == "nsfw":
        mode = "nsfw"
    else:
        mode = "sfw"
    
    # Ambil gambar waifu
    url = get_waifu_image(mode)
    if url:
        await update.message.reply_photo(photo=url, caption=f"Mode: {mode.upper()} | Waifu")
    else:
        await update.message.reply_text("Gagal mengambil gambar waifu.")