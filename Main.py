import os
from telegram.ext import Updater, CommandHandler

# Ambil token bot dari environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("🤖 Bot MicinSniper siap bantu cari coin x100 🚀")

def sniper(update, context):
    # Ini hanya contoh. Kamu bisa ganti dengan logic cari coin real.
    update.message.reply_text("🔍 Sedang mencari coin micin potensial... Tunggu sebentar...")

def main():
    if not BOT_TOKEN:
        print("❌ BOT_TOKEN belum diatur!")
        return

    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("sniper", sniper))

    # Jalankan bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
