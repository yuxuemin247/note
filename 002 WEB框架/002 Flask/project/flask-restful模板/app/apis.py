import datetime

from flask_restful import Resource, reqparse, fields, marshal_with, abort

from app.models import Channel, db, Article

article_parser = reqparse.RequestParser()
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
    'created_at': MyDTFmt,
    'updated_at': fields.DateTime(dt_format='iso8601')
}


class ArticleList(Resource):
    @marshal_with(fields=article_fields)
    def get(self):
        articles = Article.query.all()

        return articles, 200

    @marshal_with(fields=article_fields)
    def post(self):
        args = article_parser.parse_args()

        article = Article()
        article.title = args.get('title')
        article.content = args.get('content')
        article.channel_id = args.get('channel_id')

        db.session.add(article)
        db.session.commit()

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

    def put(self, id):
        article = self.get_object(id)
        args = article_parser.parse_args()

        article.title = args.get('title', article.title)
        article.content = args.get('content', article.content)
        article.channel_id = args.get('channel_id', article.channel_id)

        db.session.commit()

        return article, 200

    def patch(self, id):
        self.put(id)

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
