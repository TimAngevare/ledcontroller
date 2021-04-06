from telegram.ext import Updater
from telegram.ext import CommandHandler
import controller


# Telegram bot
updater = Updater(token='1419433214:AAE1U9AIS2zfCE2PS8JHLcHkV3K41s-E6H0', use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="This is Tim's bot at your service!")

def sad(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="sending megan sad tim...")
    controller.pulse((47,11,9))

def happy(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="sending megan happy tim...")
    controller.pulse((26,38,18))

def love(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="sending megan lovely tim...")
    controller.pulse((255,63,158))

def stopping(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Stopping now")
    updater.stop()


start_handler = CommandHandler('start', start)
sad_handler = CommandHandler('sad', sad)
happy_handler = CommandHandler('happy', happy)
love_handler = CommandHandler('ly', love)
stop = CommandHandler('stop', stopping)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(sad_handler)
dispatcher.add_handler(happy_handler)
dispatcher.add_handler(love_handler)
dispatcher.add_handler(stop)


updater.start_polling()
