from datetime import datetime
import telegram
from telebot.credentials import chat_admin, bot_token

global bot
global TOKEN 
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

def log(type, msg):
    message = '[{}] {}: {}'.format(datetime.now(), type, msg)
    print(message)

    if type == 'ERROR':
        sendError(message)

def sendError(message):
    bot.sendMessage(chat_id=chat_admin, text= message)
