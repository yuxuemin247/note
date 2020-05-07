# FHS

在早期的 UNIX 系统中，各个厂家各自定义了自己的 UNIX 系统文件目录，比较混乱。Linux 面世不久后，对文件目录进行了标准化，于1994年对根文件目录做了统一的规范，推出 FHS ( Filesystem Hierarchy Standard ) 的 Linux 文件系统层次结构标准。FHS 标准规定了 Linux 根目录各文件夹的名称及作用，统一了Linux界命名混乱的局面。

`FHS` 是根据以往无数 Linux 用户和开发者的经验总结出来的，并且会维持更新!

无论何种版本的 Linux 发行版，桌面、应用是 Linux 的外衣，文件组织、目录结构才是Linux的内心。



# 与windows的区别

windows系统下,通常会有多个盘符,路径的起始是盘符,而在linux中,没有盘符一切都从根开始,

这看起来就像一棵树形结构,就像下图:

![78f9859egw1etbt8f77f2j20io0bsgm4](https://ws4.sinaimg.cn/large/006tNc79gy1g2pkqyn76jj30io0bsgm4.jpg)

# 挂载

那其他磁盘的数据如何访问呢?,通过挂载到某个目录下来访问外置的设备,通常挂载到在mnt或是media目录下

挂载指的是使操作系统可以访问某一个存储设备的的过程,简单的是说就是分配一个路径给存储设备,等同于windows下的指定盘符!

# 目录详解:

```python
目录	说明	备注
bin	存放普通用户可执行的指令	
boot	开机引导目录	包括Linux内核文件与开机所需要的文件
dev	设备目录	所有的硬件设备及周边均放置在这个设备目录中
etc	各种配置文件目录	大部分配置属性均存放在这里
lib/lib64	开机时常用的动态链接库	bin及sbin指令也会调用对应的lib库
media	可移除设备挂载目录	类似软盘 U盘 光盘等临时挂放目录
mnt	用户临时挂载其他的文件系统	额外的设备可挂载在这里,相对临时而言
opt	第三方软件安装目录	现在习惯性的放置在/usr/local中
proc 虚拟文件系统	通常是内存中的映射,特别注意在误删除数据文件后，比如DB，只要系统不重启,还是有很大几率能将数据找回来 
root	系统管理员主目录	除root之外,其他用户均放置在/home目录下
run	系统运行是所需文件	以前防止在/var/run中,后来拆分成独立的/run目录。重启后重新生成对应的目录数据
sbin	只有root才能运行的管理指令	跟bin类似,但只属于root管理员
snap	ubunut全新软件包管理方式	snap软件包一般在/snap这个目录下
srv	服务启动后需要访问的数据目录	
lost+found这个目录平时是空的，系统非正常关机而留下“无家可归”的文件(windows下叫什么.chk)就在这里
sys	跟proc一样虚拟文件系统	记录核心系统硬件信息
tmp	存放临时文件目录	所有用户对该目录均可读写
usr	应用程序放置目录	
var 包括系统一般运行时要改变的数据.例如各种日志记录,邮件来往等,每个系统是特定的，不通过网络与其他计算机共享.
```

# etc下文件的重要文件

![image-20190504212457401](https://ws4.sinaimg.cn/large/006tNc79gy1g2plr3oomsj30ef0h979h.jpg)

![image-20190504212511319](/Users/jerry/Library/Application Support/typora-user-images/image-20190504212511319.png)

# 网卡配置详解

![image-20190504212753587](https://ws4.sinaimg.cn/large/006tNc79gy1g2plu54do7j30jd0ftgqk.jpg)

![image-20190504212801451](/Users/jerry/Library/Application Support/typora-user-images/image-20190504212801451.png)

DNS也可以在/etc/resolv.conf中进行配置

![image-20190504214613089](https://ws3.sinaimg.cn/large/006tNc79gy1g2pmd6sb2mj30ce02et8t.jpg)

![image-20190504214617739](/Users/jerry/Library/Application Support/typora-user-images/image-20190504214617739.png)

**注意key的名称**

当在network-scripts下配置之后,重启网卡会自动覆盖resolv.conf中的配置,我们可以用PEERDNS参数指定是否覆盖resolv.conf中的信息,但是最终使用的还是resolv.conf中的信息

另外resolv.conf中的配置修改了之后是立即生效的



# 主机名称的获取与修改

#### 获取主机名称

uname -n

hostname

#### 获取全部系统信息

uname -a    

hostnamectl  #更详细

#### 设置主机名称

hostnamectl  set-hostname  name

重新连接生效 也可以使用bash创建子shell 是一个新的会话环境所以可以立即显示新的主机名称

bash 可以不用重启

# 字符编码设置

#### 查看当前字符集

​	echo $LANG

​	$表示表示要查看某个环境变量 变量名称为LANG



#### 临时修改字符集

​	export LANG=en_US.UTF-8		

​	export 命令可以修改当前会话下某个环境变量的值,登出后失效



#### 测试是否生效

​	type if 

​	type 是用于输出某个值的类型 与py的type类似,查看其是否显示英文/中文



#### 永久修改字符集

​	1.修改配置文件

​	vim /etc/locale.conf

​	2.命令行修改

​	localectl set-locale LANG=en_US.UTF-8

​	**注意**:以上两种方式修改后都不会立即生效,需要重新加载配置文件

​	source /etc/locale.conf # 当然重新启动也可以

# 修改运行级别

运行级别用于控制系统运行在何种状态下

#### 查看当前级别

​	查看详细信息

​	ll /etc/systemd/system/default.target

​	vim /etc/systemd/system/default.target

​	仅级别

​	systemctl get-default

 	runlevel  #centos 6

#### 查看所有可用级别

​	ll /usr/lib/systemd/system/runlevel*.target

​	ll /etc/inittab  #centos 6

#### 修改当前级别

​	init 5  # 修改为第五个级别,使用systemctl get-default来查看效果,发现该方式在centos7下不生效

​	systemctl set-default graphical.target 

​	graphical.target 也可以修改为文件名称

​	systemctl set-default runlevel3.target

​	**注意**:通常运行在3级别

​	

# 设置别名

别名指的是 给某个指令设置别名,可用简化命令的编写,或是提供额外的功能

例如 系统的在执行删除指令前都会先提示,其实就是使用了别名,

#### 查看别名

​	alias

#### 设置新的别名(临时)

​	alias rm='echo rm is dangerouse be careful'   # 执行rm时仅提示信息

​	注意:被替换的也一定是一个命令,所以当你要输出内容时,就用echo

​	alias rm='echo rm is dangerouse be careful;rm -f' # 执行rm时提示信息  并删除	

#### 设置新的别名(永久)

​	在配置文件中编写 设置别名的指令

​	vim /etc/profile

​	![image-20190504233728674](https://ws2.sinaimg.cn/large/006tNc79gy1g2ppkyoc4tj306v03wt8r.jpg)

![image-20190504233733838](/Users/jerry/Library/Application Support/typora-user-images/image-20190504233733838.png)

退出vmi,重新加载文件

source /etc/profile

如果别名与系统重复,需要注释其中一个

vim ~/.bashrc 

注释同名的  `#alias rm ='rm -i'`

source  ~/.bashrc 



# 系统默认配置文件(环境变量)

1.全局的

/etc/profile    该文件在用户登录时加载  无论哪个用户 

/etc/bashrc   该文件在系统启动时自动加载   无论哪个用户 

2.用户自己的   只针对某个用户有效

~/.bash_profile

~/.bashrc 







# 设置变量  环境变量

#### 查看所有变量

env

#### 查看某个变量

echo $变量名称

#### 设置临时变量

export  变量名=值

#### 设置永久变量

将变量的定义放到某个环境变量文件中

vim /etc/profile

MYNAME=jerry

测试

echo $MYNAME

### 取别名的优化案例:

```shell
cat >>/etc/profile.d/color.sh<<"EOF"
alias ll='ls -l --color=auto --time-style=long-iso'
PS1='\[\e[32;1m\][\u@\h \W]\$ \[\e[0m\]'
EOF
source  /etc/profile
```



# usr目录

/usr/local 编译安装软件默认的路径

/usr/src 存放源码文件的路径

# 软件安装

## yum方式

yum是通常发行版的linux系统都内置了yum包管理器,使用它可以很方便的管理软件包,必须联网使用

#### 安装

yum install -y sl

#### 搜索

yum search sl

#### 删除

yum remove sl

#### 查看命令所在软件包

yum provides sl

#### 查看源仓库

yum repolist

## rpm方式

全称 redhat packages manager ,是一个本地的包管理器,需要提供安装文件

**1.安装一个rpm包：**

用法：`rpm -ivh rpm_name`

参数解释：
-i（install）：安装软件包。
-v（verbose）：显示安装的过程信息。可视化。
-h（hash）：软件安装的时候列出哈希标记。即显示安装进度。
另外在安装一个rpm包时常用的附带参数有：
--force : 强制安装，即使覆盖属于其他包的文件也要安装



**2.卸载一个rpm包**

命令：`rpm -e filename`

**3.查询一个包是否安装：**

命令：`rpm -qa rpm包名`

**4.列出一个rpm包安装的所有文件**

命令 `rpm -ql 包名`

**5.列出一个rpm包的配置文件**

命令 `rpm -qc 包名`

**6.查看命令所在的绝对路径**

which netstat

**7.查看文件归属软件包**

rpm -qf /usr/bin/netstat



# 编译安装源码

当我们下载的是一个tar的源码文件时,需要先编译后才能进行安装,详见笔记:

# var

![image-20190505021514795](https://ws1.sinaimg.cn/large/006tNc79gy1g2pu53x1m9j30df03twf5.jpg)

![image-20190505021519083](/Users/jerry/Library/Application Support/typora-user-images/image-20190505021519083.png)

# porc  

![image-20190505021544971](https://ws4.sinaimg.cn/large/006tNc79gy1g2pu5mj40yj30dq03paar.jpg)

![image-20190505021548426](/Users/jerry/Library/Application Support/typora-user-images/image-20190505021548426.png)

查看负载信息

​	w

​	uptime



# dev

![image-20190505022451662](https://ws1.sinaimg.cn/large/006tNc79gy1g2puf42nt6j30fu044js3.jpg)

![image-20190505022459923](/Users/jerry/Library/Application Support/typora-user-images/image-20190505022459923.png)

zero 可以用中读取任一大小的null 空数据,用于模拟数据流,或是作为黑洞设备,创建大文件,测试传输速率等

null 将一些不需要的数据重定向到该设备,以避免打印信息到屏幕

# centOS启动流程

纯了解

https://blog.csdn.net/qq_27754983/article/details/75212666

https://www.processon.com/view/link/5bffde0ae4b0f012f2382181

















processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 158
model name	: Intel(R) Core(TM) i5-7400 CPU @ 3.00GHz
stepping	: 9
microcode	: 0x84
cpu MHz		: 3000.004
cache size	: 6144 KB
physical id	: 0
siblings	: 1
core id		: 0
cpu cores	: 1
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 22
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts mmx fxsr sse sse2 ss syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts nopl xtopology tsc_reliable nonstop_tsc aperfmperf eagerfpu pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch epb fsgsbase tsc_adjust bmi1 avx2 smep bmi2 invpcid rdseed adx smap xsaveopt xsavec xgetbv1 dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp
bogomips	: 6000.00
clflush size	: 64
cache_alignment	: 64
address sizes	: 42 bits physical, 48 bits virtual
power management:

processor	: 1
vendor_id	: GenuineIntel
cpu family	: 6
model		: 158
model name	: Intel(R) Core(TM) i5-7400 CPU @ 3.00GHz
stepping	: 9
microcode	: 0x84
cpu MHz		: 3000.004
cache size	: 6144 KB
physical id	: 0
siblings	: 1
core id		: 0
cpu cores	: 1
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 22
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts mmx fxsr sse sse2 ss syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts nopl xtopology tsc_reliable nonstop_tsc aperfmperf eagerfpu pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch epb fsgsbase tsc_adjust bmi1 avx2 smep bmi2 invpcid rdseed adx smap xsaveopt xsavec xgetbv1 dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp
bogomips	: 6000.00
clflush size	: 64
cache_alignment	: 64
address sizes	: 42 bits physical, 48 bits virtual
power management:































 













