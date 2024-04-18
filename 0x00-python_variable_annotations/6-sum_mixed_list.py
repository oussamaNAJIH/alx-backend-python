#!/usr/bin/env python3
"""
Write a type-annotated function sum_mixed_list which takes a list mxd_lst of
integers and floats and returns their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
     takes a list input_list of floats and integers as argument
     and returns their sum as a float
    """
    sum: float = 0
    for num in mxd_lst:
        sum += num
    return sum
