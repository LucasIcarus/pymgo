import msgpack
import redis
from config import REDIS_HOST,REDIS_PORT
class Session(object):
    def __init__(self, session_id, *args, **kwargs):
        object.__setattr__(self, "_data", {})
        self.session_id = session_id
        self._data.update(kwargs)
        self.redis_server = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

    def save(self):
        packed = msgpack.dumps(self._data)
        self.redis_server.set(self.session_id, packed)


    def delete(self):
        self.redis_server.delete(self.session_id)


    def insert(self, **kwargs):
        self._data.update(kwargs)


    def is_empty(self):
        return False if self._data else True


    def get(self, session_id):
        data = self.redis_server.get(session_id)
        if not data:
            data = {}
        else:
            data = msgpack.loads(data)
        session = Session(**data)
        return session

    def __getattribute__(self, name):
        data = object.__getattribute__(self, "_data")
        if name in data.keys():
            return data.get(name, '')
        else:
            return object.__getattribute__(self, name)


    def __setattr__(self, name, value):
        self._data.update({name: value})