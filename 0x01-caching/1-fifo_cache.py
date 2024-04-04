#!/usr/bin/python3
""" BaseCaching module"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """BaseCaching class"""

    def __init__(self):
        """BaseCaching init"""
        super().__init__()

    def put(self, key, item):
        """BaseCaching put"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = next(iter(self.cache_data))
                self.cache_data.pop(removed)
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item

    def get(self, key):
        """BaseCaching get"""
        return self.cache_data.get(key)
