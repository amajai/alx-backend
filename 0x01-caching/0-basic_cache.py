#!/usr/bin/python3
"""
BaseCaching module
"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """BaseCaching class"""

    def put(self, key, item):
        """BaseCaching put"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """BaseCaching get"""
        return self.cache_data.get(key)
