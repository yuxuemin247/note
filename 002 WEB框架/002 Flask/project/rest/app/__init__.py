from flask import Flask
from flask_restful import Api

from app import views, ext
from app.apis import ChannelList, ChannelDetail, ArticleList, ArticleDetail, UserRegister, UserLogin


def create_app():
    app = Flask(__name__)
    # session 数据加密
    # from itsdangerous import TimedJSONWebSignatureSerializer
    # TimedJSONWebSignatureSerializer 数据加密
    # generate_password_hash，check_password_hash
    # 都会依赖 app 中的 secret_key
    app.config['SECRET_KEY'] = '110'

    ext.init_db(app)
    ext.init_migrate(app)

    api = Api(app, prefix='/api')

    api.add_resource(ChannelList, '/channels', endpoint='channel_list')
    api.add_resource(ChannelDetail, '/channels/<int:id>', endpoint='channel_detail')

    api.add_resource(ArticleList, '/articles', endpoint='article_list')
    api.add_resource(ArticleDetail, '/articles/<int:id>', endpoint='article_detail')

    api.add_resource(UserRegister, '/auth/register', endpoint='user_register')
    api.add_resource(UserLogin, '/auth/login', endpoint='user_login')

    app.register_blueprint(views.rest_bp)

    return app
