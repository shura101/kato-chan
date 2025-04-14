from telegram import Update
from telegram.ext import ContextTypes
from utils.anilist import search_anime

async def anime_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Contoh: /anime naruto")
        return

    query = " ".join(context.args)
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