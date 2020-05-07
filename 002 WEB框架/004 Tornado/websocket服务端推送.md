  一、websocket介绍

- websocket是一种在单个TCP连接上进行全双工通信的协议
- 为什么又了HTTP协议，还需要websocket协议？
  - 因为HTTP协议有一个缺陷，通信只能由客户端向服务端发出请求，服务器返回查询结果。HTTP协议做不到服务器主动向客户端推送消息。(目前HTTP2.0推送能实现请求一次，将一些css、js一起发到浏览器缓存)
  - 这种单向请求的特点，注定了如果服务器有连续的状态变化，客户端要获知就非常麻烦。我们只能使用轮询，比如每隔一秒发出一个请求。( 不论不停连接，或者 HTTP 连接始终打开，非常浪费资源 )
-  服务器可以主动向客户端推送信息，客户端也可以主动向服务器发送信息，是真正的双向平等对话，属于服务器推送技术的一种。 

二、websocket特点

- 建立在TCP协议之上，服务器端的实现比较容易
- 与HTTP协议有着良好的兼容性。默认端口也是80和443，并且握手阶段采用HTTP协议，因此握手时不容易屏蔽，能通过各种HTTP代理服务器
- 数据格式比较轻量，性能开销小，通信高效
- 可以发送文本，也可以发送二进制数据
- 没有同源限制，客户端可以与任意服务器通信
- 协议标识符是ws(如果加密，则为wss)

三、基于tornado实现的web聊天室

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import uuid
import json
import tornado.ioloop
import tornado.web
import tornado.websocket
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
class ChatHandler(tornado.websocket.WebSocketHandler):
    # 用户存储当前聊天室用户
    waiters = set()
    # 用于存储历时消息
    messages = []
    def open(self):
        """
        客户端连接成功时，自动执行
        :return: 
        """
        ChatHandler.waiters.add(self)
        uid = str(uuid.uuid4())
        self.write_message(uid)
        for msg in ChatHandler.messages:
            content = self.render_string('message.html', **msg)
            self.write_message(content)
    def on_message(self, message):
        """
        客户端连发送消息时，自动执行
        :param message: 
        :return: 
        """
        msg = json.loads(message)
        ChatHandler.messages.append(msg)
        for client in ChatHandler.waiters:
            content = client.render_string('message.html', **msg)
            client.write_message(content)
    def on_close(self):
        """
        客户端关闭连接时，，自动执行
        :return: 
        """
        ChatHandler.waiters.remove(self)
def run():
    settings = {
        'template_path': 'templates',
        'static_path': 'static',
    }
    application = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/chat", ChatHandler),
    ], **settings)
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
if __name__ == "__main__":
    run()
```

 index.html 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Python聊天室</title>
</head>
<body>
    <div>
        <input type="text" id="txt"/>
        <input type="button" id="btn" value="提交" onclick="sendMsg();"/>
        <input type="button" id="close" value="关闭连接" onclick="closeConn();"/>
    </div>
    <div id="container" style="border: 1px solid #dddddd;margin: 20px;min-height: 500px;">
    </div>
    <script src="/static/jquery-2.1.4.min.js"></script>
    <script type="text/javascript">
        $(function () {
            wsUpdater.start();
        });
        var wsUpdater = {
            socket: null,
            uid: null,
            start: function() {
                var url = "ws://127.0.0.1:8888/chat";
                wsUpdater.socket = new WebSocket(url);
                wsUpdater.socket.onmessage = function(event) {
                    console.log(event);
                    if(wsUpdater.uid){
                        wsUpdater.showMessage(event.data);
                    }else{
                        wsUpdater.uid = event.data;
                    }
                }
            },
            showMessage: function(content) {
                $('#container').append(content);
            }
        };
        function sendMsg() {
            var msg = {
                uid: wsUpdater.uid,
                message: $("#txt").val()
            };
            wsUpdater.socket.send(JSON.stringify(msg));
        }
</script>
</body>
</html>
```

message.html

```
<div style="border: 1px solid #dddddd;margin: 10px;">
    <div>游客{{uid}}</div>
    <div style="margin-left: 20px;">{{message}}</div>
</div>
```
