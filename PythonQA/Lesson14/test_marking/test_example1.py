import pytest


@pytest.mark.webtest
def test_send_http():
    pass # perform some webtest test for your app


def test_something_quick():
    pass


def test_another():
    pass


class TestClass(object):
    def test_method(self):

        pass

# Run marked tests
# pytest -v -m webtest
# pytest -v -m "not webtest"
# Using -k expr to select tests based on their name
# pytest -v -k http
# pytest -k "not send_http" -v
# pytest -k "http or quick" -v
# 
