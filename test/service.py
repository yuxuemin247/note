# coding:utf-8
import time
from concurrent import futures

import grpc
import hello_pb2 as pb2
import hello_pb2_grpc as pb2_grpc   #服务器

class Bibili(pb2_grpc.BibiliServicer):

    def helloyu(self, request, context):
        name = request.name
        age =  request.age

        result = f'my name is {name} ,i am {age} years old'
        return pb2.resp(result=result)

def main():
    grpc_server = grpc.server(
            futures.ThreadPoolExecutor(max_workers=4)
        )

    #将 Bibili注册到 grpc_server
    pb2_grpc.add_BibiliServicer_to_server(Bibili(),grpc_server)
    #绑定端口
    grpc_server.add_insecure_port('0.0.0.0:5000')
    print('grpc 服务启动')
    #启动
    grpc_server.start()
    try:
        while 1:
            time.sleep(3600)
    except  KeyboardInterrupt:
        grpc_server.stop(0)

if __name__ == '__main__':
    main()
