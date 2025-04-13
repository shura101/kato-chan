import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes,
    CallbackQueryHandler
)
from handlers.anime import animeinfo, jadwalanime, waifu, quoteanime

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Menu utama dengan tombol interaktif
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

# Handler untuk tombol menu
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "animeinfo":
        await query.edit_message_text("Ketik perintah: /animeinfo <judul>")
    elif data == "jadwalanime":
        await jadwalanime(update, context)
    elif data == "waifu":
        await waifu(update, context)
    elif data == "quoteanime":
        await quoteanime(update, context)
    elif data == "programming":
        await query.edit_message_text("Fitur *Programming* sedang dikembangkan...", parse_mode="Markdown")
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

# Fungsi utama menjalankan bot
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Command handler
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CommandHandler("animeinfo", animeinfo))
    app.add_handler(CommandHandler("jadwalanime", jadwalanime))
    app.add_handler(CommandHandler("waifu", waifu))
    app.add_handler(CommandHandler("quoteanime", quoteanime))

    # Button handler
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Kato Bot siap melayani, Tuan Andre!")
    app.run_polling()

if __name__ == "__main__":
    main()