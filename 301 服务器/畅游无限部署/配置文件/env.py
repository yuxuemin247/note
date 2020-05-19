import logging

SECRET_KEY = 'mk-emf0ppvoswdbga-r23l_*jnrc*%ns%c&#%x$2ar_-bbkt8b'

DEBUG = True
ALLOWED_HOSTS = ['*', ]

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.mysql',

        'NAME': 'customer',  # 你的数据库名称

        'USER': 'customer',  # 你的数据库用户名

        'PASSWORD': '788GoDFZnv8wnKpW',  # 你的数据库密码

        'HOST': 'rm-2zej29768369s2sl5.mysql.rds.aliyuncs.com',  # 你的数据库主机，留空默认为localhost

        'PORT': '3306',  # 你的数据库端口

        'OPTIONS': {'init_command': 'SET default_storage_engine=INNODB', }  # 选项支持事务
    }
}

REDIS_DB = 'redis://127.0.0.1:6379/0'

SESSION_CACHE_ALIAS = 'default'
SESSION_COOKIE_AGE = 60 * 60 * 24
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

LOG_LEVEL = logging.DEBUG
LOG_ADDRESS = '/dev/log'
sysopen =True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'django': {
            'format': 'customer[%(process)d]: %(levelname)s %(filename)s[line:%(lineno)d] %(message)s',
        },
    },
    'handlers': {
        'logging.handlers.SysLogHandler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.SysLogHandler',
            'facility': 'local7',
            'formatter': 'django',
            'address': '/dev/log',
        },
        'logging.StreamHandler': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'loggly_logs': {
            'handlers': ['logging.handlers.SysLogHandler', 'logging.StreamHandler'],
            'propagate': True,
            'format': '%(asctime)s customer[%(process)d]: %(levelname)s %(filename)s[line:%(lineno)d] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'level': 'DEBUG',
        },
    },
}
