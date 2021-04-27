#!/usr/bin/env python3
"""
Web
"""
import redis
from typing import Union, Callable, Optional
from functools import wraps
import requests


def count_calls(method: Callable = None) -> Callable:
    """
    takes a single method Callable argument and returns a Callable
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(url):
        """
        obtain the HTML content of a particular URL and returns it
        """
        self._redis.incr(f"count:{url}")
        html_c = self._redis.get(f"cached:{url}")
        if html_c:
            return html_c.decode('utf-8')

        html = method(url)
        self._redis.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_calls
def get_page(url: str) -> str:
    """
    times a particular URL was accessed in the key "count:{url}"
    cache the result with an expiration time of 10 seconds.
    """
    return requests.get(url).text
