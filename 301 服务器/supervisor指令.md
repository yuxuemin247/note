`sueprvisor`是一个Linux/Unix系统上的进程监控工具,由`python2`开发的进程管理程序，能将一个普通的命令行进程变为后台daemon，并监控进程状态，异常时可以自动重启。不能同`daemontools`一样，它不能监控daemon进程

##### 一、为什么用supervisor

- supervisor提供了一种统一的方式来start、stop、restart 你的进程，进程可以单独控制，也可以成组的控制。可以通过本地命令行`supervisorctl`和web接口来管理。
- 集中管理 supervisor管理的进程，进程组信息，全部都写在一个ini格式的文件里就OK了

##### 二、supervisor组件

- `supervisord` 主进程，负责管理进程的server,它会根据配置文件创建指定数量的应用程序的子进程，管理子进程的整个生命周期。同时内置了web server和`XML-RPC Interface`，轻松实现进程管理。该服务的默认配置文件在`/etc/supervisor/supervisord.conf`

  - 启动服务

    ```
    supervisord -c xxx.conf
    ```

- `supervisorctl`客户端的命令行工具，提供了一个类似shell的操作接口，通过它你可以连接到不同的`supervisord`进程来管理它们各自的子程序，命令通过UNIX socket 或者TCP来和服务通讯。用户可以通过命令行发送消息给`supervisord`，可以查看进程状态，加载配置文件，查看进程标准输出和错误输出。服务端也可以要求客户端提供身份验证之后才能操作。

  - ##### 进入客户端操作

    ```
    supervisorctl 
    ```

  - ##### 查看任务状态

    ```
    supervisorctl status
    第一列是服务名；第二列是运行状态，RUNNING表示运行中，FATAL 表示运行失败，STARTING表示正在启动,STOPED表示任务已停止；　第三/四列是进程号,最后是任务已经运行的时间。
    ```

  - ##### 启动任务

    ```
    supervisorctl  start 服务名
    ```

  - ##### 停止任务

    ```
    supervisorctl  stop 服务名
    ```

  - ##### 重启任务

    ```
    supervisorctl restart 服务名
    ```

  - ##### 更新新的配置文件到`supervisord`（不会重启原来已运行的程序）

    ```
    supervisorctl update 
    ```

  - ##### 载入所有配置文件，并按新的配置启动、管理所有进程(会重启原来已运行的程序)，重启supervisord

    ```
    supervisorctl reload
    ```

  - ##### 重启所有或进程组

    ```
    start all(或组名)
    stop  all(或组名)
    restart all(或组名)
    ```
  
  注： 能 supervisorctl、 celery 这样执行是因为 有个可执行文件，而可执行文件其实用python解释器执行

