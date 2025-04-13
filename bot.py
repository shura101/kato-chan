import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (ApplicationBuilder, CommandHandler, ContextTypes,
                          MessageHandler, filters, CallbackQueryHandler)
from handlers.anime import animeinfo, jadwalanime, waifu, quoteanime

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Menu utama
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🌀 Anime Info", callback_data="animeinfo"),
            InlineKeyboardButton("🗓️ Jadwal Anime", callback_data="jadwalanime")
        ],
        [
            InlineKeyboardButton("👧 Waifu Random", callback_data="waifu"),
            InlineKeyboardButton("💬 Anime Quote", callback_data="quoteanime")
        ],
        [
            InlineKeyboardButton("💻 Programming", callback_data="programming"),
            InlineKeyboardButton("📊 Trading & Investasi", callback_data="trading")
        ],
        [
            InlineKeyboardButton("❓ Help", callback_data="help")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Silakan pilih fitur yang tersedia:", reply_markup=reply_markup)

# Handler tombol menu
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "animeinfo":
        await query.edit_message_text("Silakan ketik perintah:\n/animeinfo <judul anime>")
    elif data == "jadwalanime":
        await jadwalanime(update, context)
    elif data == "waifu":
        await waifu(update, context)
    elif data == "quoteanime":
        await quoteanime(update, context)
    elif data == "programming":
        await query.edit_message_text("Fitur *Programming* sedang dikembangkan... tunggu ya!", parse_mode="Markdown")
    elif data == "trading":
        await query.edit_message_text("Fitur *Trading & Investasi* segera hadir!", parse_mode="Markdown")
    elif data == "help":
        help_text = (
            "*Panduan Penggunaan Kato Bot*\n\n"
            "🌀 /animeinfo <judul> — Cari info anime\n"
            "🗓️ /jadwalanime — Lihat jadwal anime hari ini\n"
            "👧 /waifu — Dapatkan waifu random\n"
            "💬 /quoteanime — Dapatkan quote anime\n\n"
            "Untuk fitur Programming & Trading, stay tuned!"
        )
        await query.edit_message_text(help_text, parse_mode="Markdown")
    else:
        await query.edit_message_text("Perintah tidak dikenali.")

# Fungsi utama
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CommandHandler("animeinfo", animeinfo))
    app.add_handler(CommandHandler("jadwalanime", jadwalanime))
    app.add_handler(CommandHandler("waifu", waifu))
    app.add_handler(CommandHandler("quoteanime", quoteanime))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()