from flask import Flask
from flask_restful import Api, Resource

"""

动作      URL         状态码    数据库操作    含义
GET     /posts        200     SELECT      从数据库中查询 blog_posts 表中的人一组数据
POST    /posts        201     INSERT      向 blog_posts 表中插入一条数据

GET     /posts/123    200     SELECT      从 blog_posts 表中查询 id 为 123 的记录
PUT     /posts/123    200     UPDATE      更新 blog_posts 表中 id 为 123 的记录（请求时提供全部字段数据）
PATCH   /posts/123    200     UPDATE      更新 blog_posts 表中 id 为 123 的记录（请求时提供部分字段数据）
DELETE  /posts/123    204     DELETE      删除 blog_posts 表中 id 为 123 的记录 

"""

app = Flask(__name__)
api = Api(app)


class PostList(Resource):
    """
    GET     /posts
    POST    /posts

    flask-restful 的所有请求是通过 类来处理的，继承自 Resource 类
    框架内部会自动根据请求的 HTTP METHOD 调用同名的实例方法
    GET -> def get(self): pass
    POST -> def post(self): pass
    """

    def get(self):
        return '从数据库中查询 blog_posts 表中的人一组数据', 200

    def post(self):
        return '向 blog_posts 表中插入一条数据', 201


class PostDetail(Resource):
    """
    框架内部也支持 url 上配置的 路由参数，路由参数会传递到具体处理请求的实例方法中

    GET     /posts/123      def get(self, post_id): pass
    """

    def get(self, post_id):
        return '从 blog_posts 表中查询 id 为 {} 的记录'.format(post_id), 200

    def put(self, post_id):
        return '更新 blog_posts 表中 id 为 {} 的记录（请求时提供全部字段数据）'.format(post_id), 200

    def patch(self, post_id):
        return '更新 blog_posts 表中 id 为 {} 的记录（请求时提供部分字段数据）'.format(post_id), 200

    def delete(self, post_id):
        return '删除 blog_posts 表中 id 为 {} 的记录'.format(post_id), 204


# api.add_resource(api资源类, 路由地址, endpoint='相当于一个路由名称，比如：blue.login ，可以在 url_for 中使用')
api.add_resource(PostList, '/posts', endpoint='post_list')
api.add_resource(PostDetail, '/posts/<int:post_id>', endpoint='post_detail')


if __name__ == '__main__':
    app.run(debug=True)
