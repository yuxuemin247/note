redis是一个内存的kv，单线程(工作线程)、IO模型(多线程，异步事务)，value常用的5大类型，每个类型都有本地方法(计算向数据移动)，c语言写的，内核（kernel）

多路复用器 反应IO事件，然后同步自己读写（串行），计算(计算)

redis单实例无法利用CPU，多实例考虑网卡

秒杀 ：

商品99个，不能超卖

高并发，负载均衡(4层或7层) 

并发连接数，并行处理数

##### 5种value

##### 1、  string

  字符串(session、uuid、VFS in main )

  数值(限流器，点击率，统计)

  bitmap 二进制操作(用户活跃统计，12306，权限)

```
#字节
setbit key offset value
setbit k1   1        1
01000000    #@
setbit k1   7        1
01000001    A
#自动扩容
setbit      k1       9999999
BITCOUNT   k1  0  -1   #-1是最后

bitop  and k3  k1 k2 [k5,k6...] #按位与
bitop  or  k4  k1 k2 [k5,k6...] #按位或
```

redis是二进制安全的(只识别字节Byte)

##### 2、 List

 双向链表，通过指针可以快速访问头和尾(0(1)), 中间访问(o(n))

list是有序的，放入顺序有序，并不会排序

```
lpush k1  a b c d e
lrange k1 0  -1
lpop k1
rpop k1 
ltrim k1 0 -1  删除区间以外的，可以用来保留热数据
```

lindex k1  下标   数组

同向指令  实现栈

异向指令  实现队列

数据从程序迁移出去，无状态

ltrim k1 0 5  删除区间以外的，保留0-5的，可以用来保留热数据。

##### 3、hash(商品详情页，聚合前景)

解决key太多,另外使用灵活，可以取属性，取值

```
hset yu name aaa
hset yu age  18
hgetall  yu
hkeys    yu
hvalues  yu
hget     yu age   
hincrby yu age -1  #也支持数值的加减
```

##### 4、set,去重，绝对无序（排序和放入顺序两个都无关），抽奖

```
sadd k1 1 2 3 4
smembers k1
集合较耗时，可以把集合操作迁移到一个独立的实例中
srandmember k1 3  返回一个集合元素个数为3不会重复的新集合
srandmember k1 -8 返回8个，可以为空
集合的交并差
sunion k1 k2   返回元素不重复的并集
sinter k1 k2   返回交集
sdiff  k1 k2   差集(左差)
共同好友，推荐系统
```

##### 5、有序集合，去重，有序。（排行榜，评论动态分页）

```
zadd k1 4 apple 3.2 banna 1.6 orange
zrange k1 0 -1 withscores   #默认是升序
zrevrange  k1 0 1 withscores #取最高的两个
type(k1)
object encoding k1  #ziplist 压缩，元素比较少(阈值64)、或者元素内容较小
                    #skiplist 跳跃表，随机造层，最高也就64层，维护多个链表。
```

持久化：基本两类，快照和日志。

快照：rdb 恢复速度比较快，没有计算的复杂度，丢失的可能会比较多。默认redis使用rdb

日志：慢，冗余量，相同操作多时，重写(rewrite把重复的操作抵消)

aof 三个级别：1、每操作 完整性

​								      2、每秒钟，自己调一下flush，刷到磁盘  （默认）

​			                          3、使用操作系统内核的一个buffer，满了在刷

其实redis主要做缓存，数据库也有全量数据，所以丢失一点问题也不大，就是可能会遇到冷启动，缓存雪崩穿透击穿等。

另外时间和空间本来就是不可调和的矛盾

混合使用：

​              

hdoop hdfs  fsimag(全量快照),edis.log(增加日志)



集群：

单机都会有 单点故障，压力比较大，服务器资源有限

单点故障：主从主备集群，数据要相同（镜像）

压力过大：分片集群

主从主备集群：数据同步

- 强一致性：得到数据先同步，再返回客户端。强一致性破坏了可用性。

  redis支持

- 弱一致性：得到数据写成功就返回客户端，维护一个队列进行同步

  redis默认

- 最终一致性

 CAP

 AKF

分片集群

- 客户端程序员自己实现，range区间，hash
- 代理proxy,由代理层实现算法
- 16384个槽位，redis自己实现的一个自有集群。只有改一个map映射，找到对应redis实例

