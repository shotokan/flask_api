import grpc
import time
import random
import uuid
import arrow
import messages_pb2 as msg
from concurrent import futures


class GrpcClient(object):

    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:50051')

    def run(self):
        stub = msg.MessagesStub(self.channel)
        req = msg.Request(id=str(uuid.uuid4()), message='se ha apagado', \
        bot='Santander', datetime=str(arrow.now()))
        resp = stub.Message(req)
        print(resp)

if __name__ == '__main__':
    client = GrpcClient()
    client.run()