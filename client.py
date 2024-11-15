from __future__ import print_function

import logging

import grpc
import hello_pb2
import hello_pb2_grpc


def run():
    print("Conectando ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = hello_pb2_grpc.HelloServiceStub(channel)
        response = stub.Hello(hello_pb2.HelloRequest(name="you", age=12))
        print("respone: ", response)
        response = stub.Hello(hello_pb2.HelloRequest(name="you 123", age=12))
        print("respone: ", response)
    print("Greeter client received: " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    run()
