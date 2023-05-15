#!/usr/bin/env python3
""" Task-12 Use mypy to validate the
following piece of code and apply any necessary changes
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """_summary_

    Args:
        lst (Tuple): _description_
        factor (int, optional): _description_. Defaults to 2.

    Returns:
        List[int]: _description_
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
