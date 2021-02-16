import os
from flask import Flask 
from .celery_utils import init_celery

def create_app(app_name=__name__, **kwargs):
    app = Flask(app_name)
    if kwargs.get('celery'):
        init_celery(kwargs.get('celery'), app)

    from ..routes import bp
    app.register_blueprint(bp)
    return app