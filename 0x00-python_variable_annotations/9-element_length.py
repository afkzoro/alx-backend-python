#!/usr/bin/env python3
""" Task-9 Annotate the below function’s
parameters and return values with the appropriate types"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence[str]]) -> List[
 Tuple[Sequence[str], int]]:
    """ Well annotated function
    """
    return [(i, len(i)) for i in lst]


print(element_length.__annotations__)