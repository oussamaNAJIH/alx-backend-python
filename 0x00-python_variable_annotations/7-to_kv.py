#!/usr/bin/env python3
"""
Write a type-annotated function to_kv that takes a string k and an
int OR float v as arguments and returns a tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """
    takes a string k and an int OR float v as arguments and returns a tuple
    The first element of the tuple is the string k. The second element is
    the square of the int/float v and should be annotated as a float
    """
    return k, float(v ** 2)
