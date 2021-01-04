# -*- coding: utf-8 -*-
from draft.learn_page_modle.page.main_page import MainPage


class TestMainPage:
    def setup_class(self):
        print("setup开始")
        self.main_page = MainPage()

        # opt = webdriver.ChromeOptions()
        # opt.debugger_address = '127.0.0.1:9222'
        # self.dr = webdriver.Chrome(options=opt)
        # self.dr.implicitly_wait(5)
        # self.dr.get("https://work.weixin.qq.com/wework_admin/frame")
        # mycookie = self.dr.get_cookies()
        # with open("cookie.yml", mode='w', encoding='UTF-8') as f:
        #     yaml.dump(mycookie, f)

    def teardown_class(self):
        print("teardown结束")
        self.main_page.quit()

    def test_adduser(self):
        resultnames = self.main_page.goto_AddUserPage().opt_add_user().opt_getuser()
        print(resultnames)
        assert '王健' in resultnames

    # def test_adduser_error(self):
    #     resultnames = self.main_page.goto_AddUserPage().opt_add_user_fail()
    #     print(resultnames)
    #     assert '该帐号已被“王健”占有' == resultnames

    def test_adduser_by_contact(self):
        res = self.main_page.goto_ContactPage().goto_AddUserPage().opt_add_user().opt_getuser()
        assert "王健" in res
