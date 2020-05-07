[TOC]

# 一、mysql介绍

```mysql
1.数据库相关概念
		数据库服务器(本质就是一台计算机,该计算机之上安装有数据库管理软件的服务端)
    数据库管理系统RDBMS(本质上就是一个C/S架构的套接字软件)
    库(文件夹)
    表(文件)
    记录(抽取一个事务所有典型的特征/数据)
2.数据库管理系统/软件分类:
		关系型:
				有表结构,存取数据前必先定义表结构,存数据必须按照字段的类型或约束来
				代表:MYsql Oracle DB2 SQLSever
		非关系型:
				存取都是采用key:value的形式
				代表:Mongodb redis
```

# 二、mysql之docker配置

```mysql
# 安装
docker pull mysql:5.7
# 配置
docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=MYsql891213 -d mysql:5.7
# 启动
docker exec -it mysql mysql -uroot -pMYsql891213
```

# 三、mysql之连接和配置

```mysql
# 连接mysql
mysql -h 127.0.0.1 -P 3306 -uroot -p'密码'

# 退出
exit | quit

# 设置密码
mysqladmin uroot -p password '123' # 设置需要原来的密码

# 破解密码
1.关闭mysql服务端
2.mysqld --skip-grant-tables # 启动服务端,跳过授权表
3.使用客户端连接,直接登陆
4.修改密码
5.update mysql.user set password=password('123') where user = 'root' and host='127.0.0.1';
6.flush privileges # 刷新权限
7.重启mysql服务端
8.可以使用修改的密码登陆

# mysql配置文件
# my.ini <=> windows
[mysqld]
# 同一字符编码
character-set-server=utf8
collation-server=utf8_general_ci
[client]
# 针对所有的客户端的配置
default-character-set=utf8
[mysql]
# 在配置文件配置登陆账号密码
user='root'
password='root'
default-character-set=utf8

# my.cnf <=> mac
[mysqld]
# 同一字符编码
character-set-server=utf8
collation-server=utf8_general_ci
[client]
# 针对所有的客户端的配置
default-character-set=utf8
[mysql]
# 在配置文件配置登陆账号密码
user='root'
password='root'
default-character-set=utf8
```

# 四、mysql基本sql语句

```mysql
DDL--数据定义语言(create, alter, drop)
DML--数据操纵语言(select, insert, delete, update)
DCL--数据控制语言(grant, revoke, commit, rollback)
DQL--数据查询语言()
\c 停止运行
\s 查看数据库信息

# database
# 创建库
create database db01 charset utf8;

# 查看库
show databases; # 查看所有库的库名
show create database db01; # 单独查看某一个库的信息

# 修改库(不能修改库名)
alter database db01 charset utf8;

# 删除库
drop database db01;
---------------------------------------------------------------------------------------------
# table
use db01; # 切换库
select database(); # 查看当前所在的库

# 创建表
create table db01.t01(id int,name char); # 不指定库,默认创建当前库下
create table t01(id int,name char);

# 查看表
show tables; # 查看当前库下的所有表
show create table t01; # 查看某一个表的信息
describe t01; # 查看表结构
desc t01; # describe简写

# 修改表
alter table t01 modify name char(32);

# 删除表
drop table t01;
---------------------------------------------------------------------------------------------
# column
# 增加记录
insert into db01.t01 values(1,'allen'),(2,'kevin');

# 查看记录
select id,name from db01.t01;

# 修改记录
update db01.t01 set name='collins' where name='kevin';

# 删除记录
delete from db01.t01; # 删除整张表的记录,但是id自增记录不会清空
delete from db01.t01 where name='collins'; # 删除指定记录
truncate t01; # 清除数据,重置表
---------------------------------------------------------------------------------------------
# 创建表的完整语法
create table 表名(
字段名1 类型[(宽度) 约束条件],
字段名2 类型[(宽度) 约束条件],
字段名3 类型[(宽度) 约束条件],
);

# 解释
类型：使用限制字段必须以什么样的数据类型传值
约束条件：约束条件是在类型之外添加一种额外的限制

# 注意:
同一张表中,字段名是不能相同的
宽度和约束条件可选
字段名和类型是必须的
最后一个字段后面不能加逗号
```

# 五、mysql数据库引擎

```mysql

```

# 六、mysql之sql_mode

```mysql
# 查看系统变量
show variables;

# 查看sql_mode
show variables like "%sql_mode%";
ONLY_FULL_GROUP_BY,
STRICT_TRANS_TABLES,
NO_ZERO_IN_DATE,
NO_ZERO_DATE,
ERROR_FOR_DIVISION_BY_ZERO,
NO_AUTO_CREATE_USER,
NO_ENGINE_SUBSTITUTION 

# 设置严格模式(STRICT_TRANS_TABLES)
# 在该模式下,如果插入的数据超过限制,则会立即报错
set global sql_mode='STRICT_TRANS_TABLES'; # 设置全局的sql_mode
set session sql_mode='STRICT_TRANS_TABLES'; # 设置当前连接的sql_mode
```



# 七、mysql数据类型之整型

```mysql
# 默认整型存储有符号
tinyint # 大小:1字节(8bytes) 范围:-128,127(有符号) 0,255(无符号)
smallint # 大小:2字节(16bytes) 范围:-32768,32767(有符号) 0,65535(无符号)
int|integer # 大小:4字节(32bytes) 范围:-8388608,8388607(有符号) 0,4294967295(无符号)
bigint # 大小:8字节(64bytes)
# 对于整形来说,数据类型后的宽度并不是存储限制,而是显示限制
```

# 八、mysql数据类型之浮点型

```mysql
# 默认浮点型存储有符号
float # 单精度浮点数 大小:4字节 数字总数个数最大值255,小数位最大30位
double # 双精度浮点数 大小:8字节 数字总数个数最大值255,小数位最大30位
decimal # 定点数类型 大小:M+2 数字总数个数最大值65,小数位最大30位
create table t01(x float(255,30));
create table t02(x double(255,30));
create table t03(x decimal(65,30));

# float与double类型能存放的整数比decimal更多
# float double decimal 精度不相同(精度从低到高 float < double < decimal)
insert into t01 values(1.1111111111111111111111);
insert into t02 values(1.1111111111111111111111);
insert into t03 values(1.1111111111111111111111);
```

# 九、mysql数据类型之字符类型

```mysql
# 定长
char
# 变定
varchar

# 字符的宽度限制单位是字符个数
create table t01(name char(4)); # 超出4个字符报错 不够4个字符则用空格补全

create table t02(name varchar(4)); # 超出4个字符报错 不够4个字符那么有几个字符就存几个字符

insert into t01 values("ACE");

insert into t02 values("ACE");

# 查看字符个数(mysql默认把char类型的空格去掉了)
select char_length(name) from t01; # 显示3
select char_length(name) from t02; # 显示3

# 配置sql_mode(查看字符填充后的长度,默认不显示填充的长度直接显示字符的长度)
set global sql_mode="PAD_CHAR_TO_FULL_LENGTH"
select char_length(name) from t01; # 显示4
select char_length(name) from t02; # 显示3

# 存储机制
# char存储是会将填充的空格也保存到文件中但会在读出结果时自动去掉末尾的空格
# name字段明确地等于一个值，该值后填充空格是没有用
# 查询的时候,可以通过存储的内容来查,也可以通过默认的显示内容来查
# 两种方式都可查询到
select * from t01 where name='ACE '
select * from t01 where name='ACE'

# name字段模糊匹配一个值，该值后填充空格是有用的
select * from t01 where name like "ACE";

name char(4)
# 缺点：浪费空间
# 优点：存取速度都快
ace.

name varchar(4)
# 缺点：存取速度都慢
# 优点：节省空间
(1bytes+ace) | (2bytes+ace)
# 头 + 数据
# mysql字符存储最大65535个
# 先取头再取数据

# 建议
# 同一张表char和varchar不要混着用
# 如果混着用char放在varchar前面
```

<table>
  <tbody>
    <tr>
      <th>Value</th>
      <th>CHAR(4)</th>
      <th>Storage Required</th>
      <th>VARCHAR(4)</th>
      <th>Storage Required</th>
    </tr>
    <tr>
      <td>""</td>
      <td>"{4}"</td>
      <td>4 bytes</td>
      <td>""</td>
      <td>1 byte</td>
    </tr>
    <tr>
      <td>"ab"</td>
      <td>"ab{2}"</td>
      <td>4 bytes</td>
      <td>"ab"</td>
      <td>3 byte</td>
    </tr>
    <tr>
      <td>"abcd"</td>
      <td>"abcd"</td>
      <td>4 bytes</td>
      <td>"abcd"</td>
      <td>5 byte</td>
    </tr>
    <tr>
      <td>"abcdefgh"</td>
      <td>"abcd"</td>
      <td>4 bytes</td>
      <td>"abcd"</td>
      <td>5 byte</td>
    </tr>
  </tbody>
</table>
# 十、mysql数据类型之文本类型

```mysql
# 注意文本都是变长
tinytext # 可变长度字符串,最多为255个字符
text # 可变长度字符串,最多为65535个字符
mediumtext # 可变长度字符串,最多为16777215个字符
longtext # 可变长度字符串,最多为4294967295个字符
```

# 十一、mysql数据类型之二进制数据类型

```mysql
# 二进制(binary)
binary # 固定长度,存储二进制格式字符串
varbinary # 可变长度,存储二进制格式字符串

# BLOB(binary large object),二进制大对象,是一个可以存储二进制文件的'容器'
# 在数据库中存放体积较大的多媒体对象就是应用程序处理BLOB的典型例子
tinyblob # 最大长度255个字节的BLOB列
blob # 最大长度65535个字节的BLOB列(最大64k)
mediumblob # 最大长度16777215个字节的BLOB列(16M)
longblob # 最大长度4294967295个字节的BLOB列(4G)
```

# 十二、mysql数据类型之日期类型

```mysql
date # 日期 1970-01-01 (1000-01-01/9999-12-31)
time #时间 00:00:00 (-838:59:59/838:59:59)
datetime #日期时间 1970-01-01 00:00:00 (1000-01-01 00:00:01/9999-12-31 23:59:59) 8字节
year # 年 1970 (1901/2155)
timestamp # (1970-01-01 00:00:00/2037) 4字节

create table t01 student(
  id int,
  name char(16),
  birth_year year,
  birth date,
  class_time time,
  register_time datetime
);

insert into student values(1,"allen","2019","2019-01-01","00:00:01","2019-01-01:00:00:01");
```

# 十三、mysql数据类型之集合

```mysql
# set:集合 多选多 
create table teacher(
	id int,
  name char(16),
  hobbies set("read","music","movie")
);

insert into teacher(1,"allen","read,musci,movie");
```

# 十四、mysql数据类型之枚举

```mysql
# enum:枚举 多选一
create table teacher(
	id int,
  name char(16),
  gender enum("male","female","others")
);

insert into teacher values(1,"allen","male");
```

# 十五、mysql数据属性之comment

```mysql
comment 'COMMENT' # 注释,给字段添加注释信息
create table t01(id int primary key auto_increment comment 'Number');
```

# 十五、mysql约束条件之unsigned

```mysql
# unsigned(无符号) 存储整型和浮点型无符号

create table t01(id int);

insert into t01 values(-1);

create table t01(id int unsigned);

insert into t01 values(1);
```

# 十六、mysql约束条件之zerofill

```mysql
# zerofill(0填充) 当显示宽度不够时使用0填充

create table t01(id int(11));

insert into t01 values(1); # 显示效果 1

create table t01(id int(11) zerofill);

insert into t01 values(1); # 显示效果 00000000001
```

# 十七、mysql约束条件之null

```mysql
# not null 非空 | null 空
create table t01(
	id int,
  name char(16) null
);

insert into t01(id) values(1); # name为空 默认值为null

create table t01(
	id int,
  name char(16) not null
);

insert into t01(id,name) values(1,"allen") 
# name不能空 规定不能为空,可以不传值但是需要设置一个默认值
```

# 十八、mysql约束条件之default

```mysql
# default 默认值
create table t01(
	id int,
  name char(16),
  gender enum("male","female") not null default "male"
);

insert into t01(id,name) values(1,"allen"); # gender不传值默认为male
# 通常not null 和 default 一起使用
```

# 十九、mysql约束条件之unique

```mysql
# unique :唯一
create table t01(
	id int unique,
  name char(16)
);

insert into t01 values(1,"allen");
insert into t01 values(2,"kevin");

# 联合唯一unique(字段1,字段2)
create table t01(
	id int unique,
  ip char(15),
  port int,
  unique(ip,port)
);

insert into t01 values(1,"127.0.0.1",3306); # ip和端口联合唯一
insert into t01 values(2,"127.0.0.2",3306); 
```

# 二十、mysql约束条件之primary key

```mysql
# primary key => 不为空且唯一
create table t01(
	id int primary key,
  name char(16)
);

insert into t01(1,"allen")
# primary key 单从约束角度去看,primary key就等同于 unique not null
1.一张表中必须有,并且只能有一个主键
# 有几种情况:
1.如果没有设置primary key,从上到下找到一个不为空且唯一的字段设置为主键
2.如果从上到下没有primary key也没有找到不为空且唯一的字段,mysql默认使用隐藏的字段设置为主键来组织数据
3.通常一张表中有一个id字段,而且通常应该把id设置为主键
create table t01(
	id int,
  name char(16) not null unique, # 该字段别识别设置为主键字段
  uuid char(32) not null unique
)engine=innodb;

# 联合主键
create table t01(
	ip char(15),
  port int,
  primary key(ip,port)
)engine=innodb;

# 把ip和port联合作为主键
```

# 二十一、mysql约束条件之auto_increment

```mysql
# auto_increment 自增
create table t01(
	id int primary key auto_increment,
  name char(16)
)engine=innodb;

# primary key和auto_increment一起使用,在插入数据值时我们可以省略id字段默认自增1

insert into t01(name) values("allen");

# 注意
# auto_increment必须指定给被定义成key的字段使用
```

# 二十二、mysql约束条件之foreign key

```mysql
# foreign key 外键 建立表和表之间关系
create table dep(
	id int primary key auto_increment,
  name char(64),
  comment text
)engine=innodb;

create table emp(
	id int primary key auto_increment,
  name char(16),
  age int,
  dep_id int,
  foreign key(dep_id) references dep(id)
)engine=innodb;
# 约束一:在创建表时,先建被关联的表depm,才能建关联表emp
# 约束二:在插入记录时,必须先插入被关联表的记录,才能插入关联表的记录
# 约束三:更新和删除都需要考虑到关联于被关联的关系
insert into dep(name,comment) values('teacher','hello teacher');
insert into dep(name,comment) values('student','hello student');

insert into emp(name,age,dep_id) values('allen',18,1);
insert into emp(name,age,dep_id)values('kevin',18,2);
insert into emp(name,age,dep_id) values('collins',18,2);
# 同步更新于同步删除
create table dep(
	id int primary key auto_increment,
  name char(16),
  comment text
)engine=innodb;

create table emp(
	id int primary key auto_increment,
  name char(16),
  age int,
  dep_id int,
  foreign key(dep_id) references dep(id) on update cascade on delete cascade
)engine=innodb;

# 以后删除或更新被关联表的记录对应关联表多关联的记录也会被删除或更新
```

# 二十三、mysql之一对多

<table>
  <tbody>
    <tr>
      <th>id</th>
      <th>name</th>
      <th>gender</th>
      <th>dep_name</th>
      <th>dep_comment</th>
    </tr>
    <tr>
      <td>1</td>
      <td>allen</td>
      <td>male</td>
      <td>teacher</td>
      <td>teach student</td>
    </tr>
    <tr>
      <td>2</td>
      <td>kevin</td>
      <td>male</td>
      <td>teacher</td>
      <td>teach student</td>
    </tr>
    <tr>
      <td>3</td>
      <td>collins</td>
      <td>female</td>
      <td>student</td>
      <td>love learning</td>
    </tr>
  </tbody>
</table>

```mysql
# 把所有的数据都存放在一张表中的弊端
1.表的组织结构复杂不清晰
2.浪费空间
3.扩展性差
4.冗余数据
# 我们把员工和部门拆成两张表
```

<table>
  <tbody>
    <tr>
      <th>id</th>
      <th>name</th>
      <th>gender</th>
      <th>dep_id</th>
    </tr>
    <tr>
      <td>1</td>
      <td>allen</td>
      <td>male</td>
      <td>1</td>
    </tr>
    <tr>
      <td>2</td>
      <td>kevin</td>
      <td>male</td>
      <td>1</td>
    </tr>
    <tr>
      <td>3</td>
      <td>collins</td>
      <td>female</td>
      <td>2</td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <th>id</th>
      <th>name</th>
      <th>comment</th>
    </tr>
    <tr>
      <td>1</td>
      <td>teacher</td>
      <td>teach student</td>
    </tr>
    <tr>
      <td>2</td>
      <td>student</td>
      <td>love learning</td>
    </tr>
  </tbody>
</table>

```mysql
# 寻找表于表之间的关系
# emp表 dep表
# part1
1.先站在左表emp的角度
2.去找左表emp的多条记录能否对应右表dep的一条记录

# part2
1.先站在右表dep的角度
2.去找右表dep的多条记录能否对应左表emp的一条记录

# part3
1.如果part2不成立,左表和右表的关系是一个单向的多对一
```

# 二十四、mysql之多对多

<table>
  <tbody>
    <tr>
      <th>id</th>
      <th>name</th>
      <th>price</th>
    </tr>
    <tr>
      <td>1</td>
      <td>python</td>
      <td>199.99</td>
    </tr>
    <tr>
      <td>2</td>
      <td>linux</td>
      <td>299.99</td>
    </tr>
    <tr>
      <td>3</td>
      <td>unix</td>
      <td>399.99</td>
    </tr>
     <tr>
      <td>3</td>
      <td>java</td>
      <td>99.99</td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <th>id</th>
      <th>name</th>
      <th>age</th>
    </tr>
    <tr>
      <td>1</td>
      <td>allen</td>
      <td>18</td>
    </tr>
    <tr>
      <td>2</td>
      <td>kevin</td>
      <td>18</td>
    </tr>
    <tr>
      <td>3</td>
      <td>collins</td>
      <td>18</td>
    </tr>
  </tbody>
</table>

<table>
    <tbody>
    <tr>
      <th>id</th>
      <th>author_id</th>
      <th>book_id</th>
    </tr>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>2</td>
      <td>1</td>
      <td>2</td>
    </tr>
      <tr>
      <td>3</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <td>4</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <td>5</td>
      <td>3</td>
      <td>4</td>
    </tr>
  </tbody>
</table>

```mysql
# 两张表之间是一个双向的多对一的关系,称之为多对多
# 建立第三章表,表中有一个字段fk左表的id,表中有一个字段fk右表的id

create table author(
	id int primary key auto_increment,
  name char(16),
  age int
)engine=innodb;

create table book(
	id int primary key auto_increment,
  name char(16),
  price decimal(5,2)
)engine=innodb;

create table author2book(
	id int primary key auto_increment,
  author_id int,
  book_id int,
  foreign key(author_id) references author(id) on update cascade on delete cascade,
  foreign key(book_id) references book(id) on update cascade on delete cascade
)engine=innodb;
```

# 二十五、mysql之一对一

<table>
    <tbody>
    <tr>
      <th>id</th>
      <th>name</th>
      <th>phone</th>
      <th>qq</th>
    </tr>
    <tr>
      <td>1</td>
      <td>allen</td>
      <td>110</td>
      <td>110</td>
    </tr>
    <tr>
      <td>2</td>
      <td>kevin</td>
      <td>120</td>
      <td>120</td>
    </tr>
    <tr>
      <td>3</td>
      <td>collins</td>
      <td>119</td>
      <td>119</td>
    </tr>
     <tr>
      <td>4</td>
      <td>mark</td>
      <td>114</td>
      <td>114</td>
    </tr>
  </tbody>
</table>

<table>
    <tbody>
    <tr>
      <th>id</th>
      <th>class_name</th>
      <th>customer_id</th>
    </tr>
    <tr>
      <td>1</td>
      <td>python01</td>
      <td>1</td>
    </tr>
    <tr>
      <td>2</td>
      <td>linux01</td>
      <td>2</td>
    </tr>
    <tr>
      <td>3</td>
      <td>python01</td>
      <td>3</td>
    </tr>
     <tr>
      <td>4</td>
      <td>linux02</td>
      <td>4</td>
    </tr>
  </tbody>
</table>

```mysql
# 一对一只需要在外键字段加上unique唯一约束
# 左表的一条记录唯一对应右表的一条记录,反之也是一样的

create table customer(
	id int primary key auto_increment,
  name char(16),
  phone char(11),
  qq char(10)
)engine=innodb;

create table student(
	id int primary key auto_increment,
  class_name char(16),
  customer_id int unique,
  foreign key(customer) references customer(id) on update cascade on delete cascade
)engine=innodb;
```

# 二十六、mysql之关联表练习

```mysql
# 查找表的关联关系使用sql语句创建

# 1
账号信息表 用户组 主机表 主机组
create table usergroup(
	id int primary key auto_increment,
  username char(16) unique,
  password char(16)
)engine=innodb;

create table user(
	id int primary key auto_increment,
  name char(16),
)engine=innodb;

create table hostgroup(
	id int primary key auto_increment,
  name char(16)
)engine=innodb;

create table host(
	id int primary key auto_increment,
  ip char(15) not null default,
)engine=innodb;

create table user2usergroup(
  id int primary key auto_increment,
  user_id int,
  usergroup_id int,
  foreign key(user_id) references d1.user(id) on update cascade on delete cascade,
  foreign key(usergroup_id) references d1.usergroup(id) on update cascade on delete cascade
)engine=innodb;

create table host2hostgroup(
	id int primary key auto_increment,
  host_id int,
  hostgroup_id int,
  foreign key(host_id) references d1.host(id) on update cascade on delete cascade,
  foreign key(hostgroup_id) references d1.host(id) on update cascade on delete cascade
)engine=innodb;
s
# 2
班级表 学生表 老师表 课程表 成绩表
create table class(
  id int primary key auto_increment,
  name char(16)
)engine=innodb;

create table student(
	id int primary key auto_increment,
  name cahr(16),
  age int,
  class_id int,
  foreign key (class_id) references class(id) on update cascade on delete cascade
)engine=innodb;

create table teacher(
	id int primary key auto_increment,
  name char(16),
  age int,
  gender enum("male","female"),
)engine=innodb;

create table course(
	id int primary key auto_increment,
  name char(16),
  teacher_id int,
  foreign key (teacher_id) references teacher(id) on update cascade on delete cascade,
)engine=innodb;

create table score(
	id int primary key auto_increment,
  score int,
  student_id int,
  course_id int,
  foreign key (student_id) references student(id) on update cascade on delete cascade,
  foreign key (course_id) references course(id) on update cascade on delete cascade
)engine=innodb;
```

# 二十七、mysql之修改表alter table

```mysql
语法：
1. 修改表名
      ALTER TABLE 表名 RENAME 新表名;

2. 增加字段
      ALTER TABLE 表名 ADD 字段名  数据类型 [完整性约束条件…],ADD 字段名  数据类型 [完整性约束条件…];
      ALTER TABLE 表名 ADD 字段名  数据类型 [完整性约束条件…]  FIRST;
      ALTER TABLE 表名 ADD 字段名  数据类型 [完整性约束条件…]  AFTER 字段名;      
alter table order add goods_sn varchar(128) unque;
3. 删除字段
      ALTER TABLE 表名 DROP 字段名;

4. 修改字段
      ALTER TABLE 表名 MODIFY  字段名 数据类型 [完整性约束条件…];
      ALTER TABLE 表名 CHANGE 旧字段名 新字段名 旧数据类型 [完整性约束条件…];
      ALTER TABLE 表名 CHANGE 旧字段名 新字段名 新数据类型 [完整性约束条件…];

#创建表
create table t01(
  id int primary key auto_increment,
  name char(16),
  age int,
  gender enum("male","female"),
  hobbies set("read","music","running"),
  birth date,
  birth_year year,
  create_time datetime,
  class_record time
)engine=innodb;

# 修改表名 rename
alter table t01 rename test01;

# 添加字段 add

# 单字段添加[默认从后追加]
alter table test01 add username char(16);

# 多字段添加[默认从后追加]
alter table test01 add password char(16),add email char(32);

# 指定位置添加字段

# 添加字段到第一个位置
alter table test01 add summary text first;

# 添加字段到某个字段的后面
alter table test01 add mobile char(11) after id;

# 指定多个位置添加
alter table test01 add id_number int first,add ssn int after summary;s

# 删除字段 drop
alter table test01 drop id_number;

# 修改字段[类型,约束] modify
alter table test01 modify ssn char(16);

# 修改字段名称[保留原来类型和约束]
alter table test01 change summary biref text;

# 修改字段名称并缺修改数据类型和约束
alter table test01 change age height float(3,2) not null default 1.80;
```

# 二十八、mysql之复制表

```mysql
# 复制表
create table book_copy select * from book; # 复制表结构 + 记录 (key不会复制: 主键、外键和索引)

# 如果想要key我们可修改
alter table book_copy modify id int primary key auto_increment;

# 只复制表结构(key不会复制: 主键、外键和索引)
create table book_copy_desc select * from book where 1=0; # 条件为假,查不到任何记录

# 复制表结构包括key(不复制记录)
create table emp01 like emp;
```

# 二十九、mysql删除表

```mysql
drop table 表名; 
```

# 三十、mysql之插入数据

```mysql
# 1.出入完整数据(顺序插入)
语法一：
insert into 表名(字段1,字段2,字段3,...字段n) values(value1,value2,value3,...valuen);
语法二:
insert into 表名 values(value1,value2,value3,...valuen); # value包括主键id

# 2.指定字段插入数据
语法:
insert into 表名(字段1,字段2,字段3) values(值1,值2,值3)

# 3.插入多条记录
语法：
insert into 表名 values
(值1,值2,值3),
(值1,值2,值3),
(值1,值2,值3),
(值1,值2,值3);

# 4.插入查询结果
语法:
insert into 表名(字段1,字段2,字段3) select (字段1,字段2,字段3) from 表2 where 条件;

#

create table test01(
	id int primary key auto_increment,
  username char(16),
  password char(16)
)engine=innodb;

# 正序插入
insert into test01(id,username,password) values(1,"allen","19891213");

# 非正序插入
insert into test01(password,username,id) values("19891213","kevin",2);

# 插入全部
insert into test01 values(3,"collins","19891213");

# 指定字段插入
insert into test01(username,password) values("mark","19891213");

# 插入多条记录
insert into test01 values(5,"mike","19891213"),(6,"lily","19891213");

# 插入查询结果
create table t01 like test01;

insert into t01 values(7,"zens","19891213"),(8,"dived","19891213");

insert into test01 select * from t01 where id > 6;
```

# 三十一、mysql之更新数据

```mysql
# 语法
update 表名 set 字段1=值1,...字段n=值n where CONDITION[条件] # 不加条件默认修改整个表

update test01 set username='hello' where username='mark';
```

# 三十二、mysql之删除数据

```mysql
# 语法
delete from 表名 where CONDITION[条件];

delete from mysql.user where password='';

delete from test01 where id<2;
```

# 三十三、mysql单表查询语法和优先级

```mysql
# 单表查询完整语法!!!
select distinct 字段1,字段2,...字段n from 表名 
																	 where 分组前过滤条件 
																	 group by 分组字段 
																	 having 分组后过滤条件
																	 order by 排序字段
																	 limit 限制条数;
# 关键字执行优先级!!!
from where group by having select distinct order by limit

# 准备数据
company.employee
员工id      id                  int             
姓名        emp_name            varchar
性别        sex                 enum
年龄        age                 int
入职日期     hire_date           date
岗位        post                varchar
职位描述     post_comment        varchar
薪水        salary               double
办公室       office              int
e部门编号    dep_id               int

create table employee(id int primary key auto_increment,
                      name char(16),
                      age int,
                      gender enum("male","female"),
                      hire_date date,
                      post char(16),
                      post_comment char(32),
                      salary float,
                      office int,
                      dep_id int
)engine=innodb;

insert into employee(name,gender,age,hire_date,post,salary,office,dep_id) values
('egon','male',18,'20170301','foreign office',7300.33,401,1),
('alex','male',78,'20150302','teacher',1000000.31,401,1),
('wupeiqi','male',81,'20130305','teacher',8300,401,1),
('yuanhao','male',73,'20140701','teacher',3500,401,1),
('liwenzhou','male',28,'20121101','teacher',2100,401,1),
('jingliyang','female',18,'20110211','teacher',9000,401,1),
('jinxin','male',18,'19000301','teacher',30000,401,1),
('cl','male',48,'20101111','teacher',10000,401,1),
('yy','female',48,'20150311','sale',3000.13,402,2),
('yaya','female',38,'20101101','sale',2000.35,402,2),
('dd','female',18,'20110312','sale',1000.37,402,2),
('xx','female',18,'20160513','sale',3000.29,402,2),
('gg','female',28,'20170127','sale',4000.33,402,2),
('zy','male',28,'20160311','operation',10000.13,403,3),
('cyj','male',18,'19970312','operation',20000,403,3),
('cyy','female',18,'20130311','operation',19000,403,3),
('cyt','male',18,'20150411','operation',18000,403,3),
('cy','female',18,'20140512','operation',17000,403,3);
```

# 三十四、mysql单表查询之简单查询

```mysql
select * from employee;
select name,gender,age,hire_date,post,salary,office,dep_id from employee;
select name,salary from employee;
```

# 三十五、mysql单表查询之四则运算查询

```mysql
# 通过四则运算查询
select name,salary*12 from employee;

select name,salary*12 as annual_salary from employee; # as 设置别名

select name,salary*12 annual_salary from employee; # 可以省略as

select name,age+1 from employee;
```

# 三十六、mysql单表查询之定义显示格式

```mysql
# 定制显示格式
# concat() 函数用于连接字符串
concat()函数连接字符串
select concat("name: ",name,"salary_annuel",salary*12) as info from employee;

# concat_ws() 第一个参数为分隔符
select concat_ws(':',name,salary*12) as info from employee;

# case语句(分支)
select (case when name = 'egon' then name 
             when name ='alex' then concat(name,"_DSB") 
             else concat(name,"SB") end) as new_name from employee;
select case when name='egon' then name 
						when name='alex' then concat(name,'_DSB') 
						else concat(name,'SB') end as new_name from employee;
```

# 三十七、mysql单表查询之where

```mysql
where字句中可以使用：

1. 比较运算符：> < >= <= <> !=
2. between 80 and 100 值在10到20之间
3. in(80,90,100) 值是10或20或30
4. like 'egon%'
    pattern可以是%或_，
    %表示任意多字符
    _表示一个字符
5. 逻辑运算符：在多个条件直接可以使用逻辑运算符 and or not

# 1.单条件查询
select name from employee where post='sale';

# 2.多条件查询
select name,salary from employee where post='teacher' and salary>10000;

# 3.关键字between and 在什么到什么中间
select name from employee where id between 1 and 10;

select name from employee where id not between 1 and 10;

# 4.关键字is null(判断某个字段是否为null不能用等号,需要使用is)
select name,post_comment from employee where post_comment is null; # 查询职位描述为空的

select name,post_comment from employee where post_comment is not null;

# 5.关键字IN集合查询
select name from employee where id in (1,2,3);

select name from employee where id not in (1,2,3);

# 6.关键字like模糊查询
# 通配符%
select name from employee where name like 'eg%';

# 通配符_
select name from employee where name like "_lex";

1.查看岗位是teacher的员工姓名、年龄
select name,age from employee where post ="teacher";

2.查看岗位是teacher且年龄大于30岁的员工姓名、年龄
select name,age from employee where age>30;

3. 查看岗位是teacher且薪资在9000-1000范围内的员工姓名、年龄、薪资
select name,age,concat("salary:",salary*12) as salary from employee where salary between 9000 and 10000;

4. 查看岗位描述不为NULL的员工信息
select * from employee where post_comment is not null;

5. 查看岗位是teacher且薪资是10000或9000或30000的员工姓名、年龄、薪资
select name,age,salary from employee where salary in (10000,9000,30000);

6. 查看岗位是teacher且薪资不是10000或9000或30000的员工姓名、年龄、薪资
select name,age,salary from employee where salary not in (10000,9000,30000);

7. 查看岗位是teacher且名字是jin开头的员工姓名、年薪
select name,salary from employee where name like "jin%";

```

# 三十八、mysql单表查询之distinct

```mysql
# distinct 对查询结果去重
select distinct post from employee;

select distinct dep_id from employee;
```

# 三十九、mysql单表查询之group_by

```mysql
# 首先明确group by 是在 where 之后使用的
# 注意:可以按照任意字段分组，但是分组完毕后，比如group by post，只能查看post字段，
# 如果想查看组内信息，需要借助于聚合函数

sql_mode:ONLY_FULL_GROUP_BY
# ONLY_FULL_GROUP_BY的语义就是确定select target list中的所有列的值都是明确语义，简单的说来，
# 在ONLY_FULL_GROUP_BY模式下，target list中的值要么是来自于聚集函数的结果，
# 要么是来自于group by list中的表达式的值

# 设置sql_mole如下操作(我们可以去掉ONLY_FULL_GROUP_BY模式)：
mysql> set global sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';
--------------------------------------------------------------------------------------------
# 单独使用 group by 关键字分组
select post from employee group by post;

# group by 和 group_concat()函数使用

select post,group_concat(name) from employee group by post;

select post,group_concat(salary*12) as salary from employee group by post;

# group by 和聚合函数使用
select post,sum(salary) from employee group by post; # 每个职位的总薪水

# 聚合函数
# 强调：聚合函数聚合的是组的内容，若是没有分组，则默认一组,也就是一张表作为一个分组
sum count max min avg

select count(*) from employee; # 所有员工的数量

select max(salary) from employee; # 工资最高的员工

select min(salary) from employee; # 工资最低的员工

select avg(salary) from employee; # 所有员工的平均工资

select sum(salary) from employee; # 所有员工的总工资

#  练习
1. 查询岗位名以及岗位包含的所有员工名字
select post,group_concat("member:",name) as member from employee group by post;

2. 查询岗位名以及各岗位内包含的员工个数
select post,count(id) as emp_count from employee group by post;

3. 查询公司内男员工和女员工的个数
select gender, count(id) from employee group by gender;

4. 查询岗位名以及各岗位的平均薪资
select post,avg(salary) from employee group by post;

5. 查询岗位名以及各岗位的最高薪资
select post,max(salary) from employee group by post;

6. 查询岗位名以及各岗位的最低薪资
select post,min(salary) from employee group by post;

7. 查询男员工与男员工的平均薪资，女员工与女员工的平均薪资
select gender,avg(salary) from employee group by gender;
```

# 四十、mysql单表查询之having

```mysql
#1.Where 发生在分组group by之前，因而Where中可以有任意字段，但是绝对不能使用聚合函数
#2.Having发生在分组group by之后，因而Having中可以使用分组的字段，无法直接取到其他字段,可以使用聚合函数

1. 查询各岗位内包含的员工个数小于2的岗位名、岗位内包含员工名字、个数
select post,group_concat(name),count(id) from employee group by post having count(id) < 2;

2. 查询各岗位平均薪资大于10000的岗位名、平均工资
select post,avg(salary) from employee group by post having avg(salary)>10000;

3. 查询各岗位平均薪资大于10000且小于20000的岗位名、平均工资
select post,avg(salary) from employee group by post having avg(salary)>10000 and avg(salary)<20000;
```

# 四十一、mysql单表查询之order by

```mysql
# order by
# 语法
select * from employee order by salary; # 默认是升序

# 升序
select * from employee order by salary asc;

# 降序
select * from employee order by salary desc;

# 按多列排序:先按照age排序，如果年纪相同，则按照薪资排序
select * from employee order by age asc,salary desc;

1. 查询所有员工信息，先按照age升序排序，如果age相同则按照hire_date降序排序
select * from employee order by age asc,hire_date desc;

2. 查询各岗位平均薪资大于10000的岗位名、平均工资,结果按平均薪资升序排列
select post,avg(salary) from employee group by post having avg(salary) >10000 order by avg(salary) asc;

3. 查询各岗位平均薪资大于10000的岗位名、平均工资,结果按平均薪资降序排列
select post,avg(salary) from employee group by post having avg(salary)>10000 order by avg(salary) desc;
```

# 四十二、mysql单表查询之limit

```mysql
# limit 限制查询的记录数
# 语法 
# 默认初始位置为0 
select * from employee limit 5;

# LIMIT 0,5 第一个参数表示offset[偏移], 第二个参数为记录数[显示数量]
select * from employee limit 0,5; # 检索1-5
select * from employee limit 2,5; # 检索3-7

# LIMIT 2 OFFSET 3 显示两条记录,偏移三个,相当于检索4-5
select * from employee limit 2 offset 3;
```

# 四十三、mysql单表查询之正则表达式

```mysql
# regexp
# 查询ale开头的员工
select * from employee where name regexp '^ale';

# 查询on结尾的员工
select * from employee where name regexp 'on$';

# 查询名字有来两个m的员工
select * from employee where name regexp 'm{2}';

1.查看所有员工中名字是jin开头，n或者g结尾的员工信息
select * from employee where name regexp '^jin.*[ng]$';
```

# 四十四、mysql多表查询之join

```mysql
# 准备数据
create table dep(id int primary key auto_increment,name char(32))engine=innodb;

create table emp(id int primary key auto_increment,name char(16),gender enum("male","female"),age int,dep_id int)engine=innodb;

insert into dep values
(200,'technology'),
(201,'Human Resources'),
(202,'Sales'),
(203,'Operation');

insert into emp(name,gender,age,dep_id) values
('egon','male',18,200),
('alex','female',48,201),
('wupeiqi','male',38,201),
('yuanhao','female',28,202),
('liwenzhou','male',18,200),
('jingliyang','female',18,204);
--------------------------------------------------------------------------------------------
# 语法
SELECT 字段列表 FROM 表1 INNER|LEFT|RIGHT JOIN 表2 ON 表1.字段 = 表2.字段;

1.交叉连接
# 不适用任何匹配条件,生成笛卡尔积
select * from dep,emp;

2.内连接:只连接匹配的行
select * from emp inner join dep on emp.dep_id=dep.id;
# 建议：使用join语句时，小表在前，大表在后

3.外链接之左连接:优先显示左表全部记录
select * from dep left join emp on dep.id=emp.dep_id;

4 外链接之右连接:优先显示右表全部记录
select * from dep right join emp on dep.id=emp.dep_id;

5 全外连接:显示左右两个表全部记录(利用union去重特性)
select * from dep left join emp on dp.id=emp.dep_id union select * from dep right join emp on dep.id=emp.dep_id;

6 内连接(NATURAL JOIN):自连接的表要有共同的列名字
# 准备表
create table country(id int primary key auto_increment,name var(32),code int);
create table city(id int primary key auto_increment,name varchar(32),countrycode int);
create table countrylanguage(id int primary key auto_increment,name varchar(32),code int);
通过自连接查询city所属国家的语言
select city.name,countrylanguage.name from city natural join countrylanguage;
# 关联相同的字段
```

# 四十五、mysql多表查询之union

```mysql
# union  将表进行上下拼接去重
select * from dep union select * from dep;

# union all 将表进行上下拼接不去重
select * from dep union all select * from dep;
```

# 四十六、mysql多表条件查询

```mysql
# 以内连接的方式查询employee和department表，并且employee表中的age字段值必须大于25,即找出年龄大于25岁的员工以及员工所在的部门
select * from emp inner join dep on emp.dep_id=dep.id where age>25;

# 以内连接的方式查询employee和department表，并且以age字段的升序方式显示
select * from emp inner join dep on emp.deo_id=dep.id order by age asc;
```

# 四十七、mysql之子查询

```mysql
# 1.自查询是将一个查询语句嵌套在另一个查询语句中
# 2.内层查询语句的查询结果,可以为外层查询语句提供查询条件
# 3.子查询中可以包含:in、not in、any、all、exists、not exists等关键字
# 4.还可以包含比较运算符:=、!=、>、<等
---------------------------------------------------------------------------------------------
1.带in关键字的子查询
# 查询平均年龄在25岁以上的部门名
select name from dep where id in (select dep_id from employee where age>25); 
# 子查询一定加上括号

# 查看技术部员工姓名
select name from emp where dep_id = (select id from dep where name='technology');
select name from emp dep_id in (select id from dep where name='technology');

# 查看不足1人的部门名(子查询得到的是有人的部门id)
select name from dep where id in (select dep_id from emp group by dep_id having count(id)<1);

2.带比较运算的子查询
# 比较运算符：=、!=、>、>=、<、<=、<>

# 查询大于所有人平均年龄的员工名与年龄
select name,age from emp where age > (select avg(age) from emp);

#查询大于部门内平均年龄的员工名、年龄 
select name,age from emp as t1 inner join (select dep_id,avg(age) as avg_age from emp group by dep_id) as t2 on t1.dep_id=t2.dep_id where t1.age>t2.avg_age;

3.带exists关键字的子查询
# EXISTS关字键字表示存在 在使用EXISTS关键字时 内层查询语句不返回查询的记录
# 而是返回一个真假值 True或False

# dep表中存在dept_id=203，Ture
select * from emp where exists (select id from dep where id=203);

# department表中存在dept_id=205，False
select * from emp where exists (select id from dep where id=205);

# 练习
company.employee
    员工id      id                  int             
    姓名        emp_name            varchar
    性别        sex                 enum
    年龄        age                 int
    入职日期     hire_date           date
    岗位        post                varchar
    职位描述     post_comment        varchar
    薪水        salary              double
    办公室       office              int
    部门编号     depart_id           int

create table emp(
	id int primary key auto_increment,
  name char(16),
  gender enum("male","female"),
  age int,
  hire_date date,
  post char(16),
  post_comment text,
  salary float,
  office int,
  dep_id int
)engine=innodb;

insert into emp(name,gender,age,hire_date,post,salary,office,dep_id) values
('egon','male',18,'20170301','foreign office',7300.33,401,1),
('alex','male',78,'20150302','teacher',1000000.31,401,1),
('wupeiqi','male',81,'20130305','teacher',8300,401,1),
('yuanhao','male',73,'20140701','teacher',3500,401,1),
('liwenzhou','male',28,'20121101','teacher',2100,401,1),
('jingliyang','female',18,'20110211','teacher',9000,401,1),
('jinxin','male',18,'19000301','teacher',30000,401,1),
('cehnglong','male',48,'20101111','teacher',10000,401,1),
('yaiyai','female',48,'20150311','sale',3000.13,402,2),
('yaya','female',38,'20101101','sale',2000.35,402,2),
('dingding','female',18,'20110312','sale',1000.37,402,2),
('xingxing','female',18,'20160513','sale',3000.29,402,2),
('gege','female',28,'20170127','sale',4000.33,402,2),
('zhangye','male',28,'20160311','operation',10000.13,403,3),
('chenyajin','male',18,'19970312','operation',20000,403,3),
('chenyayin','female',18,'20130311','operation',19000,403,3),
('chenyatong','male',18,'20150411','operation',18000,403,3),
('chenyatie','female',18,'20140512','operation',17000,403,3);
# 查询每个部门最新入职的那位员工

# 连表
select * from emp as t1 inner join (select dep_id,max(hire_date) as new_time from emp group by dep_id) as t2 on t1.dep_id=t2.dep_id where t1.hire_date=t2.new_time;

select * from emp as t1 inner join (select posdest,max(hire_date) as new_hire from emp group by post) as t2 on t1.post=t2.post where t1.hire_date=t2.new_hire;

# 子查询
select * from emp where id in (select (select id from emp as t2 where t1.post=t2.post order by hire_date desc limit 1) from emp as t1 group by post);
```

# 四十八、mysql之pymysql

```python
# 安装
pip3 install pymysql

import pymysql

conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='MYsql891213',
                       database='t001',
                       charset='utf8') # 连接数据库

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 获取游标,并将返回值设置为字典

sql = 'select * from dep;'

rows = cursor.execute(sql)

print(rows)  # 行数

# print(cursor.fetchone())  # 取出一个

# print(cursor.fetchmany(1))  # 取出指定的数量

print(cursor.fetchall())  # 取出所有

cursor.scroll(1, 'absolute')  # 绝对移动,相对于一开始的位置往后移动1条

cursor.scroll(1, 'relative')  # 相对移动,相对于你cursor当前的位置往后移动1条

print(cursor.fetchall())

cursor.close() # 关闭游标

conn.close() # 关闭连接

# 针对修改的操作每次都需要提交[commit]

# 增
sql = 'insert into dep(id,name) values(%s,%s)'

rows = cursor.execute(sql,(204,'market'))

print(cursor.lastrowid) # 获取当前插入记录的行数

cursor.commit()
# 一次插入多行记录
sql = 'insert into dep(id,name) values(%s,%s)'

rows = cursor.execute(sql,[(205,'m'),(206,'n')])

cursor.commit()
# 改
sql = 'update dep set name=%s where id=%s'

rows = cursor.execute(sql,('x',204))

cursor.execute()
# 删
sql 'delete from dep where id=%s'

rows = cursor.execute(sql,(204,))

cursor.execute()
```

# 四十九、mysql之视图(view)

```mysql
# 视图就是通过查询得到一张虚拟表然后保存下来,下次用的时候直接使用即可

# 频繁使用一张虚拟表,通过创建视图可以不需要重复查询

# 语法
create view 视图表名 as 查询语句;

# 1.在硬盘中,视图只有表结构文件,没有表数据文件
# 2.视图通常是用于查询,尽量不要修改视图中的数据(修改视图中数据会导致原表的数据也会跟着改变)

# 创建一张视图表
create view v_dep as select * from dep;

# 查询视图
select * from v_dep;

# 修改视图
# 语法 ALTER VIEW 视图名称 AS SQL语句
# 本质就是修改sql语句
alter view v_dep as select * from dep where id >200;

# 删除视图
drop view v_dep;
```

# 五十、mysql之触发器

```mysql
# 在满足对表进行【增、删、改】操作的情况下,会触发的功能
# 触发器专门针对我们对某一张表的增删改的行为,这类行为一旦执行就会触发触发器的执行,即自动运行别外一段sql代码,

# 创建触发器
# 语法：
CREATE TRIGGER 触发器名 BEFORE/AFTER INSERT/DELETE/UPDATE ON 表名 FOR EACH ROW
BEGIN
		sql代码
END;

# 准备表
create table cmd(
	id int primary key auto_increment,
  user char(16),
  priv char(16),
  cmd char(16),
  sub_time datetime,
  success enum("yes","no")
)engine=innodb;

create table errlog(
	id int primary key auto_increment,
  err_cmd char(16),
  err_time datetime
)engine=innodb;
	
# 插入之前
# delimiter // 更换mysql的结束符
delimiter //
create trigger tri_before_insert_cmd before insert on cmd for each row
begin
if new.success='no' then
insert into errlog(err_cmd,err_time) values(new.cmd,new.sub_time);
end if;
end//
delimiter ;

# 插入之后
delimiter //
create trigger tri_after_insert_cmd after insert on cmd for each row
begin
if new.success='no' then
insert into errlog(err_cmd,err_time) values(new.cmd,new.sub_time);
end if;
end//
delimiter ;

# 更新之前
delimiter //
create trigger tri_before_update_cmd before update on cmd for each row
begin
if new.success='no' then
insert into errlog(err_cmd,err_time) values(new.cmd,new.sub_time);
end if;
end//
delimiter ;

# 更新之后
delimiter //
create trigger tri_after_update_cmd after update on cmd for eache row
begin
if new.success='no' then
insert into errlog(err_cmd,err_time) values(new.cmd,new.sub_time);
end if;
end//
delimiter ;

# 删除之前
delimiter //
create trigger tri_before_delete_cmd before delete on cmd for each row
begin
if old.success='no' then
insert into errlog(err_cmd,err_time) values(old.cmd,old.sub_tiem)l
end if;
end//
delimiter ;

# 删除之后
delimiter //
create trigger tri_after_delete_cmd after delete on cmd for each row
begin
if old.success='no' then
insert into errlog(err_cmd,err_time) values(old.cmd,old.sub_time);
end if;
end//
delimiter ;
# 注意:NEW表示即将插入的数据行，OLD表示即将删除的数据行。

# 使用触发器
# 触发器无法由用户直接调用，而知由于对表的【增/删/改】操作被动引发的

# 查看触发器
# 语法
SHOW TRIGGERS 
show create trigger 触发器名

# 删除触发器
# 语法
drop trigger 触发器名;

drop trigger tri_before_insert_cmd;
```

# 五十一、mysql之事务(原子操作)

```mysql
01.什么是事务
开启一个事务可以包含一些sql语句,这些sql语句要么同时成功
要么同时失败,称之为事务的原子性
02.事务的作用

#准备表
create table user(
	id int primary key auto_increment,
  name char(16),
  balance int
)engine=innodb;

insert into user(name,balance) values('allen',1000),('kevin',1000),('collins',1000);

# 原子操作
# 语法
start transaction;
sql代码
rollback;
commit;

start transaction;
update user set balance=900 where name='allen';
update user set balance=1010 where name='kevin';
update user set balance=1090 where name='collins';
rollback; # 回滚意味着回到一面sql语句修改之前
commit; # 提交本次操作[只要不执行commit数据都不会保存到硬盘中]
```

# 五十二、mysql存储过程

```mysql
# 存储过程:包含了一系列可真行的sql语句,存储过程存放与mysql中,通过调用它的名字可以执行起=其内部的一堆sql
# 三种开发模式
1.应用程序:只需要开发应用程序的逻辑
	mysql:编写好存储过程,以供应用程序调用
	优点:开发效率,执行效率都高
	缺点:扩展性差
	
2.应用程序:开发应用程序的逻辑和编写原生sql
	mysql:只需正常运行
	优点:扩展性高
	缺点:开发效率,执行效率都低

3.应用程序:除了开发应用程序的逻辑,不需要编写原生sql,使用别人编写好的框架orm
	mysql:
	优点:不用再编写原生sql,开发效率高
# 创建存储过程
# 语法
delimiter //
# 定义存储过程
create procedure p1()
begin
sql代码
end//
delimiter ;
# 调用存储过程
call p1();
---------------------------------------------------------------------------------------------
# 无参数
delimiter //
create procedure p1()
begin
select * from dep;
end//
delimiter ;

call p1();
---------------------------------------------------------------------------------------------
# 有参数
# in    仅用于传入参数用
# out   仅用于返回值用
# inout 既可以传入又可以当作返回值

# 设置变量
set @x=1;

# 查看变量
select @x;

delimiter //
create procedure p1(in m int,in n int,out result int) 
# (in/out/inout 变量名 声明数据类型)
begin
select name from dep where id > m and id < n;
set res=1;
end//
delimiter ;
---------------------------------------------------------------------------------------------
# 查看存储过程
show create procedure p1;
# 查看所有存储过程
show procedure status;
---------------------------------------------------------------------------------------------
# 如果使用存储过程
1.在mysql中调用
set @result=0
call p1(1,3,@result); # out/inout必须传入一个变量,传一个固定值会报错
select @result; # 查看返回值

2.在python程序中调用
import pymysql

conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='MYsql891213',
                       database='t001',
                       charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
cursor.callproc('p02', (200, 202, 0))  # @_p02_0=200 @_p02_1=202 @_p02_2=0
print(cursor.fetchall())
cursor.execute('select @_p02_2')  # 查看返回值结果
print(cursor.fetchall())
cursor.close()
conn.close()
---------------------------------------------------------------------------------------------
# 删除存储过程
drop procedure 存储过程名;

drop procedure p1;
---------------------------------------------------------------------------------------------
# 注意:视图触发器存储过程都存放在创建的数据库中

# 存储过程事务的使用
delimiter //
create procedure x01(out res int)
begin
declare exit handler for sqlexception
begin
set res=1;
rollback;
end;
declare exit handler for sqlwarning
begin
set res=2;
rollback;
end;
start transaction;
update user set balance=900 where name='allen';
update user set balance=1010 where name='kevin';
update user set balance=1090 where name='collins';
commit;
set res=0;
end//
delimiter ;
```

# 五十三、mysql之函数

```mysql
一、数学函数
    ROUND(x,y)
        返回参数x的四舍五入的有y位小数的值
        
    RAND()
        返回０到１内的随机值,可以通过提供一个参数(种子)使RAND()随机数生成器生成一个指定的值。

二、聚合函数(常用于GROUP BY从句的SELECT查询中)
    AVG(col)返回指定列的平均值
    COUNT(col)返回指定列中非NULL值的个数
    MIN(col)返回指定列的最小值
    MAX(col)返回指定列的最大值
    SUM(col)返回指定列的所有值之和
    GROUP_CONCAT(col) 返回由属于一组的列值连接组合而成的结果    
    
三、字符串函数

    CHAR_LENGTH(str)
        返回值为字符串str 的长度，长度的单位为字符。一个多字节字符算作一个单字符。
    CONCAT(str1,str2,...)
        字符串拼接
        如有任何一个参数为NULL ，则返回值为 NULL。
    CONCAT_WS(separator,str1,str2,...)
        字符串拼接（自定义连接符）
        CONCAT_WS()不会忽略任何空字符串。 (然而会忽略所有的 NULL）。

    CONV(N,from_base,to_base)
        进制转换
        例如：
            SELECT CONV('a',16,2); 表示将 a 由16进制转换为2进制字符串表示

    FORMAT(X,D)
        将数字X 的格式写为'#,###,###.##',以四舍五入的方式保留小数点后 D 位， 并将结果以字符串的形式返回。若  D 为 0, 则返回结果不带有小数点，或不含小数部分。
        例如：
            SELECT FORMAT(12332.1,4); 结果为： '12,332.1000'
    INSERT(str,pos,len,newstr)
        在str的指定位置插入字符串
            pos：要替换位置其实位置
            len：替换的长度
            newstr：新字符串
        特别的：
            如果pos超过原字符串长度，则返回原字符串
            如果len超过原字符串长度，则由新字符串完全替换
    INSTR(str,substr)
        返回字符串 str 中子字符串的第一个出现位置。

    LEFT(str,len)
        返回字符串str 从开始的len位置的子序列字符。

    LOWER(str)
        变小写

    UPPER(str)
        变大写
   
    REVERSE(str)
        返回字符串 str ，顺序和字符顺序相反。
        
    SUBSTRING(str,pos) , SUBSTRING(str FROM pos) SUBSTRING(str,pos,len) , SUBSTRING(str FROM pos FOR len)
        不带有len 参数的格式从字符串str返回一个子字符串，起始于位置 pos。带有len参数的格式从字符串str返回一个长度同len字符相同的子字符串，起始于位置 pos。 使用 FROM的格式为标准 SQL 语法。也可能对pos使用一个负值。假若这样，则子字符串的位置起始于字符串结尾的pos 字符，而不是字符串的开头位置。在以下格式的函数中可以对pos 使用一个负值。

        mysql> SELECT SUBSTRING('Quadratically',5);
            -> 'ratically'

        mysql> SELECT SUBSTRING('foobarbar' FROM 4);
            -> 'barbar'

        mysql> SELECT SUBSTRING('Quadratically',5,6);
            -> 'ratica'

        mysql> SELECT SUBSTRING('Sakila', -3);
            -> 'ila'

        mysql> SELECT SUBSTRING('Sakila', -5, 3);
            -> 'aki'

        mysql> SELECT SUBSTRING('Sakila' FROM -4 FOR 2);
            -> 'ki'
            
四、日期和时间函数
    CURDATE()或CURRENT_DATE() 返回当前的日期
    CURTIME()或CURRENT_TIME() 返回当前的时间
    DAYOFWEEK(date)   返回date所代表的一星期中的第几天(1~7)
    DAYOFMONTH(date)  返回date是一个月的第几天(1~31)
    DAYOFYEAR(date)   返回date是一年的第几天(1~366)
    DAYNAME(date)   返回date的星期名，如：SELECT DAYNAME(CURRENT_DATE);
    FROM_UNIXTIME(ts,fmt)  根据指定的fmt格式，格式化UNIX时间戳ts
    HOUR(time)   返回time的小时值(0~23)
    MINUTE(time)   返回time的分钟值(0~59)
    MONTH(date)   返回date的月份值(1~12)
    MONTHNAME(date)   返回date的月份名，如：SELECT MONTHNAME(CURRENT_DATE);
    NOW()    返回当前的日期和时间
    QUARTER(date)   返回date在一年中的季度(1~4)，如SELECT QUARTER(CURRENT_DATE);
    WEEK(date)   返回日期date为一年中第几周(0~53)
    YEAR(date)   返回日期date的年份(1000~9999)
    
    重点:
    DATE_FORMAT(date,format) 根据format字符串格式化date值

       mysql> SELECT DATE_FORMAT('2009-10-04 22:23:00', '%W %M %Y');
        -> 'Sunday October 2009'
       mysql> SELECT DATE_FORMAT('2007-10-04 22:23:00', '%H:%i:%s');
        -> '22:23:00'
       mysql> SELECT DATE_FORMAT('1900-10-04 22:23:00',
        ->                 '%D %y %a %d %m %b %j');
        -> '4th 00 Thu 04 10 Oct 277'
       mysql> SELECT DATE_FORMAT('1997-10-04 22:23:00',
        ->                 '%H %k %I %r %T %S %w');
        -> '22 22 10 10:23:00 PM 22:23:00 00 6'
       mysql> SELECT DATE_FORMAT('1999-01-01', '%X %V');
        -> '1998 52'
       mysql> SELECT DATE_FORMAT('2006-06-00', '%d');
        -> '00'
        
五、加密函数
    MD5()    
        计算字符串str的MD5校验和
    PASSWORD(str)   
        返回字符串str的加密版本，这个加密过程是不可逆转的，和UNIX密码加密过程使用不同的算法。
        
六、控制流函数            
    CASE WHEN[test1] THEN [result1]...ELSE [default] END
        如果testN是真，则返回resultN，否则返回default
    CASE [test] WHEN[val1] THEN [result]...ELSE [default]END  
        如果test和valN相等，则返回resultN，否则返回default

    IF(test,t,f)   
        如果test是真，返回t；否则返回f

    IFNULL(arg1,arg2) 
        如果arg1不是空，返回arg1，否则返回arg2

    NULLIF(arg1,arg2) 
        如果arg1=arg2返回NULL；否则返回arg1    
```

# 五十四、mysql之异常处理

```mysql
# 定义一个异常处理
# 注意:declare...handler语句必须出现在变量或条件声明的后面
语法 DECLARE condition_name CONDITION FOR [condition_type]
condition_name参数表示异常的名称
condition_type参数异常类型
# 基本格式
# 未命名
BEGIN
　　DECLARE CONTINUE HANDLER FOR 1051
END;
# 有命名
BEGIN
　　DECLARE no_such_table CONDITION FOR 1051;
　　DECLARE CONTINUE HANDLER FOR no_such_table
END;
# 异常处理
DECLARE handler_type HANDLER FOR condition_value [,...] sp_statement
handler_type: CONTINUE|EXIT|UNDO
handler_type为错误处理方式，参数为3个值之一；
CONTINUE表示遇到错误不处理，继续执行；
EXIT表示遇到错误时马上退出；
UNDO表示遇到错误后撤回之前的操作，MySQL暂不支持回滚操作
# 作用域
begni..end内，哪果错误处理定义在begin ... end内，则在该begin...end之外的错误不会被捕获。
它能够捕获其它储过程的错误。
---------------------------------------------------------------------------------------------
condition_value: SQLSTATE [VALUE] sqlstate_value|
																	condition_name|
																	SQLWARNING|
																	NOT FOUND|
																	SQLEXCEPTION|
																	mysql_error_code
condition_value表示错误类型；SQLSTATE [VALUE] sqlstate_value为包含5个字符的字符串错误值；
condition_name表示DECLARE CONDITION定义的错误条件名称；
SQLWARNING匹配所有以01开头的SQLSTATE错误代码；
NOT FOUND匹配所有以02开头的SQLSTATE错误代码；
SQLEXCEPTION匹配所有没有被SQLWARNING或NOT FOUND捕获的SQLSTATE错误代码；
mysql_error_code匹配数值类型错误代码
---------------------------------------------------------------------------------------------
# 例子
//方法一：捕获sqlstate_value异常
//这种方法是捕获sqlstate_value值。如果遇到sqlstate_value值为"42S02"，执行CONTINUE操作，并输出"NO_SUCH_TABLE"信息
DECLARE CONTINUE HANDLER FOR SQLSTATE '42S02' SET @info='NO_SUCH_TABLE';

//方法二：捕获mysql_error_code异常
//这种方法是捕获mysql_error_code值。如果遇到mysql_error_code值为1146，执行CONTINUE操作，并输出"NO_SUCH_TABLE"信息；
DECLARE CONTINUE HANDLER FOR 1146 SET @info='NO_SUCH_TABLE';

//方法三：先定义条件，然后捕获异常
DECLARE no_such_table CONDITION FOR 1146;
DECLARE CONTINUE HANDLER FOR NO_SUCH_TABLE SET @info='NO_SUCH_TABLE';

//方法四：使用SQLWARNING捕获异常
DECLARE EXIT HANDLER FOR SQLWARNING SET @info='ERROR';

//方法五：使用NOT FOUND捕获异常
DECLARE EXIT HANDLER FOR NOT FOUND SET @info='NO_SUCH_TABLE';

//方法六：使用SQLEXCEPTION捕获异常
DECLARE EXIT HANDLER FOR SQLEXCEPTION SET @info='ERROR';
```

# 五十五、mysql之流程控制(条件语句)

```mysql
# 大前提mysql中的函数只能在sql语句中使用

# if
delimiter //
create procedure p01()
begin
declare i int default 0;
# 声明一个变量为整形默认值为0
if i =1 then
select 1;
elseif i=2 then
select 2;
else
select 3;
end if;
end//
delimiter ;

# case
select 
(case 
 when name='allen' then 
 name
 when name='kevin' then
 	concat('hey',name)
 else
 concat('hello',name)
 end) from user;
```

# 五十六、mysql之流程控制(循环语句)

```mysql
# 大前提mysql中的函数只能在sql语句中使用
delimiter //
create procedure auto_insert()
begin
declare i int default 1;
while (i<100001)do
insert into bench_index values(i,concat('allen',i),18,concat('allen',i,'@live.com'));
set i=i+1;
end while;
end//
delimiter ;
```

# 五十七、mysql之date_format

```mysql
create table blog(
	id int primary key auto_increment,
  name char(16),
  sub_time datetime
)engine=innodb;

# date_format格式化时间
select date_format(sub_time,'%Y-%m'),count(id) from blog 
																							 group by date_format(sub_time,'%Y-%m');
```

# 五十八、mysql之set

```mysql
# set
# 语法
# set语句可用于向系统变量或用户变量赋值
SET @var_name = expr [, @var_name = expr]

# 使用select语句来定义：
SELECT @var_name := expr [, @var_name = expr] ...


select t1.id,t1.name,t2.ct from category as t1 inner join (select category_id,count(id) as ct from article where user_id=1 group by category_id) as t2 on t1.id=t2.category_id;


select t1.id,t1.name,t2.ct from tag as t1 inner join (select tag_id,count(id) as ct from article_tag group by tag_id) as t2 on t1.id=t2.tag_id where t1.user_id=1;


select t1.title,t1.summary,t1.status,t2
select * from tag where id=1;
t1.id,t1.title,t1.summary,t1.like_num,t1.comment_num,t3.name,t1.status,t1.is_hot,t1.create_time from article as t1 inner join (select article_id from article_tag where tag_id=1) as t2 on t1.id=t2.article_id inner join (select id,name from category) as t3 on t1.category_id=t3.id;



select t1.id,t1.title,t1.summary,t1.like_num,t1.comment_num,t3.name,t1.status,t1.is_hot,t1.create_time from article as t1 inner join (select article_id from article_tag where tag_id=1) as t2 on t1.id=t2.article_id inner join (select id,name from category) as t3 on t1.category_id=t3.id;




select t1.id,t1.title,t1.summary,t1.like_num,t1.comment_num,t2.name,t1.status,t1.is_hot,t1.create_time from article as t1 inner join category as t2 on t1.category_id=t2.id where date_format(t1.create_time,"%Y-%m")=%s
```

# 五十九、mysql之do

```mysql
do sleep(5) # 睡眠5秒
SELECT c.Score, b.Rank FROM Scores c INNER JOIN ( SELECT Score, ( @i := @i + 1 ) AS Rank FROM ( SELECT Score FROM Scores GROUP BY Score ORDER BY Score DESC ) a, ( SELECT @i := 0 ) AS it ) b ON c.Score = b.Score ORDER BY c.Score DESC
```

# 六十、mysql之if、ifnull、nullif

```mysql
ifnull
# MySQL IFNULL函数是MySQL控制流函数之一，它接受两个参数，如果不是NULL，则返回第一个参数。 否则，IFNULL函数返回第二个参数
# 例子
select ifnull(1,0);
--return 1
select ifnull('',0);
--return 0
nullif
# NULLIF函数是接受2个参数的控制流函数之一。如果第一个参数等于第二个参数，则NULLIF函数返回NULL，否则返回第一个参数
# 例子
select nullif(1,1);
--return null
select nullif(1,2);
--return 1
if
# 在mysql中if()函数的用法类似于java中的三目表达式，其用处也比较多，具体语法如下:IF(expr1,expr2,expr3)，如果expr1的值为true，则返回expr2的值，如果expr1的值为false,则返回expr3的值
# 列子
select name,if(gender=0,'male','female') as gender from g01;
```

# 六十一、mysql之创建函数

```mysql
# 格式
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  set N=N-1;
  RETURN (
      # Write your MySQL query statement below.
			select ifnull(
        (select distinct Salary from Employee order by Salary desc limit 1 offset N),
        null
      )
  );
END
```

# 六十二、mysql源码编译安装(5.7)

```shell
1、下载源码包
    https://dev.mysql.com/downloads/mysql/
    # Select Operating System:Source Code
    # Select OS Version:Generic Linux(Architecture Independent)
2.MySQL的版本选择:
    MySQL5.6:
    1.选择GA 6-12个月
    2.小版本号为偶数版

    MySQL5.7
    1.选择GA 6-12个月
    2.小版本号为偶数版
    3.MySQL5.7.17以上版本   MGR
3、解压源码包
		tar xvf mysql-5.7.26.tar.gz
4、下载编译依赖(cmake是新版MySQL的编译工具)
		sudo yum install gcc gcc-c++ pcre pcre-devel openssl openssl-devel 
    sudo yum install zlib zlib-devel cmake ncurses ncurses-devel bison bison-devel
    如下的几个依赖在CentOS7中需要安装,CentOS6不需要
    sudo yum install perl perl-devel autoconf
5、安装boost
    (1)	切换到/usr/local目录，然后在这个目录下下载boost
    		MySQL5.7.26要求boost的版本是1.59，更高版本的不适用MySQL5.7.26
    (2) wget http://www.sourceforge.net/projects/boost/files/boost/1.59.0/boost_1_59_0.tar.gz
    (3) 解压并改名
        tar zxvf boost_1_59_0.tar.gz
        mv boost_1_59_0 boost
        在预编译安装MySQL时要加上-DWITH_BOOST=/usr/local/boost
6、添加mysql用户
		useradd -M -r -s /sbin/nologin mysql
7、下载MySQL
		wget https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.26.tar.gz
8、解压MySQL
		tar zxvf mysql-5.7.24.tar.gz
9、进到MySQL目录
		cd mysql-5.7.24
10、预编译
    #程序存放位置
    cmake -DCMAKE_INSTALL_PREFIX=/usr/local/mysql-5.7.26 \
    -DWITH_BOOST=/usr/local/boost \
    #socket文件存放位置
    -DMYSQL_UNIX_ADDR=/usr/local/mysql-5.7.26/tmp/mysql.sock \
     #数据存放位置
    -DMYSQL_DATADIR=/usr/local/mysql-5.7.26/data \
    #使用utf8mb4字符集
    -DDEFAULT_CHARSET=utf8 \
    #校验规则
    -DDEFAULT_COLLATION=utf8_general_ci \
    #使用其他额外的字符集
    -DWITH_EXTRA_CHARSETS=all \
    #支持的存储引擎
    -DWITH_MYISAM_STORAGE_ENGINE=1 \
    -DWITH_INNOBASE_STORAGE_ENGINE=1 \
    -DWITH_MEMORY_STORAGE_ENGINE=1 \
    -DWITH_READLINE=1 \
    -DWITH_INNODB_MEMCACHED=1 \
    -DWITH_DEBUG=OFF \
    -DWITH_ZLIB=bundled \
    -DENABLED_LOCAL_INFILE=1 \
    -DENABLED_PROFILING=ON \
    -DMYSQL_MAINTAINER_MODE=OFF \
    -DMYSQL_TCP_PORT=3306
---------------------------------------------------------------------------------------------
    cmake -DCMAKE_INSTALL_PREFIX=/usr/local/mysql-5.7.26 \
    -DWITH_BOOST=/usr/local/boost \
    -DMYSQL_UNIX_ADDR=/usr/local/mysql-5.7.26/tmp/mysql.sock \
    -DMYSQL_DATADIR=/usr/local/mysql-5.7.26/data \
    -DDEFAULT_CHARSET=utf8 \
    -DDEFAULT_COLLATION=utf8_general_ci \
    -DWITH_EXTRA_CHARSETS=all \
    -DWITH_MYISAM_STORAGE_ENGINE=1 \
    -DWITH_INNOBASE_STORAGE_ENGINE=1 \
    -DWITH_MEMORY_STORAGE_ENGINE=1 \
    -DWITH_READLINE=1 \
    -DWITH_INNODB_MEMCACHED=1 \
    -DWITH_DEBUG=OFF \
    -DWITH_ZLIB=bundled \
    -DENABLED_LOCAL_INFILE=1 \
    -DENABLED_PROFILING=ON \
    -DMYSQL_MAINTAINER_MODE=OFF \
    -DMYSQL_TCP_PORT=3306
11、编译&安装
		make && make install
12、创建数据目录
    mkdir -p /usr/local/mysql-5.7.24/{data,tmp,logs,pids}
13、创建mysqld.log 和 mysqld.pid文件
		touch /usr/local/mysql/{logs/mysqld.log,pids/mysqld.pid}
14、修改/etc/my.cnf文件
    [mysqld]
    character-set-server=utf8
    collation-server=utf8_general_ci
    basedir=/usr/local/mysql-5.7.26
    datadir=/usr/local/mysql5.7.26/data
    socket=/usr/local/mysql5.7.26/tmp/mysql.sock
    pid-file=/usr/local/mysql5.7.26/pids/mysqld.pid
    log-error=/usr/local/mysql5.7.26/logs/mysqld.log
    [client]
    # default-character-set=utf8
    socket=/usr/local/mysql5.7.26/tmp/mysql.sock
15、创建并修改mysql启动脚本
    cp /usr/local/mysql-5.7.26/support-files/mysql.server /etc/init.d/mysqld
    chmod a+x /etc/init.d/mysqld
    # 修改配置
		vim /etc/init.d/mysqld
				basedir=/usr/local/mysql-5.7.26
				datadir=/usr/local/mysql-5.7.26/data
16、授权
		chown -R mysql:mysql /usr/local/mysql-5.7.26
17、初始化数据库
		# -–initialize 表示默认生成一个安全的密码
		# -–initialize-insecure 表示不生成密码
		mysqld --initialize-insecure --user=mysql --basedir=/usr/local/mysql-5.7.26 --datadir=/usr/local/mysql-5.7.26/data
18、添加到环境变量
		vim /etc/profile
        export PATH=$PATH:/usr/local/mysql-5.7.26/bin
		source /etc/profile
19、启动MySQL
		/etc/init.d/mysqld start
20、连接mysql修改密码
    mysql -u root -p #第一次登陆不需要密码，回车即可
    set password for root@localhost = password('PASSWORD'); #修改密码
```

# 六十三、mysql二进制安装(5.7)

```shell
1、下载mysql二进制程序包
		https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.26-linux-glibc2.12-x86_64.tar.gz
2、下载mysql依赖库
    # MySQL依赖于libaio库.如果未在本地安装此库,则数据目录初始化和后续服务器启动步骤将失败.如有必要,请使用适当的包管理器进行安装.例如,在基于Yum的系统上
		yum install libaio
		#对于MySQL5.7.19及更高版本:对通用Linux构建添加了对非统一内存访问(NUMA)的支持,该构建现在依赖于libnuma库;如果您的系统上尚未安装库,请使用系统的软件包管理器来搜索并安装它
		yum install libnuma
3、创建mysql用户
		useradd -r -M -s /sbin/nologin mysql
4、解压二进制包
		tar zxvf mysql-5.7.26-linux-glibc2.12-x86_64.tar.gz
		# 移动到/usr/local目录下
		mv zxvf mysql-5.7.26-linux-glibc2.12-x86_64 /usr/local/mysql-5.7.26
5、创建mysql的数据库目录
		mkdir -R /usr/local/mysql-5.7.26/{data,tmp,logs,pids}
6、修改/etc/my.cnf配置文件
		vim /etc/my.cnf
        [mysqld]
        server_id=1
        log_bin=mysql-bin
        binlog_format=row
        relay_log_purge=0
        character-set-server=utf8
        collation-server=utf8_general_ci
        basedir=/usr/local/mysql-5.7.26
        datadir=/usr/local/mysql-5.7.26/data
        socket=/usr/local/mysql-5.7.26/tmp/mysql.sock
        pid-file=/usr/local/mysql-5.7.26/pids/mysqld.pid
        log-error=/usr/local/mysql-5.7.26/logs/mysqld.log
        [client]
        #character-set-server=utf8
        socket=/usr/local/mysql-5.7.26/tmp/mysql.sock
7、创建mysqld.log 和 mysqld.pid文件
		touch /usr/local/mysql/logs/mysqld.log
		touch /usr/local/mysql/pids/mysqld.pid

		chown mysql.mysql -R /usr/local/mysql/logs/
		chown mysql.mysql -R /usr/local/mysql/pids/
8、授权
		chown -R mysql:mysql /usr/local/mysql-5.7.26
9、创建mysql启动脚本
		# cd至support-files目录中
		cd /usr/local/mysql-5.7.26/support-files
		# 拷贝到/etc/init.d/mysqld
		cp ./support-files/mysql.server /etc/init.d/mysqld
		# 修改配置
		vim /etc/init.d/mysqld
				basedir=/usr/local/mysql-5.7.26
				datadir=/usr/local/mysql-5.7.26/data
		chmod +x /etc/init.d/mysqld
10、初始化mysql
		cd /usr/local/mysql-5.7.26/bin/
		./mysqld --initialize-insecure --user=mysql --basedir=/usr/local/mysql-5.7.26 --datadir=/usr/local/mysql-5.7.26/data
11、将mysql5.7添加环境变量
		vim /etc/profile
		export PATH=$PATH:/usr/local/mysql-5.7.26/bin
		source /etc/profile
		env # 查看环境变量
12、启动mysql5.7
		/etc/init.d/mysqld start
		# 查看服务
		netstat -tunlp | grep 3306
13、连接mysql修改密码
		mysql -h 127.0.0.1 -u root -p
		(1) update user set authentication_string=password('PASSWORD') where user='root';
		(2) alter user 'root'@'localhost' identified by 'PASSWORD';
		(3) set password for 'root'@'localhost'=password('PASSWORD');
		flush privileges; # 刷新权限
```

# 六十四、mysql之yum安装

```mysql
1. 首先进入本机的源文件目录
cd /usr/local/src

2. 使用wget下载官方yum源的rpm包：
wget https://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm

3. 安装rpm包：
rpm -ivh mysql57-community-release-el7-11.noarch.rpm

4. 再次使用yum来安装mysql-server:
yum install -y mysql-server
可以看到这次不再提示安装Mariadb了

5. 安装完成后，启动mysqld服务：
systemctl start mysqld

查看是否成功启动：
systemctl status mysqld
ps aux|grep mysqld

6. 设置mysqld服务开机自启动：
systemctl enable mysqld

7. 使用初始密码登录
由于MySQL从5.7开始不允许首次安装后，使用空密码进行登录，系统会随机生成一个密码以供管理员首次登录使用，这个密码记录在/var/log/mysqld.log文件中，使用下面的命令可以查看此密码：
cat /var/log/mysqld.log|grep 'A temporary password'

2017-11-12T13:35:37.013617Z 1 [Note] A temporary password is generated for root@localhost: bkv,dy,)o7Ss

最后一行冒号后面的部分bkv,dy,)o7Ss就是初始密码。 
使用此密码登录MySQL:

mysql -u root -p
8. 更改默认密码:
set password for 'root'@'localhost'=password('PASSWORD');
```

# 六十四、mysql恢复root账号

```shell
# 解决误操作删除root账号时,恢复
(1)
		mysqld_safe --skip-grant-tables --skip-networking & # &表示后台运行
		# 创建一个用户 
		insert into mysql.user values ('localhost','root',PASSWORD('123'),
    'Y',
    'Y',
    'Y',
    'Y',
    'Y',
    'Y',
    'Y',
    'Y',
    'Y',
    'Y',
    'Y',
    'Y',
    'Y',
    'Y',
    'Y',
    'Y',
    'Y',
    'Y',
    'Y',
    'Y',
    'Y',
    'Y',
    'Y',
    'Y',
    'Y',
    'Y',
    'Y',
    'Y',
    'Y',
    '',
    '',
    '',
    '',0,0,0,0,'mysql_native_password','','N');
(2)
		# 创建root用户并设置授权权限 - 加上with grant option
		grant all on *.* to root@'localhost' identified by '123' with grant option;
```

# 六十五、mysql体系结构管理

```shell
# 客户端与服务器模型
mysql是一个典型的C/S服务结构
		1、mysql自带的客户端程序（/application/mysql/bin）
				mysql
        mysqladmin
        mysqldump
		2、mysqld一个二进制程序，后台的守护进程
    		单进程
        多线程
---------------------------------------------------------------------------------------------
# 连接mysql的方式
1、TCP/IP
		# 凡是指定IP地址的都是通过TCP/IP
		例如:
				mysql -h 127.0.0.1 -u root -p
				mysql -h 47.100.11.65 -u root -p
2、socket
		# 不指定或指定为localhost主机都是通过socket连接的
		例如:
				mysql -h localhost -u root -p
				mysql -u root -p
#注意:TCP/IP建立连接结果三次握手和断开四次挥手,而socket直接连接,所以socket的性能要比TCP/IP高
---------------------------------------------------------------------------------------------
# mysql服务器构成
什么是实例
    1.MySQL的后台进程+线程+预分配的内存结构。
    2.MySQL在启动的过程中会启动后台守护进程，并生成工作线程，预分配内存结构供MySQL处理数据使用
mysql服务器程序构成
    程序程序-程序程序-程序程序
            连接层
            sql层
    存储引擎层(磁盘,内存,网络)
    # 连接层
    1、提供两种连接方式
        TCP/IP
        socket
    2、检验用户的合法性
    3、建立一个与SQL层交互的线程
    # sql层
    1、接收连接层传来的SQL语句
    2、检查语法
    3、检查语义(检查它属于哪种SQL语句:DDL,DML,DCL,DQL)
    4、解析器:解析SQL语句,生成多种执行计划
    5、优化器:接收解析器传来的多种执行计划,选择最优化的一条方式去执行
    6、执行器:执行优化器传来的最优方式的SQL语句
        建立一个与存储引擎层交互的线程
        接收存储引擎层,返回的结构化成表的数据
    7、写缓存
    8、记录日志
    #存储引擎层
    1、接收SQL层传来的SQL语句
    2、与磁盘交互,找到数据并结构化成表的形式,返回给SQL层
    3、建立一个与SQL层交互的线程
---------------------------------------------------------------------------------------------
# mysql结构
1.物理结构
		最底层的数据文件
2.逻辑结构
    数据库管理员操作的 对象
        库
        表=元数据+真实的数据行
        元数据=列(字段)+其他的属性(表的大小,行数...)
        列=列名字+约束(数据类型,是否为空,主键,默认值...)
3、mysql段区页
    段:一个段=一张表,一个段是由多个区构成的
    区:多个页构成的的,64k为一个区(4个页为一个区)
    页:mysql最小单位,一个页为16k
```

# 六十六、mysql创建多实例

```shell
多实例:
		多套后台进程+线程+内存结构
        多个配置文件
        多个端口
        多个socket文件
        多个日志文件
        多个server_id
        多套数据
---------------------------------------------------------------------------------------------
1、创建数据目录
		mkdir -p /data/330{7..9}
2、创建匹配文件
		touch /data/330{7..9}/my.cnf
3、编辑配置文件
		# 3307
		[mysqld]
		basedir=/usr/local/mysql-5.7.26
		datadir=/data/3307/data
		port=3307
		server-id=7
		socket=/data/3307/mysql.sock
    log_error=/data/3307/data/mysql.err
    pid-file=/data/3307/data/mysql.pid
    [client]
    socket=/data/3307/mysql.sock
    # 3308
    [mysqld]
		basedir=/usr/local/mysql-5.7.26
		datadir=/data/3308/data
		port=3308
		server-id=8
		socket=/data/3308/mysql.sock
    log_error=/data/3308/data/mysql.err
    pid-file=/data/3308/data/mysql.pid
    [client]
    socket=/data/3308/mysql.sock
    # 3309
    [mysqld]
		basedir=/usr/local/mysql-5.7.26
		datadir=/data/3309/data
		port=3309
		server-id=9
		socket=/data/3309/mysql.sock
    log_error=/data/3309/data/mysql.err
    pid-file=/data/3309/data/mysql.pid
    [client]
    socket=/data/3309/mysql.sock
4、授权数据目录
		chown -R mysql.mysql /data/330*
5、初始化多实例数据
		# -–initialize 表示默认生成一个安全的密码
		# -–initialize-insecure 表示不生成密码
		/usr/local/mysql-5.7.26/bin/mysqld --initialize-insecure --user=mysql --basedir=/usr/local/mysql-5.7.26 --datadir=/data/3307/data
		/usr/local/mysql-5.7.26/bin/mysqld --initialize-insecure --user=mysql --basedir=/usr/local/mysql-5.7.26 --datadir=/data/3308/data
		/usr/local/mysql-5.7.26/bin/mysqld --initialize-insecure --user=mysql --basedir=/usr/local/mysql-5.7.26 --datadir=/data/3309/data
		# 默认会生成密码记录下来
6、启动多实例
		mysqld_safe --defaults-file=/data/3307/my.cnf &
		mysqld_safe --defaults-file=/data/3308/my.cnf &
		mysqld_safe --defaults-file=/data/3309/my.cnf &
7、查看启动多实例
		netstat -lntup|grep 330
8、修改密码
		mysqladmin -uroot -p -S /data/3307/mysql.sock  password 'PASSWORD'
9、登陆mysql
		mysql -S /data/3307/mysql.sock -uroot -p'PASSWORD'
10、设置快捷连接
    vim /usr/local/mysql-5.7.26/bin/mysql3307
    		mysql -uroot -p'PASSWORD' -S /data/3307/mysql.sock
    vim /usr/local/mysql-5.7.26/bin/mysql3308
    		mysql -uroot -p'PASSWORD' -S /data/3308/mysql.sock
    vim /usr/local/mysql-5.7.26/bin/mysql3309
    		mysql -uroot -p'PASSWORD' -S /data/3309/mysql.sock
		chmod +x /usr/local/mysql-5.7.26/bin/mysql330* # 添加可执行权限
		# 输入mysql330*即可
        mysql3307
        mysql3308
        mysql3309
11、多实例关机
		mysqladmin -uroot -p'PASSWORD' -S /data/3307/mysql.sock shutdown
		mysqladmin -uroot -p'PASSWORD' -S /data/3308/mysql.sock shutdown
		mysqladmin -uroot -p'PASSWORD' -S /data/3309/mysql.sock shutdown
```

# 六十七、mysql之sql的种类

```mysql
1.什么是SQL
		结构化的查询语句
2.sql的种类
# DDL(Data Definition Language):数据定义语言
		库对象:库名字、库属性
		开发规范库名小写
		(1) create
				创建库:
						create database|schema
						# 规范的建库语句
						create database if not exists db01 character set=utf8 collate=utf8_general_ci;
								if not exists:表示数据库不存在时创建,否则不做操作
								character set:指定字符集
										show charset; # 查看所有字符集
								collate:校验规则
										ci:大小写不敏感
										cs|bin:大小敏感
										show collation; # 查看所有校验规则
				创建表:
						create table
						# 例子
						create table t01(id int primary key auto_increment)engine=innodb;
		(2) alter
				修改定义的库
						alter database
						# 例子
						alter database db01 charset gbk; # 修改字符编码
				修改定义的表
						alter table
						# 例子
						alter table t01 add name char(16);
		(3) drop 
				删除定义的库
						drop database
						# 例子
						drop database db01;
				删除定义的表
						drop table
						# 例子
						drop table t01;
# DCL(Data Control Language):数据控制语言,针对权限进行控制
		(1) grant # 授权
				# 例子
            授权root@10.0.0.1用户所有权限(非超级管理员)
            grant all on *.* to root@'10.0.0.1' identified by 'PASSWORD';
            授权超级管理员
            grant all on *.* to root@'10.0.0.1' identified by 'PASSWORD' with grant option;
            其他参数(扩展)
            max_queries_per_hour：一个用户每小时可发出的查询数量
            max_updates_per_hour：一个用户每小时可发出的更新数量
            max_connetions_per_hour：一个用户每小时可连接到服务器的次数
            max_user_connetions：允许同时连接数量
        # 语法
        		grant 权限... on 库.表 用户[@'host'] [identified by 'PASSWORD']
				# 限制级别
						单数据:
								on db01.*
						单数据库单表:
								on db01.t01
						单数据库单表单字段:
								grant select(name) on db01.t01
		(2) revoke # 收回权限
				# 例子
						收回select权限
						revoke select on *.* root@'10.0.0.1';
						查看权限
						show grant for root@'10.0.0.1';
						语法
						revoke 权限... on 用户[@'host'];
# DML(Data Manipulation Language):数据操纵语言
		(1) insert # 新增记录
				# 例子
						常规用法,插入数据
						insert into t01 values(1,'allen',18,'male');
						规范用法,插入数据
						insert into t01(name,age,gender) values('kevin',18,'male');
						插入多条数据
						insert into t01(name,age,gender) values
						('collins',18,'female'),
						('lily',18,'female');
		(2) update # 更新记录
				# 例子
						不规范
						update t01 set name='mike'
						规范uodate修改
						update t01 set name='mike' where id=10;
						如果要修改全部
						update t01 set name='mike' where 1=1;
		(3) delete # 删除流
				# 例子
						不规范
						delete from t01;
						规范删除(危险)
						delete from t01 where id=1;
						DDL删除表
						truncate table t01;
				# 注意:不推荐直接删除数据
						(1) 使用update作为删除,添加一个状态字段
						(2) 使用触发器 trigger
# DQL(Data Query Language):数据查询语言
		(1) select
				# 完整语法
				select distinct field... from TABLE where CONDITION group by field having CONDITION order by field [asc|desc] limit num[,num|offset num];
				# 连表查询 
            join:
                natural join:自连接
                inner join: 内连接
                left join:左连接
                right join:右连接
            union:
                union:去重合并
                union all:不去重合并
		MySQL 提供了一个 EXPLAIN 命令, 它可以对 SELECT 语句进行分析, 并输出 SELECT 执行的详细信息, 以供开发人员针对性优化
		# 例子
				explain select name from t01 where id=1;
				explain等级(null,system,const,eq_ref,ref,range,index,all) # 查询速度从高到低
            all : 即全表扫描
            index : 按索引次序扫描，先读索引，再读实际的行，结果还是全表扫描，主要优点是避免了排序。因为索引是排好的。
            range:以范围的形式扫描。
            		explain select * from a where a_id > 1\G
            ref:非唯一索引访问(只有普通索引)
                create table a(a_id int not null, key(a_id));
                insert into a values(1),(2),(3),(4),(5),(6),(7),(8),(9),(10);
                explain select * from a where a_id=1\G
            eq_ref:使用唯一索引查找(主键或唯一索引)
            const:常量查询在整个查询过程中这个表最多只会有一条匹配的行，比如主键 id=1 就肯定只有一行，只需读取一次表数据便能取得所需的结果，且表数据在分解执行计划时读取。
            当结果不是一条时，就会变成index或range等其他类型
            system:系统查询
            null:优化过程中就已经得到结果，不在访问表或索引
```

# 六十八、mysql之主从复制(单机多实例)

```shell
# 环境准备
[mysql3006]
		port=3306
[mysql3007]
		port=3307
[mysql3008]
		port=3308
[mysql3009]
		port=3309
# 主库操作
		[mysql3006]
        1、修改配置文件
            vim /etc/my.cnf
                [mysqld]
                #主库server_id为1,server_id不能与从库重复
                server_id=1
                #开启binlog日志
                log_bin=mysql-bin
        2、重启主库mysql
            systemctl restart mysqld
        3、查看Position
            show master status;# 记录 Position
        3、创建主从复制用户
            grant replication slave on *.* to rep@'%' identified by 'MYsql@891213';
            flush privileges;
# 从库操作
		[mysql3007]
        修改配置文件
        vim /etc/my.cnf
            [mysqld]
            #主库server_id为1,从库server_id不能与主库重复
            server_id=7
		[mysql3008]
				 修改配置文件
        vim /etc/my.cnf
            [mysqld]
            #主库server_id为1,从库server_id不能与主库重复
            server_id=8
		[mysql3009]
				 修改配置文件
        vim /etc/my.cnf
            [mysqld]
            #主库server_id为1,从库server_id不能与主库重复
            server_id=9
    1、设置从库与主库进行通信
        # 格式
        CHANGE MASTER TO MASTER_HOST='master_host_name',
                         MASTER_USER='replication_user_name',
                         MASTER_PASSWORD='replication_password',
                         MASTER_LOG_FILE='recorded_log_file_name',
                         MASTER_LOG_POS=recorded_log_position;
        # 执行change master(创建IO,SQL线程)
        CHANGE MASTER TO MASTER_HOST='127.0.0.1', 
                         MASTER_USER='rep',
                         MASTER_PASSWORD='MYsql@891213',
                         MASTER_LOG_FILE='mysql-bin.000001',
                         MASTER_LOG_POS=0;
    2、启动主从
        start slave;
        # stop slave; 关闭主从
    3、查看从库状态
        show slave status;
        # 显示如下表示主从启动成功
						Slave_IO_Running: Yes
            Slave_SQL_Running: Yes
#  注意开启主从复制前,对主库做全备份,保证主从数据一致性
		# 主库
		mysqldump -A -uroot -p > /tmp/full.sql
		# 从库
		source /tmp/full.sql
```

# 六十九、mysql之GTID主从复制(事务复制)

```mysql
https://www.hi-linux.com/posts/47176.html
# GTID Replication
# GTID
gtid_mode=ON
enforce_gtid_consistency=ON
log-slave-updates=ON
relay_log_purge=0
```

# 七十、mysql在线变更复制类型

```mysql
(1) 在线将基于日志的复制变更为基于事务的复制
    # 先决条件
    1.集群中所有服务器的版本均高于5.7.6
    2.集群中所有服务器gtid_mode都设置为off
        1.设置参数(主服务器和从服务器上分别执行)
            set @@global.enforce_gtid_consistency=warn;      
            # 强制设置gtid一致性，值为:warn，设置完后建议用tail -f命令查看一下mysql-error.log是否有异常信息
            set @@global.enforce_gtid_consistency=on;
            # 强制设置gtid一致性，值为:on
            set @@global.gtid_mode=off_permissive;
            # 设置gtid_mode为准备关闭状态
            set @@global.gtid_mode=on_permissive;
            # 设置gtid_mode为准备开启状态
        2.在从服务器上查看状态
            show status like 'ongoing_anonymous_transaction_count';
            # 查看基于日志的复制的事物数量,为0或者为空表示正常
            # 这一步是为了保证基于日志复制的数据的一致性,防止有事物在主服务器上执行完成
            # 在从服务器上没有被执行,导致数据丢失
            set @@global.gtid_mode=on;
            # 设置gtid_mode为开启状态
            stop slave; # 在从服务器上停止slave
            change master to master_auto_position=1;# 改变复制方式
            start slave;
        3.持久配置
            vim /etc/my.cnf
            # 修改至配置文件中保证下一次启动时基于事务的复制<不然下次启动mysql你就会发现主从挂了>
                [mysqld]
                enforce_gtid_consistency=on
                gtid_mode=on
(2) 在线将基于事务的复制变更为基于日志的复制
		# 先决条件
		1.集群中所有的服务器版本均高于5.7.6
		2.集群中所有的服务器gtid_mode都设置为on(使用 show variables like 'gtid_mode' 命令查看)
				1.停止事物复制,设置日志复制的日志文件和日志文件节点
						stop slave;
						change master to master_auto_position=0,master_log_file='file',master_log_pos=;
				2.在服务器上查看状态
						set @@global.gtid_mode=on_permissive; # 设置gtid_mode为准备开启状态
       			set @@global.gtid_mode=off_permissive; # 设置gtid_mode为准备关闭状态   
   					查看gtid_ownend是否为空字符串(在所有服务器上均要查看)
       			sellect @@global.gtid_owned;
       			set @@global.gtid_mode=off; # 关闭
				3.持久配置（重要操作）修改my.cnf中(所有的mysql服务器节点)
						[mysqld]
       			enforce_gtid_consistency=off
   					gtid_mode=off
```

# 七十一、mysql之多源复制

```mysql
https://www.hi-linux.com/posts/61083.html
```

# 七十二、mysql之并行复制

```mysql
https://www.hi-linux.com/posts/9892.html
```

# 七十、mysql备份和恢复

```mysql
mysqldump
语法:
		 mysqldump [options] [db_name [tbl_name ...]]
1.全备份
		a、mysqldump -uroot -proot --all-databases >/tmp/all.sql
		b、mysqldump -A -uroot -p123 > /tmp/full.sql
2.指定数据库备份
		a、mysqldump -uroot -proot --databases db1 db2 >/tmp/user.sql
		b、
3、指定表备份
		a、mysqldump -uroot -proot --databases db1 --tables a1 a2  >/tmp/db1.sql
		b、
4、条件备份,导出db1表a1中id=1的数据
```

# 七十一、mysql之mha

```mysql
# 软件介绍
MHA能够在较短的时间内实现自动故障检测和故障转移，通常在10-30秒以内;在复制框架中，MHA能够很好地解决复制过程中的数据一致性问题，由于不需要在现有的replication中添加额外的服务器，仅需要一个manager节点，而一个Manager能管理多套复制，所以能大大地节约服务器的数量;另外，安装简单，无性能损耗，以及不需要修改现有的复制部署也是它的优势之处。

MHA还提供在线主库切换的功能，能够安全地切换当前运行的主库到一个新的主库中(通过将从库提升为主库),大概0.5-2秒内即可完成。

MHA由两部分组成：MHA Manager（管理节点）和MHA Node（数据节点）。MHA Manager可以独立部署在一台独立的机器上管理多个Master-Slave集群，也可以部署在一台Slave上。当Master出现故障时，它可以自动将最新数据的Slave提升为新的Master,然后将所有其他的Slave重新指向新的Master。整个故障转移过程对应用程序是完全透明的。
# 工作流程
(1) 把宕机的master二进制日志保存下来
(2) 找到binlog位置点最近的slave(可以固定指定某一台salve)
(3) 在binlog位置点最近的salve上用的relay.log(和master差异日志)修复其他slave
(4) 将宕机的master上保存下来的binlog二进制日志恢复到与其位置点最近的slave上
# 为什么不先把宕机的master的binlog日志恢复到与其位置点最近的slave上呢,因为内存命中率
# 例如:位置点最近slave数据库量是:70%,其他slave的数据量是60%,相差10%,如果先从binlog日志恢复位置点最近slave,此时位置点最近slave数据量为100%,与其他slave数据量相差40%,
(5) 将含有最新位置点binlog所在的slave提升为master
(6) 将其他slave重新指向新提升的master,并开启主从复制
# mha工具
MHA软件由两部分组成,Manager工具包和Node工具包
1.Manager工具包主要包括:
		masterha_check_ssh              #检查MHA的ssh-key
    masterha_check_repl             #检查主从复制情况
    masterha_manger                 #启动MHA
    masterha_check_status           #检测MHA的运行状态
    masterha_master_monitor         #检测master是否宕机
    masterha_master_switch          #手动故障转移
    masterha_conf_host              #手动添加server信息
    masterha_secondary_check        #建立TCP连接从远程服务器
    masterha_stop                   #停止MHA
2.Node工具包主要包括:
    save_binary_logs                #保存宕机的master的binlog
    apply_diff_relay_logs           #识别relay log的差异
    filter_mysqlbinlog              #防止回滚事件
    purge_relay_logs                #清除中继日志
# MHA优点总结
(1) Masterfailover and slave promotion can be done very quickly
		自动故障转移快
(2) Mastercrash does not result in data inconsistency
		主库崩溃不存在数据一致性问题
(3) Noneed to modify current MySQL settings (MHA works with regular MySQL)
		不需要对当前mysql环境做重大修改
(4) Noneed to increase lots of servers
		不需要添加额外的服务器(仅一台manager就可管理上百个replication)
(5) Noperformance penalty
    性能优秀，可工作在半同步复制和异步复制，当监控mysql状态时，仅需要每隔N秒向master发送ping包(默认3秒)，所以对性能无影响。你可以理解为MHA的性能和简单的主从复制框架性能一样。
(6) Works with any storage engine
		只要replication支持的存储引擎，MHA都支持，不会局限于innodb
```

# 七十二、mysql之高可用(搭建mha+vip)

```shell
# MySQL环境准备
[mysql_node01]
		系统:CentOS Linux release 7.6.1810 (Core) # cat /etc/redhat-release
		内核版本:3.10.0-957.el7.x86_64 # uname -r
		IP:192.168.8.21 # hostname -I
[mysql_node02]
		系统:CentOS Linux release 7.6.1810 (Core) # cat /etc/redhat-release
		内核版本:3.10.0-957.el7.x86_64 # uname -r
		IP:192.168.8.21 # hostname -I
[mysql_node03]
		系统:CentOS Linux release 7.6.1810 (Core) # cat /etc/redhat-release
		内核版本:3.10.0-957.el7.x86_64 # uname -r
		IP:192.168.8.21 # hostname -I
# 安装MySQL[每台服务器上安装mysql]
1、下载二进制包[本次使用mysql-5.7.26]
		https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.26-linux-glibc2.12-x86_64.tar.gz
2、下载mysql依赖库
		yum -y install libaio
		yum -y install libnuma
3、解压二进制包
		tar zxvf mysql-5.7.26-linux-glibc2.12-x86_64.tar.gz
		# 移动到/usr/local目录下
		mv zxvf mysql-5.7.26-linux-glibc2.12-x86_64 /usr/local/mysql-5.7.26
4、创建mysql用户
		useradd -r -M -s /sbin/nologin mysql
5、创建mysql的数据库目录
		mkdir -R /usr/local/mysql-5.7.26/{data,tmp,logs,pids}
6、修改/etc/my.cnf配置文件
		vim /etc/my.cnf
        [mysqld]
        server_id=1 # 保证每个服务其上server_id不同
        log_bin=mysql-bin
        binlog_format=row
        relay_log_purge=0
        character-set-server=utf8
        collation-server=utf8_general_ci
        basedir=/usr/local/mysql-5.7.26
        datadir=/usr/local/mysql-5.7.26/data
        socket=/usr/local/mysql-5.7.26/tmp/mysql.sock
        pid-file=/usr/local/mysql-5.7.26/pids/mysqld.pid
        log-error=/usr/local/mysql-5.7.26/logs/mysqld.log
        [client]
        socket=/usr/local/mysql-5.7.26/tmp/mysql.sock
7、创建mysqld.log 和 mysqld.pid文件
		touch /usr/local/mysql/logs/mysqld.log /usr/local/mysql/pids/mysqld.pid
8、授权
		chown -R mysql:mysql /usr/local/mysql-5.7.26
9、创建mysql启动脚本
		# 将mysql.server拷贝到/etc/init.d/mysqld
		cp /usr/local/mysql-5.7.26/support-files/mysql.server /etc/init.d/mysqld
		# 修改启动配置
		vim /etc/init.d/mysqld
				basedir=/usr/local/mysql-5.7.26
				datadir=/usr/local/mysql-5.7.26/data
		chmod +x /etc/init.d/mysqld
10、初始化mysql
		/usr/local/mysql-5.7.26/bin/mysqld --initialize-insecure --user=mysql --basedir=/usr/local/mysql-5.7.26 --datadir=/usr/local/mysql-5.7.26/data
11、将mysql5.7添加环境变量
		vim /etc/profile
				export PATH=$PATH:/usr/local/mysql-5.7.26/bin
		source /etc/profile
		env # 查看环境变量
12、启动mysql5.7
		/etc/init.d/mysqld start
		netstat -tunlp | grep 3306 # 查看服务
13、连接mysql修改密码
		mysql -h 127.0.0.1 -u root -p
		(1) update user set authentication_string=password('PASSWORD') where user='root';
		(2) alter user 'root'@'localhost' identified by 'PASSWORD';
		(3) set password for 'root'@'localhost'=password('PASSWORD');
		flush privileges; # 刷新权限
# MySQL启动主从复制
1、修改配置
    [mysql_node01]
        # 添加并修改配置文件
        [mysqld]
            server_id=1 # 保证每个服务其上server_id不同
            log_bin=mysql-bin # 开启binlog日志
            binlog_format=row # 行级模式
            relay_log_purge=0 # 禁用自动删除relay log永久生效
    [mysql_node02]
        [mysqld]
            server_id=2 # 保证每个服务其上server_id不同
            log_bin=mysql-bin # 开启binlog日志
            binlog_format=row # 行级模式
            relay_log_purge=0 # 禁用自动删除relay log永久生效
    [mysql_node03]
        [mysqld]
            server_id=3 # 保证每个服务其上server_id不同
            log_bin=mysql-bin # 开启binlog日志
            binlog_format=row # 行级模式
            relay_log_purge=0 # 禁用自动删除relay log永久生效
2、重启MYSQL数据库并创建主从复制用户
		# 1、重启
		/etc/init.d/mysqld restart
		# 2、创建主从复制用户
		grant replication slave on *.* to rep@'%' identified by 'PASSWORD';
		flush privileges;
        # 注意:每一个主从库都需要创建
        # 否则在启动mhga提示:用户repl不存在或没有复制从属权限!其他从属服务器无法从此主机启动复制
        # User repl does not exist or does not have REPLICATION SLAVE privilege! Other slaves can not start replication from this host
		# 3、
				主库操作
						[mysql_node01]
								show master status; # 查看主库信息记录下File和Position
				从库操作
						1、设置从库与主库进行通信
                [mysql_node02]
                    CHANGE MASTER TO MASTER_HOST='192.168.8.21', MASTER_USER='rep', MASTER_PASSWORD='PASSWORD', MASTER_LOG_FILE='mysql-bin.000001', MASTER_LOG_POS=120;
                [mysql_node03]
                    CHANGE MASTER TO MASTER_HOST='192.168.8.21', MASTER_USER='rep', MASTER_PASSWORD='PASSWORD', MASTER_LOG_FILE='mysql-bin.000001', MASTER_LOG_POS=120;
						2、启动主从
								start slave;
								# stop slave; 关闭主从
						3、查看从库状态
								show slave status;
								# 显示如下表示主从启动成功
                    Slave_IO_Running: Yes
                    Slave_SQL_Running: Yes
						4、禁用自动删除relay log 永久生效
								set global relay_log_purge = 0; # 执sql了语句
# 部署MHA
1、环境准备
		[mysql_node01]
				yum -y install perl-DBD-MySQL
		[mysql_node02]
				yum -y install perl-DBD-MySQL
		[mysql_node03]
				yum -y install perl-DBD-MySQL
				# 下载阿里云epel源
				wget -O /etc/yum.repos.d/epel.repo https://mirrors.aliyun.com/repo/epel-7.repo
				yum install -y perl-Config-Tiny epel-release perl-Log-Dispatch perl-Parallel-ForkManager perl-Time-HiRes
2、安装mha
		# 下载rmp包
		mha4mysql-node-0.57-0.el7.noarch.rpm # 主库从库都需要安装
		mha4mysql-manager-0.57-0.el7.noarch.rpm	
    # 安装
    [mysql_node01]
    		rpm -ivh mha4mysql-node-0.57-0.el7.noarch.rpm
    [mysql_node02]
    		rpm -ivh mha4mysql-node-0.57-0.el7.noarch.rpm
    [mysql_node03]
    		rpm -ivh mha4mysql-node-0.57-0.el7.noarch.rpm
3、添加mha管理账号
		# 登陆主库数据库创建账号(从库自动复制)
				grant all privileges on *.* to mha@'%' identified by 'PASSWORD';
		# 检查用户是否创建成功
				select user,host from mysql.user;
4、创建软连接
		[mysql_node01]
				ln -s /usr/local/mysql-5.7.26/bin/mysqlbinlog /usr/bin
				ln -s /usr/local/mysql-5.7.26/bin/mysql /usr/bin
		[mysql_node02]
				ln -s /usr/local/mysql-5.7.26/bin/mysqlbinlog /usr/bin
				ln -s /usr/local/mysql-5.7.26/bin/mysql /usr/bin
		[mysql_node03]
				ln -s /usr/local/mysql-5.7.26/bin/mysqlbinlog /usr/bin
				ln -s /usr/local/mysql-5.7.26/bin/mysql /usr/bin
5、部署管理节点
		# 安装manager包
		[mysql_node03]
				rpm -ivh mha4mysql-manager-0.57-0.el7.noarch.rpm # 必须下载之前的依赖
		# 创建工作目录
				mkdir -p /etc/mha/app1
		# 创建配置文件
				vim /etc/mha/app1/app1.cnf
						[server default]
						#设置manager的日志
            manager_log=/etc/mha/app1/manager.log
            #设置manager的工作目录
            manager_workdir=/etc/mha/app1
            #设置master 保存binlog的位置,配置mysql时binlog目录
            master_binlog_dir=/usr/local/mysql-5.7.26/data
            # 设置监控用户
            user=mha
            # 设置监控用户密码
            password='PASSWORD'
            # 设置监控主库，发送ping包的时间间隔，尝试三次没有回应的时候自动进行failover
            ping_interval=2
            # 主从复制用户密码
            repl_password=MYsql@891213
            # 主从复制用户账号
            repl_user=rep
            # 设置ssh的登录用户名
            ssh_user=root
            
						[server1]
            hostname=192.168.8.21 # ip
            port=3306 # port

            [server2]
            hostname=192.168.8.22
            port=3306

            [server3]
            hostname=192.168.8.23
            port=3306
6、配置信任ssh(每台服务器都需要设置)
		[mysql_node01]
				ssh-keygen -t dsa -P '' -f ~/.ssh/id_dsa >/dev/null 2>&1
            ssh-copy-id -i /root/.ssh/id_dsa.pub root@192.168.8.21
            ssh-copy-id -i /root/.ssh/id_dsa.pub root@192.168.8.22
            ssh-copy-id -i /root/.ssh/id_dsa.pub root@192.168.8.23
		[mysql_node02]
				ssh-keygen -t dsa -P '' -f ~/.ssh/id_dsa >/dev/null 2>&1
            ssh-copy-id -i /root/.ssh/id_dsa.pub root@192.168.8.21
            ssh-copy-id -i /root/.ssh/id_dsa.pub root@192.168.8.22
            ssh-copy-id -i /root/.ssh/id_dsa.pub root@192.168.8.23
		[mysql_node03]
				ssh-keygen -t dsa -P '' -f ~/.ssh/id_dsa >/dev/null 2>&1
            ssh-copy-id -i /root/.ssh/id_dsa.pub root@192.168.8.21
            ssh-copy-id -i /root/.ssh/id_dsa.pub root@192.168.8.22
            ssh-copy-id -i /root/.ssh/id_dsa.pub root@192.168.8.23
7、启动测试
		[测试ssh]
        masterha_check_ssh --conf=/etc/mha/app1/app1.cnf
        # 显示如下表示成功
        All SSH connection tests passed successfully.
    [测试主从复制]
    		masterha_check_repl --conf=/etc/mha/app1/app1.cnf
    		# 显示如下表示成功(可以出现主从用户不存在或没有主从复制权限,需要每个创建同一个主从用户,请看上面)
    		MySQL Replication Health is OK.
8、启动MHA
		 nohup masterha_manager --conf=/etc/mha/app1/app1.cnf --remove_dead_master_conf --ignore_last_failover < /dev/null > /etc/mha/app1/manager.log 2>&1 &
9、检查MHA Manager的状态
		masterha_check_status --conf=/etc/mha/app1/app1.cnf
		# 如果正常,会显示"PING_OK",否则会显示"NOT_RUNNING",这代表MHA监控没有开启
10、测试切换master
		关闭当前主库[mysql_node01]
				/etc/init.d/mysqld stop
		进入从库[mysql_node02]
				show slave status;
				# 显示为空,说明已经被提升为主库
		登陆从库[mysql_node03]查看
				Master_Host: 192.168.8.22
				Master_User: rep
       	Master_Port: 3306
        Connect_Retry: 60
        # 此时主库是[mysql_node02]
11、恢复宕机的数据库
		a、查看mha管理日志中显示的CHANGE MASTER语句
				CHANGE MASTER TO MASTER_HOST='192.168.8.22', MASTER_PORT=3306, MASTER_LOG_FILE='mysql-bin.000002', MASTER_LOG_POS=832, MASTER_USER='rep', MASTER_PASSWORD='xxx';
		b、在宕机的数据库中执行 CHANGE MASTER 
CHANGE MASTER TO MASTER_HOST='192.168.8.22', MASTER_PORT=3306, MASTER_LOG_FILE='mysql-bin.000002', MASTER_LOG_POS=832, MASTER_USER='rep', MASTER_PASSWORD='MYsql@891213';
		c、启动主从复制
				start slave;
				# 查看主从
				show slave status;
	  d、修改mha管理配置(数据库宕机时,会从配置文件中清除)
	  		# 添加之前宕机的数据库
				[server1]
        hostname=192.168.8.21
        port=3306
    e、启动mha
        nohup masterha_manager --conf=/etc/mha/app1/app1.cnf --remove_dead_master_conf --ignore_last_failover < /dev/null > /etc/mha/app1/manager.log 2>&1 &
		f、查看mha启动状态
        masterha_check_status --conf=/etc/mha/app1/app1.cnf
# vip(Virtual IP ADDRESS)
		1、编辑配置文件
				vim /etc/mha/app1/app1.cnf
						master_ip_failover_script=/etc/mha/app1/master_ip_failover
		2、编辑脚本(脚本如下)
				vim etc/mha/app1/master_ip_failover
						my $vip = '192.168.8.100/24';
            my $key = '0';
            my $ssh_start_vip = "/sbin/ifconfig eth0:$key $vip";
            my $ssh_stop_vip = "/sbin/ifconfig eth0:$key down";
        # 添加执行权限
        		chmod +x /etc/mha/app1/master_ip_failover
		3、绑定vip
				# 给当前主库绑定vip
				ifconfig eth0:0 192.168.8.100/24
		4、重启mha
				masterha_stop --conf=/etc/mha/app1.cnf
				nohup masterha_manager --conf=/etc/mha/app1/app1.cnf --remove_dead_master_conf --ignore_last_failover < /dev/null > /var/log/mha/app1/manager.log 2>&1 &
		5、测试ip漂移
				# 关闭当前主库[mysql_node02]
				/etc/init.d/mysqld stop
				# 查看从库ifconfig[mysql_node01]
				show slave status\G # 显示为空
				# 进入从库[mysql_node03]
				show slave status\G
				Master_Host:192.168.8.21[mysql_node0] # 此时主库为[mysql_node01]
				# 查看[mysql_node01]vip信息
				ip a |grep eth0 # vip已经漂移过来了
				# 在查看[mysql_node02]vip信息
				ip a |grep eth0 # 发现vip已经没有了
```

# 七十三、Mysql之vip脚本

```perl
#!/usr/bin/env perl

use strict;
use warnings FATAL => 'all';

use Getopt::Long;

my (
    $command,          $ssh_user,        $orig_master_host, $orig_master_ip,
    $orig_master_port, $new_master_host, $new_master_ip,    $new_master_port
);

my $vip = '192.168.8.100/24';
my $key = '0';
my $ssh_start_vip = "/sbin/ifconfig eth0:$key $vip";
my $ssh_stop_vip = "/sbin/ifconfig eth0:$key down";

GetOptions(
    'command=s'          => \$command,
    'ssh_user=s'         => \$ssh_user,
    'orig_master_host=s' => \$orig_master_host,
    'orig_master_ip=s'   => \$orig_master_ip,
    'orig_master_port=i' => \$orig_master_port,
    'new_master_host=s'  => \$new_master_host,
    'new_master_ip=s'    => \$new_master_ip,
    'new_master_port=i'  => \$new_master_port,
);

exit &main();

sub main {

    print "\n\nIN SCRIPT TEST====$ssh_stop_vip==$ssh_start_vip===\n\n";

            &stop_vip();
            $exit_code = 0;
        };
        if ($@) {
            warn "Got Error: $@\n";
            exit $exit_code;
        }
        exit $exit_code;
    }
    elsif ( $command eq "start" ) {

        my $exit_code = 10;
        eval {
            print "Enabling the VIP - $vip on the new master - $new_master_host \n";
            &start_vip();
            $exit_code = 0;
        };
        if ($@) {
            warn $@;
            exit $exit_code;
        }
        exit $exit_code;
    }
    elsif ( $command eq "status" ) {
        print "Checking the Status of the script.. OK \n";
        exit 0;
    }
    else {
        &usage();
        exit 1;
    }
}

sub start_vip() {
    `ssh $ssh_user\@$new_master_host \" $ssh_start_vip \"`;
}
sub stop_vip() {
     return 0  unless  ($ssh_user);
    `ssh $ssh_user\@$orig_master_host \" $ssh_stop_vip \"`;
}

sub usage {
    print
    "Usage: master_ip_failover --command=start|stop|stopssh|status --orig_master_host=host --orig_master_ip=ip --orig_master_port=port --new_master_host=host --new_master_ip=ip --new_master_port=port\n";
}
```

```none
阿里云:wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
```



