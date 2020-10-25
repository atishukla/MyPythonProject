import os
import json

with open('/etc/config.json') as config_file:  # when using file on server
    config = json.load(config_file)


class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY') # for ide
    SECRET_KEY = config.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') # for ide
    SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('EMAIL_USER') # for ide
    MAIL_USERNAME = config.get('EMAIL_USER')
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASS') # for ide
    MAIL_PASSWORD = config.get('EMAIL_PASS')
