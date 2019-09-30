import unittest
import pytest


class BetaTest(unittest.TestCase):
    def test_unit_beta_1(self):
        print('\nIn test_unit_beta_1()')

    @pytest.mark.usefixtures('some_resource')
    def test_unit_beta_2(self):
        print('\nIn test_unit_beta_2()')
