import application
import pytest
from parallelrun.my_test import TestSuit


@pytest.fixture(scope='session')
def app():
    return application.Application('firefox')