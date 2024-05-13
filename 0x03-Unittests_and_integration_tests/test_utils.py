#!/usr/bin/env python3
"""
a module for testing access_nested_map function
"""
from parameterized import parameterized
import unittest
from utils import access_nested_map, get_json, memoize
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
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("requests.get")
    def test_get_json(self, input, expected, mock_get_json):
        """
        function for testing get_json function
        """
        mock_response = Mock()
        mock_response.json.return_value = expected
        mock_get_json.return_value = mock_response
        result = get_json(input)
        mock_get_json.assert_called_with(input)
        self.assertEqual(result, expected)


class TestMemoize(unittest.TestCase):
    """
    class for testing memoire function
    """
    class TestClass:
        """
        class for testing memoire function
        """
        def a_method(self):
            """
            method that returns 42
            """
            return 42

        @memoize
        def a_property(self):
            """
            property
            """
            return self.a_method()

        @patch("__main__.TestMemoize.TestClass.a_method")
        def test_memoize(self, mock_a_method):
            """
            function to test memoize function
            """
            test_instance = self.TestClass()
            mock_a_method.return_value = 42
            result1 = test_instance.a_property()
            result2 = test_instance.a_property()
            mock_a_method.assert_called_once()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == "__main__":
    unittest.main()
