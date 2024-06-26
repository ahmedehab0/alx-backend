#!/usr/bin/env python3
"""LRU caching"""


BaseCaching = __import__('base_caching').BaseCaching

class MRUCache(BaseCaching):
    """lru caching system"""
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """write to cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.order.remove(key)
                self.order.append(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    lru_key = self.order.pop()
                    del self.cache_data[lru_key]
                    print("DISCARD: {}".format(lru_key))
                self.cache_data[key] = item
                self.order.append(key)
    def get(self, key):
        """read from cache"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
