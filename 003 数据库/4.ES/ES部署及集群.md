## 一、Docker部署ES

- 拉取ES镜像

  ```
  docker pull elasticsearch
  ```

- 创建容器

  ```
  docker run -d --name es -e 'ES_JAVA_OPTS=-Xms128m -Xmx128m' -p 9200:9200 elasticsearch
  
  ES_JAVA_OPTS=-Xms128m -Xmx128m是指定内存，新版默认是1G
  discovery=single-node 
  ```

- 参数配置

  关于 `vm.max_map_count` 内核参数， 在产品模式下，至少设置为 262144

  - Linux

    ```
    $ grep vm.max_map_count /etc/sysctl.conf
    vm.max_map_count=262144
    sysctl -w vm.max_map_count=262144
    ```

## 二、集群配置

### 2.1 准备数据装载目录及配置文件

**创建数据挂载的目录**

```sh
mkdir -p es/config
```

`-p`表示递归创建es及`config`目录

**进入es目录下创建三个数据节点目录**

```shell
cd es
mkdir data1 data2 data3
```

**修改各个数据节点目录的文件权限为 775**

```sh
chmod 775 data1 data2 data3
```

在`config`目录下，创建与`data1..3`对应的三个配置文件。

es1.yml

```yaml
cluster.name: elasticsearch-cluster
node.name: es-node1
network.bind_host: 0.0.0.0
network.publish_host: 39.100.114.253
http.port: 9200
transport.tcp.port: 9300
http.cors.enabled: true
http.cors.allow-origin: "*"
node.master: true 
node.data: true  
discovery.zen.ping.unicast.hosts: ["39.100.114.253:9300","39.100.114.253:9301","39.100.114.253:9302"]
discovery.zen.minimum_master_nodes: 2
```

es2.yml

```yaml
cluster.name: elasticsearch-cluster
node.name: es-node2
network.bind_host: 0.0.0.0
network.publish_host: 39.100.114.253
http.port: 9201
transport.tcp.port: 9301
http.cors.enabled: true
http.cors.allow-origin: "*"
node.master: true 
node.data: true  
discovery.zen.ping.unicast.hosts: ["39.100.114.253:9300","39.100.114.253:9301","39.100.114.253:9302"]
discovery.zen.minimum_master_nodes: 2
```

**es3.yml**

```yaml
cluster.name: elasticsearch-cluster
node.name: es-node3
network.bind_host: 0.0.0.0
network.publish_host: 39.100.114.253
http.port: 9202
transport.tcp.port: 9302
http.cors.enabled: true
http.cors.allow-origin: "*"
node.master: true 
node.data: true  
discovery.zen.ping.unicast.hosts: ["39.100.114.253:9300","39.100.114.253:9301","39.100.114.253:9302"]
discovery.zen.minimum_master_nodes: 2
```

【注】39.100.114.253是服务器`ip`地址

配置`jvm`的最大线程限制，在` /etc/sysctl.conf `文件中,增加以下内容:  

```
vm.max_map_count=262144 
```

以上配置避免在启动容器时报以下错误

```
bootstrap checks failed max virtual memory areas vm.max_map_count [65530] likely too low, increase to at least [262144]
```

更新`sysctl`服务

```
sysctl -p
```

### 2.2 启动镜像服务

启动 es1

```sh
docker run -dit -e ES_JAVA_OPTS="-Xms256m -Xmx256m"  -p 80:9200 -p 9300:9300 -v /root/es/config/es1.yml:/usr/share/elasticsearch/config/elasticsearch.yml -v /root/es/data1:/usr/share/elasticsearch/data --name ES01 elasticsearch
```

`-v` 表示映射的数据，宿主机下的配置文件与容器内的配置文件进行同步。

启动es2

```sh
docker run -dit -e ES_JAVA_OPTS="-Xms256m -Xmx256m" -p 9201:9201 -p 9301:9301 -v /root/es/config/es2.yml:/usr/share/elasticsearch/config/elasticsearch.yml -v /root/es/data2:/usr/share/elasticsearch/data --name ES02 elasticsearch
```

启动es3

```sh
docker run -dit -e ES_JAVA_OPTS="-Xms256m -Xmx256m" -p 9202:9202 -p 9302:9302 -v /root/es/config/es3.yml:/usr/share/elasticsearch/config/elasticsearch.yml -v /root/es/data3:/usr/share/elasticsearch/data --name ES03 elasticsearch
```

【注】设置-e ES_JAVA_OPTS="-Xms256m -Xmx256m" 是因为/etc/elasticsearch/jvm.options 默认jvm最大最小内存是2G,可用docker stats命令查看.

### 2.3 测试

查看ES集群是否ok, 可以访问http://39.100.114.253/_cat/nodes?pretty查看

```
39.100.114.253 25 95  7 0.15 0.14 0.09 mdi - es-node3
39.100.114.253 24 95 14 0.15 0.14 0.09 mdi - es-node2
39.100.114.253 29 95 15 0.15 0.14 0.09 mdi * es-node1
```

显示以上信息，则表示集群部署成功。后期只需要针对第一个数据结点操作，会快速同步或分散到其它结点上。

还可以通过`docker stats ES01 ES02 ES03` 查看内存、CPU等使用情况。 

## 四、集群-compose方式

使用docker-compose编排技术， 创建docker-compose.yml 文件

```
version: '2.2'
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:6.7.0
    container_name: elasticsearch
    environment:
      - cluster.name=docker-cluster
      - bootstrap.memory_lock=true
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - esdata1:/usr/share/elasticsearch/data
    ports:
      - 9200:9200
    networks:
      - esnet
  elasticsearch2:
    image: docker.elastic.co/elasticsearch/elasticsearch:6.7.0
    container_name: elasticsearch2
    environment:
      - cluster.name=docker-cluster
      - bootstrap.memory_lock=true
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
      - "discovery.zen.ping.unicast.hosts=elasticsearch"
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - esdata2:/usr/share/elasticsearch/data
    networks:
      - esnet

volumes:
  esdata1:
    driver: local
  esdata2:
    driver: local

networks:
  esnet:
```

