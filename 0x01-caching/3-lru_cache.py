#!/usr/bin/env python3
"""LIFO caching system"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU caching system"""

    def __init__(self):
        """Initialize cache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Assign to the dictionary self.cache_data the
        item value for the key key"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Return the value in self.cache_data linked to key"""
        if key is None:
            return None
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
