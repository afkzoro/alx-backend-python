#!/usr/bin/env python3

"""
Module: utils
A collection of utility functions.
"""

from typing import Any, Dict, Tuple
import unittest
from parameterized import parameterized
from unittest.mock import patch
from utils import get_json, memoize
from testclass import TestClass


class TestGetJson(unittest.TestCase):
    """
    Unit tests for the get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test the get_json function with mocked requests.get.
        """
        mock_get.return_value.json.return_value = test_payload

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


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
    except (KeyError, TypeError) as e:
        raise KeyError(f"Key not found: {path}") from e


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
        self.assertEqual(str(cm.exception), repr(f"Key not found: {path}"))


class TestMemoize(unittest.TestCase):
    """
    Unit tests for the memoize decorator.
    """

    @patch('testclass.TestClass.a_method')
    def test_memoize(self, mock_a_method):
        """
        Test the memoize decorator.
        """
        mock_a_method.return_value = 42

        test_instance = TestClass()

        # First call to a_property
        result1 = test_instance.a_property
        # Second call to a_property
        result2 = test_instance.a_property

        mock_a_method.assert_called_once()
        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)


if __name__ == "__main__":
    unittest.main()
