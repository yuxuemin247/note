##### 1、MySQL

```
docker run -d -p 3307:3306  --name mysql-master -V /root/docker/mysql/master/conf : /etc/mysql/mysql.conf  -V /root/docker/mysql/master/data : /var/lib/mysql  -V /root/docker/mysql/master/log : var/log/mysql  -e MYSQL_ROOT_PASSWORD=y123456! mysql:5.7

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

##### 4、redis

```
docker run -itd --name redis-test -p 6379:6379 redis
```
