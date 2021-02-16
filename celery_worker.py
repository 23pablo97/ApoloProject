from telebot import celery 
from telebot.config.factory import create_app
from telebot.config.celery_utils import init_celery
app = create_app()
init_celery(celery, app)