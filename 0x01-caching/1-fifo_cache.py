#!/usr/bin/env python3
'''1-fifo_cache'''

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''Implements FIFO cache algorithm'''

    def __init__(self):
        '''Inherits methods and
        properties from parent class'''
        super().__init__()

    def put(self, key, item):
        '''Sets a new item in cache_data dict'''
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            wanted_key = list(self.cache_data)[0]
            self.cache_data.pop(wanted_key)
            print(f"DISCARD {wanted_key}")

    def get(self, key):
        '''Retrieves item from cache_data dict'''
        try:
            return self.cache_data[key]
        except KeyError:
            return None
