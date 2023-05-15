#!/usr/bin/env python3
""" Task-12 Use mypy to validate the
following piece of code and apply any necessary changes
"""
from typing import List, Tuple, Union


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """_summary_

    Args:
        lst (Tuple[int, ...]): _description_
        factor (int, optional): _description_. Defaults to 2.

    Returns:
        Tuple[int, ...]: _description_
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return tuple(zoomed_in)


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)