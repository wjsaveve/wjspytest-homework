# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By

from simple_framework.basics.base_page import BasePage
from simple_framework.page.contact_page import ContactPage


class AddUserPage(BasePage):
    _location_input_name = (By.ID, 'username')
    _location_input_count = (By.ID, "memberAdd_acctid")
    _location_input_phone = (By.ID, "memberAdd_phone")
    _location_button_OK = (By.LINK_TEXT, '保存')
    _location_messgae_count = (By.CSS_SELECTOR, '.member_edit_item.member_edit_item_Account > div > div')
    _location_messgae_phone = (
        By.CSS_SELECTOR, '.member_edit_item_right.ww_inputWithTips_WithErr .ww_inputWithTips_tips')
    _location_button_mainpagelink = (By.ID, "menu_index")
    _location_messageitem = (By.LINK_TEXT, "离开此页")

    def opt_add_user(self, addname='王健'):
        '''新增用户操作。完成后，会自动跳转到通讯录页面
        :return:ContactPage类，即通讯录页面'''
        codes = time.strftime("%m%d%H%M%S", time.localtime())
        if addname == '王健':
            name = addname + codes + "号"
        else:
            name = addname
        count = "wj" + codes
        phone = "180" + time.strftime("%m%d%M%S", time.localtime())
        # 加星号的意思是解元组，就是把元组拆成多个参数来使用
        self.find(*self._location_input_name).send_keys(name)
        self.find(*self._location_input_count).send_keys(count)
        self.find(*self._location_input_phone).send_keys(phone)
        self.find(*self._location_button_OK).click()
        return ContactPage(self.dr)
