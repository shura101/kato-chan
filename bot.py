from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Import handlers
from handlers.anime import anime_menu, info_anime, waifu
from handlers.crypto import crypto_menu
from handlers.coding import coding_menu
from handlers.unknown import unknown

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Halo, aku Kato Chan!\n"
        "Ketik salah satu perintah berikut:\n\n"
        "/anime - Fitur seputar anime\n"
        "/crypto - Harga & info crypto\n"
        "/coding - Bantu deteksi error koding"
    )
    await update.message.reply_text(text)

# Main function
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    # Menambahkan handler
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("anime", anime_menu))  # Menu utama /anime
    app.add_handler(CommandHandler("info_anime", info_anime))  # Sub-perintah info_anime
    app.add_handler(CommandHandler("waifu", waifu))  # Sub-perintah waifu
    app.add_handler(CommandHandler("crypto", crypto_menu))
    app.add_handler(CommandHandler("coding", coding_menu))

    # Tangani perintah tidak dikenal
    app.add_handler(MessageHandler(filters.COMMAND, unknown))

    print("Kato Chan Bot is running...")
    app.run_polling()