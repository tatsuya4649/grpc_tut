from __future__ import print_function
import logging

import grpc

import pb.ex_pb2 as ex_pb2
import pb.ex_pb2_grpc as ex_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = ex_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(ex_pb2.HelloRequest(name="Tanaka"))
        print("Greeter client received: " + response.message)
        response = stub.SayHello2(ex_pb2.HelloRequest(name="Suzuki"))
        print("Greeter client received: " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    run()
