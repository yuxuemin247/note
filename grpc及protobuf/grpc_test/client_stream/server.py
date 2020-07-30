# coding:utf-8
import time
from concurrent import futures
import grpc
import data_pb2 as pb2
import data_pb2_grpc as pb2_grpc

class serve1(pb2_grpc.Example):
    def test(self,request,context):
        data = request.data
        result = data

        return pb2.resp(result=result)


    def client_recv_stream(self,request,context):
        index = 1
        while  context.is_active():
            data = request.data
            index = index +1
            yield pb2.resp(result='send %s 第 %s'%(data,str(index)))

            # context.cancel() 关闭这个长连接
def run():
    grpc_server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=4)
    )

    pb2_grpc.add_ExampleServicer_to_server(serve1(),grpc_server)

    grpc_server.add_insecure_port('0.0.0.0:5000')
    print("服务端启动")
    grpc_server.start()
    try:
        while 1:
            time.sleep(3600)
    except KeyboardInterrupt:
        grpc_server.stop(0)

if __name__ == '__main__':
    run()