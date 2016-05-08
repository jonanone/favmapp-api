import os

DEBUG = True
SERVER_IP = os.environ.get('SERVER_IP', 'localhost:5000')
SERVER_HOST = SERVER_IP.split(':')[0]
SERVER_PORT = int(SERVER_IP.split(':')[1])

SECRET_KEY = os.environ['SECRET_KEY']
