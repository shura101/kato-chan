from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def genre_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Action", callback_data="genre_Action"),
         InlineKeyboardButton("Romance", callback_data="genre_Romance")],
        [InlineKeyboardButton("Kembali ke Menu", callback_data="menu")]
    ]
    await update.callback_query.edit_message_text("Pilih genre yang kamu suka~", reply_markup=InlineKeyboardMarkup(keyboard))

async def genre_result(update: Update, context: ContextTypes.DEFAULT_TYPE):
    genre = update.callback_query.data.split("_")[1]
    await update.callback_query.edit_message_text(f"Nih anime dengan genre {genre}, sedang disiapkan ya~",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Kembali ke Genre", callback_data="genre")],
                                           [InlineKeyboardButton("Kembali ke Menu", callback_data="menu")]]))