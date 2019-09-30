import unittest
from Lesson32.example_basic.main import api


class TestApi(unittest.TestCase):

    def test_api(self):
        assert api().status_code == 200
