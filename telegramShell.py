import os, platform
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime

# Telegram Token
TOKEN='YOUR_TELEGRAM_TOKEN'

# Authorized User ID
user_id='YOUR_TELEGRAM_USERID'

# Check OS
opsys = platform.system()

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Shell
def s(update, context):
        id = str(update.message.from_user.id)
        usr = str(update.message.from_user.username)
        dateTimeObj = datetime.now()
        time = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")

        if id == user_id:
         arg = ' '.join(context.args)
         if opsys == 'Linux':
          cmd = os.popen(arg).read()
         elif opsys == 'Windows':
          ps = str("powershell.exe " + arg)
          cmd = os.popen(ps).read()
        context.bot.send_message(chat_id=update.effective_chat.id, text=cmd)
# Log
        l = open('bot.log', 'a')
        l.write(time + " - User=" + str(usr) + " ID=" + str(id) + " Command=" + str(arg) + "\n")
        l.close()
s_handler = CommandHandler('s', s)
dispatcher.add_handler(s_handler)

# Help
def h(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Usage: /sh cmd")
help_handler = CommandHandler('h', h)
dispatcher.add_handler(help_handler)

# Quit
def q(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Quitting!")
        updater.stop()
q_handler = CommandHandler('q', q)
dispatcher.add_handler(q_handler)

# WTF
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Wrong Command!")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Type '/sh command'.")
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

# Start Listening
updater.start_polling()
