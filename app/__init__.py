'''
Init app
'''
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_restful import Api
from app.config import CONFIG
from app.api.bots import Bot
from app.messages.messages_server import GrpcServer
#from app.app import grpc_call
import pybreaker
import arrow


def create_app(config_name):
    app = Flask(__name__)
    api = Api(app)
    #global grpc_call
    app.config.from_object(CONFIG[config_name])
    CONFIG[config_name].init_app(app)
    Bootstrap(app)
    #grpc_call = pybreaker.CircuitBreaker(fail_max=3, reset_timeout=30)
    api.add_resource(Bot, '/bot/<action>', endpoint='bot')
    return app
