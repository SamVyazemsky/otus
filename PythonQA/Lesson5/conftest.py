from parallelrun.application import Application
import pytest
from parallelrun.my_test import TestSuit


@pytest.fixture(scope='session')
def app(browser_name):
    return Application(browser_name)