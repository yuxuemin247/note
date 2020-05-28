- 概念

WSGI是一个协议，定义了WEB服务器和WEB应用程序之间通信的规范
uWSGI是一个HTTP服务器，把HTTP协议转化成语言支持的网络协议
uwsgi 是一种 uWSGI 的内部协议，使用二进制方式和其他应用程序进行通信。

Nginx 是一个 Web 服务器其中的 HTTP 服务器功能和 uWSGI 功能很类似，但是 Nginx 还可以用作更多用途，比如静态文件处理，反向代理，负载均衡等。

CGI common gateway interfece 通用网关接口    CGI定义了Web服务器与程序间通信的接口标准，使Web服务器可以通过CGI接口执行程序，完成动态请求的处理

django 提供的是一个开发服务器，在安全上和效率上都是不行的