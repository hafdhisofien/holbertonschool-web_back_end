#!/usr/bin/env python3
"""
Exercise
"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from sys import byteorder
from functools import wraps


def count_calls(method: Callable = None) -> Callable:
    """
    takes a single method Callable argument and returns a Callable
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        increments the count for that key every time the method is called
        Returns the value returned by the original method
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    store the history of inputs and outputs for a particular function.
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        create input and output list keys
        """
        input: str = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)

        return output

    return wrapper

    def replay(func: Callable):
        """
         display the history of calls of a particular function.
        """
        r_db = redis.Redis()
        key = method.__qualname__
        calls = r_db.get(key)

        inputs_list = method.self._redis.lrange(inputs, 0, -1)
        outputs_list = mehtod.self._redis.lrange(outputs, 0, -1)

        print(f'{key} was called {calls} times:')


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

    @call_history
    @count_calls
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
