import sys
from concurrent import futures
import logging

import grpc

import pb.ex_pb2 as ex_pb2
import pb.ex_pb2_grpc as ex_pb2_grpc


class Greeter(ex_pb2_grpc.GreeterServicer):

    def SayHello(self,request,context):
        sys.stderr.write("*** Say Hello ***")
        str_out = f'Say {request.name}'
        sys.stderr.write(str_out+'\n')

        return ex_pb2.HelloReply(message=str_out)

    def SayHello2(self,request,context):
        sys.stderr.write("*** SayHello2 ***")
        str_out = f'Say2 {request.name}'
        sys.stderr.write(str_out+'\n')
        
        return ex_pb2.HelloReply(message=str_out)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ex_pb2_grpc.add_GreeterServicer_to_server(Greeter(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
