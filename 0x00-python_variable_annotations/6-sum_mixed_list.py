#!/usr/bin/env python3
"""
sum a mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Args:
        mxd_lst : mixed list of ints & floats
    Returns:
        sum of given mixed list
    """
    return sum(mxd_lst)
