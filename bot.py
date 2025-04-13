import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ChatMemberHandler
from handlers.welcome import welcome_new_member
from handlers.antilink import check_anti_link
from handlers.admin_commands import mute, unmute
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(ChatMemberHandler(welcome_new_member, ChatMemberHandler.CHAT_MEMBER))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_anti_link))
app.add_handler(CommandHandler("mute", mute))
app.add_handler(CommandHandler("unmute", unmute))

if __name__ == "__main__":
    print("Bot running...")
    app.run_polling()