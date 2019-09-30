import unittest
from mock import Mock
from mock import patch
import requests
import unittest

from Lesson32.example_basic.main import api


class TetsApi(unittest.TestCase):

    def test_api(self):
        with patch.object(requests, 'get') as get_mock:
            get_mock.return_value = mock_response = Mock()
            mock_response.status_code = 200
            assert api().status_code == 200
