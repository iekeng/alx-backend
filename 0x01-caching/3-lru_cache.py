#!/usr/bin/env python3
'''3-lru_cache'''

BaseCaching = __import__('base_caching').BaseCaching

class LRUCache(BaseCaching):
    '''Implements the Least Recently Used
    cache replacement policy'''
    def __init__(self):
        super().__init__()
        self.tracker = []

    def put(self, key, item):
        '''Sets items in cache_data dict'''
        if key is None or item is None:
            return

        elif len(self.cache_data) >= self.MAX_ITEMS\
                    and key not in self.cache_data:
                print(f'DISCARD: {self.tracker[0]}')  
                self.cache_data.pop(self.tracker[0])
                self.tracker.pop(0)

        elif key in self.tracker:
            self.cache_data[key] = item
            self.tracker.pop(self.tracker.index(key))

        self.tracker.append(key)
        self.cache_data[key] = item


    def get(self, key):
        '''Retrieves cache_data dict'''
        try:
            if key in self.tracker:
                self.tracker.pop(self.tracker.index(key))
                self.tracker.append(key)
            return self.cache_data[key]
        except KeyError:
            return None
