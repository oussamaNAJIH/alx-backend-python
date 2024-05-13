#!/usr/bin/env python3
"""
a module for testing client.GithubOrgClient
"""
from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch
from client import GithubOrgClient
from utils import get_json


from unittest.mock import patch, Mock

class TestGithubOrgClient(unittest.TestCase):
    """
    class for testing GithubOrgClient
    """
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock):
        """Test TestGithubOrgClient.org return the correct value
        """
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock.called_with_once(test_class.ORG_URL.format(org=org_name))
