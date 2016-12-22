'''GRPC SERVER'''
from concurrent import futures
import time
import grpc

import app.messages.messages_pb2 as msg
from app.messages.channel import ResponseServer

ONE_DAY_IN_SECONDS = 60 * 60 * 24


class GrpcServer(object):

    def __init__(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=15))

    def serve(self):
        ''' Start server '''
        print('Servidor...')
        msg.add_MessagesServicer_to_server(ResponseServer(), self.server)
        self.server.add_insecure_port('[::]:50051')
        self.server.start()
        try:
            while True:
                time.sleep(ONE_DAY_IN_SECONDS)
        except KeyboardInterrupt:
            self.server.stop(None)


if __name__ == '__main__':
    server = GrpcServer()
    server.serve()
