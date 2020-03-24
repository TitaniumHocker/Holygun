# -*- coding: utf-8 -*-
from os import environ, path


class BaseConfig():
    TOKEN = environ.get('TOKEN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{path.join(path.dirname(__file__), "db.sqlite3")}'
    LOGGING_LEVEL='DEBUG'


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = (f'mysql+mysqlconnector://'
                               f'{environ.get("DB_USER")}:'
                               f'{environ.get("DB_PASS")}@'
                               f'{environ.get("DB_HOST")}/'
                               f'{environ.get("DB_NAME")}')
    LOGGING_LEVEL='ERROR'


class TestingConfig(DevelopmentConfig):
    pass


configs = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}
