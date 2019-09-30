import pytest


@pytest.fixture(scope="module")
def foo(request):
    print('\nfoo setup - module fixture')

    def fin():
        print('foo teardown - module fixture')

    request.addfinalizer(fin)


@pytest.fixture()
def bar(request):
    print('bar setup - function fixture')

    def fin():
        print('bar teardown - function fixture')

    request.addfinalizer(fin)


@pytest.fixture()
def baz(request):
    print('baz setup - function fixture')

    def fin():
        print('baz teardown - function fixture')

    request.addfinalizer(fin)


def test_one(foo, bar, baz):
    print('in test_one()')


def test_two(foo, bar, baz):
    print('in test_two()')
