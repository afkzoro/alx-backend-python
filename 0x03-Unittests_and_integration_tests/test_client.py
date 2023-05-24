#!/usr/bin/env python3
"""
Unit tests for the GithubOrgClient class.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from unittest import TestCase
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """
    Test class for the GithubOrgClient.
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test the org method of GithubOrgClient.

        Args:
            org_name (str): The organization name.
            mock_get_json (Mock): The mocked get_json function.

        """
        test_payload = {"org": org_name}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, test_payload)

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    @patch('client.get_json')
    @patch.object(GithubOrgClient, '_public_repos_url',
                  new_callable=PropertyMock)
    def test_public_repos(self, mock_url, mock_get_json):
        """
        Test the public_repos method of GithubOrgClient.

        Mocks the get_json function and the _public_repos_url property to
        provide expected results.

        Verifies that the list of repositories returned by the public_repos
        method matches the expected list.

        Also checks that the mocked property and the mocked get_json function
        were called once.
        """
        known_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]

        mock_get_json.return_value = known_payload
        mock_url.return_value = "https://api.github.com/orgs/google/repos"

        org_name = "google"
        client = GithubOrgClient(org_name)

        repos = client.public_repos()
        expected_repos = [repo["name"] for repo in known_payload]
        self.assertEqual(repos, expected_repos)

        mock_url.assert_called_once()
        mock_get_json.assert_called_once()


if __name__ == '__main__':
    unittest.main()
