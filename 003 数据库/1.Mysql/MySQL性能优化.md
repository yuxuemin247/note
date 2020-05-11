## MySQL性能优化

### 1、使用索引

### 2、存储过程

过程，通常也称之为存储过程，它是事先编译好存储在数据库中的一组SQL的集合。调用存储过程可以简化应用程序开发人员的工作，减少与数据库服务器之间的通信，对于提升数据操作的性能是有帮助的，这些我们在之前的[《关系型数据库MySQL》](../Day36-40/36-38.关系型数据库MySQL.md)一文中已经提到过。

### 3、数据分区

MySQL支持做数据分区，通过分区可以存储更多的数据、优化查询，获得更大的吞吐量并快速删除过期的数据。关于这个知识点建议大家看看MySQL的[官方文档](https://dev.mysql.com/doc/refman/5.7/en/partitioning-overview.html)。数据分区有以下几种类型：

1. RANGE分区：基于连续区间范围，把数据分配到不同的分区。

   ```SQL
   CREATE TABLE tb_emp (
       eno INT NOT NULL,
       ename VARCHAR(20) NOT NULL,
       job VARCHAR(10) NOT NULL,
       hiredate DATE NOT NULL,
       dno INT NOT NULL
   )
   PARTITION BY RANGE( YEAR(hiredate) ) (
       PARTITION p0 VALUES LESS THAN (1960),
       PARTITION p1 VALUES LESS THAN (1970),
       PARTITION p2 VALUES LESS THAN (1980),
       PARTITION p3 VALUES LESS THAN (1990),
       PARTITION p4 VALUES LESS THAN MAXVALUE
   );
   ```

2. LIST分区：基于枚举值的范围，把数据分配到不同的分区。

3. HASH分区 / KEY分区：基于分区个数，把数据分配到不同的分区。

   ```SQL
   CREATE TABLE tb_emp (
       eno INT NOT NULL,
       ename VARCHAR(20) NOT NULL,
       job VARCHAR(10) NOT NULL,
       hiredate DATE NOT NULL,
       dno INT NOT NULL
   )
   PARTITION BY HASH(dno)
   PARTITIONS 4;
   ```

### 4、SQL优化

1. 定位低效率的SQL语句 - 慢查询日志。

   - 查看慢查询日志相关配置

      ```SQL
      mysql> show variables like 'slow_query%';
      +---------------------------+----------------------------------+
      | Variable_name             | Value                            |
      +---------------------------+----------------------------------+
      | slow_query_log            | OFF                              |
      | slow_query_log_file       | /mysql/data/localhost-slow.log   |
      +---------------------------+----------------------------------+

      mysql> show variables like 'long_query_time';
      +-----------------+-----------+
      | Variable_name   | Value     |
      +-----------------+-----------+
      | long_query_time | 10.000000 |
      +-----------------+-----------+
      ```

   - 修改全局慢查询日志配置。

      ```SQL
      mysql> set global slow_query_log='ON'; 
      mysql> set global long_query_time=1;
      ```

      或者直接修改MySQL配置文件启用慢查询日志。

      ```INI
      [mysqld]
      slow_query_log=ON
      slow_query_log_file=/usr/local/mysql/data/slow.log
      long_query_time=1
      ```

2. 通过`explain`了解SQL的执行计划。例如：

   ```SQL
   explain select ename, job, sal from tb_emp where dno=20\G
   *************************** 1. row ***************************
              id: 1
     select_type: SIMPLE
           table: tb_emp
            type: ref
   possible_keys: fk_emp_dno
             key: fk_emp_dno
         key_len: 5
             ref: const
            rows: 7
           Extra: NULL
   1 row in set (0.00 sec)
   ```

   - `select_type`：查询类型（SIMPLE - 简单查询、PRIMARY - 主查询、UNION - 并集、SUBQUERY - 子查询）。
   - `table`：输出结果集的表。
   - `type`：访问类型（ALL - 全表查询性能最差、index、range、ref、eq_ref、const、NULL）。
   - `possible_keys`：查询时可能用到的索引。
   - `key`：实际使用的索引。
   - `key_len`：索引字段的长度。
   - `rows`：扫描的行数，行数越少肯定性能越好。
   - `extra`：额外信息。

3. 通过`show profiles`和`show profile for query`分析SQL。

   MySQL从5.0.37开始支持剖面系统来帮助用户了解SQL执行性能的细节，可以通过下面的方式来查看MySQL是否支持和开启了剖面系统。

   ```SQL
   select @@have_profiling;
   select @@profiling;
   ```

   如果没有开启剖面系统，可以通过下面的SQL来打开它。

   ```SQL
   set profiling=1;
   ```

   接下来就可以通过剖面系统来了解SQL的执行性能，例如：

   ```SQL
   mysql> select count(*) from tb_emp;
   +----------+
   | count(*) |
   +----------+
   |       14 |
   +----------+
   1 row in set (0.00 sec)
   
   mysql> show profiles;
   +----------+------------+-----------------------------+
   | Query_ID | Duration   | Query                       |
   +----------+------------+-----------------------------+
   |        1 | 0.00029600 | select count(*) from tb_emp |
   +----------+------------+-----------------------------+
   1 row in set, 1 warning (0.00 sec)
   
   mysql> show profile for query 1;
   +----------------------+----------+
   | Status               | Duration |
   +----------------------+----------+
   | starting             | 0.000076 |
   | checking permissions | 0.000007 |
   | Opening tables       | 0.000016 |
   | init                 | 0.000013 |
   | System lock          | 0.000007 |
   | optimizing           | 0.000005 |
   | statistics           | 0.000012 |
   | preparing            | 0.000010 |
   | executing            | 0.000003 |
   | Sending data         | 0.000070 |
   | end                  | 0.000012 |
   | query end            | 0.000008 |
   | closing tables       | 0.000012 |
   | freeing items        | 0.000032 |
   | cleaning up          | 0.000013 |
   +----------------------+----------+
   15 rows in set, 1 warning (0.00 sec)
   ```

4. 优化CRUD操作。

   - 优化`insert`语句
     - 在`insert`语句后面跟上多组值进行插入在性能上优于分开`insert`。
     - 如果有多个连接向同一个表插入数据，使用`insert delayed`可以获得更好的性能。
     - 如果要从一个文本文件装载数据到表时，使用`load data infile`比`insert`性能好得多。

   - 优化`order by`语句

     - 如果`where`子句的条件和`order by`子句的条件相同，而且排序的顺序与索引的顺序相同，如果还同时满足排序字段都是升序或者降序，那么只靠索引就能完成排序。

   - 优化`group by`语句

     - 在使用`group by`子句分组时，如果希望避免排序带来的开销，可以用`order by null`禁用排序。

   - 优化嵌套查询

     - MySQL从4.1开始支持嵌套查询（子查询），这使得可以将一个查询的结果当做另一个查询的一部分来使用。在某些情况下，子查询可以被更有效率的连接查询取代，因为在连接查询时MySQL不需要在内存中创建临时表来完成这个逻辑上需要多个步骤才能完成的查询。

   - 优化or条件

     - 如果条件之间是`or`关系，则只有在所有条件都用到索引的情况下索引才会生效。

   - 优化分页查询

     - 分页查询时，一个比较头疼的事情是如同`limit 1000, 20`，此时MySQL已经排序出前1020条记录但是仅仅返回第1001到1020条记录，前1000条实际都用不上，查询和排序的代价非常高。一种常见的优化思路是在索引上完成排序和分页的操作，然后根据返回的结果做表连接操作来得到最终的结果，这样可以避免出现全表查询，也避免了外部排序。

       ```SQL
       select * from tb_emp order by ename limit 1000, 20;
       select * from tb_emp t1 inner join (select eno from tb_emp order by ename limit 1000, 20) t2 on t1.eno=t2.eno;
       ```

       上面的代码中，第2行SQL是优于第1行SQL的，当然我们的前提是已经在`ename`字段上创建了索引。

   - 使用SQL提示
     - USE INDEX：建议MySQL使用指定的索引。
     - IGNORE INDEX：建议MySQL忽略掉指定的索引。
     - FORCE INDEX：强制MySQL使用指定的索引。

### 5、配置优化

可以使用下面的命令来查看MySQL服务器配置参数的默认值。

```SQL
show variables;
show variables like 'key_%';
show variables like '%cache%';
show variables like 'innodb_buffer_pool_size';
```

通过下面的命令可以了解MySQL服务器运行状态值。

```SQL
show status;
show status like 'com_%';
show status like 'innodb_%';
show status like 'connections';
show status like 'slow_queries';
```

1. 调整`max_connections`：MySQL最大连接数量，默认151。在Linux系统上，如果内存足够且不考虑用户等待响应时间这些问题，MySQL理论上可以支持到万级连接，但是通常情况下，这个值建议控制在1000以内。
2. 调整`back_log`：TCP连接的积压请求队列大小，通常是max_connections的五分之一，最大不能超过900。
3. 调整`table_open_cache`：这个值应该设置为max_connections的N倍，其中N代表每个连接在查询时打开的表的最大个数。
4. 调整`innodb_lock_wait_timeout`：该参数可以控制InnoDB事务等待行锁的时间，默认值是50ms，对于反馈响应要求较高的应用，可以将这个值调小避免事务长时间挂起；对于后台任务，可以将这个值调大来避免发生大的回滚操作。
5. 调整`innodb_buffer_pool_size`：InnoDB数据和索引的内存缓冲区大小，以字节为单位，这个值设置得越高，访问表数据需要进行的磁盘I/O操作就越少，如果可能甚至可以将该值设置为物理内存大小的80%。
6. 更换更高效的存储引擎 ： `MyISM > InnoDB >xtraDB`(5%-10%)

### 6、架构优化

1. 通过拆分提高表的访问效率。
   - 垂直拆分
   - 水平拆分

2. 逆范式理论。数据表设计的规范程度称之为范式（Normal Form），要提升表的规范程度通常需要将大表拆分为更小的表，范式级别越高数据冗余越小，而且在插入、删除、更新数据时出问题的可能性会大幅度降低，但是节省了空间就意味着查询数据时可能花费更多的时间，原来的单表查询可能会变成连表查询。为此，项目实践中我们通常会进行逆范式操作，故意降低范式级别增加冗余来减少查询的时间开销。
   - 1NF：列的原子性，列不能再拆分
   - 2NF：所有的属性都依赖于主键，记录的唯一性
   - 3NF：字段的无冗余性，不能派生(通过其他字段计算得来)
   - BCNF：消除非平凡多值依赖

3. 使用中间表提高统计查询速度。

   使用`insert into 中间表 select ... where ...`这样的语句先将需要的数据筛选出来放到中间表中，然后再对中间表进行统计，避免不必要的运算和处理。

4. 主从复制和读写分离

   主机Master用来做数据写入，从机Slave用来数据读取

   - 常见结构：
     - 一主多从，主从通过`binlog`进行数据同步
     - 双主多从，`3M`架构

   - 读写分离
     - 程序自身实现读写分离
       - 代码连接不同数据库
     - 使用第三方代理工具，服务器实现
       - `mysql_proxy`
       - `jd`也发布了一个数据库代理服务器

5. 配置MySQL集群。

6. 设计数据库表时

   - 优化表设计，调整结构

     大表拆小表，尽量保持小表。把可变的数据和不可变的数据分开，大字段和小字段分开

     增加冗余字段，节约计算（违反第三范式）

7. 查看业务类型，业务的读写比列

   - 读密集加读缓存，用`NoSQL`做Cache
   - 写密集，加写缓冲buffer，在真正写库之前，先写到一个高速的中间层，然后再合并写入数据库.一个常见的写缓冲 `ttserver`

8. `Sharding`/分库分表/水平拆分

   前提：业务很少有跨表的全表操作

   把一个大表里的数据，按照一个规则分散到多个结构相同，但名字后缀不同的小表中，

   规则：hash （数据要求尽量均匀），hash后取后两位 

   ​			`datatime` ：最近使用效率高   订单

   ​			`geo_location ` ：数据有地理分布特性

### 7、查询缓存

```
可将如下语句
query_cache_size = 268435456
query_cache_type = 1
query_cache_limit = 1048576
存放到/etc/my.cnf文件的[mysqld]下
然后重启mysql数据库
service mysqld restart
就会启动mysql的缓存机制Query Cache。 在使用中，查询缓存会存储一个 SELECT 查询的文本与被传送到客户端的相应结果。
如果之后接收到一个同样的查询，服务器将从查询缓存中检索结果，而不是再次分析和执行这个同样的查询。
注意：查询缓存绝不返回过期数据。当数据被修改后，在查询缓存中的任何相关词条均被转储清除。
适用于更改不是太频繁的表且有大量相同查询的情况
```

### 8、云数据库

```
直接使用云数据库，或者硬件升级，升级内存。
阿里云的OcenanBase :TPC top 1
TiDB等国产新兴分布式数据库,一键水平伸缩
```

