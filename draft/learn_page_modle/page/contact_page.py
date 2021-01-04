# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from draft.learn_page_modle.page.base_page import BasePage


class ContactPage(BasePage):
    _location_listitem_name = (By.XPATH, '//*[@id="member_list"]/tr/td[2]')
    _location_button_adduser = (By.LINK_TEXT, '添加成员')

    def opt_getuser(self):
        '''
        获取成员列表，用来做断言
        :return:user_list，即用户列表（list格式）
        '''
        user_list = []
        # 加星号的意思是解元组，就是把元组拆成多个参数来使用
        eles = self.finds(*self._location_listitem_name)
        for ele in eles:
            user_list.append(ele.get_attribute('title'))
        return user_list

    def goto_AddUserPage(self):
        '''
        跳转到添加用户页面
        :return:AddUserPage类，即添加用户页面
        '''
        from draft.learn_page_modle.page.adduser_page import AddUserPage
        self.find(*self._location_button_adduser).click()
        return AddUserPage(self.dr)
