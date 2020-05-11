### 1 镜像命令

- 查看本地镜像
  
- docker images 
  
- 拉取创建镜像
  
- docker pull 镜像名
  
  - dockerfile文件创建出镜像
  
  - 创建基础镜像,创建容器,容器中安装包,容器转换成镜像
  
    ```
    docker镜像是一个配置好的只读层软件环境
    ```
  
-  搜索镜像(https://hub.docker.com/)

  - docker search 镜像名

- 查看镜像详细信息

  - docker inspect 镜像名

- 删除镜像

  - docker rmi 镜像名 

- 将image上传到仓库

  - docker push 容器名
  
- 导出加载镜像

  - docker save 镜像名  > 路径
  - docker load  < 压缩文件路径

### 2 容器(container)

- 查看所有的容器

  -  docker ps -a

- 创建容器

  - docker run  -d --name=容器名 -p  宿主机端口:容器端口 -v 宿主机目录:容器目录 --net 网段名 --ip指定ip   镜像名

    ```
    -it 要跟容器交互
    -d  后台运行
    -p  端口映射
    -v  目录挂载
    -net 指定网段
    -ip 指定ip
    -name 容器名
    ```

  - 创建mysql容器

    ```
    docker run -d -p 3307:3306  --name mysql-master -V /root/docker/mysql/master/conf : /etc/mysql/mysql.conf  -V /root/docker/mysql/master/data : /var/lib/mysql  -V /root/docker/mysql/master/log : var/log/mysql  -e MYSQL_ROOT_PASSWORD=y123456! mysql:5.7
    ```

- 启动某个容器

  docker start 容器名

- 进入运行的容器

  - docker exec  -it 容器名  /bin/bash

    exit 退出,容器并不会退出

- 查看运行的容器

  -  docker ps 

- 查看容器运行日志

  - docker logs 容器名

  - docker logs -f 容器名            类似tailf

- 查看容器的内部进程信息

  - docker top 容器名

- 查看容器详细信息

  - docker inspect  容器名

- 停止,暂停容器

  - docker stop 容器名
  - docker pause 容器名       暂停 
  - docker unpause 容器名  启动暂停的

-  删除容器

  - docker rm 容器名/id

    运行中的Docker容器是无法删除的，必须先通过docker stop或者docker kill命令停止。

- 将container保存为一个imadge

  docker commit  容器名 镜像名

### 3 创建容器的一些技术

- 网络管理技术

  - 创建固定网段

    ```
    docker network create --subnet=172.18.0.0/16 mynet     创建名为mynet的docker内部网段
    
    docker network ls         查看所有网段
    
    docker network rm mynet   删除网段
    
    docker run -it  --net mynet --ip 172.18.0.2
    参数
    	-ip 172.18.0.2
    	#172.18.0.1是网段的网关地址,不能用的
    
    家里用的是民用宽带,ip地址本来就是动态分配的,所有要用云主机
    ```

- 容器端口映射主机端口

  ```
  做了端口映射,其他机器才能访问容器.否则只有宿主机能访问
  docker run -it -p 9500:5000 -p 9600:3306  --name=p1 python3:3.8 bash 
  参数 
  	-p  宿主机端口:容器端口
  	可以映射多个端口
  	-p 宿主机端口1:容器端口1  宿主机端口2:容器端口2
  ```

  

- 目录挂载技术,容器文件和宿主机文件映射

  ```
  docker容器天生就是隔离的,为了把业务数据保存到docker环境外面 ,或者把宿主机的文件传到外面
  所以需要把容器挂载到宿主机的目录,只支持挂载目录,并支持挂载多个目录, 不支持文件挂载 (相互映射)
  docker run -it -v  /root/test:/root/project  python:3.8 bash
  参数 
  	-v  宿主机目录:容器目录
  ```

### docker安装配置

- 避免输出Sudo

  这里把当前用户加入到docker组就可以直接使用命令，而不用每次都加sudo

  $ sudo groupadd docker

  #改完后需要重新登陆用户

  sudo gpasswd -a ${USER} docker

- Docker版本

  sudo docker --version

- 启动docker

  - service docker start

- 创建mysql容器

  ```
  docker run --name 容器名 -p 宿主端口:容器端口 --net 网断名  --ip 172.18.0.3  -v 宿主地址:/var/lib/mysql  -e MYSQL_ROOT_PASSWORD=123456 -d 镜像名
  参数 
  	-e  环境参数
  	-it  在创建mysql容器时不用加,不用自己进入容器中启动容器
  用可视化客户端连接mysql,使用与原有宿主机使用mysql 没有区别,mysql 集群  REplication 和PXC等集群
  ```

- docker容器中 后台运行python

  ```
  nohup python app.pyc > logs.txt  然后直接关闭窗口(别crtul+c)
  所有的容器直接使用宿主机的linux内核,网络配置,并不会完全虚拟环境
  ```

- docker 创建postgres数据库

  ```
  docker run --name postgres1 -e POSTGRES_PASSWORD=password -p 54321:5432 -d postgres:9.4 
  ```
  
