# -*- coding: utf-8 -*-
# 创建时间：2020/12/22 22:39
import pytest
from pythonCode.calur import CalurQ


class TestCal:
    def setup_class(self):
        print("开始测试计算模块~~~")
        self.cal = CalurQ()

    def teardown_class(self):
        print("~~~~测试计算模块结束")

    def setup(self):
        print("")
        print("开始计算")

    def teardown(self):
        print("")
        print("结算结束")

    @pytest.mark.parametrize("a,b,ext", [(1, 2, 3), (-1, -3, -4), (0, 1, 1)], ids=["正数相加", "负数相加", "与0相加"])
    def test_add(self, a, b, ext):
        assert ext == self.cal.add(a, b)

    @pytest.mark.parametrize("a,b,ext", [(3, 2, 1), (-1, -3, 2), (0, 1, -1)], ids=["正数相减", "负数相减", "与0相减"])
    def test_sub(self, a, b, ext):
        assert ext == self.cal.sub(a, b)

    @pytest.mark.parametrize("a,b,ext", [(1, 2, 2), (-1, -3, 3), (0, 1, 0)], ids=["正数相乘", "负数相乘", "与0相乘"])
    def test_mul(self, a, b, ext):
        assert ext == self.cal.mul(a, b)

    @pytest.mark.parametrize("a,b,ext", [(6, 2, 3), (-3, -2, 1.5), (9, 0, 0)], ids=["正数相除", "负数相除", "与0相除"])
    def test_div(self, a, b, ext):
        assert ext == self.cal.div(a, b)
