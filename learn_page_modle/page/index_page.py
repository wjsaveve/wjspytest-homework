# -*- coding: utf-8 -*-
from learn_page_modle.page import LoginPage
from learn_page_modle.page import RegisterPage


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
