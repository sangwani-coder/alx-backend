#!/usr/bin/env python3
""" fifo_cache"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ fificache algorithm"""
    def __init__(self):
        """ constructor"""
        self.store_keys = []
        super().__init__()

    def put(self, key, item):
        """ assigns item to a dicitoanry for key key"""
        if key is not None and item is not None:
            if len(self.cache_data) == self.MAX_ITEMS:
                oldest = self.store_keys[0]
                del self.cache_data[oldest]
                print('DISCARD:', oldest)
                self.store_keys.pop(0)
            self.store_keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """returns a value from self._cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
