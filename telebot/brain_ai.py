from telebot.utils import send_photo, send_message

apolo_img = 'https://drive.google.com/uc?export=view&id=1HHrdycezqu9NUnWqoIKYmIsA4rmftRdg'

def generate_reply(text, chat_id, msg_id):
    if   text == '/start': get_start(chat_id)
    elif text == '/help': get_help(chat_id)
    elif 'pichi' in text or 'pishi' in text: get_apolo_photo(chat_id, msg_id)
        
def get_start(chat_id):
    message = [
        'Saludos humanos... soy Apolo, un bot creado por Pablo para dar algo de realidad a nuestro perro',
        'Si necesitan mas info de que cosas puedo hacer, por favor ejecuten el comando /help',
        'Guau Guau'
    ]
    send_message(chat_id=chat_id, text= message)

def get_help(chat_id):
    message = [
        'Manual en desarrollo...'
    ]
    send_message(chat_id=chat_id, text= message)
    
def get_apolo_photo(chat_id, msg_id):
    send_photo(chat_id=chat_id, photo= apolo_img, reply_to_message_id=msg_id)

