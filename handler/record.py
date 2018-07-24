import os
import time

def create(bot, update):
    chatId = update.message.chat_id
    accountBook = getAccountBook(chatId)
    record = recordFormat(update.message.text)
    accountBook.write(record)
    bot.send_message(chatId, text="成功新增一筆資料")
    accountBook.close()

def getAccountBook(chatId):
    filename = str(chatId) + '_' + time.strftime('%Y%m%d', time.localtime()) + '.csv'
    return open(os.path.join('books', filename), 'a')

def recordFormat(input):
    record = input.replace(" ", ",")
    record = record + ',' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "\n"
    return record