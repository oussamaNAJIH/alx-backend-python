#!/usr/bin/env python3
"""
a module for testing client.GithubOrgClient
"""
from parameterized import parameterized
import unittest
from unittest.mock import mock, patch
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("utils.get_json")
    def test_org(self, input, mock_org):
        test_instance = GithubOrgClient(input)
        result = test_instance.org()
        mock_org.assert_called_once_with(f"https://api.github.com/orgs/{input}")
