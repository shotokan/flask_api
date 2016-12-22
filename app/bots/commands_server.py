'''GRPC SERVER'''
from concurrent import futures
import time
import grpc
from channel import ResponseServer

import bot_commands_pb2 as commands


ONE_DAY_IN_SECONDS = 60 * 60 * 24


class GrpcServer(object):

    def __init__(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))

    def serve(self):
        ''' Start server '''
        print('Servidor...')
        commands.add_BotCommandsServicer_to_server(ResponseServer(), self.server)
        self.server.add_insecure_port('[::]:50052')
        self.server.start()
        try:
            while True:
                time.sleep(ONE_DAY_IN_SECONDS)
        except KeyboardInterrupt:
            self.server.stop(None)


if __name__ == '__main__':
    server = GrpcServer()
    server.serve()
