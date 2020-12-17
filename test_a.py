import pytest


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5


def test_answer2():
    assert func(4) == 5


@pytest.mark.parametrize('a,b', [(1, 2), (3, 8), ('a1', 'b1')])
def test_myanswaer(a, b):
    assert func(a) == b


@pytest.fixture()
def login():
    print("登录")
    username = 'wangjan'
    return username


class Testwj:
    def test_a(self, login):
        print(f"a  emmmmmmmmmmmm{login}")

    def test_b(self):
        print("b")

    def test_c(self):
        print("c")
