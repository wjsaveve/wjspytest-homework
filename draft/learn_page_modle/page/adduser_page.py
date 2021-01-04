# -*- coding: utf-8 -*-
import time
from selenium.webdriver.common.by import By

from draft.learn_page_modle.page.base_page import BasePage
from draft.learn_page_modle.page.contact_page import ContactPage


class AddUserPage(BasePage):
    _location_input_name = (By.ID, 'username')
    _location_input_count = (By.ID, "memberAdd_acctid")
    _location_input_phone = (By.ID, "memberAdd_phone")
    _location_button_OK = (By.LINK_TEXT, '保存')
    _location_messgae_count = (By.CSS_SELECTOR, '.member_edit_item.member_edit_item_Account > div > div')

    def opt_add_user(self):
        '''
        新增用户操作。完成后，会自动跳转到通讯录页面
        :return:ContactPage类，即通讯录页面
        '''
        codes = time.strftime("%m%d%H%M%S", time.localtime())
        name = "王健" + codes + "号"
        count = "wj" + codes
        phone = "180" + time.strftime("%m%d%M%S", time.localtime())
        # 加星号的意思是解元组，就是把元组拆成多个参数来使用
        self.find(*self._location_input_name).send_keys(name)
        self.find(*self._location_input_count).send_keys(count)
        self.find(*self._location_input_phone).send_keys(phone)
        self.find(*self._location_button_OK).click()
        return ContactPage(self.dr)

    def opt_add_user_fail(self):
        '''
        新增用户时，输入已存在的帐号，会返回提示信息
        :return:error_message,即错误提示信息
        '''
        count = "WangJian"
        # 加星号的意思是解元组，就是把元组拆成多个参数来使用
        self.find(*self._location_input_count).send_keys(count)
        self.find(*self._location_input_name).click()
        error_message = self.dr.find_element(*self._location_messgae_count).text
        return error_message