from flask import Blueprint, request, jsonify, abort

from app.models import Channel, db

rest_bp = Blueprint('rest', __name__, url_prefix='/rest')


@rest_bp.route('/')
def hello():
    return 'hello restful'


"""

动作      URL         状态码    数据库操作    含义
GET     /posts        200     SELECT      从数据库中查询 blog_posts 表中的人一组数据
POST    /posts        201     INSERT      向 blog_posts 表中插入一条数据

GET     /posts/123    200     SELECT      从 blog_posts 表中查询 id 为 123 的记录
PUT     /posts/123    200     UPDATE      更新 blog_posts 表中 id 为 123 的记录（请求时提供全部字段数据）
PATCH   /posts/123    200     UPDATE      更新 blog_posts 表中 id 为 123 的记录（请求时提供部分字段数据）
DELETE  /posts/123    204     DELETE      删除 blog_posts 表中 id 为 123 的记录 

"""


# /posts -> /rest/posts
@rest_bp.route('/posts', methods=['GET', 'POST'])
def post_list():
    if request.method == 'POST':
        return '向 blog_posts 表中插入一条数据', 201
    elif request.method == 'GET':
        return '从数据库中查询 blog_posts 表中的人一组数据', 200


@rest_bp.route('/posts/<post_id>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def post_detail(post_id):
    if request.method == 'GET':
        return '从 blog_posts 表中查询 id 为 {} 的记录'.format(post_id), 200
    elif request.method == 'PUT':
        return '更新 blog_posts 表中 id 为 {} 的记录（请求时提供全部字段数据）'.format(post_id), 200
    elif request.method == 'PATCH':
        return '更新 blog_posts 表中 id 为 {} 的记录（请求时提供部分字段数据）'.format(post_id), 200
    elif request.method == 'DELETE':
        return '删除 blog_posts 表中 id 为 {} 的记录'.format(post_id), 204


# /rest/channels
@rest_bp.route('/channels', methods=['GET', 'POST'])
def channel_list():
    if request.method == 'POST':
        """
        POST /channels
        
        {"name": "科技", "sort": 1}
        
        注意 postman/前端 在向服务器提交 json 数据时，需要声明提交的类型
        在 请求的 headers 增加 content-type: application/json
        flask 在确认请求数据是通过 json 提交之后，会将 json 字符串转换成 字典，保存在 request.json 中
        
        """
        # print(request.data)
        # print(request.json)

        if 'name' not in request.json or 'sort' not in request.json:
            return abort(400)

        channel = Channel()
        channel.name = request.json['name']
        channel.sort = request.json['sort']

        db.session.add(channel)
        db.session.commit()

        return jsonify({'channel': channel.to_dict()}), 201

    # 数据库查询返回的是 list 类型的数据
    _channels = Channel.query.all()
    channels = [channel.to_dict() for channel in _channels]

    # flask 视图函数只能返回 str 或 response 对象
    # 我们可以将数据库查询出来的数据 转换成 json，以满足 flask 视图函数的返回要求

    ret = {
        'channels': channels
    }

    # import json
    # json_str = json.dumps(ret)
    # return json_str

    return jsonify(ret), 200


# /rest/channels/123
@rest_bp.route('/channels/<channel_id>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def channel_detail(channel_id):
    channel = Channel.query.get(channel_id)

    if channel is None:
        return abort(404)

    if request.method == 'GET':
        return jsonify({'channel': channel.to_dict()}), 200
    elif request.method == 'PUT':
        if 'name' not in request.json or 'sort' not in request.json:
            return abort(400)

        channel.name = request.json['name']
        channel.sort = request.json['sort']

        db.session.commit()

        return jsonify({'channel': channel.to_dict()}), 200
    elif request.method == 'PATCH':

        # name = channel.name
        #
        # if 'name' in request.json:
        #     name = request.json['name']
        #
        # channel.name = name

        channel.name = request.json.get('name', channel.name)
        channel.sort = request.json.get('sort', channel.sort)

        db.session.commit()

        return jsonify({'channel': channel.to_dict()}), 200
    elif request.method == 'DELETE':
        db.session.delete(channel)
        db.session.commit()

        return '', 204
