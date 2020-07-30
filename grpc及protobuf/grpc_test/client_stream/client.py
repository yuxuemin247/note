# coding:utf-8

import grpc
import data_pb2 as pb2
import data_pb2_grpc as pb2_grpc

def run():
    conn = grpc.insecure_channel('192.168.0.111:5000')
    client = pb2_grpc.ExampleStub(channel =conn)

    resp = client.test(pb2.req(data = 'yuqweqweqw'))
    print(resp.result)

run()