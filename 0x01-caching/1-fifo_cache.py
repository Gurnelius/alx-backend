#!/usr/bin/env python3
'''FIFO caching system'''

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system"""

    def __init__(self):
        """Initialize cache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Assign to the dictionary self.cache_data the
        item value for the key key"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            self.order.append(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """Return the value in self.cache_data linked to key"""
        if key is None:
            return None
        return self.cache_data.get(key)
