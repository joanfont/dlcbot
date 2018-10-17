from dlcbot.cache import Factory as CacheFactory
from dlcbot import providers

class Dictionary:

    CACHE_TTL = 0

    def __init__(self, provider, cache):
        self._provider = provider
        self._cache = cache

    def find(self, word):
        key = self._get_cache_key(word)
        definition = self._cache.get(key)
        if definition is not None:
            return definition.decode('utf-8')

        definition = self._provider.find(word)
        self._cache.set(key, definition, self.CACHE_TTL)

        return definition

    def _get_cache_key(self, word):
        return f'{self._provider.NAME}:{word}'


class Factory:

    @classmethod
    def dlc(cls):
        provider = providers.DLC()
        cache = CacheFactory.redis()

        return Dictionary(provider, cache)

    @classmethod
    def dcvb(cls):
        provider = providers.DCVB()
        cache = CacheFactory.redis()

        return Dictionary(provider, cache)