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

    def test_public_repos_url(self):
        """
        function to test _public_repos_url
        """
        with patch("client.org",
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "http://repos.com"}
            test_instance = GithubOrgClient("exmp")
            result = test_instance._public_repos_url
            mock_org.assert_called_once_with()
            self.assertEqual(result, "http://repos.com")

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
        function to test public_repos
        """
        with patch("client._public_repos_url") as mock:
            mock.return_value = "http://repos.com"
            

