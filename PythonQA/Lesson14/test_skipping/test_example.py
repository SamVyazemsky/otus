import pytest
import sys

if not sys.platform.startswith("win"):
    pytest.skip("skipping windows-only tests", allow_module_level=True)


@pytest.mark.skipif(sys.platform == "win32", reason="does not run on windows")
class TestPosixCalls(object):
    def test_function(self):
        """will not be setup or run under 'win32' platform"""


@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown():
    pass


def test_function():
    try:
        pytest.skip("unsupported configuration")
    except BlockingIOError:
        print('')
    except KeyboardInterrupt:
        print('keyboard')
    finally:
        pass



@pytest.mark.skipif(sys.version_info < 3.6, reason="requires python3.6 or higher")
def test_function():
    pass


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (1, 2),
        pytest.param(1, 0, marks=pytest.mark.xfail),
        pytest.param(1, 3, marks=pytest.mark.xfail(reason="some bug")),
        (2, 3),
        (3, 4),
        (4, 5),
        pytest.param(
            10, 11, marks=pytest.mark.skipif(sys.version_info >= (3, 0), reason="py2k")
        ),
    ],
)
def test_increment(n, expected):
    assert n + 1 == expected






