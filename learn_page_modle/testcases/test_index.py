# -*- coding: utf-8 -*-
from learn_page_modle.page import IndexPage


class TestIndex:
    def setup_class(self):
        self.index_page = IndexPage()

    def test_login(self):
        self.index_page.goto_LoginPage().opt_login_sacnf()

    def test_register(self):
        self.index_page.goto_RegisterPage().opt_register()
