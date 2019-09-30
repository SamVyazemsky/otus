import pytest
from parallelrun.application import Application
from parallelrun.my_test import TestSuit

@pytest.fixture(scope='session')
def app():
    return Application('chrome')
    print("test chrome")