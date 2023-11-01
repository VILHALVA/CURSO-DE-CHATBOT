import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

# Substitua 'YOUR_API_TOKEN' pelo Token de API que você recebeu do BotFather
TOKEN = 'YOUR_API_TOKEN'
bot = telegram.Bot(token=TOKEN)

def start(update, context):
    update.message.reply_text("Olá! Eu sou o seu bot do Telegram. Como posso ajudar?")

def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
