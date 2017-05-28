
# Define the application directory
import os
import json
from sqlalchemy import create_engine

USERNAME = "admin"
PASSWORD = "Youshouldchangethis"
HOST = 'localhost'
PORT = 5432
SQLUSER = ''
SQLPASSWORD = ''
FILENAME = 'apply'


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
IP_ADDRESS = '0.0.0.0'
PORT = 5000
SECRET_KEY = 'rF&UM39t6Rn2S6422776H9e3!*5D62*K'
APPLICATION_NAME = "Udacity Application Tracker"
# Statement for enabling the development environment
DEBUG = True
ADMIN = frozenset(["admin"])
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
    os.path.join(BASE_DIR, FILENAME + '.db')

# PostgreSQL setup
# SQLALCHEMY_DATABASE_URI = 'postgresql://' + \
#     SQLUSER + ":" + SQLPASSWORD + '@' + HOST + \
#     '/' + FILENAME
