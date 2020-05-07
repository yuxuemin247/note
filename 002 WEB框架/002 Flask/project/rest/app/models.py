import datetime

from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

    articles = db.relationship('Article', backref='author', lazy='dynamic')

    def generate_auth_token(self, expires_in=3600):
        serializer = Serializer(current_app.config['SECRET_KEY'], expires_in=expires_in)
        token = serializer.dumps({'user_id': self.id}).decode('utf-8')

        return token

    @classmethod
    def check_auth_token(cls, token):
        serializer = Serializer(current_app.config['SECRET_KEY'])

        try:
            # 从 token 中，解密数据
            data = serializer.loads(token)
        except:
            return None

        if 'user_id' in data:
            # User.query.get()
            return cls.query.get(data['user_id'])
        else:
            return None


class Channel(db.Model):
    __tablename__ = 'channels'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True, nullable=False)
    sort = db.Column(db.Integer, nullable=False)

    articles = db.relationship('Article', backref='channel', lazy='dynamic')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'sort': self.sort
        }


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    title = db.Column(db.String(256), nullable=False)
    content = db.Column(db.String(5000), nullable=False)

    channel_id = db.Column(db.Integer, db.ForeignKey('channels.id'))

    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
