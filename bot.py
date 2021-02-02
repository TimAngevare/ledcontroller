# -*- coding: utf-8 -*-

from telegram.ext import Updater
from telegram.ext import CommandHandler
import controller


# Telegram bot
updater = Updater(token='1419433214:AAE1U9AIS2zfCE2PS8JHLcHkV3K41s-E6H0', use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="This is Tim's bot at your service!")

def sad(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Im sad")
    controller.pulse((238,57,47))

def happy(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="Im happy")
    controller.pulse((132,187,91))

def stopping(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Stopping now")
    updater.stop()


start_handler = CommandHandler('start', start)
sad_handler = CommandHandler('sad', sad)
sad_handler = CommandHandler('happy', happy)
stop = CommandHandler('stop', stopping)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(sad_handler)

def init():
    updater.start_polling()
