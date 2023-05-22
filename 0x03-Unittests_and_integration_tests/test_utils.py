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

    Raises:
        KeyError: If the specified path is not found in the nested dictionary.
    """
    try:
        for key in path:
            nested_map = nested_map[key]
        return nested_map
    except (KeyError, TypeError):
        raise KeyError(f"Key not found: {path}")


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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test that KeyError is raised for invalid paths.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), f"Key not found: {path}")


if __name__ == "__main__":
    unittest.main()
