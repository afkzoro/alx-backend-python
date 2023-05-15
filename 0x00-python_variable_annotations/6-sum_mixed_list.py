#!/usr/bin/env python3
""" Task-6 Sums a list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Sums a list made up of ints and floats
    Then returns a float
    """
    return sum(mxd_lst)
