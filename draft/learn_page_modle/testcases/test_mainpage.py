# -*- coding: utf-8 -*-
import yaml
from selenium import webdriver

from draft.learn_page_modle.page.main_page import MainPage


class TestMainPage:
    def setup_class(self):
        self.main_page = MainPage()

        opt = webdriver.ChromeOptions()
        opt.debugger_address = '127.0.0.1:9222'
        self.dr = webdriver.Chrome(options=opt)
        self.dr.implicitly_wait(5)
        self.dr.get("https://work.weixin.qq.com/wework_admin/frame")
        mycookie = self.dr.get_cookies()
        with open("cookie.yml", mode='w', encoding='UTF-8') as f:
            yaml.dump(mycookie, f)

    def teardown_class(self):
        self.dr.quit()

    def test_adduser(self):
        # res = self.main_page.goto_AddUserPage().opt_add_user().opt_getuser()
        # assert "wj" in res
        self.main_page.goto_AddUserPage().opt_add_user()

    def test_adduser_by_contact(self):
        res = self.main_page.goto_ContactPage().goto_AddUserPage().opt_add_user().opt_getuser()
        assert "wj" in res
