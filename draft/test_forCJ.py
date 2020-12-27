import pytest


@pytest.mark.flaky(reruns=6, reruns_delay=2)
def test_one():
    assert 1 == 3


def test_simple_assume():
    pytest.assume(1 == 2)
    pytest.assume(3 == 4)
    pytest.assume(False)
