#!/usr/bin/env python3
""" Task-8 type-annotated function make_multiplier """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function
    that multiplies a float by func
    multiplier
    """
    def multiplier_fn(number: float) -> float:
        return number * multiplier
    return multiplier_fn
