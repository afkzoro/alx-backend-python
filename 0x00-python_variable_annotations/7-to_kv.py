#!/usr/bin/env python3
""" Task-7 Takes two arguments and
returns a Tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Function takes a string k
    and an int or float value v
    Returns a tuple
    """
    return k, float(v ** 2)
