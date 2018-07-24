from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

def echo(bot, update):
    if update.message.text == 'stop':
        updater.idle()
    else:
        bot.send_message(chat_id=update.message.chat_id, text=update.message.text)