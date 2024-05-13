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
        """Test TestGithubOrgClient.public_repos_url
        return the correct value based on the given payload
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "something"}
            mock.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])
