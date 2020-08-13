### 1、psutil

一个开源切跨平台的库，其提供了便利的函数用来获取操作系统的信息，比如CPU，内存，磁盘，网络等。此外，psutil还可以用来进行进程管理，包括判断进程是否存在、获取进程列表、获取进程详细信息等。而且psutil还提供了许多命令行工具提供的功能，包括：ps，top，lsof，netstat，ifconfig， who，df，kill，free，nice，ionice，iostat，iotop，uptime，pidof，tty，taskset，pmap。

### 2、pyinotify

是一个python模块，用来监测文件系统的变化。Pyinotify依赖于Linux内核的功能—inotify（支持文件更改通知机制）

### 3、pathlib

 是Python内置库，Python 文档给它的定义是 Object-oriented filesystem paths（面向对象的文件系统路径）

### 4、pwd

pwd模块提供了一个unix密码数据库即/etc/passwd的操作接口，这个数据库包含本地机器用户帐户信息

pwd.getpwnam(name)：返回对应name的用户信息

os.chroot(path);
os.chroot() 方法用于更改当前进程的根目录为指定的目录，使用该函数需要管理员权限。

