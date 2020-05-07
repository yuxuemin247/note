from flask import Flask
from flask_restful import Api

from app import views, ext
from app.apis import ChannelList, ChannelDetail, ArticleList, ArticleDetail


def create_app():
    app = Flask(__name__)

    ext.init_db(app)
    ext.init_migrate(app)

    api = Api(app)
    api.add_resource(ChannelList, '/api/channels', endpoint='channel_list')
    api.add_resource(ChannelDetail, '/api/channels/<int:id>', endpoint='channel_detail')

    api.add_resource(ArticleList, '/api/articles', endpoint='article_list')
    api.add_resource(ArticleDetail, '/api/articles/<int:id>', endpoint='article_detail')
    app.register_blueprint(views.rest_bp)
    return app
