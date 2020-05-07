## 简介:

MongoDB是一个面向文档（document-oriented）的数据库，而不是关系型数据库。
不采用关系型主要是为了获得更好得扩展性。当然还有一些其他好处，与关系数据库相比，面向文档的数据库不再有“行“（row）的概念取而代之的是更为灵活的“文档”（document）模型。
通过在文档中嵌入文档和数组，面向文档的方法能够仅使用一条记录来表现复杂的层级关系，这与现代的面向对象语言的开发者对数据的看法一致。
另外，不再有预定义模式（predefined schema）：文档的键（key）和值（value）不再是固定的类型和大小。由于没有固定的模式，根据需要添加或删除字段变得更容易了。通常由于开发者能够进行快速迭代，所以开发进程得以加快。而且，实验更容易进行。开发者能尝试大量的数据模型，从中选一个最好的。

### 易扩展

应用程序数据集的大小正在以不可思议的速度增长。随着可用带宽的增长和存储器价格的下降，即使是一个小规模的应用程序，需要存储的数据量也可能大的惊人，甚至超出
了很多数据库的处理能力。过去非常罕见的T级数据，现在已经是司空见惯了。
由于需要存储的数据量不断增长，开发者面临一个问题：应该如何扩展数据库，分为纵向扩展和横向扩展，纵向扩展是最省力的做法，但缺点是大型机一般都非常贵，而且
当数据量达到机器的物理极限时，花再多的钱也买不到更强的机器了，此时选择横向扩展更为合适，但横向扩展带来的另外一个问题就是需要管理的机器太多。
MongoDB的设计采用横向扩展。面向文档的数据模型使它能很容易地在多台服务器之间进行数据分割。MongoDB能够自动处理跨集群的数据和负载，自动重新分配文档，以及将
用户的请求路由到正确的机器上。这样，开发者能够集中精力编写应用程序，而不需要考虑如何扩展的问题。如果一个集群需要更大的容量，只需要向集群添加新服务器，MongoDB就会自动将现有的数据向新服务器传送

### 功能全

MongoDB作为一款通用型数据库，除了能够创建、读取、更新和删除数据之外，还提供了一系列不断扩展的独特功能

1、索引

支持通用二级索引，允许多种快速查询，且提供唯一索引、复合索引、地理空间索引、全文索引

2、聚合

支持聚合管道，用户能通过简单的片段创建复杂的集合，并通过数据库自动优化

3、特殊的集合类型

支持存在时间有限的集合，适用于那些将在某个时刻过期的数据，如会话session。类似地，MongoDB也支持固定大小的集合，用于保存近期数据，如日志

4、文件存储

支持一种非常易用的协议，用于存储大文件和文件元数据。MongoDB并不具备一些在关系型数据库中很普遍的功能，如链接join和复杂的多行事务。省略
这些的功能是处于架构上的考虑，或者说为了得到更好的扩展性，因为在分布式系统中这两个功能难以高效地实现

### 卓越的性能

MongoDB的一个主要目标是提供卓越的性能，这很大程度上决定了MongoDB的设计。MongoDB把尽可能多的内存用作缓存cache，视图为每次查询自动选择正确的索引。
总之各方面的设计都旨在保持它的高性能
虽然MongoDB非常强大并试图保留关系型数据库的很多特性，但它并不追求具备关系型数据库的所有功能。只要有可能，数据库服务器就会将处理逻辑交给客户端。这种精简方式的设计是MongoDB能够实现如此高性能的原因之一

## 重要概念

![1036857-20180114154208504-1797989172](https://ws2.sinaimg.cn/large/006tNc79ly1g230i5haiyj31320hcmza.jpg)



### 注意事项:

```python
需要注意的是：
#1、文档中的键/值对是有序的。
#2、文档中的值不仅可以是在双引号里面的字符串，还可以是其他几种数据类型（甚至可以是整个嵌入的文档)。
#3、MongoDB区分类型和大小写。
#4、MongoDB的文档不能有重复的键。
#5、文档中的值可以是多种不同的数据类型，也可以是一个完整的内嵌文档。文档的键是字符串。除了少数例外情况，键可以使用任意UTF-8字符。

文档键命名规范：
#1、键不能含有\0 (空字符)。这个字符用来表示键的结尾。
#2、.和$有特别的意义，只有在特定环境下才能使用。
#3、以下划线"_"开头的键是保留的(不是严格要求的)。
```



## 下载安装

4.0下载地址:
https://fastdl.mongodb.org/win32/mongodb-win32-x86_64-2008plus-ssl-4.0.8-signed.msi

安装时去除多余的组件安装提高速度:

![2018081215270025](https://ws2.sinaimg.cn/large/006tNc79ly1g22v4jcxoyj30dv0asq3e.jpg)



![2018081215270126](https://ws1.sinaimg.cn/large/006tNc79ly1g22v45enftj30dv0as74y.jpg)

![2018081215270328](https://ws3.sinaimg.cn/large/006tNc79ly1g22v49gf16j30dv0as74p.jpg)



此时MongoDB已经开启，浏览器访问<http://localhost:27017/>，页面上输出：
It looks like you are trying to access MongoDB over HTTP on the native driver port.

说明MongoDB已经启动了，且它的默认端口(27017)没有被占用。

## 开始使用:

运行bin下的终端程序mongo.exe    其与mysql性质相同都是客户端!

'mongo' 看见欢迎信息则说明登录成功

![屏幕快照 2019-04-15 上午5.24.02](https://ws1.sinaimg.cn/large/006tNc79ly1g22v7rhx8sj30pt0c0gmo.jpg)

此时没有任何的权限限制,默认是管理员角色

## 创建账号

```mysql
#1、创建账号
use admin 
db.createUser(
  {
    user: "root",
    pwd: "123",
    roles: [ { role: "root", db: "admin" } ]
  }
)

use test
db.createUser(
  {
    user: "jerry",
    pwd: "123",
    roles: [ { role: "readWrite", db: "test" },
             { role: "read", db: "db1" } ]
  }
)

在mongodb中用不同的数据库来区分权限,要管理哪个数据库就在哪个数据库下创建用户即可,创建管理员账户则在admin下创建!
db 是一个全局变量 表示当前数据库
db.createUser()是调用一个内部函数用于创建用户
每个账号可以具备多个角色
```

更多角色请见:https://www.cnblogs.com/SamOk/p/5162767.html



## 开启账号认证

默认情况下mongodb不会加载认证信息就像mysql跳过授权表一样,创建完账号用户需要开启用户认证:

##### 具体方法:

修改配置文档mongod.cfg（位置：安装目录\bin 下）

首先，将bind_ip改为0.0.0.0 （让其他电脑可以访问，用于远程连接，如果bind_ip是127.0.0.1的话，就只能本地访问）

```mysql
security：
    authorization: enabled
# 注意缩进
```

然后找到 #security：改成下图所示，开启安全认证。

![20180725182019556](https://ws3.sinaimg.cn/large/006tNc79ly1g22w8uzytdj30e40ll75n.jpg)

重启MongoDB Server服务，启用认证！

#### 账号测试:

```mysql
#直接mongo进入程序  已经无法查看数据库

show dbs 
#登录方式1:  authenticationDatabase指定数据库
mongo --port 27017 -u "root" -p "123" --authenticationDatabase "admin"

#登录方式2:进入mongo后
use admin
db.auth("root","123")

#删除账号
db.dropUser('用户名');

#修改密码
db.changeUserPassword(用户名, 新密码);
```



## 库的操作

```mysql
#创建数据库:
use 数据库名称
#如果有则切换没有则创建新的,注意的是如果如果库中没有数据show dbs 中则不显示!

# 查看数据库:
show dbs

#删除
db.dropDatabase()
#注意区分大小写


```

## 集合的操作

集合是一个存储数据元素的容器类比mysql中的表

```mysql
#创建集合:
db.user

#查看集合:
show collections
show tables
# 同样的数据集合中没有数据则 不会显示

# 一下数据库之间没有任何关系仅仅是名字有相同部分 数据之间的关系需要应用程序维护
db.blog
db.blog.user
db.blog.common

#删除集合:
db.blog.user.drop()


```

## 基本数据类型

1、在概念上，MongoDB的文档与Javascript的对象相近，因而可以认为它类似于JSON。JSON（http://www.json.org）是一种简单的数据表示方式：其规范仅用一段文字就能描述清楚（其官网证明了这点），且仅包含六种数据类型。

2、这样有很多好处：易于理解、易于解析、易于记忆。然而从另一方面说，因为只有null、布尔、数字、字符串、数字和对象这几种数据类型，所以JSON的表达能力有一定的局限。

3、虽然JSON具备的这些类型已经具有很强的表现力，但绝大数应用（尤其是在于数据库打交道时）都还需要其他一些重要的类型。例如，JSON没有日期类型，这使得原本容易日期处理变得烦人。另外，JSON只有一种数字类型，无法区分浮点数和整数，更别区分32位和64位了。再者JSON无法表示其他一些通用类型，如正则表达式或函数。

4、MongoDB在保留了JSON基本键/值对特性的基础上，添加了其他一些数据类型。在不同的编程语言下，这些类型的确切表示有些许差异。下面说明了MongoDB支持的其他通用类型，以及如何正在文档中使用它们

```python
#1、null：用于表示空或不存在的字段
d={'x':null}
#2、布尔型：true和false
d={'x':true,'y':false}
#3、数值
d={'x':3,'y':3.1415926}
#4、字符串
d={'x':'egon'}
#5、日期
d={'x':new Date()}
d.x.getHours()
#6、正则表达式
d={'pattern':/^egon.*?nb$/i}

正则写在／／内，后面的i代表:
i 忽略大小写
m 多行匹配模式
x 忽略非转义的空白字符
s 单行匹配模式

#7、数组
d={'x':[1,'a','v']}

#8、内嵌文档
user={'name':'jerry','addr':{'country':'China','city':'YT'}}
user.addr.country

#9、对象id:是一个12字节的ID,是文档的唯一标识，不可变
d={'x':ObjectId()}

#案例:
db.tb.insert({"a":null,"b":1.1,"c":true,"d":100,"e":"aaaaaa","f":new Date(),"g":/^jerry.*nice$/i,"h":[1,2],"j":{"name":"smallJerry"}})

db.tb.find()
db.tb.find().pretty() # 格式化显示
```

## _id和ObjectId

```python
"""
MongoDB中存储的文档必须有一个"_id"键。这个键的值可以是任意类型，默认是个ObjectId对象。
在一个集合里，每个文档都有唯一的“_id”,确保集合里每个文档都能被唯一标识。
不同集合"_id"的值可以重复，但同一集合内"_id"的值必须唯一

#1、ObjectId
ObjectId是"_id"的默认类型。因为设计MongoDb的初衷就是用作分布式数据库，所以能够在分片环境中生成
唯一的标识符非常重要，而常规的做法：在多个服务器上同步自动增加主键既费时又费力，这就是MongoDB采用
ObjectId的原因。
ObjectId采用12字节的存储空间，是一个由24个十六进制数字组成的字符串
    0|1|2|3|   4|5|6|     7|8    9|10|11    
    时间戳      机器      PID    计数器
如果快速创建多个ObjectId，会发现每次只有最后几位有变化。另外，中间的几位数字也会变化（要是在创建过程中停顿几秒）。
这是ObjectId的创建方式导致的，如上图

时间戳单位为秒，与随后5个字节组合起来，提供了秒级的唯一性。这个4个字节隐藏了文档的创建时间，绝大多数驱动程序都会提供
一个方法，用于从ObjectId中获取这些信息。

因为使用的是当前时间，很多用户担心要对服务器进行时钟同步。其实没必要，因为时间戳的实际值并不重要，只要它总是不停增加就好。
接下来3个字节是所在主机的唯一标识符。通常是机器主机名的散列值。这样就可以保证不同主机生成不同的ObjectId，不产生冲突

接下来2个字节确保了在同一台机器上并发的多个进程产生的ObjectId是唯一的

前9个字节确保了同一秒钟不同机器不同进程产生的ObjectId是唯一的。最后3个字节是一个自动增加的 计数器。确保相同进程的同一秒产生的
ObjectId也是不一样的。

#2、自动生成_id
如果插入文档时没有"_id"键，系统会自帮你创建 一个。可以由MongoDb服务器来做这件事。
但通常会在客户端由驱动程序完成。这一做法非常好地体现了MongoDb的哲学：能交给客户端驱动程序来做的事情就不要交给服务器来做。
这种理念背后的原因是：即便是像MongoDB这样扩展性非常好的数据库，扩展应用层也要比扩展数据库层容易的多。将工作交给客户端做就
减轻了数据库扩展的负担。
"""
```



## 文档操作

### 插入数据

```mysql
#1、没有指定_id则默认ObjectId,_id不能重复，且在插入后不可变

#2、插入单条
user0={
    "name":"egon",
    "age":10,
    'hobbies':['music','read','dancing'],
    'addr':{
        'country':'China',
        'city':'BJ'
    }
}

db.test.insert(user0)
db.test.find()

# 无则插入 有责覆盖
db.test.save()


#3、插入多条
user1={
    "_id":1,
    "name":"alex",
    "age":10,
    'hobbies':['music','read','dancing'],
    'addr':{
        'country':'China',
        'city':'weifang'
    }
}

user2={
    "_id":2,
    "name":"wupeiqi",
    "age":20,
    'hobbies':['music','read','run'],
    'addr':{
        'country':'China',
        'city':'hebei'
    }
}


user3={
    "_id":3,
    "name":"yuanhao",
    "age":30,
    'hobbies':['music','drink'],
    'addr':{
        'country':'China',
        'city':'heibei'
    }
}

user4={
    "_id":4,
    "name":"jingliyang",
    "age":40,
    'hobbies':['music','read','dancing','tea'],
    'addr':{
        'country':'China',
        'city':'BJ'
    }
}

user5={
    "_id":5,
    "name":"jinxin",
    "age":50,
    'hobbies':['music','read',],
    'addr':{
        'country':'China',
        'city':'henan'
    }
}
db.user.insertMany([user1,user2,user3,user4,user5])

单条插入与多条插入

```

### 查询数据

```python
=============================比较运算=============================
find 查找所有匹配数据
findOne 查找第一个匹配的

# SQL：=,!=,>,<,>=,<=
# MongoDB：{key:value}代表什么等于什么,"$ne","$gt","$lt","gte","lte",其中"$ne"能用于所有数据类型
find 查找所有匹配数据
findOne 查找第一个匹配的


#1、select * from db1.user where name = "cxx";
db.user.find({'name':'cxx'})

#2、select * from db1.user where name != "cxx";
db.user.find({'name':{"$ne":'cxx'}})

#3、select * from db1.user where id > 2;
db.user.find({'_id':{'$gt':2}})

#4、select * from db1.user where id < 3;
db.user.find({'_id':{'$lt':3}})

#5、select * from db1.user where id >= 2;
db.user.find({"_id":{"$gte":2,}})

#6、select * from db1.user where id <= 2;
db.user.find({"_id":{"$lte":2}})

=============================逻辑运算=============================
# SQL：and，or，not
# MongoDB：字典中逗号分隔的多个条件是and关系，"$or"的条件放到[]内,"$not"

#1、select * from db1.user where id >= 2 and id < 4;
db.user.find({'_id':{"$gte":2,"$lt":4}})

#2、select * from db1.user where id >= 2 and age < 40;
db.user.find({"_id":{"$gte":2},"age":{"$lt":40}})

#3、select * from db1.user where id >= 5 or name = "cxx";
db.user.find({
    "$or":[
        {'_id':{"$gte":5}},
        {"name":"cxx"}
        ]
})

#4、select * from db1.user where id % 2=1;
db.user.find({'_id':{"$mod":[2,1]}})

#5、上题，取反
db.user.find({'_id':{"$not":{"$mod":[2,1]}}})


=============================成员运算=============================

# SQL：in，not in
# MongoDB："$in","$nin"

#1、select * from db1.user where age in (20,30,31);
db.user.find({"age":{"$in":[20,30,31]}})

#2、select * from db1.user where name not in ('alex','yuanhao');
db.user.find({"name":{"$nin":['alex','yuanhao']}})


=============================正则匹配=============================

# SQL: regexp 正则
# MongoDB: /正则表达/i

#1、select * from db1.user where name regexp '^j.*?(g|n)$';
db.user.find({'name':/^j.*?(g|n)$/i})
正则表达



=============================指定字段=============================
db.user.find({'_id':3},{'_id':0,'name':1,'age':1})
0表示不显示 默认为0  1为显示




=============================查询数组=============================
#1、查看有dancing爱好的人
db.user.find({'hobbies':'dancing'})

#2、查看既有dancing爱好又有tea爱好的人
db.user.find({
    'hobbies':{
        "$all":['dancing','tea']
        }
})

#3、查看第4个爱好为tea的人
db.user.find({"hobbies.3":'tea'})

#4、查看所有人最后两个爱好
db.user.find({},{'hobbies':{"$slice":-2},"age":0,"_id":0,"name":0,"addr":0})

#5、查看所有人的第2个到第3个爱好
db.user.find({},{'hobbies':{"$slice":[1,2]},"age":0,"_id":0,"name":0,"addr":0})

> db.blog.find().pretty()
{
        "_id" : 1,
        "name" : "alex意外死亡的真相",
        "comments" : [
                {
                        "name" : "egon",
                        "content" : "alex是谁？？？",
                        "thumb" : 200
                },
                {
                        "name" : "wxx",
                        "content" : "我去，真的假的",
                        "thumb" : 300
                },
                {
                        "name" : "yxx",
                        "content" : "吃喝嫖赌抽，欠下两个亿",
                        "thumb" : 40
                },
                {
                        "name" : "egon",
                        "content" : "xxx",
                        "thumb" : 0
                }
        ]
}
db.blog.find({},{'comments':{"$slice":-2}}).pretty() #查询最后两个
db.blog.find({},{'comments':{"$slice":[1,2]}}).pretty() #查询1到2


===============================其他===============================


# 排序:1代表升序，-1代表降序
db.user.find().sort({"name":1,})
db.user.find().sort({"age":-1,'_id':1})


# 分页:limit代表取多少个document，skip代表跳过前多少个document。 
db.user.find().sort({'age':1}).limit(1).skip(2)

# 获取数量
db.user.count({'age':{"$gt":30}}) 

#或者
db.user.find({'age':{"$gt":30}}).count()


#1、{'key':null} 匹配key的值为null或者没有这个key
db.t2.insert({'a':10,'b':111})
db.t2.insert({'a':20})
db.t2.insert({'b':null})

> db.t2.find({"b":null})
{ "_id" : ObjectId("5a5cc2a7c1b4645aad959e5a"), "a" : 20 }
{ "_id" : ObjectId("5a5cc2a8c1b4645aad959e5b"), "b" : null }


#2、查找所有
db.user.find() #等同于db.user.find({})
db.user.find().pretty()

#3、查找一个，与find用法一致，只是只取匹配成功的第一个
db.user.findOne({"_id":{"$gt":3}})

杂项
```

### 修改数据

```python
======================================update==========================================

update() 方法用于更新已存在的文档。语法格式如下：
db.collection.update(
   <query>,
   <update>,
   {
     upsert: <boolean>,
     multi: <boolean>,
     writeConcern: <document>
   }
)
参数说明：对比update db1.t1 set name='EGON',sex='Male' where name='egon' and age=18;

query : 相当于where条件。
update : update的对象和一些更新的操作符（如$,$inc...等，相当于set后面的
upsert : 可选，默认为false，代表如果不存在update的记录不更新也不插入，设置为true代表插入。
multi : 可选，默认为false，代表只更新找到的第一条记录，设为true,代表更新找到的全部记录。
writeConcern :可选，抛出异常的级别。

更新操作是不可分割的：若两个更新同时发送，先到达服务器的先执行，然后执行另外一个，不会破坏文档。


=========================================覆盖式=========================================
#注意：除非是删除，否则_id是始终不会变的
#1、覆盖式:
db.user.update({'age':20},{"name":"Wxx","hobbies_count":3})
是用{"_id":2,"name":"Wxx","hobbies_count":3}覆盖原来的记录

#2、一种最简单的更新就是用一个新的文档完全替换匹配的文档。这适用于大规模式迁移的情况。例如
var obj=db.user.findOne({"_id":2})

obj.username=obj.name+'SB'
obj.hobbies_count++
delete obj.age

db.user.update({"_id":2},obj)


=========================================设置:$set=========================================


通常文档只会有一部分需要更新。可以使用原子性的更新修改器，指定对文档中的某些字段进行更新。
更新修改器是种特殊的键，用来指定复杂的更新操作，比如修改、增加后者删除

#1、update db1.user set  name="WXX" where id = 2
db.user.update({'_id':2},{"$set":{"name":"WXX",}})

#2、没有匹配成功则新增一条{"upsert":true}
db.user.update({'_id':6},{"$set":{"name":"egon","age":18}},{"upsert":true})

#3、默认只改匹配成功的第一条,{"multi":改多条}
db.user.update({'_id':{"$gt":4}},{"$set":{"age":28}})
db.user.update({'_id':{"$gt":4}},{"$set":{"age":38}},{"multi":true})

#4、修改内嵌文档，把名字为alex的人所在的地址国家改成Japan
db.user.update({'name':"alex"},{"$set":{"addr.country":"Japan"}})

#5、把名字为alex的人的地2个爱好改成piao
db.user.update({'name':"alex"},{"$set":{"hobbies.1":"piao"}})

#6、删除alex的爱好,$unset
db.user.update({'name':"alex"},{"$unset":{"hobbies":""}})



=========================================增加和减少$i:nc=====================================
#1、所有人年龄增加一岁
db.user.update({},
    {
        "$inc":{"age":1}
    },
    {
        "multi":true
    }
    )
#2、所有人年龄减少5岁
db.user.update({},
    {
        "$inc":{"age":-5}
    },
    {
        "multi":true
    }
    )
=========================================添加删除数组元素==================================
往数组内添加元素:$push
#1、为名字为yuanhao的人添加一个爱好read
db.user.update({"name":"yuanhao"},{"$push":{"hobbies":"read"}})

#2、为名字为yuanhao的人一次添加多个爱好tea，dancing
db.user.update({"name":"yuanhao"},{"$push":{
    "hobbies":{"$each":["tea","dancing"]}
}})

按照位置且只能从开头或结尾删除元素：$pop
#3、{"$pop":{"key":1}} 从数组末尾删除一个元素

db.user.update({"name":"yuanhao"},{"$pop":{
    "hobbies":1}
})

#4、{"$pop":{"key":-1}} 从头部删除
db.user.update({"name":"yuanhao"},{"$pop":{
    "hobbies":-1}
})

#5、按照条件删除元素,："$pull" 把符合条件的统统删掉，而$pop只能从两端删
db.user.update({'addr.country':"China"},{"$pull":{
    "hobbies":"read"}
},
{
    "multi":true
}
)


=====================================避免添加重复：$addToSet===========================
#自动去除重复
db.urls.insert({"_id":1,"urls":[]})
db.urls.update({"_id":1},{"$addToSet":{"urls":'http://www.baidu.com'}})
db.urls.update({"_id":1},{"$addToSet":{"urls":'http://www.baidu.com'}})
db.urls.update({"_id":1},{"$addToSet":{"urls":'http://www.baidu.com'}})

db.urls.update({"_id":1},{
    "$addToSet":{
        "urls":{
        "$each":[
            'http://www.baidu.com',
            'http://www.baidu.com',
            'http://www.xxxx.com'
            ]
            }
        }
    }
)


=====================================其他========================================
#1、了解：限制大小"$slice"，只留最后n个

db.user.update({"_id":5},{
    "$push":{"hobbies":{
        "$each":["read",'music','dancing'],
        "$slice":-2
    }
    }
})

#2、了解：排序The $sort element value must be either 1 or -1"
db.user.update({"_id":5},{
    "$push":{"hobbies":{
        "$each":["read",'music','dancing'],
        "$slice":-1,
        "$sort":-1
    }
    }
})

#注意：不能只将"$slice"或者"$sort"与"$push"配合使用，且必须使用"$eah"

```

### 删除数据

```python
#1、删除多个中的第一个
db.user.deleteOne({ 'age': 8 })

#2、删除国家为China的全部
db.user.deleteMany( {'addr.country': 'China'} ) 

#3、删除全部
db.user.deleteMany({})
```

## pymongo

```python
from pymongo import MongoClient

#1、链接
client=MongoClient('mongodb://root:123@localhost:27017/')
# client = MongoClient('localhost', 27017)

#2、use 数据库
db=client['db2'] #等同于：client.db1

#3、查看库下所有的集合
print(db.collection_names(include_system_collections=False))

#4、创建集合
table_user=db['userinfo'] #等同于：db.user

#5、插入文档
import datetime
user0={
    "_id":1,
    "name":"egon",
    "birth":datetime.datetime.now(),
    "age":10,
    'hobbies':['music','read','dancing'],
    'addr':{
        'country':'China',
        'city':'BJ'
    }
}

user1={
    "_id":2,
    "name":"alex",
    "birth":datetime.datetime.now(),
    "age":10,
    'hobbies':['music','read','dancing'],
    'addr':{
        'country':'China',
        'city':'weifang'
    }
}
# res=table_user.insert_many([user0,user1]).inserted_ids
# print(res)
# print(table_user.count())

#6、查找

# from pprint import pprint#格式化
# pprint(table_user.find_one())
# for item in table_user.find():
#     pprint(item)

# print(table_user.find_one({"_id":{"$gte":1},"name":'egon'}))

#7、更新
table_user.update({'_id':1},{'name':'EGON'})

#8、传入新的文档替换旧的文档
table_user.save(
    {
        "_id":2,
        "name":'egon_xxx'
    }
)
```





