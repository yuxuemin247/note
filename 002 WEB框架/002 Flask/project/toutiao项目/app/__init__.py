import os

from flask import Flask
from celery import Celery

from app import views, ext
from app.models import db
def create_app():
    app = Flask(__name__)
    app.secret_key ='110119'
    #sqlites 数据库文件位置
    db_file = os.path.join(app.root_path,'sqlite3.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+db_file
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = False  # 打印sql语句
    db.init_app(app=app)
    ext.init_login_manager(app)
    app.register_blueprint(views.bp)
    #celery配置
    app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
    app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/1'
    celery = Celery(app.name,broker=app.config['CELERY_BREKER_URL'])

    #邮件配置

    return app