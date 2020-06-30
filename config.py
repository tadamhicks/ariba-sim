import os

if os.environ['ENVIRONMENT'] == 'dev':
	DEBUG = True
	SQLALCHEMY_ECHO = True
else:
	DEBUG = False
	SQLALCHEMY_ECHO = False

SQLA_DB_USER = os.environ['MYSQL_USERNAME']
SQLA_DB_PASSWORD = os.environ['MYSQL_PASSWORD']
SQLA_DB_HOST = os.environ['MYSQL_IP']
SQLA_DB_PORT = os.environ['MYSQL_PORT']
SQLA_DB_NAME = os.environ['DB_NAME']
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + SQLA_DB_USER + ':' + SQLA_DB_PASSWORD + '@' + SQLA_DB_HOST + ':' + SQLA_DB_PORT + '/' + SQLA_DB_NAME

SQLALCHEMY_TRACK_MODIFICATIONS = False