import datetime

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ModelMixin():
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return False

    @classmethod
    def save_all(cls,objs):
        try:
            db.session.add_all(objs)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return False

class  User(db.Model,UserMixin,ModelMixin):
    __tablename__ ='users'
    id =db.Column(db.Integer,primary_key=True)
    created_at =db.Column(db.DateTime,default=datetime.datetime.now())
    updated_at =db.Column(db.DateTime,default=datetime.datetime.now(),onupdate =datetime.datetime.now())
    nickname =db.Column(db.String(32),unique=True,nullable=False)
    email =db.Column(db.String(255),unique=True,nullable=False)
    is_admin =db.Column(db.Boolean,default=False)
    password =db.Column(db.String(255))
    articles =db.relationship('Article',backref='user',lazy='dynamic')


#标签
class Tag(db.Model,ModelMixin):
    __tablename__ = 'tags'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    tag_name = db.Column(db.String(16),nullable=False,unique=True)
#频道
class Channel(db.Model,ModelMixin):
    id = db.Column(db.Integer,primary_key=True)
    ch_name = db.Column(db.String(20),nullable=False,unique=True)
    ch_sort = db.Column(db.Integer,nullable=False)
    articles = db.relationship('Article',backref ='channel',lazy = 'dynamic')

#文章
class Article(db.Model,ModelMixin):
    __tablename__ ='articles'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(256),nullable=False)
    created_time = db.Column(db.DateTime,default=datetime.datetime.now())
    updated_time =db.Column(db.DateTime,default=datetime.datetime.now(),onupdate=datetime.datetime.now())
    txt_word = db.Column(db.String(5000),nullable=False)
    ch_id =db.Column(db.Integer,db.ForeignKey('channel.id'))
    user_id =db.Column(db.Integer,db.ForeignKey('users.id'))
    tags = db.relationship('Tag', secondary='article_tags', backref=db.backref('articles', lazy='dynamic'),
                               lazy='dynamic')

article_tags=db.Table('article_tags',
                     db.Column('id',db.Integer,primary_key=True),
                     db.Column('article_id',db.Integer,db.ForeignKey('articles.id')),
                     db.Column('tag_id',db.Integer,db.ForeignKey('tags.id'))
                               )









