import  config
import tornado.ioloop
from application import Application

if __name__ == '__main__':
    app = Application()
    #绑定一个端口
    app.listen(config.options['port'])

    #IOloop.current() 返回一个Ioloop的实例
    # start开始监听端口
    tornado.ioloop.IOLoop.current().start()



#开启多个进程，但windows上有问题，AttributeError: module 'os' has no attribute 'fork'
# import tornado.httpserver
# httpserver= tornado.httpserver.HTTPServer(app)
# httpserver.bind(8080)
# httpserver.start(5)   #开启5个进程


