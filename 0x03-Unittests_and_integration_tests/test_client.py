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

    def test_public_repos_url(self):
        # Define a known payload to be returned by the mocked org property
        known_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos"
            }

        with patch.object(GithubOrgClient, "org",
                          new_callable=PropertyMock) as mock_org:

            mock_org.return_value = known_payload

            org_name = "google"
            client = GithubOrgClient(org_name)
            expected_url = known_payload["repos_url"]
            self.assertEqual(client._public_repos_url, expected_url)


if __name__ == '__main__':
    unittest.main()
