#!/usr/bin/env python3
"""LIFO caching system"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system"""

    def __init__(self):
        """Initialize cache"""
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """Assign to the dictionary self.cache_data the
        item value for the key key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.last_key = key
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del self.cache_data[self.last_key]
            print(f"DISCARD: {self.last_key}")
            self.last_key = key

    def get(self, key):
        """Return the value in self.cache_data linked to key"""
        if key is None:
            return None
        return self.cache_data.get(key)
