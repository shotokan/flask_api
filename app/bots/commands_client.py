import grpc
import os
import time
import random
import uuid
import arrow
import json
import app.bots.bot_commands_pb2 as bot_cmd
from concurrent import futures
from grpc import FutureTimeoutError, FutureCancelledError, RpcError, StatusCode

class GrpcClient(object):

    def __init__(self, hosts):
        if isinstance(hosts, dict) and len(hosts) > 0:
            self.channels = dict()
            self.stub = None
            for key, val in hosts.items():
                self.channels[key] = grpc.insecure_channel(val)
        else:
            self.channel = grpc.insecure_channel('localhost:50052')

    def run(self):
        stub = bot_cmd.BotCommandsStub(self.channel)
        #req = bot.Request(id=str(uuid.uuid4()), command='start', \
        #bot='Santander', datetime=str(arrow.now()))
        #resp = stub.Message(req)
        try:
            resp = stub.Command(self.data(), 1)
        except Exception as exc:
            print("Error --- %s" % exc)
        cont = 1
        print(resp)
        for i in resp:
            print(cont)
            print(i)
            cont += 1

    def data(self):
        for msg in range(20):
            yield bot_cmd.Request(id=str(uuid.uuid4()), command='start {0}'.format(msg),\
             bot='Santander', datetime=str(arrow.now()))
            #time.sleep(random.uniform(0.5, 1.0))

    def start(self, bot, command):
        #print(type(dict(command)))
        #req = bot.Request(id=str(uuid.uuid4()), command='start', \
        #bot='Santander', datetime=str(arrow.now()))
        #resp = stub.Message(req)
        try:
            self.stub = bot_cmd.BotCommandsStub(self.channels[bot])
            command['action'] = 'start'
            #print(type(command))
            json_data = json.dumps(dict(command))
            print("--------date------{}".format(arrow.now()))
            resp = self.stub.Command(self.command(json_data), 5)
            msg = ''
            for row in resp:
                msg = row.message
            print("--------date------{}".format(arrow.now()))
            return msg
        except Exception as exc:
            print("Error --- %s" % exc)
            raise exc

    def stop(self, bot, command):
        self.stub = bot_cmd.BotCommandsStub(self.channels[bot])
        #req = bot.Request(id=str(uuid.uuid4()), command='start', \
        #bot='Santander', datetime=str(arrow.now()))
        #resp = stub.Message(req)
        try:
            command['action'] = 'stop'
            #print(type(command))
            json_data = json.dumps(dict(command))
            print("--------date------{}".format(arrow.now()))
            resp = self.stub.Command(self.command(json_data), 1)
            msg = ''
            for row in resp:
                msg = row.message
                print("--------date------{}".format(arrow.now()))
            return msg
        except Exception as exc:
            print("Error --- %s" % exc)
            raise exc

    def start2(self, bot):
        try:
            resp = self.stub.Command(self.command('start'), 1)
            print(resp)
            for row in resp:
                print(1)
                print(row)
        except Exception as exc:
            print("Error --- %s" % exc)

    def command(self, com):
        yield bot_cmd.Request(id=str(uuid.uuid4()), command=com,\
        bot='Santander', datetime=str(arrow.now()))

if __name__ == '__main__':
    client = GrpcClient({'Santander': 'localhost:50052'})
    #client = GrpcClient({})
    client.start('Santander', 'start')
    for i in range(50):
        client.start2('Santander')
