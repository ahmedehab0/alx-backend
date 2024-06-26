#!/usr/bin/env python3
"""fifo caching"""


BaseCaching = __import__('base_caching').BaseCaching

class FIFOCache(BaseCaching):
    """fifo caching system"""
    def put(self, key, item):
        """write to the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS and key not in self.cache_data:
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print("DISCARD: {}".format(first_key))
            self.cache_data[key] = item
    def get(self, key):
        """read from cache"""
        if key:
            return self.cache_data[key]
        return None
