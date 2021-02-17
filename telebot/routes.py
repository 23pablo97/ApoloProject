import telegram
import telebot
from flask import request, Blueprint
from .credentials import bot_token, bot_user_name, URL 
from .logger import log
from .brain_ai import generate_reply
from .utils import managing_periodic_tasks
from .apolo_speedtest import monitoring
import json

global bot
global TOKEN 
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)
bp = Blueprint('routes', __name__)

@bp.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    
    try:
        chat_id = update.message.chat.id 
        msg_id = update.message.message_id
        
        text = update.message.text.encode('utf-8').decode()
        log('MESSAGE','{}...'.format(text))

        generate_reply.delay(text, chat_id, msg_id)

    except Exception as e:
        log('ERROR', e)

    return 'ok'

@bp.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@bp.route('/internet/monitoring', methods=['GET', 'POST'])
def internet_monitoring():
    name_task = 'internet_monitoring'
    status = request.args.get('status')
    return managing_periodic_tasks(monitoring, name_task, status, seconds=900)


@bp.route('/internet/historical', methods=['GET', 'POST'])
def internet_historical():
    documents = telebot.apoloModel.speedtest.find({})
    response = []
    for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)


@bp.route('/')
def index():
    return 'ApoloBot is online!'
