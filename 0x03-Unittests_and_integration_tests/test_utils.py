#!/usr/bin/env python3
"""
a module for testing access_nested_map function
"""
from parameterized import parameterized
import unittest
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock


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
        @patch("utils.requests.get")
        def test_get_json(self, moke_get_json):
            """
            fucntion for testing get_json function
            """
            test_cases = [
                            ("http://example.com", {"payload": True}),
                            ("http://holberton.io", {"payload": False})
                        ]
            for test_url, test_payload in test_cases:
                moke_response = Mock()
                moke_response.json.return_value = test_payload
                moke_get_json.return_value = moke_response
                result = get_json(test_url)
                moke_get_json.assert_called_with(test_url)
                self.assertEqual(test_payload, result)
