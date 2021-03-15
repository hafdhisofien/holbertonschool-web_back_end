#!/usr/bin/env python3
"""
tuple of a string and a int/float
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Args:
        k: str
        v: union of ints or floats
    Returns:
        tuple of k & v
    """
    return (k, v * v)
