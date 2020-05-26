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
  ```

  