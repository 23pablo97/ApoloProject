import telegram
import time
from .credentials import chat_admin, bot_token

global bot
global TOKEN 
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

def send_message(chat_id, text, reply_to_message_id=None):
    for msg in text:
        bot.sendChatAction(chat_id=chat_id, action="typing")
        time.sleep(0.3)
        bot.sendMessage(chat_id=chat_id, text= msg, reply_to_message_id=reply_to_message_id)

def send_photo(chat_id, photo, reply_to_message_id=None):
    bot.sendChatAction(chat_id=chat_id, action="upload_photo")
    time.sleep(0.3)
    bot.sendPhoto(chat_id=chat_id, photo= photo, reply_to_message_id=reply_to_message_id)