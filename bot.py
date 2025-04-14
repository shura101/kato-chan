from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Import handlers
from handlers.anime import anime_menu
from handlers.crypto import crypto_menu
from handlers.coding import coding_menu
from handlers.unknown import unknown
from handlers.waifu import waifu_command  # Pastikan ada file waifu.py dengan fungsi waifu_command

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Halo, aku Kato Chan!\n"
        "Ketik salah satu perintah berikut:\n\n"
        "/anime - Fitur seputar anime\n"
        "/crypto - Harga & info crypto\n"
        "/coding - Bantu deteksi error koding\n"
        "/waifu - Gambar waifu SFW\n"
        "/waifu nsfw - Gambar waifu NSFW"
    )
    await update.message.reply_text(text)

# Main function
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    # Menambahkan handler
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("anime", anime_menu))
    app.add_handler(CommandHandler("waifu", waifu_command))  # Pastikan ada fungsi waifu_command
    app.add_handler(CommandHandler("crypto", crypto_menu))
    app.add_handler(CommandHandler("coding", coding_menu))

    # Tangani perintah tidak dikenal
    app.add_handler(MessageHandler(filters.COMMAND, unknown))

    print("Kato Chan Bot is running...")
    app.run_polling()