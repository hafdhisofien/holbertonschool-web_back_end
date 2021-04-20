#!/usr/bin/env python3
"""
Test module
"""
import client
from client import GithubOrgClient
from unittest import TestCase, mock
from unittest.mock import patch, Mock
from parameterized import parameterized


class TestGithubOrgClient(TestCase):
    """
    Testing the class
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, answer):
        """
        method to test that the method returns what it is supposed to.
        """
        self.assertEqual(access_nested_map(nested_map, path), answer)
