import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes,
    CallbackQueryHandler
)
from handler.anime import animeinfo, jadwalanime, waifu, quoteanime

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Menu utama dengan tombol
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🌀 Anime Info", callback_data="animeinfo")],
        [InlineKeyboardButton("🗓️ Jadwal Anime", callback_data="jadwalanime")],
        [InlineKeyboardButton("👧 Waifu Random", callback_data="waifu")],
        [InlineKeyboardButton("💬 Anime Quote", callback_data="quoteanime")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Silakan pilih fitur:", reply_markup=reply_markup)

# Handler tombol
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "animeinfo":
        await query.edit_message_text("Ketik perintah:\n/animeinfo <judul anime>")
    elif query.data == "jadwalanime":
        await jadwalanime(query, context)
    elif query.data == "waifu":
        await waifu(query, context)
    elif query.data == "quoteanime":
        await quoteanime(query, context)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CommandHandler("animeinfo", animeinfo))
    app.add_handler(CommandHandler("jadwalanime", jadwalanime))
    app.add_handler(CommandHandler("waifu", waifu))
    app.add_handler(CommandHandler("quoteanime", quoteanime))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Kato Bot aktif!")
    app.run_polling()

if __name__ == "__main__":
    main()