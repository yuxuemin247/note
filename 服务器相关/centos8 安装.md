##### 修改服务器主机名

-  sudo hostnamectl set-hostname yu

##### 安装mysql

-  sudo dnf install @mysql   # 使用最新的包管理器安装MySQL 

- sudo systemctl enable --now mysqld    # 启动MySQL服务并使它在启动时自动启动 

-  sudo systemctl status mysqld    # 检查MySQL服务器是否正在运行 

- 添加密码和安全设置

  ```
  sudo mysql_secure_installation
  要求你配置VALIDATE PASSWORD component（验证密码组件:输入y ，回车进入该配置
  选择密码验证策略等级， 我这里选择0 （low），回车
  输入新密码两次
  确认是否继续使用提供的密码？输入y ，回车
  移除匿名用户？ 输入y ，回车
  不允许root远程登陆？ 我这里需要远程登陆，所以输入n ，回车
  移除test数据库？ 输入y ，回车
  重新载入权限表？ 输入y ，回车
  ```

- 配置root可以远程登录

  ```
  mysql -uroot -p密码      #进入mysql
  use mysql;
  update user set host='%' where user='root';  #将将root用户的host字段设为'%',意为接受root所有IP地址的登录请求
  flush privileges; 
  exit退出mysql，回到终端shell界面，接着开启系统防火墙的3306端口：
  sudo firewall-cmd --add-port=3306/tcp --permanent
  sudo firewall-cmd --reload
  ```

- 关闭MySQL主机查询dns

  ```
  MySQL会反向解析远程连接地址的dns记录，如果MySQL主机无法连接外网，则dns可能无法解析成功，导致第一次连接MySQL速度很慢，所以在配置中可以关闭该功能
  打开/etc/my.cnf文件，添加以下配置：
  [mysqld]
  skip-name-resolve
  ```

##### 安装docker

- curl https://download.docker.com/linux/centos/docker-ce.repo -o /etc/yum.repos.d/docker-ce.repo  #下载docker-ce的repo
- yum install https://download.docker.com/linux/fedora/30/x86_64/stable/Packages/containerd.io-1.2.6-3.3.fc30.x86_64.rpm   #安装依赖l
- yum install docker-ce -y     #安装docker-ce
- systemctl start docker        #启动docker
- docker info                          #查看版本信息



安装软件的三种方法：

- 包管理工具 

  - yum

    ```
    yum search 
    yum install 
    yum remove/ yum erase  
    yum update
    yum info
    yum list installed 
    ```

- 源代码构建安装

  - ```
    make
    make install
    ```

- 二进制程序

  - 下载解压

一个查看命令的软件：

- ```
  安装node.js:  yum install -y node.js
  更换下载源：   npm config set registry https://registry.npm.taobao.org/
  更新NPM:      npm install -g npm
  安装tldr:     npm install -g tldr
  tldr nginx指令
  ```

  