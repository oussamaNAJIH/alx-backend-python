#!/usr/bin/env python3
"""
a module for testing access_nested_map function
"""
from parameterized import parameterized
import unittest
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock
from typing import Any, Dict, List, Tuple


class TestAccessNestedMap(unittest.TestCase):
    """
    class for testing access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        funntion for testing access_nested_map function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        funntion for testing errors raised by
        access_nested_map function
        """
        self.assertRaises(expected, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    class for testing get_json function
    """
    @patch("requests.get")
    def test_get_json(self, mock_get_json: Any) -> None:
        """
        Function for testing get_json function
        """
        test_cases: List[Tuple[str, Dict[str, Any]]] = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
            ]
        for test_url, test_payload in test_cases:
            mock_response: Mock = Mock()
            mock_response.json.return_value = test_payload
            mock_get_json.return_value = mock_response
            result: Dict[str, Any] = get_json(test_url)
            mock_get_json.assert_called_with(test_url)
            self.assertEqual(test_payload, result)


if __name__ == "__main__":
    unittest.main()
