#!/usr/bin/python3
""" BaseCaching module """
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """BaseCaching class"""

    def __init__(self):
        """BaseCaching init """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """BaseCaching put"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = self.order.pop(0)
                self.cache_data.pop(removed)
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """BaseCaching get"""
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data.get(key)
