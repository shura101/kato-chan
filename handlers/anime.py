from telegram import Update
from telegram.ext import ContextTypes
from utils.anilist import search_anime
from utils.waifu import get_waifu_image

async def anime_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        text = (
            "Menu Anime:\n\n"
            "/anime cari <judul> - Cari info anime\n"
            "/anime waifu [nsfw] - Kirim gambar waifu (safe/nsfw)"
        )
        await update.message.reply_text(text)
        return

    subcommand = context.args[0].lower()

    if subcommand == "cari":
        if len(context.args) < 2:
            await update.message.reply_text("Contoh: /anime cari naruto")
            return
        query = " ".join(context.args[1:])
        result = search_anime(query)
        if result:
            desc = result["description"].replace("<br>", "\n").replace("&quot;", "\"")
            text = (
                f"**{result['title']}**\n"
                f"Episodes: {result['episodes']}\n"
                f"Score: {result['score']}\n\n"
                f"{desc[:500]}...\n"
                f"[Anilist Page]({result['url']})"
            )
            await update.message.reply_text(text, parse_mode="Markdown")
        else:
            await update.message.reply_text("Anime tidak ditemukan.")
    
    elif subcommand == "waifu":
        mode = "sfw"
        if len(context.args) > 1 and context.args[1].lower() == "nsfw":
            mode = "nsfw"
        image_url = get_waifu_image(mode)
        if image_url:
            await update.message.reply_photo(photo=image_url, caption=f"Mode: {mode.upper()} | Category: waifu")
        else:
            await update.message.reply_text("Gagal mengambil gambar waifu.")
    
    else:
        await update.message.reply_text("Subcommand tidak dikenal. Ketik /anime untuk melihat daftar fitur.")