import os
from flask_restful import Resource
from flask_restful import reqparse
from pybreaker import CircuitBreakerError
from app.app import bot_breaker
from app.bots.commands_client import GrpcClient
from app.config import CONFIG

class Bot(Resource):

    def __init__(self):
        super().__init__()
        self.client = GrpcClient(CONFIG[os.getenv('FLASK_CONFIG') or 'default'].BOTS_HOST)

    def get(self):
        return {'hello': 'world'}

    def post(self, action):
        parser = reqparse.RequestParser()
        parser.add_argument('bot', type=str, help='Bot Name')
        parser.add_argument('username', type=str, help='username')
        parser.add_argument('password', type=str, help='password')
        parser.add_argument('token', type=str, help='token')
        parser.add_argument('phrase', type=str, help='phrase')
        data = parser.parse_args()
        try:
            if action == 'start':
                msg = bot_breaker.call(self.client.start, data['bot'], data)
                return {'message': '%s [%s]' % (msg, data['bot']), 'code': 200}
            elif action == 'stop' and 'bot' in data:
                msg = bot_breaker.call(self.client.stop, data['bot'], data)
                return {'message': '%s [%s]' % (msg, data['bot']), 'code': 200}
            else:
                return {'message': 'Debe enviar una acción válida', 'code': 400}
        except CircuitBreakerError as cbe:
            print(cbe)
            return {'message': 'El servicio no se encuentra disponible', 'code': 500}
        except Exception as exce:
            print(exce)
            return {'message': 'No se ha podido ejecutar el comando de inicio', 'code': 400, 'error':str(exce)}


class BotCommand(Resource):

    def __init__(self):
        super().__init__()
        self.client = GrpcClient(CONFIG[os.getenv('FLASK_CONFIG') or 'default'].BOTS_HOST)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('bot', type=str, help='Bot Name')
        parser.add_argument('', type=str, help='Bot Name')
        data = parser.parse_args(strict=True)
        try:
            pass
        except CircuitBreakerError as cbe:
            print(cbe)
            return {'message': 'El servicio no se encuentra disponible', 'code': 500}
        except Exception as exce:
            print(exce)
            return {'message': 'No se ha podido ejecutar el comando de inicio', 'code': 400, 'error':exce}
