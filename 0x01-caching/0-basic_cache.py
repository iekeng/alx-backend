#!/usr/bin/env python3
'''0-basic_cache'''

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''Inherits all methods from the BaseCaching class'''

    def put(self, key: str, item: str):
        '''sets an item in the cache_data dict'''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key: str):
        '''retrieves an item from the cache_data dict'''
        try:
            return self.cache_data[key]
        except KeyError:
            return None
