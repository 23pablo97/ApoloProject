import telebot
from telebot.config import factory

if __name__ == '__main__':
    app = factory.create_app(celery=telebot.celery)
    telebot.scheduler.start()
    app.run(threaded=True)