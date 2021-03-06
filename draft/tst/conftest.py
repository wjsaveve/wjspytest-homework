# -*- coding: utf-8 -*-
# 创建时间：2020/12/18 0:43
import pytest


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
        print(item.nodeid)


@pytest.fixture(params=["参数1", "参数2"])
def myfixture(request):
    print("\n 执行fix方法，此时参数为：%s" % request.param)
    return [request.param, "hehe"]
