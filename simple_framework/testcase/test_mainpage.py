# -*- coding: utf-8 -*-
import time

import allure
import pytest

from simple_framework.page.main_page import MainPage


@allure.feature("新增功能测试")
class TestMainPage:
    def setup_method(self):
        print("setup开始")
        self.main_page = MainPage()

    def teardown_method(self):
        print("teardown结束")
        self.main_page.quit()

    @allure.testcase("http://www.baidu.com", "默认姓名新增-测试用例")
    @allure.story("默认姓名新增")
    def test_adduser_by_contact(self):
        res = self.main_page.goto_ContactPage().goto_AddUserPage().opt_add_user().opt_getuser()
        assert "王健" in res
        time.sleep(3)
        myimg = self.main_page.screen_shot()
        allure.attach.file(myimg, "日志图片", attachment_type=allure.attachment_type.JPG)

    @allure.testcase("http://www.baidu.com", "自设姓名新增-测试用例")
    @allure.story("自设姓名新增")
    @pytest.mark.parametrize("newname",
                             [('赵大'), ('李三')])
    def test_adduser(self, newname):
        codes = time.strftime("%m%d%H%M%S", time.localtime())
        myname = newname + codes + "号"
        res = self.main_page.goto_ContactPage().goto_AddUserPage().opt_add_user(myname).opt_getuser()
        print(res)
        assert myname in res
        allure.attach("测试日志内容", "测试日志标题", attachment_type=allure.attachment_type.TEXT)
