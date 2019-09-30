import pytest


@pytest.fixture(scope="function")
def test_t():

    type(b)
    print(b)
    for i in b:
        print(i)
        assert i % 2 == 0
    # b.__next__()
    # for i in b:
    #     print(b, end=' ')
