# -*- coding: utf-8 -*-
# 创建时间：2020/12/22 22:39
import pytest
import yaml


class TestCal:

    @pytest.mark.parametrize("a,b,ext", yaml.safe_load(open("data.yml"))["add"], ids=["正数相加", "负数相加", "与0相加"])
    def test_add(self, a, b, ext, myfixture):
        assert ext == myfixture.add(a, b)

    @pytest.mark.parametrize("a,b,ext", yaml.safe_load(open("data.yml"))["sub"], ids=["正数相减", "负数相减", "与0相减"])
    def test_sub(self, a, b, ext, myfixture):
        assert ext == myfixture.sub(a, b)

    @pytest.mark.parametrize("a,b,ext", yaml.safe_load(open("data.yml"))["mul"], ids=["正数相乘", "负数相乘", "与0相乘"])
    def test_mul(self, a, b, ext, myfixture):
        assert ext == myfixture.mul(a, b)

    @pytest.mark.parametrize("a,b,ext", yaml.safe_load(open("data.yml"))["div"], ids=["正数相除", "负数相除", "与0相除"])
    def test_div(self, a, b, ext, myfixture):
        assert ext == myfixture.div(a, b)
