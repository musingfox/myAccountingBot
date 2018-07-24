from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from handler import echo
from handler import record
from command import help

updater = Updater(token='582592928:AAFNrPMwsLSKKOJe8dDCJXp-GcXiVyFqNTI')

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

recordHandler = MessageHandler(Filters.text, record.create)
dispatcher.add_handler(recordHandler)

helpHandler = CommandHandler('help', help.command)
dispatcher.add_handler(helpHandler)


updater.start_polling()

# stop bot by type Ctrl+C in terminal
updater.idle()