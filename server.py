from concurrent import futures
import logging

import grpc
import hello_pb2
import hello_pb2_grpc


class HelloWServicer(hello_pb2_grpc.HelloServiceServicer):

    def Hello(
        self, request: hello_pb2.HelloRequest, context
    ) -> hello_pb2.HelloResponse:
        return hello_pb2.HelloResponse(message=f"Hello, {request.name}!")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_HelloServiceServicer_to_server(HelloWServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
