# -*- coding: utf-8 -*-
import logging

import allure

from test_frame.black_list import BlackList


# logging.basicConfig(level=logging.INFO)
# 级别递增：info < debug < error

def balck_wrapper(fun):
    def run(*args, **kwargs):
        black_list = BlackList().get_black_list()
        basepage = args[0]
        try:
            logging.info("开始寻找元素： \n args：" + str(args) + "；kwargs：" + str(kwargs))
            return fun(*args, **kwargs)
        except Exception as e:
            allure.attach("内容：测试异常", "标题：出现了黑名单", attachment_type=allure.attachment_type.TEXT)
            img_path = basepage.screen_shot()
            allure.attach.file(img_path, "日志图片", attachment_type=allure.attachment_type.PNG)
            for black in black_list:
                eles = basepage.finds(black)
                if len(eles) > 0:
                    # 对黑名单元素进行点击，可以拓展
                    # basepage.screen_shot()
                    eles[0].click()
                    return fun(*args, **kwargs)
            # basepage.screen_shot()
            raise e

    return run
