
from conf import config
from . import global_settings


class Settings():
    def __init__(self):

        ## 整合全局配置文件
        for k in dir(global_settings):
            if k.isupper():
                v = getattr(global_settings, k)
                setattr(self, k, v)

        ## 整合自定义配置文件
        for k in dir(config):
            if k.isupper():
                v = getattr(config, k)
                setattr(self, k, v)

settings = Settings()
