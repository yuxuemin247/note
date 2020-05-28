1、查看平均延迟

redis-cli --latency  -h 'host' -p 'port'  看一下平均延迟

2、查看是不是有大集合操作

​    查看是不是一些大数据集的 交集，差集之类的。

3、查看redis的slow log来监控慢操作

4、或者用top这些看redis进程的cpu使用率，如果traffic不高，八成说明有慢操作

5、查看是不是持久化文件RDB和AOF重写  fork进程产生的

6、swapping(操作系统分页）引起的延迟

7、edis 2.6版本引进了redis看门狗(watchdog)软件，这是个调试工具用于诊断redis的延迟问题