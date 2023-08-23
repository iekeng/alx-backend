#!/usr/bin/env python3

BaseCaching=__import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            wanted_key = list(self.cache_data)[0]
            self.cache_data.pop(wanted_key)
            print(f"DISCARD {wanted_key}")
    
    def get(self, key):
        try:
            return self.cache_data[key]
        except KeyError:
            return None
