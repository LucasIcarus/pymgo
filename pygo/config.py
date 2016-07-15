
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
APP_PORT = 8888
APP_ADDR = '127.0.0.1'
MONGO_HOST='127.0.0.1'
MONGO_PORT= 27017
DEBUG = False
PROCESSES = 0

try:
    from local_config import *
except:
    pass