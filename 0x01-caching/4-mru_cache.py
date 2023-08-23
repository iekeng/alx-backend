#!/usr/bin/env python3
'''4-mru_cache'''

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    '''Implements Most Recently Used cache policy'''

    def __init__(self):
        '''inherits from super class'''
        super().__init__()
        self.tracker = []

    def put(self, key, item):
        '''Sets item for cache_data dict'''
        if key is None or item is None:
            return

        elif len(self.cache_data) >= self.MAX_ITEMS\
                and key not in self.cache_data:
            print(f'DISCARD {self.tracker[-1]}')
            self.cache_data.pop(self.tracker[-1])
            self.tracker.pop(-1)

        self.tracker.append(key)
        self.cache_data[key] = item

    def get(self, key):
        '''Retrive item for cache_data dict'''
        try:
            if key in self.cache_data:
                self.tracker.pop(self.tracker.index(key))
                self.tracker.append(key)
            return self.cache_data[key]
        except KeyError:
            return None
