from celery import Celery
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from pymongo import MongoClient

def make_celery(app_name=__name__):
    redis_uri = 'redis://localhost:6379/0'
    return Celery(app_name, backend=redis_uri, broker=redis_uri)

def init_scheduler():
    jobstores = {
        'default': RedisJobStore(host='localhost', port=6379, db=13)
    }
    executors = {
        'default': ThreadPoolExecutor(20),
        'processpool': ProcessPoolExecutor(5)
    }
    return BackgroundScheduler(jobstores=jobstores, executors=executors)

celery = make_celery()
scheduler = init_scheduler()
mongo = MongoClient('localhost')
apoloModel = mongo['ApoloBot']
