#!/usr/bin/env python3
"""LFU caching system"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU caching system"""

    def __init__(self):
        """Initialize cache"""
        super().__init__()
        self.usage_frequency = {}
        self.order = []

    def put(self, key, item):
        """Assign to the dictionary self.cache_data
        the item value for the key key"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.usage_frequency[key] += 1
        else:
            self.usage_frequency[key] = 1
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_keys = [k for k, v in sorted(self.usage_frequency.items(), key=lambda item:(item[1], self.order.index(item[0])))]
                lfu_key = lfu_keys[0]
                del self.cache_data[lfu_key]
                del self.usage_frequency[lfu_key]
                self.order.remove(lfu_key)
                print(f"DISCARD: {lfu_key}")
        self.cache_data[key] = item
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)

    def get(self, key):
        """Return the value in self.cache_data linked to key"""
        if key is None:
            return None
        if key in self.cache_data:
            self.usage_frequency[key] += 1
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
