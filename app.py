import re
from flask import Flask, request
import telegram
from telebot.credentials import bot_token, bot_user_name, URL 
from telebot.logger import log
from telebot.brain_ai import generate_reply

global bot
global TOKEN 
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    
    try:
        chat_id = update.message.chat.id 
        msg_id = update.message.message_id
        
        text = update.message.text.encode('utf-8').decode()
        log('MESSAGE','{}...'.format(text))

        generate_reply(text, chat_id, msg_id)

    except Exception as e:
        log('ERROR', e)

    return 'ok'

@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route('/')
def index():
    return '.'

if __name__ == '__main__':
    app.run(threaded=True)