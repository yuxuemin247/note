import tornado.web
from views import index
import config
from models import MYSQL
class Application(tornado.web.Application):

    def __init__(self):
        path = [
            (r'/',index.Index),
            (r'/register',index.Register),
            (r'/login',index.Login),
        ]
        super(Application,self).__init__(path,**config.settings)
        self.db = MYSQL(**config.mysql)