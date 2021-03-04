# -*- coding: utf-8 -*-
import pytest
import yaml


def func(x):
    return x + 1


@pytest.mark.parametrize("x, y", yaml.safe_load(open("data.yml")))
def test_myyaml(x, y):
    assert func(x) == y


@pytest.mark.parametrize("x", [1, 2, 3])
@pytest.mark.parametrize("y", [11, 22, 33])
def test_twoele(x, y):
    print(x, "和", y)

def test_answer():
    assert func(3) == 5


def test_answer2():
    assert func(4) == 5


@pytest.mark.parametrize('a,b', [(1, 2), (3, 8), ('a1', 'b1')])
def test_myanswaer(a, b):
    assert func(a) == b


@pytest.mark.parametrize('a,b', [(1, 2), (3, 8), ('a1', 'b1')], ids=["第1组测试数据", "第2组测试数据", "第3组测试数据"])
def test_myanswaer2(a, b):
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
