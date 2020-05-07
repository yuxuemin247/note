import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


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
