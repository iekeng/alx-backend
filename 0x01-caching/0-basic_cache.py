#!/usr/bin/env python3
'''0-basic_cache'''

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''Inherits all methods from the BaseCaching class'''

    def put(self, key: str, item: str):
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key: str):
        try:
            return self.cache_data[key]
        except KeyError:
            return None
