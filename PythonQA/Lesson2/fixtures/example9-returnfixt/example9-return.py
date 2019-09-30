import pytest


@pytest.fixture()
def some_data():
    data = {'foo': 1, 'bar': 2, 'baz': 3}
    return data


def test_foo(some_data):
    print(some_data)
    assert some_data['foo'] == 1
