import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# 配置类的基类
class Config:
    SECRET_KEY = 'luckyboy'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BOOTSTRAP_SERVE_LOCAL = True # 加载本地静态资源文件
    # 邮件发送配置
    # 邮箱服务器
    MAIL_SERVER = 'smtp.1000phone.com'
    # 用户名
    MAIL_USERNAME = 'xialigang@1000phone.com'
    # 密码
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    #  分页每页显示数据条数
    PAGE_NUM = 3
    # 文件上传配置
    UPLOADED_PHOTOS_DEST = os.path.join(BASE_DIR,'static/upload')
    MAX_CONTENT_LENGTH = 1024*1024*64


# 开发环境
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/lucky_blog'
    DEBUG = True
    TESTING = False


# 测试环境
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/test_blog'
    DEBUG = False
    TESTING = True


# 生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/blog'
    DEBUG = False
    TESTING = False


# 配置类的字典
configDict = {
    'default':DevelopmentConfig,
    'dev':DevelopmentConfig,
    'Test':TestingConfig,
    'production':ProductionConfig,
}


