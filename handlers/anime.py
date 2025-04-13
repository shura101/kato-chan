import requests
from telegram import Update
from telegram.ext import ContextTypes

API_BASE = "https://api.jikan.moe/v4"

async def animeinfo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Gunakan format: /animeinfo <judul anime>")
        return

    query = " ".join(context.args)
    url = f"{API_BASE}/anime?q={query}&limit=1"
    response = requests.get(url).json()

    if response.get("data"):
        anime = response["data"][0]
        title = anime["title"]
        synopsis = anime.get("synopsis", "Tidak ada sinopsis.")
        rating = anime.get("rating", "N/A")
        score = anime.get("score", "N/A")
        image_url = anime["images"]["jpg"]["image_url"]

        msg = f"*{title}*\nRating: {rating}\nSkor: {score}\n\n{synopsis}"
        await update.message.reply_photo(photo=image_url, caption=msg, parse_mode="Markdown")
    else:
        await update.message.reply_text("Anime tidak ditemukan.")

async def jadwalanime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from datetime import datetime
    hari = datetime.now().strftime('%A').lower()
    url = f"{API_BASE}/schedules?filter={hari}"
    response = requests.get(url).json()

    if response.get("data"):
        daftar = response["data"][:5]  # tampilkan 5 anime pertama
        msg = f"Jadwal rilis anime hari ini ({hari.title()}):\n\n"
        for anime in daftar:
            msg += f"• {anime['title']}\n"
        await update.message.reply_text(msg)
    else:
        await update.message.reply_text("Tidak ada data jadwal hari ini.")

async def waifu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    res = requests.get("https://api.waifu.pics/sfw/waifu").json()
    await update.message.reply_photo(photo=res["url"], caption="Waifumu siap menemani, Tuan Andre!")

async def quoteanime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    res = requests.get("https://animechan.xyz/api/random").json()
    quote = res.get("quote")
    character = res.get("character")
    anime = res.get("anime")

    if quote and character and anime:
        msg = f"\"{quote}\"\n\n- {character} ({anime})"
        await update.message.reply_text(msg)
    else:
        await update.message.reply_text("Gagal mengambil quote anime.")