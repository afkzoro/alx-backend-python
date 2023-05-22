#!/usr/bin/env python3

"""
Module: utils
A collection of utility functions.
"""

from typing import Any, Dict, Tuple
import unittest
from parameterized import parameterized


def access_nested_map(nested_map: Dict[str, Any], path: Tuple[str]) -> Any:
    """
    Access a nested value in a dictionary based on a given path.
    Args:
        nested_map (Dict[str, Any]): The nested dictionary.
        path (Tuple[str]): The path to the value.

    Returns:
        Any: The value at the specified path.
    """
    try:
        for key in path:
            nested_map = nested_map[key]
        return nested_map
    except (KeyError, TypeError):
        raise


class TestAccessNestedMap(unittest.TestCase):
    """
    Unit tests for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test the access_nested_map function.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)


if __name__ == "__main__":
    unittest.main()
