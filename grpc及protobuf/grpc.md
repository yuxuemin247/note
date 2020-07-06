##### 一、简介

`GRPC`是一个高性能、通用的开源RPC框架，基于HTTP/2协议标准和Protobuf序列化协议开发，支持众多的开发语言

##### 二、使用

- 安装

  ```
  pip install grpcio       #gRPC 的安装
  pip install protobuf     #安装 ProtoBuf 相关的 python 依赖库
  pip install grpcio-tools #安装 python grpc 的 protobuf 编译工具
  ```

- 定义`gRPC`接口(`data.proto`)

  ```
  syntax = "proto3";
  package example;
  service FormatData {
    rpc DoFormat(Data) returns (Data){}
  }
  message Data {
    string text = 1;
  }
  ```

  - 编译` protobuf`

    ```
    python -m grpc_tools.protoc -i. --python_out=. --grpc_python_out=. ./data.proto
    #目录中执行编译，会生成：data_pb2.py 与 data_pb2_grpc.py
    ```

- 实现server端

  ```
  #! /usr/bin/env python
  # -*- coding: utf-8 -*-
  import grpc
  import time
  from concurrent import futures
  from example import data_pb2, data_pb2_grpc
  
  _ONE_DAY_IN_SECONDS = 60 * 60 * 24
  _HOST = 'localhost'
  _PORT = '8080'
  
  class FormatData(data_pb2_grpc.FormatDataServicer):
      def DoFormat(self, request, context):
          str = request.text
          return data_pb2.Data(text=str.upper())
  
  def serve():
      grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
      data_pb2_grpc.add_FormatDataServicer_to_server(FormatData(), grpcServer)
      grpcServer.add_insecure_port(_HOST + ':' + _PORT)
      grpcServer.start()
      try:
          while True:
              time.sleep(_ONE_DAY_IN_SECONDS)
      except KeyboardInterrupt:
          grpcServer.stop(0)
  
  if __name__ == '__main__':
      serve()
  ```

- 实现服务端

  ```
  #! /usr/bin/env python
  # -*- coding: utf-8 -*-
  import grpc
  from example import data_pb2, data_pb2_grpc
  
  _HOST = 'localhost'
  _PORT = '8080'
  
  def run():
      conn = grpc.insecure_channel(_HOST + ':' + _PORT)
      client = data_pb2_grpc.FormatDataStub(channel=conn)
      response = client.DoFormat(data_pb2.Data(text='hello,world!'))
      print("received: " + response.text)
  
  if __name__ == '__main__':
      run()
  ```

  [博客](https://www.jianshu.com/p/a24c88c0526a)

- stub对象调用

  首先需要创建一个 stub对象，用stub对象去调用服务。

  使用`.proto`中生成的`skyc2_pb2_grpc`模块的函数`FormatDataStub`来生成stub对象

  ```
  #同步(阻塞)，只获取response
  channel = grpc.insecure_channel(host+':'+str(port))
  stub = skyc2_pb2_grpc.FormatDataStub(channel=channel)
  metadata= [('ip','127.0.0.1'),('hello','360')]
  response = stub.Dofomat(
  				skyc2_pb2.Data(text=json.dumps(command_json)),
                  metadata = metadata,
                  timeout=timeout,
                  credentials=credentials
  			)
  ```

  ```
  #同步阻塞，同时获取response和_rendezvous Call对象
  #with_call
  channel = grpc.insecure_channel(host+':'+str(port))
  stub = skyc2_pb2_grpc.FormatDataStub(channel=channel)
  metadata= [('ip','127.0.0.1'),('hello','360')]
  response,call = stub.Dofomat.with_call(
  				skyc2_pb2.Data(text=json.dumps(command_json)),
                  metadata = metadata,
                  timeout=timeout,
                  credentials=None
  			)
  for meta in call.initial_metadata():
  	print meta
  #打印结果
  #('ip','127.0.0.1')
  #('hello','360')
  ```

  ```
  #异步(非阻塞)，获取_Rendezvous Call对象
  #future
  channel = grpc.insecure_channel(host+':'+str(port))
  stub = skyc2_pb2_grpc.FormatDataStub(channel=channel)
  metadata= [('ip','127.0.0.1'),('hello','360')]
  future = stub.Dofomat.future(
  				skyc2_pb2.Data(text=json.dumps(command_json)),
                  metadata = metadata,
                  timeout=timeout,
                  credentials=None
  			)
  #获取响应
  response = future.result()
  for meta in future.initial_metadata():
  	print meta
  #打印结果
  #('ip','127.0.0.1')
  #('hello','360')
  ```

  

三、其他

`gRPC` 默认一次传输数据大小为` 4MB`，超过就会报错,想要修改这个数值，需要在server和client端 创建的时候在options参数里配置需要的值

```
options = [(cygrpc.ChannelArgKey.max_send_message_lengthx, 100 * 1024 * 1024),
           (cygrpc.ChannelArgKey.max_receive_message_length, 100 * 1024 * 1024)]
channel = grpc_test.insecure_channel(host + ':' + str(port), options =options)

options = [(cygrpc.ChannelArgKey.max_send_message_lengthx, 100 * 1024 * 1024),
           (cygrpc.ChannelArgKey.max_receive_message_length, 100 * 1024 * 1024)]
server = grpc.server(futures.ThreadPoolExecutor(MAX_WORKERS),options=options)
```

