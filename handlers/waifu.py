from telegram import Update
from telegram.ext import ContextTypes
from utils.waifu import get_waifu_image  # Mengimpor fungsi get_waifu_image

async def waifu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Periksa apakah mode NSFW diminta
    if len(context.args) > 0 and context.args[0].lower() == "nsfw":
        mode = "nsfw"
    else:
        mode = "sfw"
    
    # Ambil gambar waifu dari API
    url = get_waifu_image(mode)
    if url:
        await update.message.reply_photo(photo=url, caption=f"Mode: {mode.upper()} | Waifu")
    else:
        await update.message.reply_text("Gagal mengambil gambar waifu.")