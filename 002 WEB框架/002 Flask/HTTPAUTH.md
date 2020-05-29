### Flask-HTTPAuth

说明：RESTful API 无法使用 Flask-Login 扩展来实现用户认证（RESTful API 不保存状态，无法依赖 Cookie及 Session 来保存用户信息）。需要使用 Flask-HTTPAuth 扩展，完成 RESTful API 的用户认证工作。

Flask-HTTPAuth 提供了几种不同的 Auth 方法，比如 HTTPBasicAuth，HTTPTokenAuth，MultiAuth 和HTTPDigestAuth。

安装：

```
pip install flask-httpauth
```

令牌（Token）认证

在对 HTTP 形式的 API 发请求时，大部分情况我们不是通过用户名密码做验证，而是通过一个令牌，也就是Token来做验证。此时，我们就要使用 Flask-HTTPAuth 扩展中的 HTTPTokenAuth 对象。

它也提供”login_required”装饰器来认证视图函数，”error_handler”装饰器来处理错误。它提供了”verify_token”装饰器来验证令牌。我们来看下代码，为了简化，将 Token 与用户的关系保存在一个字典中：

```python
from flask import Flask, g
from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired

# 初始化实例时不需要传入app对象，也不需要调用auth.init_app(app)注入应用对象
auth = HTTPTokenAuth()

app = Flask(__name__)
# 使用 HTTPTokenAuth 必须设置 SECRET_KEY
app.config['SECRET_KEY'] = '110'
token_serializer = Serializer(app.config['SECRET_KEY'], expires_in=3600)

users = ['jack', 'tom']

for u in users:
    token = token_serializer.dumps({'username': u}).decode('utf-8')
    print('token for {}: {}'.format(u, token))


@auth.verify_token
def verify_token(token):
    g.user = None
    try:
        data = token_serializer.loads(token)
    except BadSignature:
        return False
    except SignatureExpired:
        return False

    if 'username' in data:
        g.user = data['username']
        return True
    return False

@app.route('/')
@auth.login_required
def hello_world():
    return 'Hello {}!'.format(g.user)


if __name__ == '__main__':
    app.run()
```

在”verify_token()”方法里，我们验证传入的Token是否合法，合法的话返回True，否则返回False。另外，我们通过Token获取了用户信息，并保存在全局变量g中，这样视图中可以获取它。

初始化HTTPTokenAuth对象时，我们传入了”scheme=’Bearer'”。这个scheme，就是我们在发送请求时，在HTTP头”Authorization”中要用的scheme字段。

#### 使用itsdangerous库来管理令牌

itsdangerous库提供了对信息加签名（Signature）的功能，我们可以通过它来生成并验证令牌。Flask 默认已经安装。

```python
from flask import Flask, g
from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired

auth = HTTPTokenAuth()

app = Flask(__name__)
app.config['SECRET_KEY'] = '110'
# 我们实例化了一个针对JSON的签名序列化对象 token_serializer
# 它是有时效性的，60分钟后序列化后的签名即会失效
token_serializer = Serializer(app.config['SECRET_KEY'], expires_in=3600)

users = ['jack', 'tom']
for user in users:
    token = token_serializer.dumps({'username': user}).decode('utf-8')
    print('*** token for {}: {}\n'.format(user, token))
```

