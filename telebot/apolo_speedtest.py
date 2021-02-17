import speedtest
from telebot import celery
from .logger import log
from datetime import datetime
from pymongo import MongoClient
from .credentials import user_mongo, pass_mongo

servers = []
threads = None
bias = 20

def calculate_speedtest():
    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download(threads=threads)
    s.upload(threads=threads)
    s.results.share()

    res = s.results.dict()
    res['download'] = int(res['download']/1000000)
    res['upload'] = int(res['upload']/1000000)

    res['status'] = 'good' if res['download'] > bias else 'bad'
    return res

@celery.task()
def calculate_saving_data():
    speedtest = calculate_speedtest()
    mongo = MongoClient('mongodb://{USER}:{PASS}@127.0.0.1'.format(USER=user_mongo, PASS=pass_mongo))
    apoloModel = mongo['ApoloBot']
    apoloModel.speedtest.insert_one(speedtest).inserted_id

    if speedtest['status'] == 'bad':
        msg = 'oops, he detectado una baja en la velocidad del internet. Actualmente la velocidad de descarga es de {} mbps.\nPara mas info: {}'.format(
            speedtest['download'],  
            speedtest['share'])
        log('ALERT', msg)
    

def monitoring():
    calculate_saving_data.delay()
