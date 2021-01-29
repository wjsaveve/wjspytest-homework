# -*- coding: utf-8 -*-
from test_frame.black_list import BlackList


def balck_wrapper(fun):
    def run(*args, **kwargs):
        black_list = BlackList().get_black_list()
        basepage = args[0]
        try:
            return fun(*args, **kwargs)
        except Exception as e:
            for black in black_list:
                eles = basepage.finds(black)
                if len(eles) > 0:
                    # 对黑名单元素进行点击，可以拓展
                    eles[0].click()
                    return fun(*args, **kwargs)
            raise e

    return run
