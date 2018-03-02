import redis


class Cache:

    def get(self, key, default=None):
        raise NotImplementedError()

    def set(self, key, value, ttl=0):
        raise NotImplementedError()

    def has(self, key):
        raise NotImplementedError()


class Redis(Cache):

    def __init__(self, host, port, db=0):
        self._redis = redis.StrictRedis(
            host=host,
            port=port,
            db=db
        )

    def get(self, key, default=None):
        value = self._redis.get(key)
        return value if value is not None else default

    def set(self, key, value, ttl=0):
        self._redis.set(key, value)

        if ttl:
            self._redis.expire(key, ttl)

    def has(self, key):
        return self.get(key) is not None

