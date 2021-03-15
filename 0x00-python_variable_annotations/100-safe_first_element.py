#!/usr/bin/env python3
"""
duck-typed annotations
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Args:
        lst: list of different types
    Returns:
        first element of list otherwise none
    """
    if lst:
        return[0]
    else:
        return none
