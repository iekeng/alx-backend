#!/usr/bin/env python3
'''2-lifo_cache'''

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''implements LIFO cache replacement policy'''

    def __init__(self):
        '''inherits from the super class'''
        super().__init__()

    def put(self, key, item):
        '''Sets an item in the cache_data dict'''
        if key is None or item is None:
            return

        elif len(self.cache_data) >= self.MAX_ITEMS \
                and key not in self.cache_data:
            newest_key = list(self.cache_data)[-1]
            self.cache_data.pop(newest_key)
            print(f'DISCARD: {newest_key}')

        elif key in self.cache_data:
            self.cache_data[key] = item
            print(f'DISCARD: {key}')

        self.cache_data[key] = item

    def get(self, key):
        '''retrives an item from the cache_data dict'''
        try:
            return self.cache_data[key]
        except KeyError:
            return None
