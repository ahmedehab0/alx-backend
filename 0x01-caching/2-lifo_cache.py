#!/usr/bin/python3
"""lifo caching"""


BaseCaching = __import__('base_caching').BaseCaching

class LIFOCache(BaseCaching):
    """lifo caching replacement system"""
    def put(self, key, item):
        """write to cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS and key not in self.cache_data:
                last_key = self.cache_data.popitem()
                print("DISCARD: {}".format(last_key[0]))
            self.cache_data[key] = item

    def get(self, key):
        """read from the cache"""
        if key in self.cache_data:
            return self.cache_data[item]
        return None
