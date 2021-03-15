#!/usr/bin/env python3
"""
multiplies a float by given multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Args:
        multiplier: float
    Returns:
        fn that multiplie float by a multiplier
    """
    return lambda x: x * multiplier
