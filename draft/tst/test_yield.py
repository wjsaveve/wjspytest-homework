import pytest


@pytest.fixture(params=["参数1", "参数2"])
def connect_db(request):
    print("开始连接数据库！")
    yield request.param
    print("执行teardown，关闭数据库连接")


def test_print_param(connect_db):
    print("执行test_two")
    # print(connect_db)
    assert 1 == 1
