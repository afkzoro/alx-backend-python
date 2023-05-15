#!/usr/bin/env python3
""" Task-100 Augment the following code
with the correct duck-typed annotations
"""
from typing import Any, Optional, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Fixed the
 safe_first_element function
 """
    if lst:
        return lst[0]
    else:
        return None
