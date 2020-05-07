
import tornado.web   # tornado的 基础web框架模块
from tornado.web import authenticated

#登录验证，重写函数get_current_user

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        account = self.get_secure_cookie('account',None)
        print('cookie里面存的内容',account)
        #self.application.db.insert()
        return None

class Index(BaseHandler):
    @authenticated
    def get(self):
        current_user = self.get_current_user()

class Register(tornado.web.RequestHandler):
    def get(self):
        self.render('register.html')

    def post(self):
        pass


class  Login(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        account = self.get_body_argument('username',None)
        pwd = self.get_body_argument('password',None)
        print(account,pwd)
        if 1:
            self.set_secure_cookie('account', account)
            self.redirect('/')
        else:
            print('123123')
            self.render('login.html')
        #这里也可以设置 加密cookie set_secure_cookie ,但必须要在appliacation下设置cookie_secret='xxxx'对cookie加密









#获取get请求的参数值
#self.get_query_argument(name,default,strip = True)  返回一个值
#self.get_query_arguements(name,default,strip =True) 返回一个列表
#获取post请求的参数值
#self.get_body_arguement(name,default,strip =True)   一个值
#self.get_body_arguements(name,default,strip =True)  返回一个列表
#  static_url 生成静态文件路径<link href="{{static_url("css/common.css")}}" rel="stylesheet" />




# if __name__ == '__main__':
#     # 实例化一个对象，Appliaction 是 tornado的一个核心类，里面保存了路由映射表，有一个listen 方法，创建了一个socket服务器，并绑定了一个端口8001
#     app = tornado.web.Application([
#         (r'/hello', Index),
#
#     ])
#     # 绑定监听端口，此时我们的服务器并没有开始监听
#     app.listen(8001)
#
#     # IOLoop.current:返回当前线程的IOLoop实例
#     # IOLoop.start:启动IOLoop实例的I/o循环，同时开启了监听
#     tornado.ioloop.IOLoop.current().start()

#异步

#client = tornado.httpclient.AsyncHTTPClient()