#!/usr/bin/env python3
""" Task-11 Given the parameters and
the return values, add type annotations to the function
"""
from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')  # Value Type


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """_summary_

    Args:
        dct (Mapping): _description_
        key (Any): _description_
        default (Union[T, None], optional): _description_. Defaults to None.

    Returns:
        Union[Any, T]: _description_
    """
    if key in dct:
        return dct[key]
    else:
        return default
