from telegram import Update, ChatPermissions
from telegram.ext import ContextTypes

async def mute(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_chat.get_member(update.effective_user.id).status in ["administrator", "creator"]:
        await update.message.reply_text("Hanya admin yang bisa menggunakan perintah ini.")
        return
    if not context.args:
        await update.message.reply_text("Contoh: /mute @username")
        return
    try:
        user = update.message.reply_to_message.from_user
        await context.bot.restrict_chat_member(
            chat_id=update.effective_chat.id,
            user_id=user.id,
            permissions=ChatPermissions(can_send_messages=False)
        )
        await update.message.reply_text(f"{user.full_name} telah dibisukan.")
    except:
        await update.message.reply_text("Gagal membisukan pengguna.")

async def unmute(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_chat.get_member(update.effective_user.id).status in ["administrator", "creator"]:
        await update.message.reply_text("Hanya admin yang bisa menggunakan perintah ini.")
        return
    try:
        user = update.message.reply_to_message.from_user
        await context.bot.restrict_chat_member(
            chat_id=update.effective_chat.id,
            user_id=user.id,
            permissions=ChatPermissions(can_send_messages=True)
        )
        await update.message.reply_text(f"{user.full_name} telah dibuka suaranya.")
    except:
        await update.message.reply_text("Gagal membuka suara pengguna.")