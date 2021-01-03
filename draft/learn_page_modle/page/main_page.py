# -*- coding: utf-8 -*-
import yaml
from selenium.webdriver.common.by import By
from draft.learn_page_modle.page.adduser_page import AddUserPage
from draft.learn_page_modle.page.base_page import BasePage
from draft.learn_page_modle.page.contact_page import ContactPage
from selenium import webdriver


class MainPage(BasePage):
    def goto_ContactPage(self):
        '''
        跳转到通讯录页面
        :return:ContactPage类，即通讯录页面
        '''
        return ContactPage()

    def goto_AddUserPage(self):
        '''
        跳转到添加用户页面
        :return:AddUserPage类，即添加用户页面
        '''
        self.dr.get("https://work.weixin.qq.com/wework_admin/frame")
        with open("cookie.yml", mode='r', encoding='UTF-8') as f:
            dates = yaml.safe_load(f)
            for date in dates:
                self.dr.add_cookie(date)
        self.dr.get("https://work.weixin.qq.com/wework_admin/frame")
        self.dr.find_element(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        return AddUserPage()
