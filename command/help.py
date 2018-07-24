def command(bot, update):
    helpMsg = getHelpMsg()
    bot.send_message(chat_id=update.message.chat_id, text=helpMsg)

def getHelpMsg():
    return "嗨，我是你的記帳機器人！"