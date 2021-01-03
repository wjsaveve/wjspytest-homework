# -*- coding: utf-8 -*-

class ContactPage:
    def opt_getuser(self):
        '''
        获取成员列表，用来做断言
        :return:user_list，即用户列表（list格式）
        '''
        user_list = []
        return user_list

    def goto_AddUserPage(self):
        '''
        跳转到添加用户页面
        :return:AddUserPage类，即添加用户页面
        '''
        from draft.learn_page_modle.page.adduser_page import AddUserPage
        return AddUserPage()
