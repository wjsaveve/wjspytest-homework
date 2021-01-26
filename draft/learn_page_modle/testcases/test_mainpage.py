# -*- coding: utf-8 -*-
import pytest

from draft.learn_page_modle.page.main_page import MainPage


class TestMainPage:
    def setup_class(self):
        print("setup开始")
        self.main_page = MainPage()

    # def test_get_cookie(self):
    #     opt = webdriver.ChromeOptions()
    #     opt.debugger_address = '127.0.0.1:9222'
    #     driver = webdriver.Chrome(options=opt)
    #     driver.implicitly_wait(5)
    #     driver.get("https://work.weixin.qq.com/wework_admin/frame")
    #     mycookie = driver.get_cookies()
    #     with open("cookie.yml", mode='w', encoding='UTF-8') as f:
    #         yaml.dump(mycookie, f)

    def teardown_class(self):
        print("teardown结束")
        self.main_page.quit()

    def test_adduser(self):
        resultnames = self.main_page.goto_AddUserPage().opt_add_user().opt_getuser()
        print(resultnames)
        assert '王健' in resultnames

    @pytest.mark.parametrize("myaccount,myphone,res",
                             [('WangJian', '18016010501', '该帐号已被“王健”占有'), ('wj010501', '18016387081', '该手机已被“王健”占有')])
    def test_adduser_error(self, myaccount, myphone, res):
        resultnames = self.main_page.goto_AddUserPage().opt_add_user_fail(myaccount, myphone)
        print(resultnames)
        assert res in resultnames

    def test_adduser_by_contact(self):
        res = self.main_page.goto_ContactPage().goto_AddUserPage().opt_add_user().opt_getuser()
        assert "王健" in res

    def test_adddepart(self):
        res = self.main_page.goto_ContactPage().add_depart()
        assert "新建部门成功" in res
