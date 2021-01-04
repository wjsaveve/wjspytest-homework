# -*- coding: utf-8 -*-
import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, base_driver=None):
        # 注解，不是赋值操作。用作ide的类型提示
        base_driver: WebDriver
        if base_driver is None:
            self.dr = webdriver.Chrome()
            self.dr.get("https://work.weixin.qq.com/wework_admin/frame")
            self.__cookie_login()
        else:
            self.dr = base_driver
        self.dr.maximize_window()
        self.dr.implicitly_wait(5)

    def __cookie_login(self):
        with open("cookie.yml", mode='r', encoding='UTF-8') as f:
            dates = yaml.safe_load(f)
            for date in dates:
                self.dr.add_cookie(date)
        self.dr.get("https://work.weixin.qq.com/wework_admin/frame")

    def find(self, mystype, myvalue=None):
        if myvalue is None:
            return self.dr.find_element(*mystype)
        else:
            return self.dr.find_element(by=mystype, value=myvalue)

    def finds(self, mystype, myvalue=None):
        if myvalue is None:
            return self.dr.find_elements(*mystype)
        else:
            return self.dr.find_elements(by=mystype, value=myvalue)

    def quit(self):
        self.dr.quit()
