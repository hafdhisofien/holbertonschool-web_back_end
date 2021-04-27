#!/usr/bin/env python3
"""
Exercise
"""
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """
    Class for caching methods
    """
    def __init__(self):
        """
        Constructer
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        generate a random key
        store the input data in Redis using the random key.
        Return the key
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
