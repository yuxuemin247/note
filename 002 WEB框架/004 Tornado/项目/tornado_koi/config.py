import os
BASE_DIR = os.path.dirname(__file__)
options = {
    'port':9999
}

mysql = {
    'dbhost':'182.92.7.134',
    'dbuser':'root',
    'dbpwd':'123456',
    'dbname':'text',
    'dbcharset':'utf8'
}

settings = {
    'debug' :False,
    'static_path':os.path.join(BASE_DIR,'static'),
    'template_path': os.path.join(BASE_DIR,'templates'),
    'xsrf_cookies':False , # 就是csrf 不同缩写
    'cookie_secret':'test',
    'login_url':'/login'
}

# debug 设置tornado是工作在调试环境下还是生产环境下，
#debug 设置为 True
# tornado应用会监控源代码文件，当有代码改动的时候便会重启服务器，不用手动重启服务器
#取消缓存编译的模板
#取消缓存静态文件
#提供错误追踪信息

