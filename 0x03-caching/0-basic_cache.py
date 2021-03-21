#!/usr/bin/python3
"""
0. Basic dictionary
"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    Args:
        BaseCaching: Base class
    Returns:
        Value in self.cache_data linked to key
        None if key is none or dosen't exist
    """
    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value for the key key
        """
        if key and item:
            self.cache_data[key] = item
        else:
            pass
    
    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist return none.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data.get(key)