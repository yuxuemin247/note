import os

from flask_httpauth import HTTPTokenAuth
from flask_migrate import Migrate

from app.models import db

migrate = Migrate()
auth = HTTPTokenAuth()


def init_db(app):
    """
    向 flask app 初始化 SQLAlchemy
    :param app:
    :return:
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'sqlite3.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app=app)


def init_migrate(app):
    """
    向 flask app 初始化 flask_migrate
    :param app:
    :return:
    """
    migrate.init_app(app=app, db=db)
