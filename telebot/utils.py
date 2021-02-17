import telegram
import telebot
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

def managing_periodic_tasks(func_task, name_task, status, seconds=0):
    if status == 'enabled':
        if telebot.scheduler.get_job(name_task):
            return 'Task already started!'
        telebot.scheduler.add_job(func_task, 'interval', seconds=seconds, id=name_task)
        return 'Task started!'

    elif status == 'disabled':
        if not telebot.scheduler.get_job(name_task):
            return 'Task is not started!'
        telebot.scheduler.remove_job(name_task)
        return 'Task stopped!'