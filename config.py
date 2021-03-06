#!/bin/env python2.7
#! -*- coding: UTF-8 -*-
import os
basedir = os.path.abspath( os.path.dirname( __file__ ))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dsf,.ddsuper secret key'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SUBJECT_PREFIX = '[songy blog]'
    MAIL_SENDER         = 'Admin <symyself@163.com>'
    ADMIN_EMAIL               = os.environ.get('FLASK_ADMIN_EMAIL') or 'symyself@163.com'
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    ##MAIL_USERNAME = os.getenv.get('MAIL_USERNAME')
    ##MAIL_PASSWROD = os.getenv.get('MAIL_PASSWROD')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = 'mysql://flask:flask@127.0.0.1/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    #使用本地地址，不使用cdn
    BOOTSTRAP_SERVE_LOCAL = True
    TABLE_PREFIX='blog_'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://flask:flask@127.0.0.1/flask_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    #使用本地地址，不使用cdn
    BOOTSTRAP_SERVE_LOCAL = True
    TABLE_PREFIX='blog_'
    #禁用csrf,便于测试提交表单
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    #使用本地地址，不使用cdn
    BOOTSTRAP_SERVE_LOCAL = True
    SQLALCHEMY_DATABASE_URI = 'mysql://flask:flask@127.0.0.1/flask_pro'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


config = {
    'dev' : DevelopmentConfig,
    'test'   : TestingConfig,
    'product': ProductionConfig,
    'default'   : DevelopmentConfig
}

if __name__ == '__main__':
    print __file__
    print os.path.dirname( __file__ )
    print basedir
