import pytest


@pytest.fixture()
def before():
    print('\nbefore each test')


def test_1(before):
    print('test_1()')


def test_2(before):
    print('test_2()')


##########################################
@pytest.mark.usefixtures("before")
def test_1():
    print('test_1()')


@pytest.mark.usefixtures("before")
def test_2():
    print('test_2()')

###########################################


class Test:
    @pytest.mark.usefixtures("before")
    def test_1(self):
        print('test_1()')

    @pytest.mark.usefixtures("before")
    def test_2(self):
        print('test_2()')

##########################################


@pytest.mark.usefixtures("before")
class Test:
    def test_1(self):
        print('test_1()')

    def test_2(self):
        print('test_2()')