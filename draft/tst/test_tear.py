# -*- coding: utf-8 -*-
# 创建时间：2020/12/22 0:16
import pytest


def setup_module(self):
    print("")
    print("这是方法setup_module的输出")


def teardown_module(self):
    print("这是方法teardown_module的输出")


def setup_function(self):
    print("")
    print("这是方法setup_function的输出")


def teardown_function(self):
    print("这是方法teardown_function的输出")


def test_out():
    print("")
    print("用例out开始执行")


def test_out2():
    print("")
    print("用例out2开始执行")


@pytest.fixture()
def login():
    print("登录")
    username = 'wangjan'
    return username


class TestUPDM:
    def setup_class(self):
        print("")
        print("这是方法setup_class的输出")

    def teardown_class(self):
        print("这是方法teardown_class的输出")

    def setup_method(self):
        print("")
        print("这是方法setup_method的输出")

    def teardown_method(self):
        print("这是方法teardown_method的输出")

    def setup(self):
        print("这是方法setup的输出")

    def teardown(self):
        print("这是方法teardown的输出")

    @pytest.mark.parametrize("a", [11, 22])
    def test_a(self, a):
        print("")
        print("用例A开始执行，参数是：", a)

    def test_b(self, login):
        print("")
        print(f"调用fixture方法：{login}")
        print("用例b开始执行")
