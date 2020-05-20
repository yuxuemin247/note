##### 1、MySQL

```
docker run -d --name 容器名 -p 宿主端口:容器端口  -v 宿主地址:/var/lib/mysql  -e MYSQL_ROOT_PASSWORD=123456  镜像名
```

##### 2、postgresql

```
docker run --name postgres1 -p 54321:5432 -e POSTGRES_PASSWORD=password  -d postgres:9.4
```

##### 3、ES

```
docker run -d --name es -e 'ES_JAVA_OPTS=-Xms128m -Xmx128m' -p 9200:9200 elasticsearch

ES_JAVA_OPTS=-Xms128m -Xmx128m是指定内存，新版默认是1G
discovery=single-node 
```

