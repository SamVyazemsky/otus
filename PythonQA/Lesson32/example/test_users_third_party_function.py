import unittest
from unittest.mock import patch, Mock
from Lesson32.example.users import get_users


class BasicTests(unittest.TestCase):
    @patch('users.get_users')
    def test_get_one_user(self, mock_get_users):
        """
        Test for getting one user using their userID
        Demonstrates mocking third party functions
        """
        users = [
            {'phone': '514-794-6957', 'first_name': 'Brant', 'last_name': 'Mekhi', 'id': 0},
            {'phone': '772-370-0117', 'first_name': 'Thalia', 'last_name': 'Kenyatta', 'id': 1},
            {'phone': '176-290-7637', 'first_name': 'Destin', 'last_name': 'Soledad', 'id': 2}
        ]
        mock_get_users.return_value = Mock()
        mock_get_users.return_value.json.return_value = users
        user = get_users(2)
        self.assertEqual(user, users[2])


if __name__ == "__main__":
    unittest.main()
