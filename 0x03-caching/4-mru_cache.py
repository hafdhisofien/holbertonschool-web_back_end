#!/usr/bin/python3
"""
4. MRU Caching
"""
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """
    Args:
        BaseCaching: Base class
    """
    LRUkeys = []

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
        if key not in self.LRUkeys:
            self.LRUkeys.append(key)
        else:
            self.LRUkeys.append(self.LRUkeys.pop(self.LRUkeys.index(key)))
        if len(self.LRUkeys) > BaseCaching.MAX_ITEMS:
            discard = self.LRUkeys.pop(-2)
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))

    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        else:
            self.LRUkeys.append(self.LRUkeys.pop(self.LRUkeys.index(key)))
            return self.cache_data.get(key)
