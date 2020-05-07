import datetime

from flask import g

from flask_restful import Resource, reqparse, fields, marshal_with, abort
from werkzeug.security import generate_password_hash, check_password_hash
from app.ext import auth
from app.models import Channel, db, Article, User

# 通过 reqparse.RequestParser 的实例对象完成对 请求参数（通常是 客户端提交的 json 数据）的数据校验
article_parser = reqparse.RequestParser()
# add_argument：第一个参数为 客户端提交的数据的 字段名称（如：json 数据的 key）
article_parser.add_argument('title', required=True, type=str, help='标题必填')
article_parser.add_argument('content', required=True, type=str, help='正文必填')
article_parser.add_argument('channel_id', required=True, type=int, help='频道必填')


class MyDTFmt(fields.Raw):
    def format(self, value):
        return datetime.datetime.strftime(value, '%Y-%m-%d %H:%M:%S')


article_fields = {
    'id': fields.Integer,
    'url': fields.Url(endpoint='article_detail', absolute=True),
    'title': fields.String,
    'content': fields.String,
    # 'channel': fields.Nested(channel_fields),
    'channel': fields.Nested({
        'name': fields.String,
        'url': fields.Url(endpoint='channel_detail', absolute=True)
    }),
    'author': fields.Nested({
        'id': fields.Integer,
        'name': fields.String(attribute='username')
    }),
    'created_at': MyDTFmt,
    'updated_at': fields.DateTime(dt_format='iso8601')
}


class ArticleList(Resource):
    @marshal_with(fields=article_fields)
    def get(self):
        articles = Article.query.all()

        return articles, 200

    @auth.login_required
    @marshal_with(fields=article_fields)
    def post(self):
        # 通过 reqparse.RequestParser 的实例对象，验证客户端的请求数据
        # 如果不满足验证条件，则直接报错返回（400 状态码）
        args = article_parser.parse_args()

        article = Article()
        article.title = args.get('title')
        article.content = args.get('content')
        article.channel_id = args.get('channel_id')

        # 登录状态下，设置文章的作者
        article.author_id = g.user.id

        db.session.add(article)
        db.session.commit()

        # flask-restful 类视图的实例方法只能返回 字典
        # 通过 marshal_with 装饰器可以定制化输出格式
        return article, 201


class ArticleDetail(Resource):
    def get_object(self, id):
        article = Article.query.get(id)
        if article is None:
            return abort(404, message='找不到对象')

        return article

    @marshal_with(fields=article_fields)
    def get(self, id):
        article = self.get_object(id)
        return article, 200

    @auth.login_required
    def put(self, id):
        article = self.get_object(id)
        args = article_parser.parse_args()

        article.title = args.get('title', article.title)
        article.content = args.get('content', article.content)
        article.channel_id = args.get('channel_id', article.channel_id)

        db.session.commit()

        return article, 200

    @auth.login_required
    def patch(self, id):
        self.put(id)

    @auth.login_required
    def delete(self, id):
        article = self.get_object(id)

        db.session.delete(article)
        db.session.commit()

        return '', 204


def validate_channel_name(value):
    """
    自定义验证后，必须把验证通过的值返回
    :param value:
    :return:
    """
    if Channel.query.filter_by(name=value).count() > 0:
        raise ValueError('频道名重复')

    return value


# flask-restful 通过 reqparse 包的 RequestParser 类提供客户端请求数据的验证功能
channel_parser = reqparse.RequestParser()
# channel_parser.add_argument('name', required=True, type=str)
channel_parser.add_argument('name', required=True, type=validate_channel_name)  # 自定义验证
channel_parser.add_argument('sort', required=True, type=int, help='sort 为必填项, int 类型')

# 通过 fields 和 marshal_with 一起完成自定义输出的功能，让 api 接口可以直接返回对象，系统内部将对象
# 根据 fields 的定义转换成字典类型
channel_fields = {
    'id': fields.Integer,
    'url': fields.Url(endpoint='channel_detail', absolute=True),
    'name': fields.String,
    'sort': fields.Integer
}

channel_articles_fields = {
    'id': fields.Integer,
    'url': fields.Url(endpoint='channel_detail', absolute=True),
    'name': fields.String,
    'articles': fields.List(fields.Nested(article_fields))
}


class ChannelList(Resource):
    """
    GET     /channels
    POST    /channels
    """

    @marshal_with(fields=channel_fields)
    def get(self):
        # 数据库查询返回的是 list 类型的数据
        # _channels = [<Channel 1>, <Channel 2>]
        _channels = Channel.query.all()
        # channels = [channel.to_dict() for channel in _channels]

        # flask 视图函数只能返回 str 或 response 对象
        # 我们可以将数据库查询出来的数据 转换成 json，以满足 flask 视图函数的返回要求

        # flask-restful 返回字典，框架内部会自动转换为 json
        # return {'channels': channels}, 200

        return _channels, 200

    @marshal_with(fields=channel_fields)
    def post(self):
        args = channel_parser.parse_args()

        channel = Channel()
        channel.name = args['name']
        channel.sort = args['sort']

        db.session.add(channel)
        db.session.commit()

        return channel, 201
        # return {'channel': channel.to_dict()}, 201


class ChannelDetail(Resource):
    """
    GET     /channels/123
    PUT     /channels/234
    PATCH   /channels/123
    DELETE  /channels/123
    """

    def get_object(self, id):
        channel = Channel.query.get(id)

        if channel is None:
            return abort(404, message='找不到对象')

        return channel

    @marshal_with(fields=channel_articles_fields)
    def get(self, id):
        channel = self.get_object(id)
        # channel.articles 代表了当前频道下的文章列表
        return channel, 200

    @marshal_with(fields=channel_fields)
    def put(self, id):
        channel = self.get_object(id)
        args = channel_parser.parse_args()

        channel.name = args.get('name', channel.name)
        channel.sort = args.get('sort', channel.sort)

        db.session.commit()

        return channel, 200

    def patch(self, id):
        self.put(id)

    def delete(self, id):
        channel = self.get_object(id)
        db.session.delete(channel)
        db.session.commit()

        return '', 204




user_fields = {
    'id': fields.Integer,
    'username': fields.String
}

user_parser = reqparse.RequestParser()
user_parser.add_argument('username', required=True, type=str)
user_parser.add_argument('password', required=True, type=str)
class UserRegister(Resource):
    @marshal_with(fields=user_fields)
    def post(self):
        args = user_parser.parse_args()

        # 需要自定义验证，验证用户名是否重复

        user = User()
        user.username = args.get('username')
        user.password = generate_password_hash(args['password'])

        db.session.add(user)
        db.session.commit()

        return user, 201


class UserLogin(Resource):
    def post(self):
        args = user_parser.parse_args()

        user = User.query.filter_by(username=args['username']).first()

        if user is None or not check_password_hash(user.password, args['password']):
            return {'msg': '用户名密码错误'}, 400

        token = user.generate_auth_token()

        return {'token': token}


@auth.verify_token
def verify_token(token):
    """
    验证 token 的 回调函数
    如果验证成功，则返回 True，否则返回 False
    :param token:
    :return:
    """

    # 验证 token，
    # 如果验证成功，则使用 token 中的用户身份信息（user_id）从数据库中查询当前登录用户数据，返回 uesr 对象
    # 如果验证不成功，则 返回 None
    user = User.check_auth_token(token)

    if user is None:
        return False

    # 验证成功后，将当前登录用户的对象设置到 g 对象中，供后续使用
    g.user = user
    return True
