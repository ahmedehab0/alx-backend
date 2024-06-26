#!/usr/bin/python3
"""Basic dictionary"""


BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """Basic caching system"""
    def put(self, key, item):
        """write to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """read from cache"""
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
