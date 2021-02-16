from .utils import send_photo, send_message
from .apolo_speedtest import calculate_speedtest
from telebot import celery

apolo_img = 'https://drive.google.com/uc?export=view&id=1HHrdycezqu9NUnWqoIKYmIsA4rmftRdg'

@celery.task()
def generate_reply(text, chat_id, msg_id):
    if   text == '/start': get_start(chat_id)
    elif text == '/help': get_help(chat_id)
    elif 'pichi' in text.lower() or 'pishi' in text.lower(): get_apolo_photo(chat_id, msg_id)
    elif 'velocidad del internet' in text.lower(): get_speedtest(chat_id, msg_id)
    elif text == '/internet': get_speedtest(chat_id)
        
def get_start(chat_id):
    message = [
        'Saludos humanos... soy Apolo, un bot creado para dar algo de realidad a nuestro perro',
        'Si necesitan mas info de que cosas puedo hacer, por favor ejecuten el comando /help',
        'Guau Guau'
    ]
    send_message(chat_id=chat_id, text= message)

def get_help(chat_id):
    message = [
        """
Comandos:
/start - comando de bienvenida
/help - manual de usuario
/internet - mide la velocidad del internet

Otros:
* Si tu frase contiene la palabra "pishi" o "pichi" retorna una foto del Apolo
* Si tu frase contiene "velocidad del internet" automaticamente se calcula la velocidad del internet
        """
    ]
    send_message(chat_id=chat_id, text= message)
    
def get_apolo_photo(chat_id, msg_id):
    send_photo(chat_id=chat_id, photo= apolo_img, reply_to_message_id=msg_id)

def get_speedtest(chat_id, msg_id=None):
    message_1 = ['mmmm... dejame calcular la velocidad']
    send_message(chat_id=chat_id, text= message_1, reply_to_message_id=msg_id)

    speedtest = calculate_speedtest()
    message_2 = [
        'La velocidad de descarga es de {} mbps, y la de subida es de {} mbps.\nPara mas info: {}'.format(
        speedtest['download'], 
        speedtest['upload'], 
        speedtest['share'])
    ]
    send_message(chat_id=chat_id, text= message_2, reply_to_message_id=msg_id)