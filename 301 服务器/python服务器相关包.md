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

### 5、subprocess

subprocess 模块允许你生成新的进程，连接它们的输入、输出、错误管道，并且获取它们的返回码。此模块打算代替一些老旧的模块与功能：os.system,os.spawn*

subprocess 提供了 call、check_call、check_output 这三个函数，作用都是执行命令，只不过返回值不同。chekout_output返回执行结果，call和check_call返回 状态码（0）。

### 6、OS

- os.path

  ```
  print(os.path.abspath('.'))  #到文件夹的绝对路径，不包括文件名称
  print(__file__)              #文件名
  print(sys.argv)  获取命令行输入的参数
  os.path.split() #按照路径将文件名和路径分割开
  ```

- os.system()

  os.spawnv() 也是 os 模块提供的一个执行命令的内置功能函数。不同于 os.system() 只能执行 shell 命令，os.spawnv() 可以执行任何“可执行”文件，包括 C 编译后的可执行文件，以及 Python 可以执行文件，当然也包括了 shell 命令。

  ```
  os.system("ls -a")
  ```

- os.popen() 

  用于从一个命令打开一个管道。

- os.walk

  test_os/
  ├── 1
  │   ├── 1.txt
  │   └── 3
  │       └── 3.txt
  └── 2
      ├── 2.txt
      └── 4
          └── 4.txt

  ```
  for root,dirs,files in os.walk("./test_os",topdown=True):
  	print(root)
      print(dirs)
      print(files)
  #root 所指的是当前正在遍历的这个文件夹的本身的地址
  #dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
  #files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
  ./test_os
  ['1', '2']
  []
  --------------------
  ./test_os/1
  ['3']
  ['1.txt']
  --------------------
  ./test_os/1/3
  []
  ['3.txt']
  --------------------
  ./test_os/2
  ['4']
  ['2.txt']
  --------------------
  ./test_os/2/4
  []
  ['4.txt']
  --------------------
  ```

### 7、 sys

- sys.stdin.read（） 

  python的标准输入，可以输入多行。输入完成按 ctrl + d