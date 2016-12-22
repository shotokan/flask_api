'''
Channel for messages
'''
from pprint import pprint
from grpc import FutureTimeoutError, FutureCancelledError
import arrow

import app.messages.messages_pb2 as messages_pb2

class ResponseServer(messages_pb2.MessagesServicer):
    ''''Clase que se encarga de devolver el mensaje al cliente'''

    def Message(self, request, context):
        '''Save data received from bots into database and response with a message and code'''
        try:
            #payments = Payments.PaymentModel()
            #payments.add_payment(self.parse_request(request.p))
            pprint(request)
            return messages_pb2.Response(id=request.id, message='Ok', code=200)
        except FutureTimeoutError as fte:
            print('FutureTimeOut {0}'.format(str(fte)))
            return messages_pb2.Response(id=request.id, message=str(fte), \
             code=400, datetime=str(arrow.now()))
        except FutureCancelledError as fce:
            print('CancelError {0}'.format(str(fce)))
            return messages_pb2.Response(id=request.id, message=str(fce), datetime=str(arrow.now()))
        except Exception as excep:
            print('Exception {}'.format(str(excep)))
            return messages_pb2.Response(id=request.id, message=str(excep),\
            code=400, datetime=str(arrow.now()))

