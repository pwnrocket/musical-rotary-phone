import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
        ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'MLApp Admin <MLApp@example.com>'
    FLASKY_ADMIN = os.environ.get('MLApp_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASKY_POSTS_PER_PAGE = 20    

    @staticmethod
    def init_app(app):  
        pass


class DevelopmentConfig(Config):
    DEBUG = True 
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://phpUser:root1234@localhost:3306/newsdb'

class TestingConfig(Config):
    TESTING = True 
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://phpUser:root1234@localhost:3306/newsdb'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://phpUser:root1234@localhost:3306/newsdb'

config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'production' : ProductionConfig,

    'default' : DevelopmentConfig
}