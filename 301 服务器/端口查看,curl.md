##### 1、lsof

lsof(list open files)是一个列出当前系统打开文件的工具。

在linux环境下，任何事物都以文件的形式存在，通过文件不仅仅可以访问常规数据，还可以访问网络连接和硬件。所以如传输控制协议(TCP)和用户数据报协议(UDP)套接字等，系统在后台都为该应用程序分配了一个文件描述符。

无论这个文件的本质是什么，该文件描述符为应用程序与基础操作系统之间的交互提供了通用接口。
应用程序打开文件的描述符提供了大量关于这个应用程序本身的信息，因此可以通过lsof工具能够查看这个列表对系统监测以及排错由很大帮助

- lsof 查看端口占用语法格式：

  ```
  lsof -i:端口号
  查看服务器 8000 端口的占用情况：
   sudo lsof -i:8000
   #lsof -i 需要 root 用户的权限来执行
  
  COMMAND   PID USER   FD   TYPE   DEVICE SIZE/OFF NODE NAME
  nodejs  26993 root   10u  IPv4 37999514      0t0  TCP *:8000 (LISTEN)
  可以看到 8000 端口已经被轻 nodejs 服务占用。
  
  ```

- 更多 lsof 的命令如下：

  ```
  lsof -i:8080：查看8080端口占用
  lsof abc.txt：显示开启文件abc.txt的进程
  lsof -c abc：显示abc进程现在打开的文件
  lsof -c -p 1234：列出进程号为1234的进程所打开的文件
  lsof -g gid：显示归属gid的进程情况
  lsof +d /usr/local/：显示目录下被进程开启的文件
  lsof +D /usr/local/：同上，但是会搜索目录下的目录，时间较长
  lsof -d 4：显示使用fd为4的进程
  lsof -i -U：显示所有打开的端口和UNIX domain文件
  ```
  
  

##### 2、netstat

```
netstat -tunlp 用于显示 tcp，udp 的端口和进程等相关情况。
netstat 查看端口占用语法格式：

netstat -tunlp | grep 端口号
-t (tcp) 仅显示tcp相关选项
-u (udp)仅显示udp相关选项
-n 拒绝显示别名，能显示数字的全部转化为数字
-l 仅列出在Listen(监听)的服务状态
-p 显示建立相关链接的程序名
例如查看 8000 端口的情况，使用以下命令：

###### netstat -tunlp | grep 8000
tcp        0      0 0.0.0.0:8000            0.0.0.0:*               LISTEN      26993/nodejs   
更多命令：
kill 在查到端口占用的进程后，如果你要杀掉对应的进程可以使用 kill 命令：

kill -9 PID
如上实例，我们看到 8000 端口对应的 PID 为 26993，使用以下命令杀死进程：
kill -9 26993

nginx -v 查看nginx版本号
nginx -V 选项查看当前都配置了哪些模块
ps -ef | grep nginx  master process 后跟的 是可执行文件， -c后跟的就是配置文件。
```

##### 3、curl

- get 请求

  ```
  curl  请求地址
  curl  http://ip:port/xx/?a=1\&b=2  
  # &会转义，浏览器器中我们多个变量连接是&&
  -v  详细的请求信息
  -X  指定请求方法
  -H  指定请求头
  ```

- POST请求

  ```
  #一个普通的 post带两个参数请求：
  url http://ip:port/xx  -X POST -d "a=1&b=2"
  
  但是，当我们的接口都是 json 格式的时候，我们可以用 -H 参数来申明请求的 header
  curl http://ip:port/xx  -X POST -H "Content-Type:application/json" -d '{"a:'1','b':'2'"}'
  
  我们可以用 -H 来设置更多的 header ，同样，我们也可以用 -v 来查看详细的请求信息
  上面的两种请求，都是只传输字符串数据
  ```

- 上传文件

  ```
  我们添加参数 -F "file=@FILE_PATH" 传输文件即可
  curl http://ip:port/xx  -F " file=@/Users/local/imgs/my.png"  -v
  ```

##### 4、 wget

- ```
  wget http://ip:port/xx?a=1\&b=2\&type=1
  wget下载比较厉害，支持断点
  curl支持复杂的，就是一个精简的命令行浏览器
  ```
