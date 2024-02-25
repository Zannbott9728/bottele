from telegram.ext import Updater, CommandHandler

# Fungsi untuk perintah /start
def start(update, context):
    update.message.reply_text('Halo! Saya adalah bot.')

def main():
    updater = Updater("7017046698:AAGFfFRQygagSBUDkDbtN5VXVm-69suWCO4", use_context=True)
    dp = updater.dispatcher

    # Menambahkan handler perintah /start
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()