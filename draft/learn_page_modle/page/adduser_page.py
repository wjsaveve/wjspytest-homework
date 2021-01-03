# -*- coding: utf-8 -*-
import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

from draft.learn_page_modle.page.base_page import BasePage
from draft.learn_page_modle.page.contact_page import ContactPage


class AddUserPage(BasePage):
    def opt_add_user(self):
        '''
        新增用户操作。完成后，会自动跳转到通讯录页面
        :return:ContactPage类，即通讯录页面
        '''
        codes = time.strftime("%m%d%H%M%S", time.localtime())
        name = "王健" + codes + "号"
        count = "wj" + codes
        phone = "180" + time.strftime("%m%d%M%S", time.localtime())
        self.dr.find_element(By.ID, 'username').send_keys(name)
        self.dr.find_element(By.ID, "memberAdd_acctid").send_keys(count)
        self.dr.find_element(By.ID, "memberAdd_phone").send_keys(phone)
        self.dr.find_element_by_link_text("保存").click()
        return ContactPage()
