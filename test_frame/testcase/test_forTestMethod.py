# -*- coding: utf-8 -*-
# 为了测试共用方法而使用的，无意义
import yaml

from test_frame.black_list import BlackList


class TestForTest:
    def test_aaa(self):
        ap = BlackList()
        ap.set_black_list(('ww', 'yy'))
        ap.set_black_list("ss", 'dd')
        print(ap.get_black_list())

    def test_bb(self):
        with open("..//page/main_page.yaml", encoding="UTF-8") as f:
            data = yaml.load(f)
            print(data)
