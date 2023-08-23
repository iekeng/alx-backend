#!/usr/bin/env python3
'''1-fifo_cache'''
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """A caching system"""

    def __init__(self):
        '''inherits from the parent class'''
        super().__init__()

    def put(self, key, item):
        '''Sets an item in the cache_data dict'''
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS and \
                key not in self.cache_data:
            oldest_key = next(iter(self.cache_data))
            print(f"DISCARD: {oldest_key}")
            self.cache_data.pop(oldest_key)
        self.cache_data[key] = item

    def get(self, key):
        '''retrieve an item by key'''
        try:
            return self.cache_data[key]
        except KeyError:
            return None
