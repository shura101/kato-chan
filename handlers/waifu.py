from telegram import Update
from telegram.ext import ContextTypes
from utils.waifu import get_waifu_image  # Mengimpor fungsi get_waifu_image
import aiohttp

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

async def fetch_random_waifu():
    url = "https://api.waifu.pics/sfw/waifu"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                return data["url"]
            else:
                return "https://media.tenor.com/f0uvs96FfXsAAAAd/waifu-anime.gif"  # fallback