# coding: utf-8

import grpc
import hello_pb2 as pb2
import hello_pb2_grpc as pb2_grpc

#pip install grpcio grpcio-tools protobuf
#定义频道
def run():
    conn = grpc.insecure_channel('10.110.51.238:5000')
    #定义客户端
    client = pb2_grpc.BibiliStub(channel=conn)
    response =client.helloyu(pb2.req(name='yu',age=33))
    print(response.result)

if __name__ == '__main__':
    run()