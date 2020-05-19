

#### 1、软件安装

- 包管理工具

  - yum

    ```
    yum search 
    yum install 
    yum remove/ yum erase  
    yum updat
    yum info
    yum list installed 
    ```

  - rpm (`Rehat package Manager`)

    ```
    rpm -ivh
    rpm -e
    rpm -qa
    ```

    

- 源代码安装

  - ```
    make && make install 
    ```

- 二进制程序

  - ```
    下载解压即可
    ```

#### 2、其他修改

- 修改服务器主机名

  ```
  sudo hostnamectl set-hostname yu
  ```

- 查看命令帮助的软件：

  ```
  安装node.js:  yum install -y node.js
  更换下载源：    npm config set registry https://registry.npm.taobao.org/
  更新NPM:      npm install -g npm
  安装tldr:     npm install -g tldr
  使用：         tldr nginx指令
  ```

#### 3、安装docker

- 方式一

  - 更新底层库

    ```
    yum install
    ```

  - 移除可能存在的旧Docker版本

    ```
    yum erase -y docker docker-common docker-engine
    ```

  - 安装docker

    ```
    yum install -y docker 
    ```

  - 启动docker服务,查看版本

    ```
    systemctl start docker
    docker --version
    ```

    





