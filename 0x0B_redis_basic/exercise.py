#!/usr/bin/env python3
"""
Exercise
"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional


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

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float]:
        """
        Args:
            key: string argument
            fn: optional Callable argument
        Returns:
            callable will convert the data back to the desired format
            else
            conserve the original Redis.get behavior if the key does not exist.
        """
        key = self._redis.get(key)

        if fn:
            key = fn(key)
        return key

    def get_str(self, data: bytes) -> str:
        """
        automatically parametrize Cache.get
        """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """
        automatically parametrize Cache.get
        """
        return int.from_bytes(data, byteorder)
