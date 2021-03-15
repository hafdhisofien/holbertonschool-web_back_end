#!/usr/bin/env python3
"""
validate the following piece of code and apply any necessary changes using mypy
"""
from typing import Any, Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Args:
        lst: tuple
        factor: int that defaults to 2
    Returns:
        variable annotation of a list
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array)), int(3.0)
