'''test for grpc server'''
print(__name__)
from app.messages.messages_server import GrpcServer

SERVER = GrpcServer()
SERVER.serve()
