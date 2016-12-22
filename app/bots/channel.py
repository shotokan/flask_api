import bot_commands_pb2 as bot_commands_pb2
from pprint import pprint
from grpc import FutureTimeoutError, FutureCancelledError
import arrow

class ResponseServer(bot_commands_pb2.BotCommandsServicer):
    ''''Clase que se encarga de devolver el mensaje al cliente'''


    def Command(self, request, context):
        '''Save data received from bots into database and response with a message and code'''
        try:
            band = False
            #payments = Payments.PaymentModel()
            #payments.add_payment(self.parse_request(request.p))
            cont = 1
            for r in request:
                print('------%d-----'%cont)
                print(r.id)
                print(r.command)
                print(arrow.now())
                cont += 1
                yield bot_commands_pb2.Response(id=r.id, message="entregado %s"%(r.datetime), code=200)
                #if band:
                #    for i in range(10):
                #        yield bot_commands_pb2.Response(id=r.id, message="entregado %s range %d"%(r.datetime, i), code=200)
                #    band = False
                #else:
                #    band = True
        except FutureTimeoutError as ft:
            print(str(ft))
            #return bot_commands_pb2.Response(id=r.id, message=str(ft), code=400)
        except Exception as ex:
            print(str(ex))
            #return bot_commands_pb2.Response(id=request.id, message=str(ex), code=400)
