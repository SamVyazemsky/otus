import mock
import requests
import unittest

from Lesson32.example2.client import MyAPIClient


class CustomHTTPException(Exception):
    pass


class CustomConnException(Exception):
    pass


class ClientTestCase(unittest.TestCase):

    def setUp(self):

        self.client = MyAPIClient()

    @mock.patch('client.requests.get')
    def test_get_ok(self, mock_get):
        """
        Test getting a 200 OK response from the _get method of MyAPIClient.
        """
        # Construct our mock response object, giving it relevant expected
        # behaviours
        mock_response = mock.Mock()
        expected_dict = {
            "breeds": [
                "pembroke",
                "cardigan",
            ]
        }
        mock_response.json.return_value = expected_dict

        # Assign our mock response as the result of our patched function
        mock_get.return_value = mock_response

        url = 'http://api.corgidata.com/breeds/'
        response_dict = self.client._get(url=url)

        # Check that our function made the expected internal calls
        mock_get.assert_called_once_with(url=url)
        self.assertEqual(1, mock_response.json.call_count)

        # If we want, we can check the contents of the response
        self.assertEqual(response_dict, expected_dict)

    @mock.patch('client.MyAPIClient._handle_http_error')
    @mock.patch('client.requests.get')
    def test_get_http_error(self, mock_get, mock_http_error_handler):
        """
        Test getting a HTTP error in the _get method of MyAPIClient.
        """
        # Construct our mock response object, giving it relevant expected
        # behaviours
        mock_response = mock.Mock()
        http_error = requests.exceptions.HTTPError()
        mock_response.raise_for_status.side_effect = http_error

        # Assign our mock response as the result of our patched function
        mock_get.return_value = mock_response

        # Make our patched error handler raise a custom exception
        mock_http_error_handler.side_effect = CustomHTTPException()

        url = 'http://api.corgidata.com/breeds/'
        with self.assertRaises(CustomHTTPException):
            self.client._get(url=url)

        # Check that our function made the expected internal calls
        mock_get.assert_called_once_with(url=url)
        self.assertEqual(1, mock_response.raise_for_status.call_count)

        # Make sure we did not attempt to deserialize the response
        self.assertEqual(0, mock_response.json.call_count)

        # Make sure our HTTP error handler is called
        mock_http_error_handler.assert_called_once_with(http_error)

    @mock.patch('client.MyAPIClient._handle_connection_error')
    @mock.patch('client.requests.get')
    def test_get_connection_error(self, mock_get, mock_conn_error_handler):
        """
        Test getting a persistent connection error in the _get method of
        MyAPIClient.
        """
        # Make our patched `requests.get` raise a connection error
        conn_error = requests.exceptions.ConnectionError()
        mock_get.side_effect = conn_error

        # Make our patched error handler raise a custom exception
        mock_conn_error_handler.side_effect = CustomConnException()

        url = 'http://api.corgidata.com/breeds/'
        with self.assertRaises(CustomConnException):
            self.client._get(url=url)

        # Check that our function made the expected internal calls
        expected_calls = [mock.call(url=url)] * 3
        self.assertEqual(expected_calls, mock_get.call_args_list)

        # Make sure our connection error handler is called
        mock_conn_error_handler.assert_called_once_with(conn_error)

    @mock.patch('client.requests.get')
    def test_get_connection_error_then_success(self, mock_get):
        """
        Test getting a connection error, then a successful response,
        in the _get method of MyAPIClient.
        """
        # Construct our mock response object for the success case
        mock_response = mock.Mock()
        expected_dict = {
            "breeds": [
                "pembroke",
                "cardigan",
            ]
        }
        mock_response.json.return_value = expected_dict

        # Make an instance of ConnectionError for our failure case
        conn_error = requests.exceptions.ConnectionError()

        # Give our patched get a list of behaviours to display
        mock_get.side_effect = [conn_error, conn_error, mock_response]

        url = 'http://api.corgidata.com/breeds/'
        response_dict = self.client._get(url=url)

        # Check that our function made the expected internal calls
        expected_calls = [mock.call(url=url)] * 3
        self.assertEqual(expected_calls, mock_get.call_args_list)
        self.assertEqual(1, mock_response.json.call_count)

        # Check the result
        self.assertEqual(response_dict, expected_dict)


if __name__ == "__main__":
    unittest.main()
