##### 1、生产者

```
from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'mybroker1,mybroker2'})

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

for data in some_data_source:
    # Trigger any available delivery report callbacks from previous produce() calls
    p.poll(0)

    # Asynchronously produce a message, the delivery report callback
    # will be triggered from poll() above, or flush() below, when the message has
    # been successfully delivered or failed permanently.
    p.produce('mytopic', data.encode('utf-8'), callback=delivery_report)

# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
p.flush()
```

##### 2、消费者

```
from confluent_kafka import Consumer,KafkaError

c = Consumer({
    'bootstrap.servers':'10.47.121.12:9092',
    'group.id': 'mygroup',
    'default.topic.config': {
        'enable.auto.commit': True,
        'auto.offset.reset': 'earliest',  #换组后重新更新offset到最小
    }
})

c.subscribe(['KAFKA_ALARM_TOPIC'])   #订阅主题

while True:
    msg = c.poll(timeout=1.0)
    if msg is None:
        print ("Msg is none")
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:     #_PARTITION_EOF = -191
            continue
        else:
            print(msg.error())
            break
    print('Received message: {}'.format(msg.value().decode('utf-8')))
c.close()
```

##### 3、管理员客户端

```
from confluent_kafka.admin import AdminClient, NewTopic

a = AdminClient({'bootstrap.servers': 'mybroker'})

new_topics = [NewTopic(topic, num_partitions=3, replication_factor=1) for topic in ["topic1", "topic2"]]
# Note: In a multi-cluster production scenario, it is more typical to use a replication_factor of 3 for durability.

# Call create_topics to asynchronously create topics. A dict of <topic,future> is returned.
fs = a.create_topics(new_topics)

# Wait for each operation to finish.
for topic, f in fs.items():
    try:
        f.result()  # The result itself is None
        print("Topic {} created".format(topic))
    except Exception as e:
        print("Failed to create topic {}: {}".format(topic, e))
```

##### 4、`avro`生成者

```
from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer


value_schema_str = """
{
   "namespace": "my.test",
   "name": "value",
   "type": "record",
   "fields" : [
     {
       "name" : "name",
       "type" : "string"
     }
   ]
}
"""

key_schema_str = """
{
   "namespace": "my.test",
   "name": "key",
   "type": "record",
   "fields" : [
     {
       "name" : "name",
       "type" : "string"
     }
   ]
}
"""

value_schema = avro.loads(value_schema_str)
key_schema = avro.loads(key_schema_str)
value = {"name": "Value"}
key = {"name": "Key"}


def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


avroProducer = AvroProducer({
    'bootstrap.servers': 'mybroker,mybroker2',
    'on_delivery': delivery_report,
    'schema.registry.url': 'http://schema_registry_host:port'
    }, default_key_schema=key_schema, default_value_schema=value_schema)

avroProducer.produce(topic='my_topic', value=value, key=key)
avroProducer.flush()
```

##### 5、`avro`消费者

```
from confluent_kafka import KafkaError
from confluent_kafka.avro import AvroConsumer
from confluent_kafka.avro.serializer import SerializerError


c = AvroConsumer({
    'bootstrap.servers': 'mybroker,mybroker2',
    'group.id': 'groupid',
    'schema.registry.url': 'http://127.0.0.1:8081'})

c.subscribe(['my_topic'])

while True:
    try:
        msg = c.poll(10)

    except SerializerError as e:
        print("Message deserialization failed for {}: {}".format(msg, e))
        break

    if msg is None:
        continue

    if msg.error():
        print("AvroConsumer error: {}".format(msg.error()))
        continue

    print(msg.value())

c.close()
```

[博客1](![image-20200528185434345](C:\Users\L-yuxuemin\AppData\Roaming\Typora\typora-user-images\image-20200528185434345.png))

[博客2](https://support.huaweicloud.com/devg-dms/dms-devg-0312005.html)

参数

| 参数                   | 默认值   | 推荐值               | 说明                                                         |
| ---------------------- | -------- | -------------------- | ------------------------------------------------------------ |
| `acks`                 | 1        | 高可靠：all高吞吐：1 | producer需要server接收到数据之后发出的确认接收的信号，此项配置就是指`procuder`需要多少个这样的确认信号。此配置实际上代表了数据备份的可用性。以下设置为常用选项：（1）`acks`=0：设置为0表示producer不需要等待任何确认收到的信息。副本将立即加到socket buffer并认为已经发送。没有任何保障可以保证此种情况下server已经成功接收数据，同时重试配置不会发生作用（因为客户端不知道是否失败）回馈的offset会总是设置为-1；（2）`acks`=1：这意味着至少要等待leader已经成功将数据写入本地log，但是并没有等待所有follower是否成功写入。这种情况下，如果follower没有成功备份数据，而此时leader又无法提供服务，则消息会丢失。（3）`acks`=all：这意味着leader需要等待所有备份都成功写入日志，这种策略会保证只要有一个备份存活就不会丢失数据。 |
| retries                | 0        | 0                    | 设置大于0的值将使客户端重新发送任何数据，一旦这些数据发送失败。注意，这些重试与客户端接收到发送错误时的重试没有什么不同。允许重试将潜在的改变数据的顺序，如果这两个消息记录都是发送到同一个partition，则第一个消息失败第二个发送成功，则第二条消息会比第一条消息出现要早。 |
| `request.timeout.ms`   | 30000    | 120000               | 设置一个请求最大等待时间，超过这个时间则会抛Timeout异常      |
| `block.on.buffer.full` | TRUE     | 默认值               | 当我们内存缓存用尽时，必须停止接收新消息记录或者抛出错误。默认情况下，这个设置为真，然而某些阻塞可能不值得期待，因此立即抛出错误更好。设置为false则会这样：producer会抛出一个异常错误：`BufferExhaustedException` |
| `batch.size`           | 16384    | 262144               | producer将试图批处理消息记录，以减少请求次数。这将改善client与server之间的性能。这项配置控制默认的批量处理消息字节数。不会试图处理大于这个字节数的消息字节数。发送到brokers的请求将包含多个批量处理，其中会包含对每个partition的一个请求。较小的批量处理数值比较少用，并且可能降低吞吐量（0则会仅用批量处理）。较大的批量处理数值将会浪费更多内存空间，这样就需要分配特定批量处理数值的内存大小。 |
| `buffer.memory`        | 33554432 | 536870912            | producer可以用来缓存数据的内存大小。如果数据产生速度大于向broker发送的速度，producer会阻塞或者抛出异常，以`block.on.buffer.full`来表明。这项设置将和producer能够使用的总内存相关，但并不是一个硬性的限制，因为不是producer使用的所有内存都是用于缓存。一些额外的内存会用于压缩（如果引入压缩机制），同样还有一些用于维护请求。 |

| 参数                      | 默认值 | 推荐值   | 说明                                                         |
| ------------------------- | ------ | -------- | ------------------------------------------------------------ |
| `auto.commit.enable`      | TRUE   | FALSE    | 如果为真，consumer所fetch的消息的offset将会自动的同步到`zookeeper`。这项提交的offset将在进程无法提供服务时，由新的consumer使用。约束： 设置为false后，需要先成功消费再提交，避免消息丢失。 |
| `auto.offset.reset`       | latest | earliest | 没有初始化offset或者offset被删除时，可以设置以下值 ：1、earliest：自动复位offset为最早。2、latest：自动复位offset为最新  3、none：如果没有发现offset则向消费者抛出异常 4、anything   else：向消费者抛出异常。 |
| `connections.max.idle.ms` | 600000 | 30000    | 空连接的超时时间，设置为30000可以在网络异常场景下减少请求卡顿的时间。 |