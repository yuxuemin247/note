import celery
from flask_login import LoginManager

login_manager =LoginManager()

def init_login_manager(app):
    login_manager.init_app(app=app)
    login_manager.login_view ='blue.login'

@celery.task
def celery_try(x):
    return x