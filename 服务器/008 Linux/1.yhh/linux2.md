# 修改网卡命名规范

​	   a 如何进入到救援模式

```python
修改网卡
1.修改配置文件名称
	/etc/sysconfig/network-scripts/	名称为:ifcfg-xxx
2.修改配置文件内的 device 和name  
	
3.修改内核参数
	vi /etc/sysconfig/grub
	quiet 前加入 net.ifnames=0 biosdevname=0
4.更新参数
	grub2-mkconfig -o /boot/grub2/grub.cfg
5.重启
	shutdown -r now
```



# 远程连接出现异常的排查思路


01. 确保网络链路是否通畅
    ping IP地址信息
	
	解决问题：
	a. 虚拟网络设置是否正确
	b. 虚拟主机网卡设置
	c. 虚拟主机系统中网络地址配置
	d. 在系统的服务中（window+r->services.msc vmware nat services 是否开启）
	e. 确认物理主机上有和虚拟主机相同虚拟网卡信息（地址配置正确）
	
02. 有你的女朋友阻止你
  
	解决问题： 
	a. 网络安全服务进行了阻止（iptables firewalld 防火墙服务）


   03. telnet 地址信息  服务端口号
       ​     
       解决问题：

      	a. 确认远程连接服务是否开启
      	b. 确认服务端口号信息是否发生了变化

2. 操作管理系统必知必会内容
   a. 命令提示符
      [root@oldboysh03-znb ~]# 	   
      熟悉命令提示符组成部分

   b. 命令格式规范（语法规范）
      01. linux中的命令区分大小写
      02. linux命令使用过程中，注意空格的用法

   c. 系统路径信息（目录结构）
      一切从根开始

   d. 路径信息查找方法
      绝对路径：从根开始查找  /etc  /etc/hosts
      缺点：如果层级比较多的时候，利用绝对路径查找数据会比较麻烦
      优点：定位查询数据的准确性更高


      相对路径：不从根开始进行查找， 相对于当前路径而言， 进行查找数据
      优点：如果层级比较多的时候，利用相对路径查找数据会比较方便
      缺点：路径信息不正确，数据无法有效查询到

# 系统操作命令说明

1）系统运行命令

   * 关机命令 
     shutdown
	
	 shutdown -h 10  ---》指定多少分钟后进行关机
	 [root@oldboysh03-znb ~]# shutdown -h 10
     Shutdown scheduled for Tue 2018-12-04 11:32:21 CST, use 'shutdown -c' to cancel.
     关机     方案          什么时间将进行关机            shutdown -c取消关机          
	
     Broadcast message from root@oldboysh03-znb (Tue 2018-12-04 11:22:21 CST): 多用户
	 广播      消息         
     
     The system is going down for power-off at Tue 2018-12-04 11:32:21 CST!
	 系统将在什么时间进行关机

	 shutdown -c    ---》取消关机方案
	 [root@oldboysh03-znb ~]# shutdown -c
     [root@oldboysh03-znb ~]# 
     Broadcast message from root@oldboysh03-znb (Tue 2018-12-04 11:29:42 CST):
	 取消关机信息进行广播
     
     The system shutdown has been cancelled at Tue 2018-12-04 11:30:42 CST!
	 关机方案已经被取消掉了
	
	
	 shutdown -h 0/now  ---》立即关机

   重启命令	   
   shutdown
   shutdown -r 10       ---》指定多少分钟后进行重启
   shutdown -r 0/now    ---》表示进行立即重启操作
   shutdown -c          ---》取消重启方案

# 命令规范	

帮助命令   man  mannual  帮助手册信息
man  命令信息shutdown
命令帮助信息中， 语法中的中括号信息可有可无

补充说明：有些命令是不能通过man手册获取帮助信息 

[root@oldboysh03-znb ~]# man shutdown
SHUTDOWN(8)                                                       shutdown                                                      SHUTDOWN(8)

NAME   第一个部分：简单说明命令的作用
​       shutdown - Halt, power-off or reboot the machine
​	              暂停; 断电 or 重启服务器
​	              
SYNOPSIS 第二个部分：命令使用规范（命令语法）
​       shutdown [OPTIONS...][TIME] [WALL...]

DESCRIPTION  第三个部分：命令的详细描述说明
​       shutdown may be used to halt, power-off or reboot the machine.

OPTIONS   第四个部分：命令的参数说明
​       The following options are understood:

--help
Print a short help text and exit.

-H, --halt
Halt the machine.



# 关机-重启-退出

shutdown

halt 注意避免使用   仅关闭系统 不关闭电源 

poweroff

init 0 

重启:

shutdown - r now 

退出 logout    /  exit

# 系统中的快捷方式使用

01. 显示历史输入命令信息 
    利用方向键 上 下
02. 清楚所有屏幕信息输出
    ctrl + L  clear
03. 中断取消命令执行过程
    ctrl + c  cancel 取消
04. 快速移动光标到行首
    ctrl + a  
05. 快速移动光标到行尾
    ctrl + e   end
06. 将光标所在位置到行首的信息进行删除（剪切）
    ctrl + u 
	将光标所在位置到行尾的信息进行删除（剪切）
	ctrl + k
07. 将剪切内容进行粘贴回来
    ctrl + y
08. 锁定系统窗口信息状态
    ctrl + s
    解锁系统窗口信息状态
    ctrl + q  quit 		
09. 系统命令补全快捷方式
    tab
10. 命令行中快速移动光标
    ctrl + 方向键 左 右 （按照英文单词进行移动光标）



# 和目录结构相关命令




	1）显示当前路径信息  
	   pwd - print working directory	显示当前所在路径
	
	   [root@oldboysh03-znb sysconfig]# pwd
	   /etc/sysconfig
	2）切换目录结构
	   cd  - change directory    改变目录信息
	   cd 你要去往的路径信息
	   
	   ①. 快速切换路径，返回到上一次所在路径信息
	   [root@oldboysh03-znb tmp]# cd /etc/sysconfig/network-scripts/
	   [root@oldboysh03-znb network-scripts]# pwd
	   /etc/sysconfig/network-scripts
	   [root@oldboysh03-znb network-scripts]# cd /tmp/
	   [root@oldboysh03-znb tmp]# pwd
	   /tmp
	   [root@oldboysh03-znb tmp]# cd -
	   /etc/sysconfig/network-scripts
	   [root@oldboysh03-znb network-scripts]# pwd
	   /etc/sysconfig/network-scripts
	   [root@oldboysh03-znb network-scripts]# cd -
	   /tmp
	   
	   ②. 快速切换路径，返回到当前路径的上一级目录中
	   [root@oldboysh03-znb tmp]# cd -
	   /etc/sysconfig/network-scripts
	   [root@oldboysh03-znb network-scripts]# cd ..
	   [root@oldboysh03-znb sysconfig]# pwd
	   /etc/sysconfig
	   [root@oldboysh03-znb sysconfig]# cd -
	   /etc/sysconfig/network-scripts
	   [root@oldboysh03-znb network-scripts]# cd ../..
	   [root@oldboysh03-znb etc]# pwd
	   /etc
	   [root@oldboysh03-znb etc]# cd -
	   /etc/sysconfig/network-scripts
	   [root@oldboysh03-znb network-scripts]# cd ../../../../../../
	   [root@oldboysh03-znb /]# 

​	   
​	   [root@oldboysh03-znb sysconfig]# pwd
​	   /etc/sysconfig
​	   [root@oldboysh03-znb sysconfig]# cd .
​	   [root@oldboysh03-znb sysconfig]# pwd
​	   /etc/sysconfig
​	   [root@oldboysh03-znb sysconfig]# cd ./network-scripts/
​	   [root@oldboysh03-znb network-scripts]# cd -
​	   /etc/sysconfig
​	   [root@oldboysh03-znb sysconfig]# cd network-scripts/
​	   [root@oldboysh03-znb network-scripts]# 
​	   
​	   3. 快速切换路径，返回到当前登陆用户的家目录中
​	   [root@oldboysh03-znb /]# cd /tmp/
​	   [root@oldboysh03-znb tmp]# pwd
​	   /tmp
​	   [root@oldboysh03-znb tmp]# cd ~
​	   [root@oldboysh03-znb ~]# pwd
​	   /root
​	   [root@oldboysh03-znb ~]# cd /etc/sysconfig/network-scripts/
​	   [root@oldboysh03-znb network-scripts]# pwd
​	   /etc/sysconfig/network-scripts
​	   [root@oldboysh03-znb network-scripts]# cd
​	   PS：Linux系统中执行的一些命令，在没有任何消息输出的时候，就是最好的消息
​	
​	3）创建目录信息
​	   make directory == mkdir
​	   [root@oldboysh03-znb ~]# cd /oldboy
​	   -bash: cd: /oldboy: No such file or directory
​	   [root@oldboysh03-znb ~]# mkdir /oldboy
​	   [root@oldboysh03-znb ~]# cd /oldboy
​	   [root@oldboysh03-znb oldboy]# pwd
​	   /oldboy
​	   
​	   需求在已有的/oldboy目录中创建多级目录
​	   [root@oldboysh03-znb oldboy]# mkdir /oldboy/oldgirl/olddog/
​	   mkdir: cannot create directory ‘/oldboy/oldgirl/olddog/’: No such file or directory
​	   [root@oldboysh03-znb oldboy]# mkdir /oldboy/oldgirl/
​	   [root@oldboysh03-znb oldboy]# 
​	   [root@oldboysh03-znb oldboy]# mkdir -p /oldboy/hedanchun/alex
​	   [root@oldboysh03-znb oldboy]# cd /oldboy/hedanchun/alex/
​	   [root@oldboysh03-znb alex]# pwd
​	   /oldboy/hedanchun/alex
​	   [root@oldboysh03-znb alex]# mkdir  /oldboy/hedanchun/alex
​	   mkdir: cannot create directory ‘/oldboy/hedanchun/alex’: File exists
​	   [root@oldboysh03-znb alex]# mkdir -p /oldboy/hedanchun/alex
​	

	   建议创建目录时，以绝对路径创建目录
	   [root@oldboysh03-znb alex]# mkdir oldgirl
	   [root@oldboysh03-znb alex]# ls /oldgirl
	   ls: cannot access /oldgirl: No such file or directory
	   [root@oldboysh03-znb alex]# ls ./
	   oldgirl


# 文件和目录都相关的命令

1）如何创建文件信息
   touch （摸） 

   [root@oldboysh03-znb alex]# cd /oldboy/
   [root@oldboysh03-znb oldboy]# touch oldboy.txt
   或者创建文件方法
   touch /oldboy/oldboy.txt 
   说明：touch命令反复执行不会有报错信息

2）如何检查文件或目录是否存在
   list -- ls 

创建目录或文件信息是否存在

   [root@oldboysh03-znb oldboy]# ls
   hedanchun  oldboy.txt  oldgirl
   [root@oldboysh03-znb oldboy]# ls oldboy.txt 
   oldboy.txt
   [root@oldboysh03-znb oldboy]# ls oldgirl.txt 
   ls: cannot access oldgirl.txt: No such file or directory
   [root@oldboysh03-znb oldboy]# ls
   hedanchun  oldboy.txt  oldgirl
   [root@oldboysh03-znb oldboy]# ls /oldboy
   hedanchun  oldboy.txt  oldgirl
   [root@oldboysh03-znb oldboy]# ls /oldboy/
   hedanchun  oldboy.txt  oldgirl
   [root@oldboysh03-znb oldboy]# ls /oldboy/ -d
   /oldboy/

   显示文件/目录数据详细信息
   [root@oldboysh03-znb oldboy]# ls -l oldboy.txt
   -rw-r--r--. 1 root root 0 Dec  5 10:02 oldboy.txt

   [root@oldboysh03-znb oldboy]# ls -l -d /oldboy
   drwxr-xr-x. 4 root root 56 Dec  5 09:57 /oldboy
   [root@oldboysh03-znb oldboy]# ls -ld /oldboy
   drwxr-xr-x. 4 root root 56 Dec  5 09:57 /oldboy

   按照时间反向排序，显示最新创建的数据信息
   ls -ltr

3）如何查看文件信息
​       cat 查看文件信息命令
​       [root@oldboysh03-znb oldboy]# cat /etc/hosts
​       127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
​       ::1         localhost localhost.localdomain localhost6 localhost6.localdomain6

利用cat命令和整合多个文件信息到一个文件中
​       [root@oldboysh03-znb oldboy]# cat oldgirl.txt 
​       hello world
​       [root@oldboysh03-znb oldboy]# cat oldboy.txt oldgirl.txt 
​       oldboyedu.com
​       oldboyedu02.com
​       hello world
​       [root@oldboysh03-znb oldboy]# cat oldboy.txt oldgirl.txt >olddog.txt
​       [root@oldboysh03-znb oldboy]# cat olddog.txt 
​       oldboyedu.com
​       oldboyedu02.com
​       hello world



4）在空文件中生成据

信息
​       echo   将信息进行输出
​       

       强调：在linux系统中，尽量不要输入中文符号信息（命令行）
       [root@oldboysh03-znb oldboy]# echo "hello world“
       > ^C
       [root@oldboysh03-znb oldboy]# ”“”“’‘’‘’》《【】￥￥￥￥（）

​	   [root@oldboysh03-znb oldboy]# echo hello world
​	   hello world
​	   
​	   # 希望将指定的信息输出到指定文件中
​	   [root@oldboysh03-znb oldboy]# echo hello world > /oldboy/oldboy.txt
​	   [root@oldboysh03-znb oldboy]# cat /oldboy/oldboy.txt 
​	   hello world
​	   [root@oldboysh03-znb oldboy]# echo oldboyedu.com > /oldboy/oldboy.txt
​	   [root@oldboysh03-znb oldboy]# cat /oldboy/oldboy.txt 
​	   oldboyedu.com
​	   [root@oldboysh03-znb oldboy]# echo oldboyedu02.com >> /oldboy/oldboy.txt
​	   [root@oldboysh03-znb oldboy]# cat /oldboy/oldboy.txt 
​	   oldboyedu.com
​	   oldboyedu02.com
​	
​	5）对文件或目录数据信息进行拷贝（复制）
​	   copy --- cp
​	   语法格式  cp 参数信息 要进行复制的信息  复制到什么位置
​	   

	   # 将/etc/hosts文件复制到/oldboy目录中
	   
	   常见问题：
	   在复制文件时，不要再文件名称后面加上/ 一般只有目录后面有/
	   [root@oldboysh03-znb oldboy]# cp /etc/hosts  /oldboy
	   [root@oldboysh03-znb oldboy]# ll /oldboy/
	   total 16
	   drwxr-xr-x. 3 root root  18 Dec  5 09:33 hedanchun
	   -rw-r--r--. 1 root root 158 Dec  5 10:53 hosts
	   -rw-r--r--. 1 root root  30 Dec  5 10:17 oldboy.txt
	   -rw-r--r--. 1 root root  42 Dec  5 10:41 olddog.txt
	   drwxr-xr-x. 2 root root   6 Dec  5 09:31 oldgirl
	   -rw-r--r--. 1 root root  12 Dec  5 10:40 oldgirl.txt
	   [root@oldboysh03-znb oldboy]# cp /etc/hosts  /oldboy01
	   [root@oldboysh03-znb oldboy]# ll /oldboy01
	   -rw-r--r--. 1 root root 158 Dec  5 10:53 /oldboy01
	   
	   正确复制文件方法
	   [root@oldboysh03-znb oldboy]# cp /etc/hosts  /oldboy/
	   cp: overwrite ‘/oldboy/hosts’? y
	   说明：文件没有存在会直接复制， 如果已经存在会提示是否覆盖
	   
	   如何正确复制目录信息
	   [root@oldboysh03-znb oldboy]# cp /etc/sysconfig/  /oldboy/oldgirl/
	   cp: omitting directory ‘/etc/sysconfig/’
	   [root@oldboysh03-znb oldboy]# cp -r /etc/sysconfig/  /oldboy/oldgirl/
	   [root@oldboysh03-znb oldboy]# ll /oldboy/oldgirl
	   total 4
	   drwxr-xr-x. 6 root root 4096 Dec  5 11:03 sysconfig

​	   
​	   [root@oldboysh03-znb oldboy]# cp -a /etc/  /oldboy/oldgirl/
​	   [root@oldboysh03-znb oldboy]# ls /oldboy/oldgirl
​	   etc  sysconfig

# 对文件或目录数据信息进行剪切（移动）

	   move -- mv
		mv 参数 要移动数据信息  移动到什么位置
		移动/etc/selinux/config 到 /oldboy/shanghai/
	   [root@oldboysh03-znb oldboy]# ls /oldboy/shanghai
	   ls: cannot access /oldboy/shanghai: No such file or directory
	   [root@oldboysh03-znb oldboy]# mkdir /oldboy/shanghai
	   [root@oldboysh03-znb oldboy]# mv /etc/selinux/config /oldboy/shanghai/
	   [root@oldboysh03-znb oldboy]# ls /oldboy/shanghai/
	   config
	   
	  
	   [root@oldboysh03-znb oldboy]# mv /etc/selinux/config /oldboy/shanghai/
	   mv: cannot stat ‘/etc/selinux/config’: No such file or directory
	   [root@oldboysh03-znb oldboy]# mv  /oldboy/shanghai/config  /etc/selinux/
	   [root@oldboysh03-znb oldboy]# ls /etc/selinux/
	   config  final  semanage.conf  targeted  tmp
	   
	   可以对文件信息进行重命名操作
	   [root@oldboysh03-znb oldboy]# ls
	   hedanchun  hosts  oldboy.txt  oldboy.txt.bak  olddog.txt  oldgirl  oldgirl.txt  shanghai
	   [root@oldboysh03-znb oldboy]# mv hosts hosts01
	   [root@oldboysh03-znb oldboy]# ls
	   hedanchun  hosts01  oldboy.txt  oldboy.txt.bak  olddog.txt  oldgirl  oldgirl.txt  shanghai
	
	7）数据的删除命令
	   remove -- rm
	   rm 参数 要删除的数据信息
	   
	   # 删除oldboy目录中的hosts01文件
	   [root@oldboysh03-znb oldboy]# ls
	   hedanchun  hosts01  oldboy.txt  oldboy.txt.bak  olddog.txt  oldgirl  oldgirl.txt  shanghai
	   [root@oldboysh03-znb oldboy]# rm hosts01
	   rm: remove regular file ‘hosts01’? y
	   [root@oldboysh03-znb oldboy]# ls
	   hedanchun  oldboy.txt  oldboy.txt.bak  olddog.txt  oldgirl  oldgirl.txt  shanghai
	   
	   # 删除目录操作
	   [root@oldboysh03-znb oldboy]# ls
	   hedanchun  oldboy.txt  oldboy.txt.bak  olddog.txt  oldgirl  oldgirl.txt  shanghai
	   [root@oldboysh03-znb oldboy]# rm shanghai/
	   rm: cannot remove ‘shanghai/’: Is a directory
	   [root@oldboysh03-znb oldboy]# rm -r shanghai/
	   rm: remove directory ‘shanghai/’? y
	   
	   # 如何强制删除数据信息
	   [root@oldboysh03-znb oldboy]# rm -f  olddog.txt
	   [root@oldboysh03-znb oldboy]# ls olddog.txt
	   ls: cannot access olddog.txt: No such file or directory
	   [root@oldboysh03-znb oldboy]# rm -fr hedanchun
	   [root@oldboysh03-znb oldboy]# ls hedanchun -d
	   ls: cannot access hedanchun: No such file or directory
	   
	   [root@oldboysh03-znb oldboy]# rm -fr /  oldboy/oldboy.txt
	   rm: it is dangerous to operate recursively on ‘/’
	   rm: use --no-preserve-root to override this failsafe
	   [root@oldboysh03-znb oldboy]# rm -fr / --no-preserve-root
	   说明：默认从centos6.7 开始就有/目录自我保护机制
# 文本编辑命令说明

vi == nodepad++
vi 你要编辑的文件信息

# 编辑文件的操作步骤
第一个里程：利用vi命令打开文件
vi oldboy.txt 

第二个里程：进入到编辑模式，开始编辑文件
按键盘上 小写字母 i == insert

第三个里程：进行编辑

第四个里程：退出编辑模式
按 esc 进行退出

第五个里程：关闭打开的文件
:wq   w-write  q-quit  保存退出
:q                     不保存进行退出



ESC从编辑模式退出到命令模式   可以使用的命令非常多 参考

https://blog.csdn.net/qq_37896194/article/details/80369432











