import requests
from telegram import Update
from telegram.ext import ContextTypes

async def search_anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Ketik judul anime setelah /anime ya, contohnya: /anime Naruto")
        return
    query = " ".join(context.args)
    res = requests.get(f"https://api.jikan.moe/v4/anime?q={query}&limit=1")
    data = res.json()['data'][0]
    reply = f"*{data['title']}*\nSkor: {data['score']}\nEpisodes: {data['episodes']}\n{data['synopsis'][:300]}..."
    await update.message.reply_text(reply, parse_mode="Markdown")