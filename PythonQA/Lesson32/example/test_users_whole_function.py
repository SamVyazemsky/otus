import unittest
from unittest.mock import patch, Mock
from Lesson32.example.users import get_users


class BasicTests(unittest.TestCase):
    def test_mock_whole_function(self):
        """Mocking a whole function"""
        mock_get_patcher = patch('users.requests.get')
        users = [{
            "id": 0,
            "first_name": "Dell",
            "last_name": "Norval",
            "phone": "994-979-3976"
        }]

        # Start patching 'requests.get'.
        mock_get = mock_get_patcher.start()

        # Configure the mock to return a response with status code 200 and a list of users.
        mock_get.return_value = Mock(status_code = 200)
        mock_get.return_value.json.return_value = users

        # Call the service, which will send a request to the server.
        response = get_users()

        # Stop patching 'requests'.
        mock_get_patcher.stop()

        # Assert that the request-response cycle completed successfully.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), users)


if __name__ == "__main__":
    unittest.main()
