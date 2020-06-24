- `docker-compose -f xxx.yml up -d`

  #根据`yml`文件下载镜像创建容器

- `docker-compose -f xxx.yml down`

  #停止卸载容器

##### 1、安装`kafak`

```
#xxx.yml
version: '3.2'
services:
  zookeeper:
    image: wurstmeister/zookeeper
    ports:
      - "2181:2181"
    restart: always
  kafka:
    image: wurstmeister/kafka:2.12-2.3.0
    ports:
      - "9092:9092"
    environment:
      - KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181
      - KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://${IP}:9092
      - KAFKA_LISTENERS=PLAINTEXT://:9092
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    restart: always
```

```
`docker-compose -f xxx.yml up -d`
```

[博客](https://www.cnblogs.com/snow-backup/p/12750602.html)

