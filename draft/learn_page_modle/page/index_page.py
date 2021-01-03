# -*- coding: utf-8 -*-
from draft.learn_page_modle.page.login_page import LoginPage
from draft.learn_page_modle.page.register_page import RegisterPage


class IndexPage:
    def goto_LoginPage(self):
        '''
        跳转到登录页面
        :return:返回一个登录页面实例
        '''
        return LoginPage()

    def goto_RegisterPage(self):
        '''
        跳转到注册页面
        :return:返回一个注册页面实例
        '''
        return RegisterPage()
