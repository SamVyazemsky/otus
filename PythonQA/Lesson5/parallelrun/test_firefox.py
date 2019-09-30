from parallelrun.application import Application
import pytest
from parallelrun.my_test import TestSuit


@pytest.fixture(scope='session')
def app():
    return Application('firefox')
    print("test firefox")
