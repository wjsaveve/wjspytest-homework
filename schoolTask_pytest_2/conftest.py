# -*- coding: utf-8 -*-
# 创建时间：2020/12/22 22:50
import pytest
from pythonCode.calur import CalurQ


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
        print(item.nodeid)


@pytest.fixture(scope="module")
def myfixture():
    print("\n  使用fix当setup用 \n")
    cal = CalurQ()
    yield cal
    print("\n  使用fix当teardown用 \n")
