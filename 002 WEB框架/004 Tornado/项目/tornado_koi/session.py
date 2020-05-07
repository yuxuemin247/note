import os
import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler
import hashlib
import time


# 生成一个随机的字符串
def gen_random_str():
    md5 = hashlib.md5()
    md5.update(str(time.time()).encode('utf-8'))
    return md5.hexdigest()


# session类
class CacheSession(object):
    container = {}

    def __init__(self, handler):
        self.handler = handler
        client_random_str = self.handler.get_cookie("session_id")
        if client_random_str and client_random_str in self.container:
            self.random_str = client_random_str
        else:
            self.random_str = gen_random_str()
            self.container[self.random_str] = {}

        expires = time.time() + 300
        self.handler.set_cookie("session_id", self.random_str, expires=expires)

    def __setitem__(self, key, value):
        self.container[self.random_str][key] = value

    def __getitem__(self, item):
        return self.container[self.random_str].get(item)


class SessionHandler(RequestHandler):
    def initialize(self):
        # self指代的是当前的对象
        self.session = CacheSession(self)


class LoginHandler(SessionHandler, RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html')

    def post(self, *args, **kwargs):
        username = self.get_argument('username')
        password = self.get_argument('password')
        if username == 'admin' and password == '123':
            self.session['username'] = username
            self.redirect('/main')
        else:
            self.redirect('/login')


class MainHandler(SessionHandler, RequestHandler):
    def get(self, *args, **kwargs):
        username = self.session['username']
        if username:
            self.write('this is main page')
        else:
            self.redirect('/login')

    def post(self, *args, **kwargs):
        pass


settings = {
    "static_path": os.path.join(os.path.dirname(__file__), 'static'),
    "static_url_prefix": "static",
    "template_path": 'views',
    "xsrf_cookies": True,
}


def make_app():
    return tornado.web.Application([
        (r"/login", LoginHandler),
        (r"/main", MainHandler),
    ], **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()