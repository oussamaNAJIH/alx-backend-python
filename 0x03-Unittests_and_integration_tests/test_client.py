#!/usr/bin/env python3
"""
a module for testing client.GithubOrgClient
"""
from parameterized import parameterized
import unittest
from unittest.mock import Mock, PropertyMock, patch
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """
    class for testing GithubOrgClient
    """
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input, mock_get_json):
        """
        function for testing GithubOrgClient
        """
        test_instance = GithubOrgClient(input)
        test_instance.org()
        mock_get_json.called_with_once(test_instance.ORG_URL.format(org=input))

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        function to test _public_repos_url
        """
        mock_org.return_value = {"repos_url": "http://repos.com"}
        test_instance = GithubOrgClient("exmp")
        result = test_instance._public_repos_url
        mock_org.assert_called_once_with()
        self.assertEqual(result, "http://repos.com")
