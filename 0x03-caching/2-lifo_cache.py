#!/usr/bin/python3
"""
2. LIFO Caching
"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """
    Args:
        BaseCaching: Base class
    """
    def __init__(self):
        """
        init
        """
        super().__init__()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data
        the item value for the key [key]
        """
        if key is None or item is None:
            pass
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard = sorted(self.cache_data.keys())
            self.cache_data.pop(discard[-2])
            print("DISCARD: {}".format(discard[-2]))

    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        else:
            return self.cache_data.get(key)
