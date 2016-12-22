'''
App Configuration
'''

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    pass

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    BOTS_HOST = {
        'Santander': '192.168.15.5:50052',
        'Banorte': 'localhost:50053',
        'Bancoppel': 'localhost:50054'
    }

CONFIG = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
    'production': ''
}
