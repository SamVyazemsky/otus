import pytest


@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 42),
], ids=["3+5", "2+4", "6*9"])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
