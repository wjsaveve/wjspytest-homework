# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from draft.learn_page_modle.page.adduser_page import AddUserPage
from draft.learn_page_modle.page.base_page import BasePage
from draft.learn_page_modle.page.contact_page import ContactPage


class MainPage(BasePage):
    _location_button_adduser = (By.CSS_SELECTOR, ".ww_indexImg_AddMember")
    _location_button_contactlink = (By.ID, "menu_contacts")

    def goto_ContactPage(self):
        '''
        跳转到通讯录页面
        :return:ContactPage类，即通讯录页面
        '''
        self.find(*self._location_button_contactlink).click()
        return ContactPage(self.dr)

    def goto_AddUserPage(self):
        '''
        跳转到添加用户页面
        :return:AddUserPage类，即添加用户页面
        '''
        # 加星号的意思是解元组，就是把元组拆成多个参数来使用
        self.find(*self._location_button_adduser).click()
        return AddUserPage(self.dr)
