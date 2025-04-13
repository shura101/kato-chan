from telegram import Update
from telegram.ext import ContextTypes
import re

LINK_REGEX = re.compile(r"(https?://|t\.me|telegram\.me)")

async def check_anti_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if LINK_REGEX.search(update.message.text):
        try:
            await update.message.delete()
        except:
            pass