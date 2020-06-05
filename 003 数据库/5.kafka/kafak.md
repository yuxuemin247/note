- 创建topic 

  ```
  bin/kafka-topics.sh --create --zookeeper 39.100.114.253:2181 --topic first --partitions 2 --replication-factor 1
  ```

- 创建生产者

  ```
  bin/kafka-console-producer.sh --topic first --broker-list 39.100.114.253:9092
  ```

- 创建消费者

  ```
  bin/kafka-console-consumer.sh --topic first --bootstrap-server 39.100.114.253:9092 --from-beginning
  #这是新的，使用kafka本地的toPic来存消费信息(日志目录中会有50个offset文件)
  bin/kafka-console-consumer.sh --topic first --zookeeper 39.100.114.253:2182 
  #topic名-分区 文件夹下有 xxx.log(实际存储数据)
  ```
- 消费者组

```
bin/kafka-console-consumer.sh --zookeeper 39.100.114.253:2182 --topic first  --consumer.config  config/consumer.properties  #指定配置文件consumer.propertie 这个文件中的group_id要一样。
--zookeeper 与 --bootstrap-server 都一样
```

  ```
- ookeeper
- 消费
  高级`API`，写起来简单，不需要自行去管理offset,不需要管理分区，副本等情况。
  低级`API`，开发者自己控制`offset`，选择哪个分区，找到分区leader  
  ```